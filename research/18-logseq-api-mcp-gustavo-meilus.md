# logseq-api-mcp (gustavo-meilus)

**Source:** https://github.com/gustavo-meilus/logseq-api-mcp
**Language:** Python 3.11+ | **Protocol:** MCP

## Description

Integration layer connecting MCP clients with Logseq knowledge bases. Enables AI assistants to interact with notes, extract educational content, and analyze knowledge relationships.

## Core Features

**Read Operations:**
- get_all_pages — Complete page listing with metadata
- get_page_blocks — Hierarchical block structure analysis
- get_page_links — Relationship and reference discovery
- get_block_content — Detailed block content with children
- get_all_page_content — Comprehensive page extraction
- get_linked_flashcards — Advanced flashcard collection

**Write Operations:**
- append_block_in_page — Append blocks with positioning
- create_page — New pages with properties and format
- edit_block — Edit blocks with content and properties

## Architecture

Dynamic tool discovery: auto-scans `src/tools/`, imports functions, registers with MCP server without manual config. Uses UV package manager, pytest (80% coverage minimum), Ruff linting, MyPy, Bandit security analysis.

## What Makes It Unique

- Zero-configuration tool addition (auto-discovery)
- Educational focus (flashcards and learning materials)
- AI-optimized output formatting
- Dynamic registration of new tools
