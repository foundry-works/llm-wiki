# LLM Wiki

A large language model (LLM) that builds and maintains a personal knowledge wiki from your source documents. You feed it sources — papers, articles, reports, transcripts — and it extracts the knowledge, integrates it with what's already known, and surfaces contradictions. It builds cross-references and maintains the whole thing over time. The result is a persistent, compounding knowledge base in plain markdown, browsable in Obsidian.

Based on [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285) and the 387 community comments it received.

## Why this exists

Most systems that combine LLMs with documents treat the LLM as a search engine — retrieve relevant chunks at query time, generate an answer, discard everything. The system rebuilds the knowledge from scratch on every question. Nothing accumulates.

The LLM Wiki makes a different bet: **compilation over retrieval**. When the LLM reads a source, it doesn't just index it — it extracts claims and labels each one (sourced fact, inference, unverified, gap). It integrates them with existing knowledge and builds cross-references. The synthesis has already been done. The connections are already there. The contradictions have already been flagged.

## Who it's for

The sweet spot is domains where knowledge accumulates across many sources and the connections between sources matter more than any individual source. It shines when sources overlap, contradict each other, and change over time — and when you need to explain the whole picture, not just find one fact.

**A researcher** building a knowledge base on automated scoring in education ingests 20 key papers. The wiki builds entity pages for each scoring system, concept pages for evaluation metrics and fairness criteria, and source summaries with provenance. After 10 ingests, asking "which approaches have been validated for formative vs. summative use?" draws from compiled knowledge across all sources. The wiki traces claims to their origins and surfaces contradictions.

**A product manager (PM)** doing competitive landscape research ingests product docs, analyst reports, and customer interviews. Entity pages track each competitor's capabilities and market position. As new reports come out, re-ingesting updates existing pages rather than creating disconnected notes. The synthesis page evolves into a living landscape doc.

**A software engineer (SWE)** onboarding onto a complex system ingests architecture docs, design docs, incident postmortems, and key PR descriptions. The wiki builds a map of the system that no single document contains — the kind of cross-referenced knowledge that normally lives only in senior engineers' heads.

In every case, the value is the same: the LLM handles the maintenance burden (cross-references, index updates, contradiction tracking, synthesis revision) that causes humans to abandon knowledge bases. The human directs, reviews, and asks questions. The wiki compounds.

## Why Obsidian CLI

The system is implemented as a Claude Code skill backed by the Obsidian command-line interface (CLI) and direct file I/O. This choice is deliberate:

- **Graph for free.** Wikilinks create an implicit knowledge graph. Obsidian's CLI commands (`orphans`, `deadends`, `unresolved`, `backlinks`, `links`) let the agent traverse and audit that graph without building graph infrastructure.
- **Search without a search engine.** `obsidian search` provides full-text search across the vault, delaying the need for SQLite Full-Text Search (FTS5) or vector search until real scale problems appear.
- **The human's reading environment.** The wiki isn't just for the LLM — the human browses it in Obsidian with graph view, backlinks panel, and Dataview queries. The same tool serves both the agent's maintenance work and the human's exploration.
- **Markdown stays the source of truth.** Obsidian is a thin layer over plain files. If you stop using Obsidian, the wiki is still markdown in git. No lock-in.

This aligns with the design philosophy: start with what markdown and existing tools give you for free, add infrastructure only when concrete bottlenecks demand it.

## What's here

### Source material

- **`llm-wiki.md`** — Karpathy's original gist. Describes the core pattern: an LLM incrementally builds and maintains a persistent wiki of interlinked markdown files, sitting between you and your raw source documents. Defines the three-layer architecture (raw sources, wiki, schema) and the three operations (ingest, query, lint).

- **`comments/`** — 387 individual comment files (`001.md` through `387.md`) extracted from the gist's comment thread. Each file is one comment: questions, implementations, critiques, tips, and discussion.

- **`obsidian-cli/`** — Reference documentation for the Obsidian CLI.
  - `cli-reference.md` — Full command reference for the Obsidian CLI (requires Obsidian 1.12.7+, desktop app running).
  - `headless-sync.md` — Documentation for Obsidian Headless Sync (npm package for syncing without the desktop app).

