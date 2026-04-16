---
name: wiki-ingest
description: Ingest a source into the LLM wiki, or re-audit a past ingest. Use when the user asks to ingest a source ("ingest the source at raw/foo.pdf", "/wiki-ingest raw/foo.md", "add this paper to the wiki") or to audit a past ingest ("/wiki-ingest --audit-only <source>", "audit the Williamson ingest", "what did we miss in <source>?"). Orchestrates the pipeline — convert PDF if needed, hash the raw file, present the pre-check, run the wiki-extractor subagent, run the wiki-auditor subagent, append the audit report to the source-summary. In audit-only mode (or on a hash-matching re-ingest), skips extraction and runs only the audit. Does not commit to git; the human reviews first.
---

# wiki-ingest

You are orchestrating an ingest into the LLM wiki, or re-auditing a past ingest. The vault root has a `CLAUDE.md` that describes the schema; this skill describes the *workflow* on top of that schema.

## Modes

The skill has two modes:

- **Full ingest** (default): stage source, pre-check, extract, audit, append gap callout.
- **Audit-only**: skip staging and extraction, run only the auditor against an existing source-summary and its derived pages, replace the gap callout. Triggered by `--audit-only`, by phrases like "audit the Williamson ingest" / "what did we miss in <source>?", or automatically when a re-ingest computes a `raw_hash` matching the existing source-summary's `raw_hash` (the source is unchanged, so re-extracting would duplicate work).

## When to invoke (full ingest)

- User says "ingest the source at <path>" or "/wiki-ingest <path>"
- User asks to add a paper / article / document to the wiki
- User pastes a source path and says "add this"

If the user has not provided a source path, ask for one. Do not invent.

## When to invoke (audit-only)

- User says "/wiki-ingest --audit-only <source>" or "audit the <name> ingest"
- User asks "what did we miss in <source>?"
- A re-ingest detects a hash match (skip extraction, run audit)

If the user references an existing ingest vaguely ("the Williamson paper"), search `wiki/sources/` for matches; if multiple, ask which.

## Steps

### 1. Resolve source and mode

Determine which path you're on.

**Audit-only path** (skip to step 5) when:
- User passed `--audit-only` or used audit-phrasing ("audit the X ingest", "what did we miss in X?")
- User gave a source name and a matching source-summary already exists in `wiki/sources/`, AND the recomputed `raw_hash` matches the source-summary's stored `raw_hash`

**Full-ingest path** (steps 2-7) otherwise.

For audit-only on a vague reference, search `wiki/sources/` and confirm with the user before proceeding.

### 2. Stage the source (full ingest)

- If the source is a PDF: convert to markdown via `pymupdf4llm`. Store the converted `.md` alongside the original in `raw/`. The original PDF is the immutable artifact.
  ```bash
  python -c "import pymupdf4llm; open('raw/<name>.md','w').write(pymupdf4llm.to_markdown('raw/<name>.pdf'))"
  ```
- If the source is already markdown: it should already be at `raw/<name>.md`. If the user gave a path outside `raw/`, copy it in first; never read from outside `raw/` for ingestion.
- Compute SHA256 of the **original** file (the PDF for PDFs, the .md for markdown sources):
  ```bash
  shasum -a 256 raw/<name>.<ext>
  ```
- If a source-summary already exists for this source, compare the new hash to the stored `raw_hash`:
  - **Match** → switch to audit-only path (the source is unchanged; re-extracting would duplicate work). Tell the user.
  - **Mismatch** → this is a source update. Ask the user whether to refresh affected pages (re-extract over the existing pages) or treat as a new source. Do not silently overwrite.
- Note today's date in ISO 8601.

### 3. Read context (full ingest)

- Read `CLAUDE.md` at the vault root.
- Read `purpose.md`. If it is empty (only the placeholder template), note that — the extractor will not get research-direction steering.
- Read the source markdown end to end.

### 4. Present the pre-check (full ingest)

Show the user, before any pages are written:

1. **Citation** — author(s), year, title, venue.
2. **Key takeaways** — 4-8 substantive claims you'd extract.
3. **Planned new pages** — sources/, entities/, concepts/, comparisons/. For each, the filename you'd use (Title Case, matching the wikilink) and a one-line note on what it covers.
4. **Existing pages to update** — search `wiki/` for entities and concepts that overlap with the source (`obsidian search query="..." path=wiki` or `grep -ri "..." wiki/`). For each match, what you'd add.
5. **Potential contradictions** — claims in the source that disagree with existing wiki content; claims internal to the source that disagree with each other.

End with: "Proceed?"

