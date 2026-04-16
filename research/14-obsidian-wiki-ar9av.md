# obsidian-wiki (Ar9av)

**Source:** https://github.com/Ar9av/obsidian-wiki
**Stars:** 383 | **Forks:** 62 | **Languages:** Python 60.6%, HTML 35.2%, Shell 4.2% | **License:** MIT

## Description

Framework enabling AI coding agents to automatically build and maintain a personal knowledge management system using Obsidian. Implements Karpathy's LLM Wiki pattern — compiling knowledge into interconnected markdown files that agents keep current.

## Core Features

**Ingest & Processing:**
- Handles markdown, PDFs, JSONL exports, plain text logs, chat transcripts, images
- Four-stage pipeline: Ingest → Extract → Resolve → Schema maintenance
- Delta tracking via `.manifest.json` prevents re-processing unchanged sources
- Staging directory (`_raw/`) for quick captures

**Knowledge Organization:**
- Project-based + global knowledge with cross-references
- Automated wikilink discovery and insertion
- Controlled tag taxonomy in `_meta/taxonomy.md`
- Provenance tracking: extracted facts vs. inferred content vs. ambiguous claims

**Quality & Analysis:**
- Linting: orphaned pages, broken links, contradictions, stale content
- Wiki insights: vault structure analysis (hubs, bridges, tag cohesion)
- Graph export: JSON, GraphML (Gephi/yEd), Neo4j Cypher, interactive HTML
- Tiered retrieval: scan titles/summaries before full page reads

## Architecture — 16 Skills

| Skill | Function |
|-------|----------|
| wiki-setup | Initialize vault |
| wiki-ingest | Process documents |
| wiki-history-ingest | Route Claude/Codex history |
| wiki-status | Ingestion status & delta |
| wiki-rebuild | Archive, rebuild, restore |
| wiki-query | Search and answer |
| wiki-lint | Quality checks |
| cross-linker | Auto-insert missing wikilinks |
| tag-taxonomy | Normalize tags |
| wiki-export | Graph export |
| wiki-update | Sync project knowledge globally |

**Agent Compatibility:** Claude Code, Cursor, Windsurf, Codex, Antigravity (Google), OpenClaw, GitHub Copilot, Kilocode

## What Makes It Unique

- Delta tracking prevents redundant re-ingestion
- Project isolation with global cross-reference
- Archive & restore for vault versioning
- Multi-source ingest (Claude/Codex history, Slack logs, transcripts)
- Multimodal support (screenshots, diagrams)
- Provenance tagging (fact vs. inference)
- Graph analytics (hubs, bridges, cohesion)
- Tiered query cost through index-first retrieval
- QMD integration for semantic search
