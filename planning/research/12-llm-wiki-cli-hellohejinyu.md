# llm-wiki CLI (hellohejinyu)

**Source:** https://github.com/hellohejinyu/llm-wiki
**Stars:** 50 | **Forks:** 11 | **Languages:** TypeScript 84.9%, Handlebars 9.7%, JavaScript 5.4% | **License:** MIT

## Description

Open-source command-line tool that builds and maintains a persistent, interlinked personal knowledge base. Uses LLMs to incrementally integrate sources into structured wiki pages with automatic cross-linking and citation tracking.

## Core Features

| Feature | Purpose |
|---------|---------|
| Smart Ingestion | LLM parses raw materials into structured wiki pages with citations |
| Automatic Linking | Cross-references new knowledge with existing pages |
| Multi-Step Retrieval | ReAct agent iteratively dives into source files |
| Wiki Lint | Detects orphans, dead links, contradictions, shallow content |
| List Tools | Browse raw sources, wiki pages, backlink relationships |
| Zero Lock-in | Pure Markdown; compatible with Obsidian, VS Code, any editor |
| LLM Flexibility | OpenAI, Anthropic, DeepSeek, Ollama, any OpenAI-compatible API |

## Commands

| Command | Function |
|---------|----------|
| `wiki init` | Scaffold structure and generate `.wikirc.yaml` |
| `wiki raw` | Interactively add sources with metadata |
| `wiki ingest` | Process raw sources into wiki |
| `wiki query` | Ask questions with citations |
| `wiki list` | Browse files, pages, orphans, backlinks |
| `wiki lint` | Static + semantic analysis with auto-fix |

## Architecture

```
raw/untracked/  – New sources awaiting processing
raw/ingested/   – Processed sources (archived)
wiki/index.md   – Auto-maintained index
wiki/concepts/  – LLM-generated concept pages
wiki/sources/   – Source attribution pages
wiki/answers/   – Saved query responses
```

## Tech Stack

- Runtime: Node.js 22+
- Package Manager: pnpm
- Build Tool: tsup
- Config: `.wikirc.yaml` (auto-gitignored)

## What Makes It Unique

- Knowledge accumulation (wiki persists and grows unlike ephemeral RAG)
- Citation tracking (all answers traceable to sources)
- ReAct agent for multi-step retrieval
- Multiple LLM provider support
- References Vannevar Bush's 1945 Memex concept
