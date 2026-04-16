# obsidian-claude-pkm (ballred)

**Source:** https://github.com/ballred/obsidian-claude-pkm
**Stars:** 1.3k | **Forks:** 92 | **Languages:** Shell 83.3%, Batchfile 16.7% | **License:** MIT

## Description

Personal knowledge management system bridging vision planning to daily execution, with AI accountability features in Obsidian through Claude Code. Both a starter template and adoption tool for existing vaults.

## Core Architecture — The Cascade

Strategic planning connected to daily actions:

**Vision** → **Annual Goals** → **Active Projects** → **Monthly Goals** → **Weekly Review** → **Daily Tasks**

## Key Features

**Slash Commands:**
- `/daily` — Morning planning, check-ins, evening reflection
- `/weekly` — 30-minute structured review with project rollup
- `/monthly` — Monthly review + quarterly milestone verification
- `/project` — Create, track, archive goal-linked initiatives
- `/review` — Context-aware router detecting appropriate review type
- `/push` — Git commit/push integration
- `/onboard` — Interactive personalization
- `/adopt` — Adapt system to existing vaults
- `/upgrade` — Version updates with backup

**AI Agents (cross-session memory):**
- goal-aligner — Audits daily activity against objectives
- weekly-reviewer — Three-phase reflection
- note-organizer — Link management and deduplication
- inbox-processor — GTD-style categorization

**Productivity Coach Mode:** Transforms Claude into accountability partner challenging assumptions and flagging goal-action misalignment.

## What Makes It Unique

- Execution-focused (accountability over information capture)
- Non-destructive adoption: `/adopt` scans existing vaults, detects methods (PARA, Zettelkasten, LYT)
- Auto-commit hooks on file modification
- Zero dependencies (bash + markdown only)
- Not a wiki builder — it's a GTD/goal-tracking system using the wiki pattern

## Workflow

- Morning: `/daily` generates today's note with week's priority
- Evening: Summarizes goal/project attention, flags orphaned tasks
- Sunday: `/weekly` aggregates, scans projects, calculates progress
- Month-End: `/monthly` rolls up, verifies quarterly milestones