If the user has set the session to batch mode (e.g., "skip the pre-check from now on" or "ingest these without pre-check"), skip this step.

### 5. Extract (full ingest only — subagent: wiki-extractor)

On approval, invoke the `wiki-extractor` subagent with a single message containing:

- `source_md_path`, `raw_path`, `raw_hash`, `today_iso`
- `purpose_md` contents (verbatim, including placeholder if empty)
- The approved `plan` (the pre-check structure the user signed off on, condensed)

Wait for the extractor to return its structured report (`pages_created`, `pages_updated`, `index_entries_added`, `log_entry`, `synthesis_changed`, `surprises`, `unresolved_during_extraction`).

If the extractor reports `surprises` (e.g., an entity already existed that the plan missed), present them to the user before invoking the auditor; ask whether to proceed.

### 6. Audit (both paths — subagent: wiki-auditor)

Invoke the `wiki-auditor` subagent **independently** — do not pass any extractor reasoning. The auditor's job is to read the source fresh against the pages.

For the **full-ingest path**, pass:
- `source_md_path`
- `source_summary_path` (from extractor's `pages_created`)
- `pages_created` (paths only)
- `pages_updated` (paths plus `what_changed` summary)
- `today_iso`

For the **audit-only path**, derive the page list authoritatively before calling the auditor:
- Get `raw_path`, `raw_hash`, and the source-summary path from the user's reference.
- Verify the raw source still matches the stored `raw_hash`. Mismatch → stop, the source has drifted; recommend re-ingest. (This is the same check as step 2; an audit-only invocation triggered by the user must run it explicitly since step 2 was skipped.)
- If `raw_path` is a PDF, ensure the converted `.md` exists in `raw/`; if not, regenerate via `pymupdf4llm`.
- Find all wiki pages whose `sources` frontmatter contains a wikilink to this source-summary:
  ```bash
  grep -rl "[[<source-summary-stem>]]" wiki/
  ```
- Pass `pages_created` = that full list, `pages_updated` = `[]`. The auditor doesn't care whether pages came from the original ingest or were added later.

Wait for the auditor's gap report.

### 7. Append the gap report to the source-summary

Edit the source-summary page. Add or replace a `[!gap] Extraction coverage of this ingest (self-audit, <today_iso>)` callout containing the auditor's findings. If a prior audit callout exists, replace it (do not stack stale audits). If the user explicitly wants to preserve audit history, rename the prior one to `... — superseded` and append the new one.

### 7.5. Do not fix gaps inline

The skill produces pages plus a gap callout. It does not produce fixed pages. Do not attempt to backfill missing pages, revise `[!source]` claims the auditor flagged, or edit existing pages in response to the gap list. Those are human-triaged and either handled by a follow-up `/wiki-lint` pass or deferred to the next ingest that would touch the same pages.

Exception: surface attribution-mismatch findings (actual misattributions — `[!source]` callouts the source does not support, overstated paraphrases, reconstructed figures mislabeled as `[!source]`) prominently in the summary. The human decides whether to fix inline or file as known errors.

This keeps the skill's contract clean: ingest adds knowledge and reports what's missing; lint fixes. Mixing the two stretches invocations and blurs what went wrong when something went wrong.

### 8. Summarize to the user

Show:

- Source path and `raw_hash`
- (Full ingest) Pages created, pages updated, index/log/synthesis updates confirmed
- (Audit-only) Number of linked pages audited; whether this superseded a prior audit
- Auditor's gap report inline (so the human can triage in place)
- (Full ingest) Extractor `surprises` and `unresolved_during_extraction` highlighted separately
- A reminder to commit when ready (do **not** auto-commit)

### 9. Wait for human

Do not commit, do not run lint, do not start a follow-on ingest. The human reviews. Corrections go to `CLAUDE.md` Wiki Conventions (you can offer to draft them as a separate step).

## Error handling

- **`pymupdf4llm` not installed**: stop, instruct the user to `pip install pymupdf4llm`.
- **Hash mismatch detected during audit-only**: the raw source has changed since ingestion. Stop and recommend a full re-ingest; do not run the audit (the gap list would conflate "we missed this" with "this didn't exist when we ingested").
- **Auditor finds attribution-mismatch anomalies**: surface prominently. These are potential extraction errors, not extraction gaps.

## What this skill does not do

- Does not commit to git. Human reviews and commits.
- Does not run lint (`/wiki-lint`, when it exists). Lint is a separate operation.
- Does not modify `CLAUDE.md`, `purpose.md`, `writing-style.md`, or anything in `raw/`.
- Does not bulk-ingest. One source per invocation. Long sources should be split into chapters/sections by the user; each chunk is a separate invocation.
