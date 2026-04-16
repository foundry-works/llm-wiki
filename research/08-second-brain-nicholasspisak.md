# second-brain (NicholasSpisak)

**Source:** https://github.com/NicholasSpisak/second-brain
**Stars:** 160 | **Forks:** 20 | **License:** Open Source

## Description

LLM-powered personal knowledge management system for Obsidian. Implements Karpathy's LLM Wiki pattern by automating organization of raw source materials into a structured, interconnected wiki.

## Core Features

**Four Primary Skills:**
- `/second-brain` — Guided setup wizard for new vaults
- `/second-brain-ingest` — Processes raw sources into wiki pages
- `/second-brain-query` — Question-answering against wiki content
- `/second-brain-lint` — Health checks and consistency verification

**Optional Integrations:**
- Obsidian Web Clipper for capturing articles
- `summarize` tool for link and media summaries
- `qmd` for local markdown search
- `agent-browser` for automated web research

## Vault Structure

```
your-vault/
├── raw/              # Source inbox
├── wiki/             # LLM-generated content
│   ├── sources/      # Source summaries
│   ├── entities/     # People, orgs, products
│   ├── concepts/     # Ideas, frameworks
│   ├── synthesis/    # Analysis, comparisons
│   ├── index.md      # Master catalog
│   └── log.md        # Operation history
└── output/           # Generated reports
```

## Tech Stack

- Markdown-based (all content in .md files)
- Obsidian (primary browsing interface with graph visualization)
- Node.js (required for skill installation)
- Multi-agent compatible (Claude Code, Cursor, Gemini CLI, Codex, 40+ agents via Agent Skills standard)
- Shell scripting (100% implementation)

## Installation

Single command: `npx skills add NicholasSpisak/second-brain`

## What Makes It Unique

- Agent-agnostic via standardized Agent Skills protocol
- Works across 40+ AI platforms
- Idempotent setup (safe to re-run)
- Pattern-based approach implementing proven Karpathy methodology
- Minimal footprint — pure shell scripts, no complex dependencies
