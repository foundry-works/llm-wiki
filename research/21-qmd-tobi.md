# qmd — Query Markup Documents (tobi)

**Source:** https://github.com/tobi/qmd
**Languages:** TypeScript 80.1% | **License:** MIT

## Description

Local, on-device search engine for indexing and querying personal knowledge repositories. Processes markdown notes, meeting transcripts, documentation, and knowledge bases through hybrid search — all without cloud services.

## Core Features

**Search:**
- BM25 full-text keyword search (FTS5)
- Vector semantic search using embedding models
- Hybrid search with LLM-powered query expansion and re-ranking
- Collection-scoped searching
- Multiple output formats (CLI, JSON, CSV, Markdown, XML)

**Indexing:**
- Auto document discovery via glob patterns
- Smart markdown chunking (~900 tokens, 15% overlap)
- AST-aware code chunking (TypeScript, Python, Go, Rust, JS)
- Context tagging for improved relevance
- SQLite FTS5 full-text indexing

**Integration:**
- CLI (npm/Bun globally installable)
- MCP server for Claude and LLM clients
- HTTP transport for shared instances
- JavaScript/TypeScript SDK

## Architecture — Four-Stage Retrieval Pipeline

1. **Query Expansion**: Original query (2x weight) + LLM-generated variation
2. **Parallel Retrieval**: Each query searches BM25 and vector indexes simultaneously
3. **RRF Fusion**: `Σ(1/(k+rank+1))` with position bonuses for top-ranking docs
4. **LLM Re-ranking**: Neural reranker scores top-30, position-aware blending

## Tech Stack

- Node.js ≥22 or Bun ≥1.0
- SQLite with FTS5 + sqlite-vec
- Local GGUF models via node-llama-cpp:
  - embeddinggemma-300M (~300MB): Vector embeddings
  - qwen3-reranker-0.6b (~640MB): Cross-encoder scoring
  - qmd-query-expansion-1.7B (~1.1GB): Query variation generator

## What Makes It Unique

- Fully local (zero cloud dependencies)
- Hybrid keyword + semantic + neural re-ranking pipeline
- AST-aware code chunking at function/class boundaries
- Position-aware fusion preserving exact matches
- MCP-native for agentic workflows
- SDK-first design (embeddable library)
