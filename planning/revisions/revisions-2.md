# Revisions (Round 2)

Changes to `implementation-proposal.md`, `plan.md`, and `plan-checklist.md` based on a comparative review of the planning documents against `llm-wiki.md`, `PHILOSOPHY.md`, `intermediate/`, `synthesis/`, and the Round 1 revision.

Key themes of this revision:
1. **Honor the data contracts consistently.** Fix places where scaffolds and templates don't fully comply with the spec they define.
2. **Add concrete thresholds where "use judgment" is insufficient.** The community reported specific failure points; the plan should acknowledge them.
3. **Elevate community-tested principles that were partially captured.** Dual output and the ingestion gap were identified as important but only weakly reflected.
4. **Keep revisions lean.** This file contains rationale and diffs only — not full document copies. The top-level files are the source of truth.

---

## Change 1: Complete synthesis.md scaffold frontmatter

**Problem:** The frontmatter spec says every wiki page must have `type`, `sources`, `created`, `updated`, `status`, and `tags`. The synthesis.md scaffold only has `type`, `updated`, and `status` — missing three required fields. This violates the "strict where it matters" principle: if tools depend on consistent frontmatter, the scaffold that ships with the wiki should model it correctly.

**Files changed:** `implementation-proposal.md`, `plan.md`, `revisions/revisions-1.md`

**Change:** In all three files, replace the synthesis.md scaffold frontmatter:

```yaml
# Before
---
type: synthesis
updated: ""
status: current
---

# After
---
type: synthesis
sources: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
status: current
tags: []
---
```

`sources` will typically be `[]` for synthesis (it draws from the wiki, not from specific source-summary pages). `created` gets the actual creation date at setup time. The agent fills `tags` as the wiki develops a tagging vocabulary.

---

## Change 2: Add claim typing guidance for synthesis.md

**Problem:** The spec says "every substantive claim" needs a callout type. synthesis.md is an entire page of analytical content. Wrapping it in `[!analysis]` callouts would be impractical and ugly. The CLAUDE.md Synthesis guidance section doesn't address this, leaving the agent to guess.

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** Add to the CLAUDE.md Synthesis guidance section, after "It should reflect the current state of the wiki's knowledge, not just the latest source.":

```
Synthesis is analytical by nature — its `type: synthesis` signals that
all content represents your integrated understanding. Write in prose
without per-claim callout wrappers. If you reference a specific source
directly, use a `[!source]` callout for that claim. Otherwise, the page
is implicitly `[!analysis]`.
```

**Rationale:** This exempts synthesis.md from the per-claim callout requirement while preserving the principle. The page-level type serves the same epistemic function: readers know this is the agent's synthesis, not sourced fact.

---

## Change 3: Clarify `sources` field on source-summary pages

**Problem:** The source-summary template has `sources: []` in its frontmatter. A source-summary page summarizes a raw source — its provenance comes from `raw_path`, not from other source-summary pages. The agent may be confused about what should go in `sources` and attempt to fill it incorrectly (self-reference, or leave it looking "incomplete").

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** Add to the CLAUDE.md "Other Conventions" section:

```
- For source-summary pages, provenance comes from `raw_path`.
  The `sources` field is typically `[]` unless the summary draws on
  other source-summary pages (e.g., a review paper referencing
  earlier sources already in the wiki).
```

**Rationale:** Eliminates ambiguity without changing the schema. The field stays in the template for the rare case where it's useful; the convention tells the agent not to force-fill it.

---

## Change 4: Add concrete index split threshold

**Problem:** The revision removed the index token budget, replacing it with "keep entries concise" and "split into per-category indexes when unwieldy." But "unwieldy" is subjective, and the community's strongest operational warning ([372.md]) was that unbounded index files cause Claude Code's context compaction to silently drop CLAUDE.md conventions. The agent has no signal for when to split.

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** In the CLAUDE.md Index Format section, after "When the index becomes unwieldy, split into per-category indexes.", add:

```
Rule of thumb: split when the index exceeds ~100 entries.
```

**Rationale:** 100 entries is concrete enough to act on, loose enough to adapt. It's based on the community's reported ~200-page retrieval ceiling — splitting at 100 entries keeps each category index well under that threshold. This honors PHILOSOPHY's "start simple, add infrastructure when earned" by naming the specific earned point.

---

