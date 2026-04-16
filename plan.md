# Implementation Plan

Implements the proposal in `implementation-proposal.md`. Ten deliverable files (1 skill file, 4 templates, 3 wiki scaffolds, 1 human-owned file, 1 writing-style reference), a vault directory structure, and a tested end-to-end workflow.

Phases 0-1 constitute the **Init workflow** — they produce a ready-to-use wiki vault from scratch. This workflow is repeatable: spinning up a new wiki for a different domain means running Phases 0-1 again in a fresh vault. Phases 2-4 are per-wiki — they build the specific wiki's content and refine its schema through use.

---

## Phase 0: Prerequisites & Environment

**Goal:** Confirm the toolchain works before writing anything. These checks are the same for every new wiki.

### 0.1 Verify Obsidian CLI

Obsidian 1.12.7+ required. CLI enabled in Settings > General > Command line interface.

```bash
obsidian version
```

### 0.2 Verify Git

```bash
git --version
```

### 0.3 Verify pymupdf4llm

Required for converting PDFs to markdown at ingest time. PDFs are the primary source format in research workflows.

```bash
python -c "import pymupdf4llm; print('pymupdf4llm OK')"
```

If not installed: `pip install pymupdf4llm`.

### 0.4 Choose or Create the Vault

Use an existing vault or create a new one via Obsidian's UI. The vault must be open in the Obsidian desktop app for CLI search/graph commands.

### 0.5 Configure Obsidian Settings

- **Settings > Files and links > Default location for new notes:** `wiki/`
- **Settings > Files and links > Attachment folder path:** `raw/assets/`
- **Settings > Templates > Template folder location:** `templates/`
- **Settings > Core plugins:** Enable Templates

### 0.6 Initialize Git

```bash
cd /path/to/vault
git init
```

Create `.gitignore`:
```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.trash/
```

```bash
git add .gitignore
git commit -m "Initialize vault"
```

---

## Phase 1: Minimal Setup

**Goal:** Create the directory structure, templates, wiki scaffolds, and CLAUDE.md — everything needed to do a first ingest. This is the same scaffold for any domain; no customization needed at this stage.

**Depends on:** Phase 0

### 1.1 Create Directories

```bash
mkdir -p raw/assets
mkdir -p wiki/entities wiki/concepts wiki/sources wiki/comparisons
mkdir -p templates
```

### 1.2 Create Wiki Scaffolds

**`wiki/index.md`:**
```markdown
# Wiki Index

## Entities

## Concepts

## Sources

## Comparisons
```

**`wiki/log.md`:**
```markdown
# Wiki Log
```

**`wiki/synthesis.md`:**
```markdown
---
type: synthesis
sources: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
status: current
tags: []
---

> [!tldr]
> High-level synthesis of the wiki's knowledge. Updated as the wiki grows.

## Overview

*No content yet. Updated after the first few sources are ingested.*
```

**`purpose.md`** (vault root):
```markdown
# Purpose

## Goal
<!-- What are you trying to understand or build? -->

## Key Questions
<!-- The primary questions driving this wiki -->
1.
2.
3.

## Scope
<!-- What is in scope? What is explicitly out of scope? -->
**In scope:**
-

**Out of scope:**
-

## Thesis
<!-- Your current working hypothesis or conclusion. Update as research progresses. -->
> TBD
```

**`writing-style.md`** (vault root): full content from the Writing Style Reference section of `implementation-proposal.md`. The agent reads it when drafting or revising prose; the operational summary lives in CLAUDE.md's Guidance → Writing Style subsection.

### 1.3 Write Templates

Create all four templates (entity, concept, source-summary, comparison) as specified in the proposal. These define the required frontmatter fields, TLDR callout, claim-typed sections, and default structure for each page type.

### 1.4 Test CLI and Direct Approaches

Test both CLI and direct approaches for each operation to determine which works best:

```bash
obsidian create name="Test Entity" path=wiki/entities template=entity
obsidian read path="wiki/entities/Test Entity.md"
```

Verify: page created in correct directory, frontmatter intact, `{{date}}` resolved.

If `template=` doesn't work: the direct alternative is reading template content and creating the page with content directly. Document the working approach.

Clean up test page.

Also verify the graph commands used by lint:

```bash
obsidian orphans
obsidian deadends
obsidian unresolved
```

If any don't work: the direct alternative is reading the file tree and parsing wikilinks. Document which approach works best for each operation.

Test search directory scoping:

```bash
obsidian search query=test path=wiki/entities
obsidian search query=test folder=wiki/entities
```

If neither syntax filters results by directory, the direct alternative is `grep -ri "<terms>" wiki/`. Document the working approach in CLAUDE.md so the agent doesn't re-discover it each session.

Test callout search:

```bash
obsidian search:context query="[!source]" path=wiki
```

If the brackets or exclamation mark prevent literal matching, try quoting or escaping. If callout syntax isn't searchable via the CLI, the direct alternative is `grep -r "\[!unverified\]" wiki/`. Document the working approach in CLAUDE.md so lint operations use the correct tool.

