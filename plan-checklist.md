# Implementation Checklist

Tracks progress on the LLM Wiki implementation. See `plan.md` for details on each step.

---

## Phase 0: Prerequisites & Environment

- [ ] **0.1** Obsidian 1.12.7+ installed, CLI enabled, `obsidian version` works
- [ ] **0.2** `git --version` and `shasum --version` both work
- [ ] **0.3** Vault created or chosen, open in Obsidian desktop app
- [ ] **0.4** Obsidian settings configured:
  - [ ] Default note location -> `wiki/`
  - [ ] Attachment folder -> `raw/assets/`
  - [ ] Template folder -> `templates/`
  - [ ] Templates core plugin enabled
- [ ] **0.5** Git initialized in vault root with `.gitignore`

---

## Phase 1: Vault Directory Structure

- [ ] **1.1** Directories created:
  - [ ] `raw/`
  - [ ] `raw/assets/`
  - [ ] `wiki/entities/`
  - [ ] `wiki/concepts/`
  - [ ] `wiki/sources/`
  - [ ] `wiki/comparisons/`
  - [ ] `templates/`
  - [ ] `scripts/`
- [ ] **1.2** `wiki/index.md` created (empty scaffold with category headers)
- [ ] **1.3** `wiki/synthesis.md` created (empty scaffold with frontmatter)
- [ ] **1.4** Committed to git

---

## Phase 2: Templates

- [ ] **2.1** `templates/entity.md` written (frontmatter + TLDR + callout sections)
- [ ] **2.2** `templates/concept.md` written
- [ ] **2.3** `templates/source-summary.md` written
- [ ] **2.4** `templates/comparison.md` written
- [ ] **2.5** CLI template creation tested:
  - [ ] `obsidian create ... template=entity` works
  - [ ] Frontmatter intact in created page
  - [ ] `{{date}}` resolved correctly
  - [ ] If template= doesn't work: fallback approach documented
  - [ ] Test page cleaned up
- [ ] **2.6** Committed to git

---

## Phase 3: Supporting Scripts

- [ ] **3.1** `scripts/hash-sources.sh` written and `chmod +x`
- [ ] **3.2** hash-sources.sh tested:
  - [ ] Produces valid JSON output
  - [ ] Hash matches `shasum -a 256` directly
  - [ ] Empty raw/ returns `{}`
  - [ ] Handles filenames with spaces
- [ ] **3.3** `scripts/check-stale.sh` written and `chmod +x`
- [ ] **3.4** check-stale.sh tested:
  - [ ] Detects stale page (bad hash in frontmatter)
  - [ ] Reports clean when hashes match
  - [ ] Frontmatter parsing works with actual `property:set` output format
  - [ ] If nested YAML parsing fails: fallback approach decided and documented
- [ ] **3.5** `scripts/build-index.sh` written and `chmod +x`
- [ ] **3.6** build-index.sh tested:
  - [ ] Produces valid markdown output
  - [ ] TLDR extraction works
  - [ ] Handles pages without TLDRs
- [ ] **3.7** Test artifacts cleaned up
- [ ] **3.8** Committed to git

---

## Phase 4: The Skill File

- [ ] **4.1** `CLAUDE.md` written with all sections:
  - [ ] Role definition
  - [ ] Vault structure reference
  - [ ] Ingest operation workflow with CLI commands
  - [ ] Query operation workflow with CLI commands
  - [ ] Lint operation workflow with CLI commands
  - [ ] Claim typing rules
  - [ ] Provenance rules
  - [ ] Index rules (token budget, TLDR requirement)
  - [ ] Conventions
  - [ ] Accumulated Corrections section (empty)
- [ ] **4.2** CLI commands adjusted based on Phase 2/3 findings
- [ ] **4.3** Committed to git

---

## Phase 5: Smoke Test — Ingest

