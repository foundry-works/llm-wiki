# Progressive Disclosure UX Plan

## Goal

Make a mature LLM Wiki easy for a human to enter, skim, trust, and deepen without losing the current plain-markdown, agent-maintained model.

The wiki should work like an iceberg:

- **Surface:** the human sees the current answer, what changed, what needs attention, and where to start.
- **Skim:** the human can browse compact catalogs and task-oriented dashboards.
- **Read:** the human can open a page and quickly understand its conclusion, confidence, sources, gaps, and relationships.
- **Dive:** the human can inspect claim callouts, source summaries, audits, raw-source provenance, decisions, and history.

## Lessons From Existing Vaults

The useful patterns in `~/ObsidianVaults/SupplementsResearch` and `~/ObsidianVaults/Investments` are:

- Start with user intent, not folder structure.
- Treat `synthesis.md` as a front door, not just a summary page.
- Maintain compact decision surfaces such as quick references, dashboards, and generated indexes.
- Make recurring questions durable by filing reusable query answers.
- Use health and briefing outputs to surface what needs attention now.
- Preserve auditability with source callouts, gaps, decision logs, and append-only history.
- Keep Obsidian-only views optional; markdown artifacts must remain useful outside Obsidian.

## Target Surface Artifacts

### 1. `wiki/dashboard.md`

The main above-the-surface artifact.

Purpose:

- Show the wiki's current state at a glance.
- Route the human by intent.
- Surface recent changes, open gaps, stale areas, and high-value entry points.
- Link to deeper catalogs and source-grounded pages.

Likely sections:

- Current synthesis snapshot
- Start by intent
- Recent activity
- Priority gaps
- Contradictions and debates
- Stale or thin areas
- Key hubs
- Deeper maps

Implementation direction:

- Prefer generated or semi-generated content where possible.
- Keep hand-authored analytical prose in `wiki/synthesis.md`.
- Keep the dashboard short enough to read at session start.

### 2. `wiki/queries/`

A durable home for recurring questions.

Files:

- `wiki/queries/query-hub.md` as the question hub. Avoid a generic
  `README.md` filename so Obsidian wikilinks keep a single unambiguous
  page target if directory README pages are added later.
- Individual query answer pages when an answer synthesizes multiple pages and is likely to be reused.

Purpose:

- Convert repeated human questions into stable artifacts.
- Reduce the need to reconstruct the same synthesis from scratch.
- Provide an intent-based entry point distinct from entity/concept browsing.

### 3. `wiki/debates.md`

A single surface for disagreements, contradictions, and unresolved tensions.

Purpose:

- Make disagreement visible without forcing the human to discover it page by page.
- Link each debate to the relevant source summaries, concepts, entities, or comparisons.
- Separate "sources disagree" from "the wiki has a gap."

### 4. Directory README Pages

Add lightweight README pages for major content folders once useful:

- `wiki/entities/README.md`
- `wiki/concepts/README.md`
- `wiki/sources/README.md`
- `wiki/comparisons/README.md`

Purpose:

- Explain what belongs in the folder.
- Provide local browsing routes.
- Link to relevant indexes or dashboard sections.

### 5. Briefing Output

Add a command or lint mode that answers: "What needs attention now?"

Candidate shape:

```bash
python3 scripts/wiki-lint.py --briefing
```

Briefing should include:

- Page counts by type
- Recent ingests and queries
- Open gaps
- Thinly sourced pages
- Stale hub pages
- Source summaries missing extraction audits
- Hash drift
- Handoff state

This can be printed to the terminal first. Later it can optionally render into `wiki/dashboard.md`.

### 6. Optional Obsidian Bases

Provide optional `.base` dashboard templates for Obsidian users.

Possible views:

- Knowledge Map
- Sources
- Open Gaps
- Stale Pages
- Comparisons

Constraint:

- Bases must not become required infrastructure. Markdown remains the portable source of truth.

## Page-Level Progressive Disclosure

