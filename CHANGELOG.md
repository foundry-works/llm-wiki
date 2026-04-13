# Changelog

## 2026-04-13 — Revision 3

Data contract completions, risk coverage, and guidance additions based on comparative review of all planning documents against source materials (`llm-wiki.md`, `PHILOSOPHY.md`, `intermediate/`, `synthesis/`). See `revisions/revisions-3.md` for full rationale.

### Added

- **Page naming convention.** Title Case with spaces, matching wikilink text exactly. Disambiguate with parentheticals. Added to Specifications in both the proposal body and the CLAUDE.md content. (`implementation-proposal.md`)
- **Lint graph command testing.** `obsidian orphans`, `deadends`, `unresolved` now tested in Phase 1.4 alongside template creation. Fallback documented: agent reads file tree and parses wikilinks manually. (`plan.md`, `plan-checklist.md`)
- **Source granularity guidance.** For long sources, ingest chapter by chapter. Each chunk gets its own source-summary page. Added to Ingest principles and CLAUDE.md Ingest guidance. (`implementation-proposal.md`)
- **Bare-claims risk.** New risk register entry: LLM writes substantive claims as regular prose outside any callout. Rated High/High. Mitigation: review in Phase 2, add explicit correction to Wiki Conventions if it occurs. (`plan.md`)
- **Page length guidance.** If a page grows past ~1,500 words, consider splitting it. Same pattern as the ~100-entry index split threshold. (`implementation-proposal.md`, CLAUDE.md Other Conventions)

### Changed

- **Log format: H2 to H3.** Log entries now use `### [YYYY-MM-DD]` instead of `## [YYYY-MM-DD]`. Preserves grep-parsability (`grep "^### \["`) while keeping the Obsidian outline usable at scale. Updated in Specifications, CLAUDE.md, and the grep example. (`implementation-proposal.md`)

## 2026-04-13 — Revision 2

Refinements to `implementation-proposal.md`, `plan.md`, and `plan-checklist.md` based on comparative review against source material. See `revisions/revisions-2.md` for full rationale.

### Changed

- **synthesis.md scaffold frontmatter completed.** Added missing `sources`, `created`, `tags` fields to comply with the spec's "every wiki page" requirement. (`plan.md`)
- **Claim typing guidance for synthesis.md.** Synthesis is implicitly analytical — `type: synthesis` signals the page is the agent's integrated understanding. Prose is fine without per-claim callout wrappers; `[!source]` used only when referencing a specific source directly. (`implementation-proposal.md`, CLAUDE.md Synthesis section)
- **Source-summary `sources` field clarified.** Convention added: provenance comes from `raw_path`; `sources` is typically `[]` unless the summary draws on other source-summary pages. (`implementation-proposal.md`, CLAUDE.md Other Conventions)
- **Index split threshold added.** Rule of thumb: split when the index exceeds ~100 entries. Based on community-reported ~200-page retrieval ceiling. (`implementation-proposal.md`, CLAUDE.md Index Format)
- **Dual output elevated to universal convention.** Every ingest and query updates the wiki — index, log, and synthesis updates are part of the deliverable, not afterthoughts. (`implementation-proposal.md`, CLAUDE.md Other Conventions)
- **Ingestion gap acknowledged.** Note added to Phase 4: a partially-built wiki can underperform no wiki at all. The wiki's value compounds after a minimum coverage threshold. (`plan.md`)
- **Diff-before-commit flagged for Phase 4 review.** Question added to schema review: is "prefer targeted updates" sufficient, or should the agent show proposed diffs? (`plan.md`, `plan-checklist.md`)

### Meta

- **Revisions format established.** `revisions-2.md` contains rationale and diffs only — no full document copies. `revisions-1.md` is a frozen historical snapshot.

## 2026-04-13 — Revision 1

Major revision to `implementation-proposal.md`, `plan.md`, and `plan-checklist.md`. Added `PHILOSOPHY.md`. See `revisions/revisions-1.md` for full rationale.

### Added

- **`PHILOSOPHY.md`** — Design philosophy document. Seven principles: compilation over retrieval, agent as writer, strict/flexible split, epistemic integrity, human as editor-in-chief, schema co-evolution, compounding value.
- **`wiki/log.md`** — Chronological operation log restored from the original `llm-wiki.md`. Append-only, parseable with `grep "^### \[" log.md | tail -5`. Integrated into all three operations.
- **`wiki/synthesis.md`** — Given a real operational role. Updated on every ingest, reviewed during lint.
- **Generative lint** — Lint now includes a conceptual review phase: the agent identifies thinly covered topics, unanswered questions, and suggested investigations. Not just structural janitorial work.
- **Specifications vs. guidance split** — CLAUDE.md reorganized into two sections: strict data contracts (frontmatter, callouts, directories, formats) and flexible guidance (goals and principles for each operation).
- **Wiki Conventions section** — Replaces "Accumulated Corrections" in CLAUDE.md. The agent actively maintains learned patterns, domain conventions, and workflow refinements — not just reactive error fixes.
- **Query output formats** — Queries can produce markdown pages, comparison tables, Marp slide decks, or other formats as appropriate. Agent chooses based on the question.

### Changed

- **Plan condensed from 9 phases to 5.** First ingest now happens in Phase 2 (second phase of work), not Phase 5. Templates, directories, CLAUDE.md, and scaffolds are all created in a single Phase 1.
- **Obsidian CLI role narrowed.** CLI used for search and graph operations (`obsidian search`, `obsidian backlinks`, `obsidian orphans`, `obsidian deadends`, `obsidian unresolved`). Direct file I/O used for reading and writing markdown. Removes hard dependency on desktop app for basic operations.
- **Operations described by goals and principles**, not numbered step-by-step procedures. The agent exercises judgment about how to accomplish each operation based on the specific source, question, or wiki state.
- **Templates: strict structure, flexible sections.** Frontmatter schema, TLDR callout, and claim typing syntax are mandatory (tools depend on them). Default section headings adapt to the domain.
- **Deliverables changed from 8 files to 8 files** (same count, different composition): 1 skill file, 4 templates, 3 wiki scaffolds. Replaces: 1 skill file, 4 templates, 3 shell scripts.
- **Risk register updated.** Removed script-related risks. Added risks for duplicate page creation and claim typing errors.
- **Success criteria updated.** Now includes log entries, synthesis updates, and Wiki Conventions entries.

### Removed

- **Shell scripts** (`hash-sources.sh`, `check-stale.sh`, `build-index.sh`) — removed from V1 deliverables. The LLM performs these operations natively. Hash-based staleness deferred to the scaling plan.
- **SHA-256 source hashes in frontmatter** (`source_hashes` field) — removed from templates. Provenance tracked via `sources` wikilinks. Git provides change history. Hash tracking available in the scaling plan if needed later.
- **Token budget on index** (was 3,000 tokens) — removed. Convention is to keep entries concise and split into per-category indexes when the single file becomes unwieldy. Agent judges when.
- **`scripts/` directory** — removed from vault structure.
- **`shasum` prerequisite** — no longer needed without hash scripts.

## 2026-04-13 — Initial documents

- `implementation-proposal.md` — Initial proposal with Obsidian CLI exclusivity, shell scripts, hash-based provenance, 8 deliverables (1 skill file, 4 templates, 3 scripts).
- `plan.md` — 9-phase plan with dependency graph.
- `plan-checklist.md` — 72-item checklist.
