# claude-obsidian (AgriciDaniel)

**Source:** https://github.com/AgriciDaniel/claude-obsidian
**Stars:** 1.3k | **Forks:** 140 | **License:** MIT

## Description

AI-powered knowledge management system integrating Claude with Obsidian to create a self-organizing wiki vault. Implements Karpathy's LLM Wiki pattern with autonomous organization, cross-referencing, and maintenance.

## Core Features

**Autonomous Operations:**
- `ingest`: Reads sources and creates 8-15 interconnected wiki pages automatically
- `query`: Answers questions by scanning index and citing specific wiki pages
- `lint`: Identifies orphaned pages, dead links, stale claims, missing cross-references
- `/autoresearch`: Three-round autonomous research with gap-filling
- `/save`: Files conversations as structured wiki notes
- `/canvas`: Visual layer for images, PDFs, pinned notes

**Knowledge Management:**
- Hot cache system persists recent context between sessions
- Contradiction flagging with source citations
- Multi-model support (Claude, Gemini, Codex, Cursor, Windsurf)
- Batch ingestion with parallel processing
- Six wiki modes (Website, GitHub, Business, Personal, Research, Book/Course)

## Architecture

```
skills/     - 10 skill modules (wiki, ingest, query, lint, save, autoresearch, canvas)
agents/     - Parallel ingestion and health-check agents
commands/   - CLI-style command implementations
hooks/      - Session start/stop handlers updating hot cache
_templates/ - Obsidian Templater automations
wiki/       - Vault structure with index, concepts, entities, sources, meta dashboards
```

## Tech Stack

- Obsidian (note-taking platform)
- Claude Code (AI execution)
- Shell scripting (setup automation)
- Obsidian Bases (native database dashboard)
- Obsidian Templater (automation)
- Optional: Local REST API plugin (MCP server), Obsidian Git, Calendar, Thino, Excalidraw, Dataview

## What Makes It Unique

- Creates and organizes notes autonomously (not just chat interface)
- Maintains vault health with contradiction detection
- Persistent session memory via hot cache
- Parallel batch ingestion
- 8-category lint system
- Visual canvas integration with autonomous layouts
- Pre-seeded with concepts and entities to bootstrap wiki

## Community

- 2,800+ member AI Marketing Hub community
- YouTube tutorial channel
- Companion plugin: claude-canvas (12 templates, 6 layout algorithms)