Test link traversal commands (used by query and lint):

```bash
obsidian backlinks file="Test Entity"
obsidian links file="Test Entity"
```

Run these against the test page created earlier (before cleanup). Verify that `backlinks` returns files linking to the test page and `links` returns outgoing links from it. If the `file=` parameter doesn't resolve Title Case names with spaces, try `path=` instead. The direct alternative for backlinks is `grep -rl "\[\[Page Name\]\]" wiki/`. Document the working approach in CLAUDE.md.

### 1.5 Write CLAUDE.md

Create `CLAUDE.md` in the vault root as specified in the proposal. Two sections: Specifications (strict data contracts) and Guidance (flexible principles). Include empty "Wiki Conventions" section. Reference `purpose.md` in the Vault Layout, Ingest, and Query sections. Include the Writing Style subsection under Guidance (operational rules) with a pointer to `writing-style.md` for detail.

Adjust any CLI commands based on findings from 1.4.

### 1.6 Commit

```bash
git add -A
git commit -m "Initial vault setup: structure, templates, schema"
```

---

## Phase 2: First Ingest (Smoke Test)

**Goal:** Ingest a real source end-to-end. This is the most important phase — it validates the entire system against real content and reveals what needs adjustment.

**This is the start of the training period.** Review every page the agent creates or updates — not just the source summary. File corrections to Wiki Conventions immediately. Continue this level of review through Phase 4 (~10 ingests total). The conventions accumulated during this period are the schema's most valuable content.

**Depends on:** Phase 1

### 2.1 Add a Source

Choose a real source document — a short article or paper. Copy or clip it into `raw/`.

### 2.2 Run Ingest

Open a Claude Code session in the vault directory. CLAUDE.md loads automatically.

```
Ingest the source at raw/<filename>.md
```

The agent should present an ingest pre-check (key takeaways, planned pages, updates, contradictions) before writing. Review and approve.

### 2.3 Verify Results

**Source summary:**
- Created in `wiki/sources/`?
- Frontmatter populated (raw_path, raw_hash, sources, created date, tags)?
- TLDR present and accurate?
- Key takeaways use `[!source]` callouts with wikilinks?

**Entity and concept pages:**
- Created in correct directories?
- No duplicates (agent searched before creating)?
- Frontmatter includes source reference?
- Claims properly typed (source vs. analysis)?

**Index:** Updated with new pages and TLDRs?

**Log:** Entry appended to `wiki/log.md`?

**Synthesis:** `wiki/synthesis.md` updated?

**Claim typing:** No bare claims outside callout blocks? Source callouts include links? Analysis callouts show reasoning? Multi-source claims cite all sources?

**Purpose:** Agent read `purpose.md` and used it to steer extraction (if populated)?

### 2.4 Record Issues

Problems found become the first entries in the CLAUDE.md "Wiki Conventions" section. CLI command adjustments go into the Specifications section.

### 2.5 Commit

```bash
git add -A
git commit -m "First ingest: <source-name>"
```

---

## Phase 3: Query and Lint Smoke Tests

**Goal:** Validate the remaining two operations.

**Depends on:** Phase 2

### 3.1 Query Test

Ask a question that requires reading multiple wiki pages:

```
What are the main themes in the wiki so far?
```

Or a more specific question based on the ingested source.

Verify:
- Index consulted, search used, relevant pages read
- Links followed (backlinks/outgoing)
- Answer cites specific wiki pages
- Sourced claims distinguished from inferences
- Dual output: wiki pages updated as side effect if applicable
- Log entry appended if a new page was created

**Future:** Query output formats (comparison tables, Marp slides, etc.) are supported but not tested in this phase. Exercise them once the basic query workflow is validated.

### 3.2 Lint Test

```
Run a lint check on the wiki.
```

Verify:
- Structural checks ran (orphans, dead ends, unresolved links)
- Schema checks ran:
  - Frontmatter completeness per type (core fields plus per-type fields; ISO 8601 dates; `sources`/`tags`/`subjects` as YAML lists)
  - TLDR is the first content block after frontmatter on every wiki page
  - Filenames in Title Case, matching wikilink text
  - Index consistency (every wiki page has an entry; every entry resolves; source counts match `len(sources)`; TLDRs match)
- Source drift check ran (recomputed `raw_hash` for each source-summary against its `raw_path`, flagged mismatches)
- Bare-claim heuristic ran (prose claims outside typed callouts reported as candidates, `synthesis.md` exempt)
- Unverified claims and gaps scanned
- Claim-audit sampling ran (2-3 `[!source]` claims traced to cited sources; rotation honored if prior lint log entries exist)
- Conceptual review produced specific findings (thinly-sourced pages, pages lacking `[!analysis]`, stale hubs, unanswered gaps, missing cross-links) — not generic suggestions
- Report presented with categories and recommended actions
- No fixes applied without approval
- Log entry appended, including audited claim references for future rotation

### 3.3 Record Issues and Commit

Same pattern as Phase 2.

---

## Phase 4: Iteration & Refinement

