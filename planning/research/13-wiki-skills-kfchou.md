# wiki-skills (kfchou)

**Source:** https://github.com/kfchou/wiki-skills
**License:** MIT

## Description

Claude Code plugin implementing Karpathy's LLM Wiki pattern — a persistent, evolving knowledge base that compounds over time rather than re-deriving answers from raw documents.

## Core Features

**Five Skills:**
- `wiki-init` — Bootstrap a new domain-specific wiki
- `wiki-ingest` — Add sources (papers, URLs, files, transcripts)
- `wiki-query` — Question the wiki with optional answer filing
- `wiki-lint` — Health audits detecting contradictions and gaps
- `wiki-update` — Revise pages when knowledge changes

## Architecture

Three-layer structure:
- **SCHEMA.md** — Conventions and root path reference
- **raw/** — Immutable source documents
- **wiki/** — Index, log, overview, and flat-named pages
- **assets/** — Supporting media

## Workflow

Init → Ingest (repeat) → Query → Lint → Update

**Key behaviors:**
- Ingest surfaces takeaways before writing, then runs backlink audits
- Query always reads the wiki, offers to file answers as new pages with citations
- Lint produces severity-tiered reports and logs unconditionally
- Update shows diffs, cites sources, sweeps for stale claims

## What Makes It Unique

Minimal, focused implementation. Shifts from RAG to wiki-building where accumulated knowledge grows richer with each interaction.
