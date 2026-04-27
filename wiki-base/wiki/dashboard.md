---
type: meta
sources: []
created: "{{date}}"
updated: "{{date}}"
status: current
tags: []
---

> [!tldr]
> Session-start front door for the wiki: what changed, what needs attention, and where to begin reading.

This dashboard is agent-maintained. Keep it short enough to read at the start of a session, and use `python3 scripts/wiki-lint.py --briefing` for the current deterministic health snapshot.

## Current Synthesis Snapshot

Start with [[synthesis]] for the current integrated view.

## Start By Intent

- **Understand the current answer:** read [[synthesis]], then follow links into the supporting entity, concept, source, and comparison pages.
- **Find what changed recently:** read [[log]] and the recent activity lines from `python3 scripts/wiki-lint.py --briefing`.
- **Pick up active work:** read [[handoff]] and the open rows in [[backlog]].
- **Inspect disagreements:** read [[debates]] and relevant comparison pages.
- **Ask a recurring question:** check [[query-hub]], then file reusable query answers in `wiki/queries/` when they are not a better fit for `wiki/comparisons/`.

## Recent Activity

*No activity yet. Summarize recent ingests, reusable queries, repairs, and lint passes here after they materially affect the reading path.*

## Priority Gaps

See [[backlog]] for the ranked queue.

## Contradictions And Debates

See [[debates]].

## Stale Or Thin Areas

Run:

```bash
python3 scripts/wiki-lint.py --briefing
```

Use the thin, stale, missing-audit, and hash-drift counts to decide what deserves attention before the next ingest or query.

## Key Hubs

*No hubs yet. Add stable entry points once the wiki has enough content for repeated browsing routes.*

## Deeper Maps

- [[index]] - generated content catalog
- [[backlog]] - open gaps and unverified claims
- [[handoff]] - cross-session state
- [[decisions]] - structural decisions and rationale
- [[graph-protocol]] - graph invariants and validation rules
