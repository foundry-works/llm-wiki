# OMEGA Memory

**Source:** https://github.com/omega-memory/omega-memory
**Language:** Python 3.11+ | **License:** Apache 2.0

## Description

Local-first persistent memory system for AI coding agents. Works across multiple LLM platforms independently. "Your agent's brain shouldn't live on someone else's server, or be locked to one provider."

## Core Features

**Memory & Learning (25 tools):**
- Semantic search with embeddings across decisions, lessons, errors, preferences
- Storage, querying, deletion, editing, timeline views, consolidation
- Auto-surfaces relevant memories during coding sessions
- Checkpointing/resuming tasks, reminders, relationship graphs, weekly digests

**Multi-Agent Coordination (omega-pro: 29 tools):**
- File and branch locking
- Session management with task queues and dependencies
- Agent-to-agent messaging and intent broadcasting
- Audit trails

**Intelligent LLM Routing (omega-pro):**
- Task classification to optimal models
- Sub-2ms intent classification, four priority modes

**Knowledge Base (omega-pro):**
- PDF, markdown, web page ingestion
- Entity registry with hierarchies
- AES-256 encryption, macOS Keychain

## Architecture

MCP server bridging multiple clients (Claude Code, Cursor, Claw Code, Windsurf). Single SQLite database (`omega.db`) with memories, relationships, vector embeddings. ONNX-based bge-small-en-v1.5 embeddings (384-dim, ~90MB).

**Search Pipeline:**
1. Vector similarity via sqlite-vec
2. Full-text via FTS5
3. Type-weighted scoring (decisions/lessons 2x)
4. Contextual re-ranking (tag, project, content)
5. Real-time deduplication

**Memory Management:**
- SHA256 deduplication + embedding similarity (0.85+ threshold)
- Evolution: 55-95% similar content appends vs. duplicates
- Auto-relationship creation (0.45+ similarity)
- Compaction clusters and summarizes
- Session summaries expire after 1 day; lessons/preferences persist

## Performance

- Startup: ~31MB RAM
- Post-model-load: ~337MB
- DB: ~10.5MB for ~242 memories
- Local embedding inference (no API calls)
- Intent classification: <2ms

## What Makes It Unique

- Multi-provider (Claude, GPT, Gemini, Llama)
- Fully local, no cloud
- Multi-agent coordination
- vs. Anthropic Memory: cross-provider, on-device
- vs. Mem0: no cloud dependency
- vs. Zep: broader agent compatibility, coordination tools