**Goal:** Stress-test with more sources. Build real cross-references. Refine the schema.

**Note:** A partially-built wiki can underperform no wiki at all — incomplete cross-references and partial synthesis can mislead rather than help. Until the wiki has 8-10+ sources with overlapping topics, treat wiki answers as starting points, not authoritative. Cross-references and synthesis only become reliable when multiple sources cover the same entities and concepts. This phase is where the wiki crosses that threshold.

**Depends on:** Phases 2-3

### 4.1 Ingest 3-5 More Sources

Choose sources that overlap (shared entities/concepts) to test cross-referencing. Include at least one source that contradicts or updates a claim from an earlier source.

After each ingest, review:
- Cross-references created correctly?
- Existing pages updated (not duplicated)?
- Contradictions surfaced (not smoothed)?
- Index staying clean?
- Synthesis evolving meaningfully?
- Log accumulating?

### 4.2 Test Source Update (Staleness)

Modify one raw source. Tell the agent to re-ingest the updated source. Verify:
- Agent detects the source has changed via `raw_hash` comparison
- Affected wiki pages updated
- Frontmatter `updated` dates refreshed
- Contradictions from the update surfaced

Also test re-ingesting an unchanged source — the agent should detect the matching hash and skip.

### 4.3 Review and Evolve the Schema

By this point the "Wiki Conventions" section in CLAUDE.md should have several entries. Review them:
- Are the corrections specific and useful?
- Has the agent learned patterns about the domain?
- Do the templates need adjustment for this domain?
- Is a new page type needed?
- Is "prefer targeted updates" sufficient, or should the agent show proposed diffs before committing? (More important as supervision decreases.)

Adjust CLAUDE.md, templates, or conventions as needed. This is the schema co-evolution the original describes.

### 4.4 Commit

```bash
git add -A
git commit -m "Complete initial wiki buildout (<N> sources, <M> wiki pages)"
```

---

## Dependency Graph

```
Phase 0 (Prerequisites)        ─┐
  |                              │ Init workflow
  v                              │ (repeatable for any new vault)
Phase 1 (Minimal Setup)        ─┘
  |
  v
Phase 2 (First Ingest)        ─┐
  |                              │ Per-wiki
  v                              │ (domain-specific content & refinement)
Phase 3 (Query + Lint)          │
  |                              │
  v                              │
Phase 4 (Iteration)            ─┘
```

Phases 0-1 (Init) are domain-agnostic and repeatable. First real content appears in Phase 2.

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| `obsidian create ... template=` doesn't work as expected | Medium | Medium | Test in Phase 1.4. Direct alternative: read template, create page with content directly. |
| Obsidian desktop app not running when CLI commands execute | Low | Medium | Only affects search/graph commands. Document clearly. Direct file I/O works without the app. |
| LLM creates duplicate pages instead of updating existing ones | Medium | Medium | CLAUDE.md specifies "search before creating." Review in Phase 2. Add correction if needed. |
| LLM marks inferences as `[!source]` | Medium | High | CLAUDE.md emphasizes this distinction. Review claim typing in Phase 2. Correct aggressively. |
| Context compaction drops CLAUDE.md conventions mid-session | Medium | High | Keep CLAUDE.md concise. For long sessions, the agent can re-read it. |
| Lint graph commands (`obsidian orphans/deadends/unresolved`) don't work as expected | Medium | Medium | Test in Phase 1.4. Direct alternative: agent reads file tree and parses wikilinks. More expensive but no CLI dependency. |
| LLM writes substantive claims as regular prose (no callout) | High | High | CLAUDE.md claim typing spec emphasizes this. Review in Phase 2. If it happens, add an explicit correction to Wiki Conventions: "Every factual or analytical statement must be inside a typed callout." |
| `obsidian search path=` doesn't filter results as documented | Low | Low | CLI reference documents `path=<folder>` for search. Test in Phase 1.4 to confirm behavior matches docs. Direct alternative: `grep -ri "<terms>" wiki/`. |
| Callout syntax (`[!source]`, `[!gap]`) not searchable via `obsidian search` | Medium | Medium | Test in Phase 1.4. Direct alternative: `grep -r "\[!source\]" wiki/`. Document in CLAUDE.md. |
| `pymupdf4llm` produces poor markdown from complex PDFs (tables, multi-column, scanned images) | Medium | Medium | Review converted markdown before ingesting. For scanned/image-heavy PDFs, supplement with Claude's native PDF reading (up to 20 pages per request). |

---

## Success Criteria

The implementation is complete when:

1. All 10 deliverable files exist and are committed to git
2. A source has been ingested end-to-end with correct claim typing and provenance
3. A query has been answered using wiki content with proper citations
4. A lint pass has run all checks (structural, schema, source drift, bare-claim, claim-audit sampling, conceptual) and produced a report
5. The wiki has 4+ sources ingested with cross-referenced entity and concept pages
6. `wiki/log.md` has entries for ingests, queries, and lint
7. `wiki/synthesis.md` has been updated across multiple ingests
8. CLAUDE.md "Wiki Conventions" section has entries from real use