- [ ] **5.1** Real source document added to `raw/`
- [ ] **5.2** Ingest run via Claude Code
- [ ] **5.3** Results verified:
  - [ ] Source summary page created in `wiki/sources/`
  - [ ] Frontmatter populated (raw_path, source_hash, date, tags)
  - [ ] TLDR present and accurate
  - [ ] Key takeaways use `[!source]` callouts
  - [ ] Entity pages created in `wiki/entities/`
  - [ ] Concept pages created in `wiki/concepts/`
  - [ ] No duplicate pages (search performed before creation)
  - [ ] `wiki/index.md` updated with new pages and TLDRs
  - [ ] Source hash in frontmatter matches `hash-sources.sh` output
  - [ ] All claims properly typed (no bare claims outside callouts)
  - [ ] Source callouts include `[[source-page]]` links
  - [ ] Analysis callouts show reasoning
  - [ ] Uncertain claims marked `[!unverified]`
- [ ] **5.4** Issues recorded, corrections added to CLAUDE.md
- [ ] **5.5** Committed to git

---

## Phase 6: Smoke Test — Query

- [ ] **6.1** Question asked requiring multi-page synthesis
- [ ] **6.2** Query workflow verified:
  - [ ] Index consulted first
  - [ ] `obsidian search` used for specifics
  - [ ] Relevant pages read
  - [ ] Links followed (backlinks/outgoing)
  - [ ] Answer cites specific wiki pages
  - [ ] Sourced claims distinguished from inferences
- [ ] **6.3** Dual output verified:
  - [ ] Wiki pages updated as side effect (if applicable)
  - [ ] Gaps marked with `[!gap]` (if applicable)
  - [ ] Valuable answer filed as new page (if applicable)
- [ ] **6.4** Issues recorded, committed to git

---

## Phase 7: Smoke Test — Lint

- [ ] **7.1** Lint run via Claude Code
- [ ] **7.2** Each check verified:
  - [ ] `check-stale.sh` ran without errors
  - [ ] `obsidian orphans` ran
  - [ ] `obsidian deadends` ran
  - [ ] `obsidian unresolved` ran
  - [ ] `[!unverified]` search ran
  - [ ] `[!gap]` search ran
  - [ ] `build-index.sh` compared to current index
  - [ ] Summary report presented
  - [ ] No fixes applied without human approval
- [ ] **7.3** Issues recorded, committed to git

---

## Phase 8: Iteration & Refinement

- [ ] **8.1** Additional sources ingested (target: 3-5 more):
  - [ ] Source 2 ingested and reviewed
  - [ ] Source 3 ingested and reviewed
  - [ ] Source 4 ingested and reviewed
  - [ ] Cross-references created correctly between sources
  - [ ] Existing pages updated (not duplicated)
  - [ ] Contradictions surfaced (not smoothed)
  - [ ] Index staying manageable
- [ ] **8.2** Staleness detection tested:
  - [ ] Raw source modified
  - [ ] `check-stale.sh` reports stale pages
  - [ ] Re-ingest updates affected pages
  - [ ] Hashes refreshed in frontmatter
- [ ] **8.3** CLAUDE.md corrections reviewed and updated
- [ ] **8.4** Template fitness assessed:
  - [ ] Entity template adequate for domain?
  - [ ] Concept template adequate?
  - [ ] Source summary template adequate?
  - [ ] Comparison template adequate?
  - [ ] Additional template needed? (if so, created)
- [ ] **8.5** Final commit

---

## Completion Criteria

- [ ] All 8 deliverable files exist and are committed:
  - [ ] `CLAUDE.md`
  - [ ] `templates/entity.md`
  - [ ] `templates/concept.md`
  - [ ] `templates/source-summary.md`
  - [ ] `templates/comparison.md`
  - [ ] `scripts/hash-sources.sh`
  - [ ] `scripts/check-stale.sh`
  - [ ] `scripts/build-index.sh`
- [ ] End-to-end ingest tested with correct claim typing and provenance
- [ ] Query tested with citations and dual output
- [ ] Lint tested with all checks producing a report
- [ ] Staleness detected and recompiled at least once
- [ ] CLAUDE.md has at least one accumulated correction
- [ ] Wiki has 4+ ingested sources with cross-referenced pages
