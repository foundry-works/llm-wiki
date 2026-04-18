# llm-wiki-agent (SamurAIGPT)

**Source:** https://github.com/SamurAIGPT/llm-wiki-agent

## Description

A coding agent skill that automatically builds and maintains a personal knowledge base. Drop markdown documents into a `raw/` directory; the agent reads, extracts knowledge, and constructs a persistent, interlinked wiki.

## Core Features

**Automated Wiki Construction:**
- Reads source documents and synthesizes into structured markdown
- Creates entity pages (people, companies, projects) automatically
- Generates concept pages for frameworks and ideas across sources
- Maintains living overview (`overview.md`) reflecting current synthesis

**Knowledge Organization:**
- `wiki/index.md` catalogs all pages (updated each ingest)
- `wiki/log.md` provides append-only operation record
- `sources/`, `entities/`, `concepts/`, `syntheses/` folders auto-populate

**Quality Control:**
- Flags contradictions between sources at ingest time
- Identifies orphaned pages and broken links
- Detects data gaps with suggestions for missing sources
- SHA256-cached graph for efficient reprocessing

**Knowledge Graph Visualization:**
- Interactive `graph.html` using vis.js and Louvain community detection
- Distinguishes wikilinks from agent-inferred relationships
- Clusters related topics through community detection
- Runs entirely locally

## Tech Stack

NetworkX, Louvain clustering, Claude AI, vis.js. Plain markdown files with optional git. Graph construction: two-pass (deterministic wikilink parsing + semantic inference with confidence scoring).

## Supported Agents

- Claude Code (via CLAUDE.md)
- Codex / OpenCode (via AGENTS.md)
- Gemini CLI (via GEMINI.md)

## What Makes It Unique

- Compiles once, keeps current (vs RAG re-derive)
- Pre-builds cross-references and surfaces contradictions immediately
- Accumulates evidence across sessions
- Designed for symlink integration with Obsidian
