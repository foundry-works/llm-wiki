# llm-wiki (nvk) — Multi-Agent Research Wiki

**Source:** https://github.com/nvk/llm-wiki
**Languages:** 80.6% Shell, 19.4% JavaScript | **License:** Not specified

## Description

LLM-compiled knowledge bases for any AI agent. Parallel multi-agent research, thesis-driven investigation, source ingestion, wiki compilation, querying, and artifact generation. Ships as a Claude Code plugin or portable AGENTS.md.

## Core Features

**Research Capabilities:**
- Parallel multi-agent investigation (5, 8, or 10 agents depending on mode)
- Thesis-driven research that decomposes claims and evaluates evidence
- Question-to-playbook conversion (questions auto-decompose into research subtasks)
- Smart time-budgeted research rounds that drill into gaps

**Knowledge Management:**
- URL/file/text ingestion with automatic compilation
- Dual-linking (Obsidian wikilinks + standard markdown)
- Confidence scoring on articles (high/medium/low)
- Activity logging and session resumption via `--resume`

**Query & Output:**
- Three query depths: quick (indexes only), standard (articles + search), deep (everything + sibling wikis)
- Artifact generation: summaries, reports, study guides, slides, timelines, glossaries, comparisons
- Gap analysis tool assessing repos against compiled research + market context
- Cross-wiki synthesis via `--with` flag

## Architecture

Hub-and-spokes topology:
```
~/wiki/                          # Lightweight registry hub
├── wikis.json                   # Topic wiki registry
├── _index.md                    # Hub listing with stats
└── topics/<name>/               # Isolated topic wikis
    ├── raw/                     # Immutable sources
    ├── wiki/                    # Compiled articles
    ├── output/                  # Generated artifacts
    └── _index.md                # Topic navigation
```

## Research Modes

| Mode | Agents | Character |
|------|--------|-----------|
| Standard | 5 | Academic, technical, applied, news, contrarian |
| Deep | 8 | Adds historical, adjacent fields, data/statistics |
| Retardmax | 10 | Widest net; skips planning; speed + aggressive ingestion |

## Thesis-Driven Investigation

Anti-confirmation-bias mechanisms:
- Decomposes claims into testable variables and falsification criteria
- Splits agents: supporting, opposing, mechanistic, and meta roles
- Multi-round investigation auto-focuses on weaker evidence
- Verdicts: supported/partially supported/contradicted/insufficient/mixed

## What Makes It Unique

- Zero vendor lock-in (portable AGENTS.md)
- No database required (markdown-native, Git-compatible)
- Parallel agent coordination (not sequential querying)
- Time-budgeted research (keeps investigating for specified durations)
- Thesis as bloat-filter (focused evidence collection)
- Fuzzy intent router understanding natural language commands
