# Revisions (Round 3)

Changes to `implementation-proposal.md`, `plan.md`, and `plan-checklist.md` based on a comparative review of all planning documents against `llm-wiki.md`, `PHILOSOPHY.md`, `intermediate/`, `synthesis/`, and the Round 1-2 revisions.

Key themes of this revision:
1. **Complete the data contracts.** File naming is a spec-level concern that tooling depends on -- wikilinks, graph view, and backlink resolution all resolve by filename.
2. **Test what you depend on.** Lint's structural checks rely on CLI commands that are never verified. Either test them or document the fallback.
3. **Add guidance where the agent needs a starting point.** Source granularity and page length are judgment calls, but the agent benefits from a sensible default -- the same way the ~100 entry index split gives it a concrete threshold.
4. **Surface a likely failure mode.** Bare claims outside callouts is the path of least resistance for the LLM and the most common way epistemic integrity breaks silently.
5. **Keep revisions lean.** Rationale and diffs only. Top-level files are the source of truth.

---

## Change 1: Add file naming convention to specifications

**Problem:** The specs define directory placement, frontmatter schema, TLDR format, index format, log format, and cross-reference format -- but not how pages are *named*. Wikilinks resolve by filename. If the agent creates `transformer-architecture.md` but another page links to `[[Transformer Architecture]]`, the link breaks in Obsidian. This is a data contract -- graph view, backlink resolution, orphan detection, and the index all depend on filenames matching wikilink text.

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** Add a new subsection to the CLAUDE.md Specifications section, after "Cross-References" and before "Index Format":

```markdown
### Page Naming

Page filenames use Title Case with spaces: `Transformer Architecture.md`,
linked as `[[Transformer Architecture]]`. The filename must match the
wikilink text exactly -- Obsidian resolves links by filename.

No special characters beyond spaces and hyphens. If a page name is
ambiguous, disambiguate with a parenthetical: `Mercury (Planet).md`.
```

**Rationale:** This is the same kind of data contract as wikilink format or directory placement. Tools depend on it. Without it, the agent will default to whatever naming it feels like -- and inconsistency breaks cross-references silently.

---

## Change 2: Test lint CLI commands in Phase 1.4

**Problem:** Lint (Phase 3.2) depends on `obsidian orphans`, `obsidian deadends`, and `obsidian unresolved`. These commands are never tested. Phase 1.4 tests `obsidian create` and `obsidian search`, and the risk register covers those with fallbacks. But if the graph commands don't work (wrong syntax, require a plugin, only work with the app running), the entire lint structural check fails with no documented alternative.

**Files changed:** `plan.md`, `plan-checklist.md`

**Change in `plan.md`:** Add to Phase 1.4, after the CLI template creation test:

```markdown
Also verify the graph commands used by lint:

```bash
obsidian orphans
obsidian deadends
obsidian unresolved
```

If any don't work: the agent can compute these by reading the file tree
and parsing wikilinks directly. Document which commands work and which
need the manual fallback. This determines how CLAUDE.md references lint
operations.
```

**Change in `plan-checklist.md`:** Add to Phase 1.4:

```markdown
  - [ ] Lint graph commands tested (`obsidian orphans`, `deadends`, `unresolved`) or fallback documented
```

**Change in `plan.md` risk register:** Add a row:

```
| Lint graph commands (`obsidian orphans/deadends/unresolved`) don't work as expected | Medium | Medium | Test in Phase 1.4. Fallback: agent reads file tree and parses wikilinks manually. More expensive but no CLI dependency. |
```

**Rationale:** Same logic as the existing `obsidian create template=` risk. If you depend on it, test it early and have a fallback.

---

## Change 3: Add source granularity guidance

**Problem:** The original llm-wiki.md mentions "filing each chapter as you go" for books, implying chapter-level source granularity. The proposal gives no guidance on whether a 50-page paper should be ingested as one source or broken into sections. This will matter in Phase 2 when the user picks their first real source. Too long produces shallow extraction; too granular fragments provenance.

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** Add to the CLAUDE.md Ingest guidance section, after "Commit via git.":

```
For long sources (books, lengthy reports), ingest chapter by chapter or
section by section. Each chunk gets its own source-summary page. This
produces better extraction than ingesting a full document at once.
```

