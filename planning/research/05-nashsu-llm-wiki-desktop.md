# llm_wiki Desktop App (nashsu)

**Source:** https://github.com/nashsu/llm_wiki
**Stars:** 1.4k | **Forks:** 151 | **License:** GPL-3.0

## Description

Cross-platform desktop application that transforms documents into an automatically organized, interconnected knowledge base. Implements Karpathy's LLM Wiki methodology as a full-featured desktop app with substantial enhancements.

## Core Features

**Knowledge Management:**
- Two-step chain-of-thought ingest process with source traceability
- Persistent ingest queue with crash recovery
- Folder import with directory structure preservation
- Multi-format document support (PDF, DOCX, PPTX, XLSX, images, web clips)
- SHA256-based incremental caching to skip unchanged files

**Graph & Discovery:**
- Four-signal relevance model (direct links, source overlap, Adamic-Adar scoring, type affinity)
- Louvain community detection for automatic knowledge clustering
- sigma.js graph visualization with interactive exploration
- Surprising connections detection and knowledge gap identification
- Deep Research feature triggered from graph insights

**Search & Retrieval:**
- Tokenized search with CJK bigram support for Chinese content
- Optional vector semantic search via LanceDB
- Multi-phase retrieval pipeline with graph expansion
- Configurable context window (4K to 1M tokens)

**Collaboration & Review:**
- Asynchronous review system for human-in-the-loop validation
- Multi-conversation chat with persistence
- Thinking/reasoning display for models supporting extended reasoning
- Citation tracking showing which wiki pages informed each response
- Web clipper Chrome extension for one-click page capture

## Tech Stack

- **Backend:** Tauri v2 (Rust), LanceDB, pdf-extract, docx-rs, calamine
- **Frontend:** React 19, TypeScript, Vite, shadcn/ui, Tailwind CSS v4
- **Knowledge Graph:** sigma.js, graphology, ForceAtlas2, graphology-communities-louvain
- **LLM Integration:** Streaming fetch supporting OpenAI, Anthropic, Google, Ollama, custom endpoints
- **State:** Zustand, Tauri Store
- **i18n:** react-i18next (English/Chinese)

## What Makes It Unique

- **Purpose.md** — Beyond Karpathy's schema, explicitly defines wiki goals, key questions, and evolving thesis
- **Desktop-first** — Full-featured app with three-column layout, real-time activity tracking
- **4-Signal Relevance Model** — Weights: direct link x3.0, source overlap x4.0, Adamic-Adar x1.5, type affinity x1.0
- **Community Detection** — Auto-clusters knowledge areas using Louvain algorithm
- **Source Traceability** — Every page includes `sources[]` frontmatter for cascade deletion and impact analysis

## Project Structure

```
my-wiki/
├── purpose.md              # Goals and research scope
├── schema.md               # Structure and page type rules
├── raw/sources/            # Uploaded documents
├── wiki/
│   ├── index.md            # Content catalog
│   ├── overview.md         # Auto-updated summary
│   ├── entities/           # People, organizations
│   ├── concepts/           # Theories, methods
│   └── sources/            # Document summaries
└── .llm-wiki/              # App config and chat history
```
