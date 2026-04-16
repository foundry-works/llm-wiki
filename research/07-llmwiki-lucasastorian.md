# llmwiki (lucasastorian)

**Source:** https://github.com/lucasastorian/llmwiki
**Stars:** 404 | **Forks:** 53 | **License:** Apache 2.0
**Live Demo:** llmwiki.app

## Description

Open-source implementation of Karpathy's LLM Wiki. Upload documents, connect Claude via MCP (Model Context Protocol), and have Claude automatically generate and maintain a compiled knowledge base with cross-references and citations.

## Core Features

**Three-Layer Architecture:**
1. Raw Sources — immutable PDFs, articles, notes, transcripts
2. The Wiki — LLM-generated markdown with summaries, entity pages, cross-references, diagrams
3. Tools — search, read, and write functionality via MCP

**Key Operations:**
- **Ingest**: Drop sources; Claude reads and updates 10-15+ related wiki pages automatically
- **Query**: Ask complex questions against synthesized knowledge
- **Lint**: Health checks for inconsistencies, stale claims, missing cross-references

**MCP Tools Available to Claude:**
- `guide`: Explains wiki functionality and lists knowledge bases
- `search`: Browse files or keyword search with PGroonga ranking
- `read`: Access documents with page ranges, images, batch operations
- `write`: Create/edit wiki pages, support SVG and CSV assets
- `delete`: Archive documents by path or pattern

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Next.js 16, React 19, Tailwind, Radix UI |
| Backend | FastAPI, asyncpg, aioboto3 |
| Document Conversion | LibreOffice |
| MCP Server | MCP SDK, Supabase OAuth |
| Database | Supabase (Postgres + RLS + PGroonga) |
| Storage | S3-compatible bucket |

## Architecture

```
Next.js Frontend ──▶ FastAPI Backend ──▶ Supabase Database
                            │
                        MCP Server ◀──── Claude
```

## What Makes It Unique

- Full web app with hosted option (llmwiki.app) plus self-hosting
- MCP-based integration — Claude connects via standardized protocol
- PGroonga-powered search ranking
- Self-hostable with Supabase + S3
- Language distribution: TypeScript 61.9%, Python 32.3%
