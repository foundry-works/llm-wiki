# LLM Wiki

A large language model (LLM) that builds and maintains a personal knowledge wiki from your source documents. You feed it sources — papers, articles, reports, transcripts — and it extracts the knowledge, integrates it with what's already known, and surfaces contradictions. It builds cross-references and maintains the whole thing over time. The result is a persistent, compounding knowledge base in plain markdown — browsable in any editor, or in Obsidian for graph view and backlinks.

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

Every Obsidian CLI call has a grep/file-I/O fallback in the schema, so Obsidian is the preferred path, not a required one.

## Getting started

Install the repo and a launcher on your `PATH`:

```sh
curl -fsSL https://raw.githubusercontent.com/tylerburleigh/llm-wiki/main/install.sh | sh
```

This clones the repo to `~/.local/share/llm-wiki` and symlinks `scripts/new-wiki.sh` to `~/.local/bin/llm-wiki-new`. Override with `LLM_WIKI_DIR` / `LLM_WIKI_BIN` if you prefer different paths. Re-run the installer to update.

Then spawn your first wiki:

```sh
llm-wiki-new ~/wikis/my-wiki --git
cd ~/wikis/my-wiki
# edit purpose.md, drop a source into raw/, then:
claude     # and invoke: /wiki-ingest raw/<your-source>
```

If you'd rather not pipe `install.sh` into a shell, clone manually and run `scripts/new-wiki.sh` directly — the launcher is just a convenience.

Obsidian is optional. The vault is plain markdown and every agent operation has a grep/file-I/O fallback; Obsidian only adds graph view, backlinks panel, and live wikilink rendering for human browsing.

## What's here

### Source material

- **`wiki-base/`** — Scaffolding for a new wiki: an empty Obsidian vault skeleton (`CLAUDE.md` schema, templates, empty `index.md`/`log.md`/`synthesis.md`), three Claude Code skills (`/wiki-ingest`, `/wiki-query`, `/wiki-purpose`), the `wiki-extractor` and `wiki-auditor` subagents that back ingest, and `scripts/wiki-lint.py` for deterministic schema validation. This is the headline deliverable — `llm-wiki-new` (after `install.sh`) spawns a fresh wiki from it.

- **`scripts/new-wiki.sh`** — Spawns a new wiki from `wiki-base/` into a target directory. Creates the expected subdirectories (entities, concepts, sources, comparisons, raw/assets) with `.gitkeep` files. Pass `--git` to initialize a fresh git repo for the new wiki, `--force` to overwrite an existing target. `install.sh` symlinks this as `llm-wiki-new` on your `PATH`; direct invocation is the manual-install path.

- **`install.sh`** — One-shot installer. Clones the repo to `~/.local/share/llm-wiki` and symlinks `scripts/new-wiki.sh` as `llm-wiki-new` in `~/.local/bin`. See [Getting started](#getting-started).

- **`PHILOSOPHY.md`** — The principles behind the LLM Wiki design. Covers: compilation over retrieval, agent as writer (not pipeline), strict data contracts with flexible workflows, epistemic integrity via claim typing, human-as-editor-in-chief, schema co-evolution, and compounding value.

- **`CHANGELOG.md`** — Revision-by-revision log of changes to the proposal and plan during the design phase.

## Reading order

To use the tool: [Getting started](#getting-started) -> `wiki-base/CLAUDE.md` (schema reference) -> the relevant skill docs under `wiki-base/.claude/skills/`.

For the design rationale: `PHILOSOPHY.md`.
