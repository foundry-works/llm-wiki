# llm-wiki (MehmetGoekce)

**Source:** https://github.com/MehmetGoekce/llm-wiki
**Stars:** 44 | **Forks:** 8 | **Languages:** Shell 89.5%, Mermaid 10.5%

## Description

LLM Wiki implementation with Claude Code supporting Logseq or Obsidian. Features a novel L1/L2 cache system for context-window optimization.

## Core Features

**Commands:**
- `/wiki ingest` — Processes sources, updates 5-15 wiki pages
- `/wiki query` — Searches wiki, synthesizes answers with attribution
- `/wiki lint` — Health checks (orphans, stale content, broken refs, credential leaks)
- `/wiki status` — Metrics dashboard

**Quality Management:**
- Orphan page detection (no incoming links)
- Stale content flagging (90+ days)
- Missing required properties
- Broken references
- Credential exposure detection

## Revolutionary Feature: L1/L2 Cache System

**L1 — Claude Memory:**
- Auto-loaded every session (~10-20 files)
- Contains rules, gotchas, identity, credentials
- Never git-tracked (secure for secrets)

**L2 — Wiki Storage:**
- On-demand access (~50-200 pages)
- Projects, workflows, research, deep knowledge
- Typically git-tracked

**Routing principle:** Knowledge that could cause dangerous/embarrassing errors if missing → L1; inconvenient mistakes → L2.

## Ingest Workflow (5 phases)

1. Analysis — Extract entities, facts, relationships, dates
2. Wiki Scanning — Identify affected pages
3. Page Updates — Create new or append to existing
4. Quality Gate — Verify properties, cross-refs, credential safety
5. Reporting — Summarize changes, flag warnings

## Schema

- 8 namespaces (Business, Tech, Content, Projects, People, Learning, Reference, Careers)
- 5 page types (Entity, Project, Knowledge, Feedback, Hub)
- Automated lint rules

## What Makes It Unique

- L1/L2 boundary for explicit context-window optimization (unique among implementations)
- Append-only updates (never overwrites)
- Dual-platform (Logseq + Obsidian)
- Automated quality gates before commit
- 5-minute setup via `./setup.sh`