**Rationale:** This is guidance, not a spec -- it says what works well, not what's required. The agent can still exercise judgment about where to split. But without any starting point, it will default to ingesting a 40-page paper as a single source and produce a shallow summary.

---

## Change 4: Add bare-claims risk to risk register and Phase 2 verification

**Problem:** The risk register flags "LLM marks inferences as `[!source]`" (Medium likelihood, High impact). But there's an equally likely failure mode: the LLM writes substantive claims as regular prose *outside any callout at all*. Normal markdown is the LLM's default output format. Wrapping every claim in a callout is unusual behavior that requires constant discipline. Phase 2.3 partially checks for this ("No bare claims outside callout blocks?") but it's not in the risk register and the mitigation isn't explicit.

**Files changed:** `plan.md`

**Change:** Add a row to the risk register:

```
| LLM writes substantive claims as regular prose (no callout) | High | High | CLAUDE.md claim typing spec emphasizes this. Review in Phase 2. If it happens, add an explicit correction to Wiki Conventions: "Every factual or analytical statement must be inside a typed callout." |
```

**Rationale:** This is the most natural way for an LLM to violate epistemic integrity -- not by mislabeling a claim, but by not labeling it at all. PHILOSOPHY says "epistemic integrity is a first-class concern" and "the failure mode is silent." Naming this risk explicitly makes it visible during Phase 2 review.

---

## Change 5: Add page length guidance

**Problem:** Only synthesis.md has a length guideline (~1,000 words). Entity, concept, and other page types have no length guidance. After several ingests, entity pages can grow past 3,000 words. When the agent reads these during a query, they consume significant context. The TLDR-first design helps (the agent can decide whether to read further), but there's no signal for when a page has grown too large and should be split.

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** Add to the CLAUDE.md "Other Conventions" section:

```
- If a page grows past ~1,500 words, consider splitting it. An entity
  page might spawn a dedicated comparison, timeline, or sub-topic page.
  Each sub-page gets its own frontmatter, TLDR, and index entry.
```

**Rationale:** Same pattern as the ~100 entry index split threshold from revisions-2. A concrete-enough number to act on, loose enough to adapt. Keeps individual pages within a size the agent can read without consuming excessive context.

---

## Change 6: Trim log format note

**Problem:** The log format (`## [YYYY-MM-DD] operation | description`) makes every entry an H2 heading. At 100+ entries, Obsidian's outline pane becomes a wall of headings. The current format prioritizes grep-parsability, which is the right tradeoff for the LLM and for unix tools. But a minor adjustment preserves parsability while keeping the outline usable.

**Files changed:** `implementation-proposal.md` (the CLAUDE.md content within it)

**Change:** In the CLAUDE.md Log Format section, change:

```markdown
# Before
`wiki/log.md`: append-only. Each entry:
`## [YYYY-MM-DD] operation | description`

# After
`wiki/log.md`: append-only. Each entry:
`### [YYYY-MM-DD] operation | description`
```

Also update the corresponding log format in the Specifications section of the proposal (outside the CLAUDE.md block) and in `plan.md` wherever the format appears.

**Rationale:** H3 instead of H2 is a minor change that keeps grep-parsability intact (`grep "^### \[" log.md | tail -5`) while making the Obsidian outline less overwhelming. The log file's H1 title (`# Wiki Log`) remains the only top-level heading; log entries nest under it properly.

---

## Summary

| # | Change | Files | Complexity |
|---|--------|-------|------------|
| 1 | File naming convention | implementation-proposal (CLAUDE.md) | One subsection |
| 2 | Test lint CLI commands | plan, plan-checklist | One paragraph + one checklist item + one risk row |
| 3 | Source granularity guidance | implementation-proposal (CLAUDE.md) | Two sentences |
| 4 | Bare-claims risk | plan | One risk register row |
| 5 | Page length guidance | implementation-proposal (CLAUDE.md) | One bullet |
| 6 | Log format H2 to H3 | implementation-proposal, plan | Find-and-replace |

No architectural changes. No new deliverables. No removed features. Changes 1 and 6 are data contract completions. Changes 2 and 4 are risk coverage. Changes 3 and 5 are guidance additions. All consistent with PHILOSOPHY: strict where tooling depends on it (1, 6), test before you depend (2), earned thresholds from community evidence (5), epistemic integrity as first-class concern (4), and flexible guidance that gives the agent a starting point without dictating procedure (3).