Current page templates already require TLDRs and typed callouts. Extend them with a more deliberate top section.

Candidate page header pattern:

- TLDR
- At a Glance
- Why It Matters
- Confidence / Source Posture
- Key Gaps
- Dive Deeper

This should be applied conservatively. The goal is not larger pages; it is faster orientation before the deep claim body.

## Implementation Phases

### Phase 1: Document the UX Contract

Deliverables:

- Add this plan.
- Update `README.md` to name the surface artifacts and reading path.
- Update `wiki-base/CLAUDE.md` with a "Progressive Disclosure" guidance section.
- Define which files are generated, agent-maintained, or human-owned.

Acceptance criteria:

- A new user can tell where to start without learning the whole schema.
- The agent has clear instructions for maintaining surface artifacts.

### Phase 2: Scaffold Surface Pages

Deliverables:

- Add `wiki-base/wiki/dashboard.md`.
- Add `wiki-base/wiki/debates.md`.
- Add `wiki-base/wiki/queries/query-hub.md`.
- Consider directory README pages for the default scaffold.
- Update templates or schema rules so these pages validate as `type: meta`.

Acceptance criteria:

- A newly created wiki has a visible front door.
- The scaffold still passes smoke tests and wiki lint.

### Phase 3: Add Briefing Support

Deliverables:

- Extend `wiki-base/scripts/wiki-lint.py` with `--briefing` or similar.
- Reuse existing health-summary logic where possible.
- Include recent log and handoff signals.
- Add unit tests around output shape.

Acceptance criteria:

- The command gives a compact session-start summary.
- It works without Obsidian.
- It does not mutate files.

### Phase 4: Dashboard Maintenance

Deliverables:

- Decide whether `wiki/dashboard.md` is fully generated, semi-generated, or agent-maintained.
- If generated, add `--rebuild-dashboard`.
- If agent-maintained, update ingest/query/lint skills to refresh it when relevant.
- Add tests for generated dashboard sections if applicable.

Acceptance criteria:

- The dashboard does not drift silently from index, backlog, synthesis, and log.
- The maintenance burden stays on the agent/tooling, not the human.

### Phase 5: Skill Updates

Deliverables:

- Update `/wiki-ingest` to mention dashboard/debates/query surfaces in done criteria.
- Update `/wiki-query` to route reusable answers into `wiki/queries/`.
- Update `/wiki-lint` to report dashboard freshness and briefing output.
- Update `/wiki-repair` only where repairs affect surface artifacts.

Acceptance criteria:

- Normal wiki operations keep the surface current.
- Surface updates remain scoped and auditable.

### Phase 6: Optional Obsidian Enhancements

Deliverables:

- Add generic `.base` files only if they provide clear value.
- Document them as optional.
- Keep markdown fallbacks for every important view.

Acceptance criteria:

- Obsidian users get richer browsing.
- Non-Obsidian users lose no core functionality.

## Design Decisions To Make

- Is `wiki/dashboard.md` generated from deterministic data, or maintained by the agent as prose?
- Should `wiki/synthesis.md` remain the primary front door, or should `wiki/dashboard.md` become the front door with synthesis as its main linked analysis?
- Should `wiki/index.md` stay a compact catalog, or become a multi-view markdown dashboard?
- Should `wiki/backlog.md` remain a manually triaged queue, or should it gain generated sections from gaps and stale pages?
- How much page-level "At a Glance" structure is useful before it becomes template noise?

## Initial Slice

Start with the smallest useful product:

1. Add `wiki/dashboard.md`, `wiki/debates.md`, and `wiki/queries/query-hub.md` to the scaffold.
2. Update `README.md` to introduce them as surface artifacts.
3. Update `CLAUDE.md` so agents know how to maintain them.
4. Add or adjust tests so the new scaffold files are expected and valid.

Do not start with Obsidian Bases or a full dashboard generator. Those are useful only after the scaffolded surface proves its shape.