### Analysis (intermediate)

- **`intermediate/`** — Thematic syntheses of the comment thread, organized by comment type. These were the first analytical pass over the raw comments.
  - `01_questions.md` — Synthesis of questions raised in the thread, grouped by theme (error handling, scaling, structure, collaboration, comparisons to prior art, tooling).
  - `02_implementations.md` — Synthesis of 178 concrete implementations shared in the thread, grouped by architectural approach (filesystem, databases, provenance, agent skills, knowledge graphs, multi-agent, research, voice/mobile, local/offline, domain-specific).
  - `03_others.md` — Synthesis of 169 discussion comments: critiques, production experience reports, conceptual extensions, practical tips, prior art connections, and meta-discussion.

### Analysis (synthesis)

- **`synthesis/`** — Higher-order analysis that combines the intermediate syntheses into prioritized findings.
  - `04_intermediate_synthesis.md` — Consolidates questions, implementations, and discussion into a single document organized around the core pattern. Identifies gaps, opportunities, and concrete solutions for each theme (epistemic integrity, provenance, scaling, structure, human role, multi-agent, conceptual extensions).
  - `05_critical_synthesis.md` — Critical assessment of every proposed idea for plausibility, feasibility, effectiveness, and complexity. Identifies 6 core challenges ranked by severity, evaluates solutions in 3 tiers (implement first / implement when needed / defer or skip), and surfaces 3 underappreciated findings. Ends with a 4-phase priority stack.

### Design philosophy

- **`PHILOSOPHY.md`** — The principles behind the LLM Wiki design. Covers: compilation over retrieval, agent as writer (not pipeline), strict data contracts with flexible workflows, epistemic integrity via claim typing, human-as-editor-in-chief, schema co-evolution, and compounding value.

### Implementation

- **`implementation-proposal.md`** — Concrete proposal for implementing the LLM Wiki as a Claude Code skill backed by the Obsidian CLI (for search/graph) and direct file I/O (for reads/writes). Specifies: vault structure, four page templates with claim typing (Source/Analysis/Unverified/Gap), the full CLAUDE.md skill file with specifications/guidance split, and a scaling plan. Four operations: init (instantiate a new wiki in any vault), ingest, query, and lint — each described by goals and principles, not rigid procedures. The deliverables are domain-agnostic: one skill file, four templates, three wiki scaffolds. Domain adaptation happens through use, not upfront configuration.

- **`plan.md`** — Implementation plan in five phases. Phases 0-1 (Init) are the domain-agnostic setup — repeatable for spinning up any new wiki. Phases 2-4 are per-wiki: first ingest, query/lint smoke tests, and iteration with schema refinement. Includes a risk register and success criteria.

- **`plan-checklist.md`** — Trackable checklist version of the plan. Organized by phase, with verification steps for each deliverable.

### Revision history

- **`revisions/`** — Records of design revisions with rationale.
  - `revisions-1.md` — Round 1. Specifications/guidance split, log.md and synthesis.md restored, shell scripts removed, plan condensed from nine to five phases, Obsidian CLI exclusivity relaxed.
  - `revisions-2.md` — Round 2. Frontmatter compliance, claim typing for synthesis, index split threshold, dual output convention, ingestion gap acknowledged.
  - `revisions-3.md` — Round 3. Page naming convention, lint CLI tests, source granularity guidance, bare-claims risk, page length guidance, log format H3.
  - `revisions-4.md` — Round 4. Training period formalized, search scoping test, index entry conciseness, image handling, ingestion gap threshold strengthened. Includes philosophy check that withdrew two candidate changes.
  - `revisions-5.md` — Round 5. Callout search test, link traversal test, risk register corrections, documentation fixes.

## Reading order

For understanding the analysis: `llm-wiki.md` -> `intermediate/` (01, 02, 03) -> `synthesis/` (04, 05)

For understanding the design: `PHILOSOPHY.md` -> `implementation-proposal.md`

For building the wiki: `implementation-proposal.md` -> `plan.md` -> `plan-checklist.md`
