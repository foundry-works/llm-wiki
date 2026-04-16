# Implementation Checklist

Tracks progress on the LLM Wiki implementation. See `plan.md` for details on each step.

Phases 0-1 (Init) are the domain-agnostic setup — repeatable for any new vault. Phases 2-4 are per-wiki.

---

## Phase 0: Prerequisites & Environment

- [ ] **0.1** Obsidian 1.12.7+ installed, CLI enabled, `obsidian version` works
- [ ] **0.2** `git --version` works
- [ ] **0.3** `pymupdf4llm` installed (`python -c "import pymupdf4llm"` succeeds)
- [ ] **0.4** Vault created or chosen, open in Obsidian desktop app
- [ ] **0.5** Obsidian settings configured:
  - [ ] Default note location -> `wiki/`
  - [ ] Attachment folder -> `raw/assets/`
  - [ ] Template folder -> `templates/`
  - [ ] Templates core plugin enabled
- [ ] **0.6** Git initialized with `.gitignore`

---

## Phase 1: Minimal Setup

- [ ] **1.1** Directories created: `raw/assets/`, `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/comparisons/`, `templates/`
- [ ] **1.2** Wiki scaffolds and human-owned files created:
  - [ ] `wiki/index.md` (category headers)
  - [ ] `wiki/log.md` (empty scaffold)
  - [ ] `wiki/synthesis.md` (frontmatter + TLDR + placeholder)
  - [ ] `purpose.md` (template scaffolded at vault root)
  - [ ] `writing-style.md` (full reference at vault root, per proposal)
- [ ] **1.3** Templates written:
  - [ ] `templates/entity.md`
  - [ ] `templates/concept.md`
  - [ ] `templates/source-summary.md`
  - [ ] `templates/comparison.md`
- [ ] **1.4** CLI and direct approaches tested:
  - [ ] Page creation: `obsidian create ... template=entity` or direct file I/O — working approach documented
  - [ ] Frontmatter intact, `{{date}}` resolved
  - [ ] Test page cleaned up
  - [ ] Orphan/dead-end/unresolved detection: CLI commands or file-tree parsing — working approach documented
  - [ ] Search: CLI with path scoping or `grep` — working approach documented
  - [ ] Callout search: CLI or `grep -r "\[!source\]"` — working approach documented
  - [ ] Link traversal: CLI or `grep`/file parsing — working approach documented
- [ ] **1.5** `CLAUDE.md` written:
  - [ ] Specifications section (vault layout, frontmatter, TLDR, claim typing, cross-refs, page naming, index format, log format, conventions)
  - [ ] Guidance section (writing style, ingest, query, lint, synthesis)
  - [ ] Writing Style subsection includes operational rules and points to `writing-style.md` for detail
  - [ ] `purpose.md` referenced in vault layout, ingest, and query sections
  - [ ] Wiki Conventions section (empty)
  - [ ] CLI commands adjusted based on 1.4 findings
- [ ] **1.6** Committed to git

---

## Phase 2: First Ingest

- [ ] **2.1** Real source added to `raw/`
- [ ] **2.2** Ingest run via Claude Code
- [ ] **2.3** Results verified:
  - [ ] Source summary page in `wiki/sources/` with correct frontmatter (including `raw_hash`) and TLDR
  - [ ] Entity pages in `wiki/entities/` (no duplicates, Title Case naming)
  - [ ] Concept pages in `wiki/concepts/` (no duplicates, Title Case naming)
  - [ ] All claims properly typed (source callouts have links, analysis shows reasoning, multi-source claims cite all sources)
  - [ ] Agent read `purpose.md` during ingest (if populated)
  - [ ] `wiki/index.md` updated
  - [ ] `wiki/log.md` entry appended
  - [ ] `wiki/synthesis.md` updated
- [ ] Every created/updated page reviewed (not just spot-checked)
- [ ] Corrections filed to Wiki Conventions
- [ ] **2.4** Issues recorded in CLAUDE.md Wiki Conventions
- [ ] **2.5** Committed to git

---

## Phase 3: Query & Lint Smoke Tests

- [ ] **3.1** Query tested:
  - [ ] Index consulted, search used, pages read, links followed
  - [ ] Answer cites specific wiki pages
  - [ ] Sourced claims distinguished from inferences
  - [ ] Dual output (wiki updates as side effect, if applicable)
  - [ ] Log entry appended if a new page was created
- [ ] **3.2** Lint tested:
  - [ ] Orphans, dead ends, unresolved links checked
  - [ ] Schema checks ran:
    - [ ] Frontmatter completeness per type (core + per-type fields; ISO 8601 dates; `sources`/`tags`/`subjects` as YAML lists)
    - [ ] TLDR is the first content block after frontmatter on every page
    - [ ] Filenames in Title Case, match wikilink text
    - [ ] Index consistency (every page has an entry; every entry resolves; source counts match; TLDRs match)
  - [ ] Source drift check ran (recomputed `raw_hash` for each source-summary, flagged mismatches)
  - [ ] Bare-claim heuristic ran (prose claims outside typed callouts reported as candidates; `synthesis.md` exempt)
  - [ ] Unverified claims and gaps scanned
  - [ ] Claim-audit sampling ran (2-3 `[!source]` claims verified against cited sources; rotation honored)
  - [ ] Conceptual review produced specific findings (not generic suggestions)
  - [ ] Report presented, no fixes without approval
  - [ ] Log entry appended with audited claim references
- [ ] **3.3** Issues recorded, committed to git

---

## Phase 4: Iteration & Refinement

- [ ] **4.1** Additional sources ingested (target: 3-5):
  - [ ] Source 2 ingested and reviewed
  - [ ] Source 3 ingested and reviewed
  - [ ] Source 4 ingested and reviewed
  - [ ] Cross-references correct, existing pages updated not duplicated
  - [ ] Contradictions surfaced
  - [ ] Index clean, log accumulating, synthesis evolving
- [ ] **4.2** Source update tested:
  - [ ] Raw source modified
  - [ ] Agent detects change via `raw_hash` comparison
  - [ ] Re-ingest updates affected pages
  - [ ] Updated dates refreshed
  - [ ] Unchanged source re-ingest correctly skipped (hash match)
- [ ] **4.3** Schema reviewed and evolved:
  - [ ] Wiki Conventions has entries from real use
  - [ ] Templates assessed for domain fitness
  - [ ] New page type added if needed
  - [ ] Reviewed whether diff-before-commit convention is needed
- [ ] **4.4** Committed to git

---

## Completion Criteria

- [ ] All 10 deliverables committed:
  - [ ] `CLAUDE.md`
  - [ ] `purpose.md`
  - [ ] `writing-style.md`
  - [ ] `templates/entity.md`
  - [ ] `templates/concept.md`
  - [ ] `templates/source-summary.md`
  - [ ] `templates/comparison.md`
  - [ ] `wiki/index.md`
  - [ ] `wiki/log.md`
  - [ ] `wiki/synthesis.md`
- [ ] End-to-end ingest with correct claim typing and provenance
- [ ] Query with citations and dual output
- [ ] Lint with structural + conceptual checks
- [ ] 4+ sources ingested with cross-referenced pages
- [ ] Log has entries for ingests, queries, and lint
- [ ] Synthesis updated across multiple ingests
- [ ] CLAUDE.md Wiki Conventions has entries from real use