## Change 5: Elevate dual output to a universal convention

**Problem:** The critical synthesis rated "every task produces two outputs" as Tier 1. The implementation captures it partially — query guidance mentions updating wiki pages as a side effect — but doesn't elevate it to a principle that applies to all operations. PHILOSOPHY's "everything compounds" says every interaction should make the wiki more valuable.

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** Add to the CLAUDE.md "Other Conventions" section:

```
- Every ingest and query updates the wiki — not just answers the
  immediate question. Index, log, and synthesis updates are part of
  the deliverable, not afterthoughts.
```

**Rationale:** This makes the compounding principle operational. The agent already does most of this for ingest (the principles list index/synthesis/log updates). This convention ensures query operations get the same treatment and that the agent treats wiki maintenance as integral, not optional.

---

## Change 6: Acknowledge the ingestion gap in plan.md

**Problem:** Head-to-head tests ([320.md]) found a mostly-built wiki performed 17% worse than a fully compiled one. A wiki at 60% coverage can mislead rather than help, because partial cross-references and incomplete synthesis create false confidence. The plan pushes for 4+ sources in Phase 4 but doesn't set expectations about when the wiki becomes reliable.

**Files changed:** `plan.md`

**Change:** Add a note to the Phase 4 introduction, after "Build real cross-references. Refine the schema.":

```
**Note:** A partially-built wiki can underperform no wiki at all —
incomplete cross-references and partial synthesis can mislead rather
than help. The wiki's value compounds after a minimum coverage
threshold. Treat the wiki as a work-in-progress until cross-references
form a meaningful web and synthesis reflects multiple sources. This
phase is where the wiki crosses that threshold.
```

**Rationale:** Sets honest expectations. Doesn't change the plan structure — Phase 4 already targets this. Just names the phenomenon so the builder knows why Phase 4 matters and doesn't declare victory after a single ingest.

---

## Change 7: Flag "diffs not overwrites" for Phase 4 review

**Problem:** The critical synthesis rated "LLM proposes diffs, not overwrites" as Tier 1. The implementation says "prefer targeted updates over full page rewrites" — a weaker convention that doesn't require the agent to show proposed changes before committing. For V1 with human supervision this is acceptable, but the gap should be tracked for review as supervision decreases.

**Files changed:** `plan.md`

**Change:** Add a bullet to Phase 4.3 ("Review and Evolve the Schema"), in the review questions list:

```
- Is "prefer targeted updates" sufficient, or should the agent show
  proposed diffs before committing? (More important as supervision
  decreases.)
```

Also add to `plan-checklist.md` Phase 4.3:

```
  - [ ] Reviewed whether diff-before-commit convention is needed
```

**Rationale:** No change to V1 behavior. The current convention is adequate for supervised operation. This just ensures the question gets asked at the right time (Phase 4 schema review) rather than forgotten.

---

## Change 8: Note on revisions file format

**Problem:** `revisions/revisions-1.md` contains the full text of the revised proposal, plan, and checklist — duplicating every top-level file. If someone edits the top-level files, the copies in revisions-1.md drift silently.

**Recommendation (not a file change):** Going forward, revisions files contain rationale and diffs only (as this file does). The top-level files are the single source of truth. `revisions-1.md` is treated as a frozen historical snapshot and should not be kept in sync with future edits to the top-level files.

---

## Summary

| # | Change | Files | Complexity |
|---|--------|-------|------------|
| 1 | Complete synthesis.md frontmatter | implementation-proposal, plan, revisions-1 | Trivial |
| 2 | Claim typing guidance for synthesis | implementation-proposal (CLAUDE.md) | One paragraph |
| 3 | Clarify source-summary `sources` field | implementation-proposal (CLAUDE.md) | One bullet |
| 4 | Index split threshold (~100 entries) | implementation-proposal (CLAUDE.md) | One line |
| 5 | Dual output as universal convention | implementation-proposal (CLAUDE.md) | One bullet |
| 6 | Ingestion gap note | plan | One paragraph |
| 7 | Diff-before-commit review flag | plan, plan-checklist | One bullet each |
| 8 | Revisions format note | N/A (convention) | N/A |

No architectural changes. No new deliverables. No removed features. All changes either fix data contract compliance (1-3), add concrete thresholds where the community reported failures (4), elevate partially-captured principles (5-6), or track a deferred decision (7).
