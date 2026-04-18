# llm-wiki-compiler (ussumant)

**Source:** https://github.com/ussumant/llm-wiki-compiler
**Languages:** 61.1% HTML, 21.5% JavaScript, 17.4% Shell | **License:** MIT

## Description

Claude Code plugin that transforms scattered markdown files and codebases into synthesized, topic-based wikis. Implements Karpathy's LLM Knowledge Base pattern for AI agents to access compiled knowledge instead of repeatedly processing raw sources.

## Core Features

**Knowledge Compilation:**
- Batch processes 100+ markdown files into organized topic articles
- Supports both knowledge bases and entire codebases
- Auto-detects project type and generates domain-specific structures
- 84-90% token reduction compared to raw sources

**Commands:**
- `/wiki-init`: Auto-detect content, sample files, propose structure
- `/wiki-compile`: Batch compilation with incremental updates
- `/wiki-ingest`: Add single sources interactively
- `/wiki-search`: Keyword/phrase search across articles
- `/wiki-lint`: Health checks for stale articles, orphans, contradictions
- `/wiki-visualize`: Interactive knowledge graph
- `/wiki-migrate`: Transition to wiki-first approach

**Coverage Transparency:**
- High (5+ sources): Trust directly
- Medium (2-4 sources): Good overview, check raw for specifics
- Low (0-1 sources): Refer to raw sources

## Architecture

```
Raw Sources → Compilation → Topic Articles → AI Agent Reads Wiki
(13 files)    (5-10 min)   (with backlinks)   (89% fewer tokens)
```

**Codebase Mode (v2.0):**
- Discovers services in monorepos via manifest files
- Scans documentation (READMEs, ADRs, API specs, Docker configs)
- Optional deep_scan reads source code
- Generates per-service articles with dependency maps

## Cost Metrics

- **Compilation:** ~880K tokens ($13 Opus / $2.60 Sonnet) first run; ~100K daily incremental
- **Savings:** ~79K → ~8.5K tokens per session (89% reduction)
- **Break-even:** First session at Opus pricing
- **Compression:** 1,183 files → 14 articles (84x reduction)

## What Makes It Unique

- Coverage tags eliminate false confidence
- Safety first: source files never modified, wiki always regeneratable
- Staged adoption (staging → recommended → primary)
- Zero infrastructure: plugin-based, no hosted platform
- Concept discovery: auto-identifies cross-cutting patterns
