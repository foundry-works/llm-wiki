# LLM Wiki (Karpathy's Original Gist)

**Source:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Core Concept

Andrej Karpathy's gist proposes a pattern for maintaining personal knowledge bases where LLMs incrementally build and sustain structured markdown wikis rather than repeatedly retrieving from raw documents.

**Key distinction:** "The wiki is a persistent, compounding artifact" instead of performing retrieval-augmented generation on each query.

## Three-Layer Architecture

**Raw sources** — Immutable curated documents (articles, papers, images, data files) that LLMs read but never modify.

**The wiki** — LLM-generated markdown files organized by summaries, entity pages, concept pages, comparisons, and syntheses. The LLM fully owns this layer.

**The schema** — Configuration document (CLAUDE.md or AGENTS.md) specifying wiki structure, conventions, and workflows for ingesting sources and maintaining consistency.

## Three Core Operations

**Ingest:** New source documents trigger LLM processing—reading, extracting key information, updating entity pages, flagging contradictions, and maintaining cross-references across 10-15 wiki pages per source.

**Query:** Users ask questions; LLMs search relevant pages, synthesize answers with citations, and file valuable results back into the wiki for future compounds.

**Lint:** Periodic health checks identifying contradictions, stale claims, orphan pages, missing cross-references, and data gaps requiring investigation.

## Supporting Infrastructure

**index.md** — Content-oriented catalog listing every wiki page with summaries, organized by category, updated at each ingest.

**log.md** — Append-only chronological record of ingests, queries, and lint passes with consistent prefixes for parsing via Unix tools.

## Practical Implementation

Users interact through Obsidian (markdown editor) on one side while the LLM operates on the other. The LLM handles summarizing, cross-referencing, filing, and bookkeeping while humans source materials and ask strategic questions.

## Use Cases Mentioned

- Personal goal and psychology tracking
- Research paper deep-dives
- Book chapter organization building companion wikis
- Team/business internal wikis fed by Slack transcripts and meeting notes
- Competitive analysis, due diligence, trip planning, hobby exploration

## Why This Works

"The tedious part of maintaining a knowledge base is not the reading...it's the bookkeeping." LLMs excel at updating cross-references, maintaining consistency, and touching multiple files simultaneously—tasks humans abandon. The human curates sources and directs analysis; the LLM handles everything else.

## Optional Tooling

- **Web Clipper** — Browser extension converting articles to markdown
- **Local image downloads** — Obsidian settings allow attachment storage
- **Graph view** — Visualizes wiki connectivity
- **Marp** — Markdown-based slide generation
- **Dataview** — Obsidian plugin querying frontmatter metadata
- **qmd** — Local markdown search engine with BM25/vector hybrid search

## Critical Design Notes

The document explicitly states this is intentionally abstract, describing a pattern rather than implementation. Directory structure, schema conventions, page formats, and tooling depend on domain, user preference, and LLM choice. Users should collaborate with their LLM to instantiate versions matching their specific needs.

## Community Extensions & Implementations

The gist generated extensive discussion with multiple implementations:

- **OmegaWiki** — 23 Claude Code skills, typed entities, bilingual support
- **Synthadoc** — Production-grade implementation with async ingestion, domain scaffolding, plugin architecture
- **Nimbalyst** — Integrated markdown editor with automated daily/weekly maintenance schedules
- **Graphite Atlas** — Property graph approach with Cypher queries, multi-user collaboration
- **AgentWiki** — Autonomous newsletter ingestion with daily updates
- **AIOS** — Linux-based AI operating environment treating wiki as system primitive
- **llmwiki-cli** — Node.js CLI tool with Git backend, interactive visualization

## Criticism & Tensions

Comments raised substantial concerns:

- **Data corruption risk** — LLM errors compound without human validation
- **Scaling limitations** — Markdown-based systems collapse at thousands of pages
- **Schema entropy** — Without rigorous curation, contradictions accumulate
- **Architectural confusion** — Many implementations revert to RAG despite non-RAG intentions
- **Personal vs. team utility** — Knowledge bases exhibit value asymmetries across users with different roles
- **Maintenance burden underestimation** — The claim that LLMs eliminate bookkeeping overlooks validation requirements

## Historical Context

References Doug Engelbart's 1945 Memex concept and Open Hyperdocument System, noting that the original vision prioritized curated, privately-controlled knowledge with meaningful associative trails—elements this pattern attempts to revive through LLM-assisted maintenance.
