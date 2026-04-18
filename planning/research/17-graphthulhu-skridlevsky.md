# graphthulhu (skridlevsky)

**Source:** https://github.com/skridlevsky/graphthulhu
**Language:** Go | **Protocol:** MCP

## Description

MCP server enabling AI assistants like Claude to read and write to Logseq and Obsidian knowledge graphs. Bridges interconnected note systems with AI capabilities.

## Core Features

**Navigation & Access:**
- Full recursive block trees with parsed links, tags, properties
- Forward/backward link traversal with contextual references
- BFS path-finding between pages through the link graph
- Block-level access by UUID with ancestor chains and siblings

**Search:**
- Full-text search with parent chain + sibling context
- Property-based queries (eq, contains, gt, lt)
- Tag searching with child hierarchy support
- Raw DataScript/Datalog queries for Logseq (escape hatch)

**Analysis:**
- Graph overview: stats, most-connected pages, namespaces
- Knowledge gap detection: orphans and dead ends
- Topic clustering via connected component analysis
- Shortest paths between concepts

**Content Management:**
- Create pages with properties and initial blocks
- Batch create nested hierarchies with upsert
- Update/delete/move blocks (cross-page)
- Page renaming with automatic link updates

**Specialized:**
- Decision tracking with deadlines and deferral warnings
- Flashcard management with spaced repetition stats
- Journal entry access across date ranges
- Whiteboard exploration (Logseq only)

## Architecture

Modular backend interface supporting multiple vault systems. In-memory graph construction for rapid analysis. File watching (Obsidian) keeps index synchronized. Logseq via HTTP API; Obsidian parses .md files directly.

## What Makes It Unique

- Returns complete nested hierarchy with parsed metadata (not flat results)
- Search includes full context (parent chains + siblings)
- DataScript escape hatch for complex custom logic
- Supports both Logseq and Obsidian from single server
