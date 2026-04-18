# Nexus / claudesidian-mcp (ProfSynapse)

**Source:** https://github.com/ProfSynapse/claudesidian-mcp
**Stars:** 103 | **Forks:** 16 | **Languages:** TypeScript 96.9% | **License:** MIT

## Description

Obsidian plugin granting AI agents and built-in chat access to vault. Natural language operations for reading, writing, searching, and organizing notes with local storage.

## Core Features

**Dual Modes:**
- Native chat within Obsidian with configurable providers
- External agent connectivity via MCP (Claude Desktop, Cursor, Cline, Gemini CLI, Codex CLI)

**Functionality:**
- Vault search (semantic + keyword)
- Note CRUD through conversation
- Workspace memory (persistent context across sessions)
- Task and project management tracking
- Inline text editing within notes
- File ingestion (PDFs, audio, DOCX)
- Web content capture (Markdown/PNG/PDF)

**Advanced:**
- Semantic search by meaning across notes and conversations
- File merging and concatenation
- Recurring workflow automation

## Architecture

TypeScript + esbuild + ESLint + Jest. Desktop: all features. Mobile (iOS/Android): native chat only.

## What Makes It Unique

- Local-first (no external sync)
- Multi-agent flexibility
- Mobile support for chat
- Extensive documentation (10+ guides)
- Two-tool architecture design
