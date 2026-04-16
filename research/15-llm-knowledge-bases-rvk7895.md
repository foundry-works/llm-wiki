# llm-knowledge-bases (rvk7895)

**Source:** https://github.com/rvk7895/llm-knowledge-bases
**Languages:** Shell 50.7%, Python 49.3%

## Description

Claude Code plugin that transforms raw research materials into an LLM-maintained Obsidian wiki. Automates knowledge compilation with interconnected wiki articles, indexes, backlinks, and multi-depth querying.

## Core Features

**Knowledge Compilation:**
- Ingests diverse sources (articles, papers, repos, transcripts, images, datasets)
- Generates structured Obsidian vaults with auto-generated summaries and backlinks
- Creates concept articles and automated indexes

**Query System (Three Tiers):**
- Quick: wiki indexes and summaries only
- Standard: cross-reference full wiki with web search supplements
- Deep: multi-agent research pipelines with parallel web search

**Output Generation:**
- Markdown reports, Marp slides, matplotlib charts
- Saves to output directory with optional wiki integration

**Maintenance:**
- Automated health checks (broken links, orphaned content)
- Suggestions for new articles and conceptual connections
- Continuous refinement

## Architecture

```
raw/          -- Source documents
wiki/         -- Compiled Obsidian vault
output/       -- Query results and generated content
kb.yaml       -- Configuration file
CLAUDE.md     -- Claude project instructions
```

## Workflow

Place materials in `raw/` → `/kb compile` → `/kb query` → `/kb lint`

## What Makes It Unique

- Multi-agent deep research with parallel agents
- Three-tier query system
- Automatic maintenance and health checking
- Optional X/Twitter ingestion via Smaug tool
