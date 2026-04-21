---
name: wiki-purpose
description: Propose updates to purpose.md based on what the wiki has actually accumulated. Use when the human says "review purpose", "/wiki-purpose", "has the wiki drifted from purpose?", "update the research direction", or after a batch of ingests that may have shifted the scope. Reads purpose.md, the synthesis, the index, and recent log entries; proposes targeted edits to Goal, Key Questions, Scope, and Thesis where the wiki's accumulated state has diverged from the stated direction. Never modifies purpose.md without explicit approval — purpose.md is human-owned.
---

# wiki-purpose

You are proposing updates to `purpose.md` — the human-owned file that states the wiki's research direction. The file drives `/wiki-ingest` and `/wiki-query` via the `purpose_md` context they read. When it goes stale, every downstream operation loses its compass.

The point of this skill is a recurring check: does `purpose.md` still describe what the wiki actually is? If not, what's the smallest, specific edit?

## When to invoke

- User says "/wiki-purpose", "review purpose", "update the research direction"
- User asks "has the wiki drifted from its stated purpose?"
- User finishes a batch of ingests and wants to reassess direction
- You notice during `/wiki-query` or `/wiki-ingest` that the wiki's accumulated content is substantially broader or narrower than `purpose.md` suggests — offer the skill to the user; do not invoke unasked

Do not invoke if the wiki has fewer than ~5 pages. Purpose drift is a compound-interest problem; there's nothing to diff against yet.

## The invariant

`purpose.md` is human-owned. This skill only *proposes*. It does not write to `purpose.md` unless the user approves an explicit proposed version and asks to apply it.

## Arguments

- No positional args required. The user just invokes the skill.
- `--apply` — apply a proposed edit after the user has approved it. Requires the proposal to have been shown first; do not combine proposal and apply in one step without an intervening user confirmation.

## Steps

### 1. Read state

- Read `purpose.md`. Note which sections (Goal, Key Questions, Scope, Thesis) have content vs. placeholders (`TBD`, empty lists).
- Read `wiki/synthesis.md`. This is the wiki's current integrated understanding.
- Read `wiki/index.md`. Count entries per category (Entities, Concepts, Sources, Comparisons). Note the topic clusters suggested by page names and TLDRs.
- Read the last ~10 entries of `wiki/log.md`. Note which operations have been running and what sources have been ingested recently.

### 2. Compute drift per section

For each section of `purpose.md`, ask: does the current text match what the wiki actually contains?

- **Goal.** Does the stated goal still cover the wiki's subject matter? If the wiki has accumulated substantial material outside the stated goal, the goal may need widening; if the stated goal is broader than the wiki's actual focus, it may need narrowing. A one-sentence goal that obscures half the wiki's pages is stale.
- **Key Questions.** Which of the listed questions has the wiki materially answered (synthesis.md now states a position)? Which have shifted in formulation as the human learned the domain? Which new questions emerged from ingests that aren't listed? Propose replacing answered questions with still-open ones; do not let the list grow past ~5 — it's supposed to be the primary questions, not a backlog.
- **Scope.** Does the in-scope/out-of-scope boundary still match what's been ingested? If out-of-scope items are appearing as wiki pages, either the scope drifted or those pages shouldn't exist (surface the latter case separately as a finding, don't try to fix here).
- **Thesis.** If the thesis is still `TBD` but `synthesis.md` now states a coherent position, propose lifting that position into Thesis. If the thesis is stated but `synthesis.md` has moved, propose updating it. If the thesis is still genuinely uncertain, leave it.

Each section gets one of three verdicts: **unchanged**, **minor edit**, **material edit**.

### 3. Draft the proposed diff

For each section with a verdict of minor-or-material-edit, show:

- The current text (quoted).
- The proposed replacement text (quoted).
- One-sentence rationale citing what in the wiki drove the proposal. Prefer specific citations: "`[[Page Name]]` and three other pages argue X, but Goal says Y" beats "the wiki has grown."

Group the diffs by section. Don't rewrite sections you're leaving unchanged.

If no section needs editing, say so explicitly: "No drift detected; `purpose.md` still matches the wiki's state." Stop there.

### 4. Present and wait

Show the proposed diffs to the user. Ask:

- "Apply all?"
- "Apply section N only?"
- "Revise a proposal?"
- "Reject and close?"

Do not apply anything automatically, even if the user previously set a batch-mode preference. `purpose.md` edits cross the human-owned-file line and always require explicit confirmation.

### 5. Apply (on `--apply` or on explicit user approval)

Only after the user approves an explicit proposal:

- Write the approved sections back to `purpose.md`.
- Do not touch sections the user didn't approve.
- Preserve the file structure (`## Goal`, `## Key Questions`, `## Scope`, `## Thesis`). Do not add or remove sections.
- Do not add a changelog or dated footer to `purpose.md`; git history is the record.

Then append a `wiki/log.md` entry: `### [YYYY-MM-DD] purpose | <short description of what changed>`.

### 6. Remind

If Goal or Scope changed materially, remind the user that existing pages may now be out of scope or that new territory just opened up — but do **not** start ingesting or deleting pages in response. Those are separate operations the human initiates.

## Error handling

- **`purpose.md` not found**: stop. Tell the user. `purpose.md` should have been created by `new-wiki.sh`; if missing, something was deleted.
- **`purpose.md` is only placeholders (TBD, empty lists) and the wiki has content**: propose filling sections based on the wiki's accumulated state, but mark every proposed value as a "first draft" the user should revise. You are inferring intent from output, which is weaker than the human stating it directly.
- **`synthesis.md` is empty or still placeholder**: Goal and Scope proposals can still be computed from `index.md`, but skip Thesis proposals — there is no integrated understanding to lift from.
- **User approves a partial apply**: apply exactly the approved sections and nothing else. State what you applied and what you left alone.

## What this skill does not do

- Does not modify `purpose.md` without explicit user approval.
- Does not ingest new sources or answer questions — that's `/wiki-ingest` and `/wiki-query`.
- Does not delete or reorganize wiki pages when scope narrows. It proposes the purpose change; follow-up page cleanup is a separate, human-initiated operation.
- Does not modify `CLAUDE.md`, `writing-style.md`, `wiki/conventions.md`, `wiki/synthesis.md`, or anything in `raw/`.
- Does not commit to git.
