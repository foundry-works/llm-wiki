# lazyqmd (AlexZeitler)

**Source:** https://github.com/AlexZeitler/lazyqmd
**Stars:** 36 | **Languages:** TypeScript 97.4% | **Status:** Active (v0.6.3)

## Description

Terminal-based UI for browsing, searching, and previewing qmd document collections. Interactive way to manage and explore knowledge bases stored in qmd format.

## Core Features

**Search (3 modes):**
- Full-text BM25 (fast, no LLM)
- Vector similarity (requires embeddings)
- Hybrid query with auto-expansion
- Structured prefixes: `lex:`, `vec:`, `hyde:`, `expand:`

**Collection Management:**
- Browse and search across multiple collections
- Add, delete, rename collections
- Edit collection context descriptions
- Per-collection or global search scope

**Document Features:**
- File browser with fuzzy matching
- Live HTML preview in Chrome with auto-reload
- External editor integration ($EDITOR)
- Scrollable document viewing

**Advanced:**
- Explain mode showing score breakdowns
- Local index support for project-specific collections
- Database cleanup and cache management

## Tech Stack

- Bun runtime
- @opentui/core for UI components
- TypeScript
- Requires qmd CLI v2.0.1+
- Chromium-based browser (auto-detected)

## What Makes It Unique

- TUI companion to qmd (not a standalone tool)
- Multi-modal search in one interface
- Live preview during editing
- Context-aware search using collection metadata
