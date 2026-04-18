# Proposal: LLM Wiki for Obsidian via Claude Code

A concrete implementation of the LLM Wiki pattern as a Claude Code skill backed by the Obsidian CLI and direct file I/O.

---

## Design Principles

1. **Markdown is the source of truth.** No databases, no embeddings, no infrastructure beyond Obsidian and git.
2. **Strict data contracts, flexible workflows.** Frontmatter schemas, directory layout, callout syntax, wikilink format, and log/index entry format are non-negotiable — tools, scripts, and queries depend on them. How the agent plans and executes its work is guided by principles and goals, not rigid step-by-step procedures.
3. **Obsidian CLI for search and graph; direct I/O for reads and writes.** Use `obsidian search`, `obsidian backlinks`, `obsidian orphans`, `obsidian unresolved`, and similar commands for operations where the CLI adds value. Read and write markdown files directly — don't route basic file operations through the CLI.
4. **Epistemic integrity over convenience.** Every wiki claim is typed (Source, Analysis, Unverified, Gap). Provenance is tracked via source links in frontmatter. The system knows what it doesn't know.
5. **Human as editor-in-chief.** The LLM writes; the human directs, reviews, and corrects. The schema is a living document the agent co-maintains based on experience.
6. **Complexity is added only when earned.** Start with conventions and the LLM's native capabilities. Add infrastructure (scripts, search engines, databases) only when concrete failures demand it.
7. **The pattern is reusable; each wiki is unique.** The directory structure, templates, data contracts, and operations are domain-agnostic. Spinning up a new wiki means instantiating the same skeleton in a fresh vault. Domain-specific adaptation happens through use (the training period and Wiki Conventions), not through upfront configuration.

---

## Prerequisites

- **Obsidian 1.12.7+** with the CLI enabled (Settings > General > Command line interface)
- **Obsidian desktop app running** (required for CLI search and graph commands)
- **Claude Code** with CLAUDE.md loaded
- **Git** initialized in the vault root
- **pymupdf4llm** (`pip install pymupdf4llm`) — converts PDFs to markdown for ingestion. PDFs are the primary source format in research workflows; this is a required dependency, not optional.

---

## Vault Structure

```
vault/
  raw/                          # Layer 1: Immutable source documents
    assets/                     # Downloaded images, attachments
    <source-files>.md           # Clipped articles, papers, notes
    <source-files>.pdf          # PDFs (converted to .md at ingest time)
  wiki/                         # Layer 2: LLM-generated knowledge base
    index.md                    # Content catalog
    log.md                      # Chronological operation log
    synthesis.md                # Evolving high-level synthesis
    entities/                   # Entity pages (people, orgs, tools, etc.)
    concepts/                   # Concept pages (ideas, theories, patterns)
    sources/                    # Source summary pages (one per raw source)
    comparisons/                # Comparison and analysis pages
  templates/                    # Obsidian templates for each page type
    entity.md
    concept.md
    source-summary.md
    comparison.md
  purpose.md                    # Human-owned research direction (read-only for LLM)
  writing-style.md              # Writing style reference (agent reads for detail)
  CLAUDE.md                     # Layer 3: Schema (specifications + guidance)
```

### Why This Structure

- **`raw/`** is never modified by the LLM. It's the source of truth the human curates. Sources may be markdown, PDF, or other formats. Non-markdown sources are converted to markdown at ingest time; both the original and the converted `.md` live in `raw/`.
- **`wiki/`** is entirely LLM-owned. The human reads it; the LLM writes and maintains it.
- **`wiki/log.md`** is an append-only chronological record of operations. Parseable with `grep "^### \[" log.md | tail -5`.
- **`wiki/synthesis.md`** is the evolving high-level synthesis. Updated on every ingest. Readable as a standalone summary.
- **`templates/`** are Obsidian templates. The LLM uses them as starting points for new pages.
- **`purpose.md`** is the human's research direction — what they're trying to understand, key questions, scope, and working thesis. The LLM reads it for context but never modifies it. It steers what the agent emphasizes during ingest and query.
- **`writing-style.md`** is the long-form writing style reference. CLAUDE.md holds the operational summary; this file has examples, before/after pairs, and rationale. The agent consults it when drafting or revising prose on wiki pages.
- **`CLAUDE.md`** is the schema — loaded automatically by Claude Code. It defines specifications (data contracts) and guidance (principles and goals).

---

## Specifications (Strict)

These data contracts enable programmatic parsing, CLI tooling, graph traversal, search indexing, and Dataview queries. They are non-negotiable.

### Directory Placement

| Page type | Directory |
|-----------|-----------|
| Entity | `wiki/entities/` |
| Concept | `wiki/concepts/` |
| Source summary | `wiki/sources/` |
| Comparison/analysis | `wiki/comparisons/` |

One page per entity. One source summary per raw source. The agent searches before creating to avoid duplicates.

### Frontmatter Schema

Every wiki page must have YAML frontmatter with these fields:

```yaml
---
type: entity | concept | source-summary | comparison | synthesis
sources: []          # List of wikilinks to source summary pages
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
status: current | stale
tags: []
---
```

Additional fields by page type:

- **Entity:** `entity_type: ""` (person, org, tool, place, etc.)
- **Source summary:** `raw_path: ""` (path to the raw source file), `raw_hash: ""` (SHA256 of raw source file at ingest time)
- **Comparison:** `subjects: []` (list of wikilinks to the compared pages)

Field types must be consistent. Dates in ISO 8601. Tags as a YAML list. Sources as a list of wikilinks. Tools depend on these formats.

### TLDR Requirement

Every wiki page must have `> [!tldr]` as its first content block (immediately after frontmatter). One sentence. The index builder extracts this from a known position.

### Claim Typing

Every substantive claim uses one of four Obsidian callout types:

| Callout | Meaning | Rule |
|---------|---------|------|
| `> [!source]` | Fact directly from a source | Must include `[[source-summary]]` link. If you can't cite it, it's not Source. |
| `> [!analysis]` | Inference drawn from sourced facts | Must show reasoning. Must link to the Source claims it's derived from. |
| `> [!unverified]` | Claim without an authoritative source | Flagged for verification. Never present as fact. |
| `> [!gap]` | Explicitly missing knowledge | Never fill with a guess. Marks what the wiki doesn't know. |

The critical distinction is Source vs. Analysis. If the LLM is paraphrasing, synthesizing, or inferring — even if it feels obvious — it's Analysis, not Source. These callout names are exact — they are grep-parseable and form the basis of lint checks.

When multiple sources support the same claim, cite all of them: `> [!source] Claim text. [[Source A]], [[Source B]], [[Source C]]`. This makes corroboration visible at the claim level.

### Cross-References

All cross-references use wikilinks (`[[Page Name]]`). Not raw markdown links. The graph, backlink resolution, and orphan detection depend on this.

### Page Naming

Page filenames use Title Case with spaces: `Transformer Architecture.md`, linked as `[[Transformer Architecture]]`. The filename must match the wikilink text exactly — Obsidian resolves links by filename. No special characters beyond spaces and hyphens. If a page name is ambiguous, disambiguate with a parenthetical: `Mercury (Planet).md`.

### Index Format

`wiki/index.md` lists every wiki page organized by category. Each entry: one wikilink, a parenthetical source count, and a one-line TLDR. The source count is the number of entries in the page's `sources: []` frontmatter list.

```markdown
## Entities

- [[Entity Name]] (3) — One-line TLDR.

## Concepts

- [[Concept Name]] (2) — One-line TLDR.
```

No token budget. Keep entries concise. When the index becomes unwieldy to scan, split into per-category indexes (`wiki/entities/index.md`, etc.).

### Log Format

`wiki/log.md` is append-only. Each entry uses a consistent prefix so it's parseable with simple unix tools.

```markdown
### [YYYY-MM-DD] operation | description

Brief details. What was ingested/queried/linted, what changed.
```

Operations logged: every ingest, every query that generates a wiki page, every lint pass.

---

## Templates

Each page type has a template enforcing the required structure above. Templates define the **required structural elements** (frontmatter, TLDR, callout syntax) and **default sections** (which the agent may adapt to the domain).

### Entity Template (`templates/entity.md`)

```markdown
---
type: entity
entity_type: ""
sources: []
created: "{{date}}"
updated: "{{date}}"
status: current
tags: []
---

> [!tldr]
> One-sentence summary of this entity.

## Overview

> [!source] Key facts
> Verbatim or closely paraphrased facts with `[[source]]` links.

> [!analysis] Interpretation
> Inferences drawn from sourced facts. Reasoning shown.

## Relationships

- Links to related entity and concept pages.

## Open Questions

> [!gap] What's missing
> Explicitly stated gaps in knowledge about this entity.
```

### Concept Template (`templates/concept.md`)

```markdown
---
type: concept
sources: []
created: "{{date}}"
updated: "{{date}}"
status: current
tags: []
---

> [!tldr]
> One-sentence summary of this concept.

## Definition

> [!source] Core definition
> Definition with source attribution.

## Key Claims

> [!source] Claim 1
> Sourced claim.

> [!analysis] Claim 2
> Inferred claim with reasoning.

> [!unverified] Claim 3
> Claim without authoritative source. Needs verification.

## Connections

- Links to related concepts, entities, and sources.

## Contradictions & Tensions

- Where sources disagree about this concept.

## Open Questions

> [!gap] What's missing
> Explicitly stated gaps.
```

### Source Summary Template (`templates/source-summary.md`)

```markdown
---
type: source-summary
raw_path: ""
raw_hash: ""
sources: []
created: "{{date}}"
updated: "{{date}}"
status: current
tags: []
---

> [!tldr]
> One-sentence summary of this source.

## Key Takeaways

> [!source] Takeaway 1
> Direct extraction from source.

## Entities Mentioned

- Links to entity pages created or updated from this source.

## Concepts Covered

- Links to concept pages created or updated from this source.

## Notes

> [!analysis] Editorial notes
> Context, significance, or interpretation added during ingest.
```

### Comparison Template (`templates/comparison.md`)

```markdown
---
type: comparison
subjects: []
sources: []
created: "{{date}}"
updated: "{{date}}"
status: current
tags: []
---

> [!tldr]
> One-sentence summary of what's being compared and the key finding.

## Comparison

| Dimension | Subject A | Subject B |
|-----------|-----------|-----------|
|           |           |           |

## Analysis

> [!analysis] Interpretation
> What the comparison reveals, with reasoning.

## Open Questions

> [!gap] What's missing
> Gaps in the comparison.
```

### Template Flexibility

Default sections (Overview, Key Claims, Relationships, etc.) adapt to the domain. An entity page about a historical figure might need a "Timeline" section. A concept page in a cooking wiki might not need "Contradictions & Tensions." The agent may propose new page types — any new template must include the standard frontmatter fields and a TLDR callout so it integrates with the index, search, and lint systems.

---

## Writing Style Reference

`writing-style.md` lives at the vault root. CLAUDE.md holds the operational summary of these rules; this file has the examples and before/after pairs the agent reaches for when prose quality needs attention. Content:

```markdown
# Writing Style Reference

The agent reads this for detail and examples when drafting or revising
wiki pages. The short rules in CLAUDE.md are the operational summary;
this file is the long form.

## Funnel structure

Each document, section, and paragraph flows from broad to narrow: result
first, then context, then detail. A reader who stops at any point should
have the most important information so far.

- **Page level:** The `[!tldr]` states the key takeaway. Body expands:
  context → claims → open questions.
- **Section level:** Open with the conclusion, then support it.
- **Paragraph level:** Lead with the point, then explain. Don't make the
  reader hold details in memory while waiting for the result.

## Plain language

Prefer concrete, everyday words over academic phrasing.

| Instead of | Write |
|---|---|
| "derive from" | "come from" |
| "sufficient" | "enough" |
| "may require" | "will likely need" |
| "binding constraint" | "bottleneck" |
| "utilize" | "use" |

## Short sentences

If a sentence has more than one clause doing real work, split it.

Before:
> The inference confidence is computed per claim from the model's raw
> logits, scaled by a temperature parameter, and compared against a
> tier-specific threshold.

After:
> Inference confidence is computed per claim from the model's scaled
> logits. Each value is compared against a tier-specific threshold.

## Avoid hedging stacks

One qualifier is fine. Stacking dilutes the point.

Before: "It should be noted that this might potentially suggest that the
threshold could possibly be too strict."

After: "This suggests the threshold is too strict."

Be direct about limitations: state them plainly rather than burying them
in hedged language.

## Avoid overusing emdashes

Emdashes are useful for parenthetical asides, but overuse makes prose
breathless. Limit to one emdash pair per paragraph. If you reach for a
second, use a comma, colon, period, or parentheses instead. For numeric
ranges, use a hyphen (9-10), not an emdash (9—10) or en-dash (9–10).

## Define acronyms on first use per page

Wiki pages are read standalone. Spell out on first mention — "inter-rater
reliability (IRR)" — then use the acronym within that page.

## Name recurring concepts

When a pattern is referenced across sections or pages, give it a compact
label on first introduction ("the three-judge panel," "write-once
semantics"). Later references can use the shorthand without re-explaining.

## Lead in to tables and figures

Don't drop a table or figure cold. Tell the reader what to look for.

> Table 1 shows source counts by entity, ordered by centrality. The
> rightmost column flags entities with only one cited source.

Caption format: `**Table N.** Description` and `**Figure N.** Description`.
Descriptions should be specific enough to interpret the table without
surrounding text.

## Anchor thresholds to their names

Pair a number with its concept on first mention. A bare number has no
meaning until the reader knows what it belongs to.

Before: "We include only entities with ≥ 3 sources."

After: "We include only entities meeting the corroboration threshold
(≥ 3 cited sources)."

## State assumptions explicitly

List assumptions up front — in a bullet list — rather than embedding them
in prose where they're easy to miss. This applies to `[!analysis]`
callouts and comparison pages especially.

Before:
> Because sources overlap substantially and use comparable methods, we
> can pool their estimates.

After:
> **Assumptions:**
> - Sources cover overlapping populations.
> - Methods are comparable enough that estimates can be pooled.
>
> Under these assumptions, we pool the estimates…

## Consistent numbers and formatting

- Pick a rounding convention per page. Don't mix "0.7" and "0.70" for
  the same quantity.
- Spell out numbers under 10 in prose ("three items") unless grouped
  with larger numbers ("items 3, 7, and 12").
- Use commas in thousands (18,000 not 18000).
- Use hyphens for numeric ranges (0.70-0.80, grades 3-5), not en-dashes
  or emdashes.

## For comparison and synthesis pages

- **Translate findings into practical implications.** Don't just restate
  results — say what they mean for the research direction. Each major
  finding should have a "so what" the reader can act on.
- **Qualify cross-source comparisons.** When comparing results across
  sources, note the boundary conditions — different methods, domains, or
  scope. Don't let a favorable comparison imply more generality than the
  sources support.
```

---

## Operations

Four operations. Init is run once per wiki; the other three are ongoing. Each is described by its **goal** and **principles**, not a rigid step-by-step procedure. The agent exercises judgment about how to accomplish the goal based on the specific source, question, or wiki state.

### Init

**Goal:** Instantiate a new wiki in a fresh Obsidian vault — create the directory structure, templates, scaffolds, and CLAUDE.md so the vault is ready for its first ingest.

**Principles:**
- Create the full directory structure (`raw/assets/`, `wiki/` subdirectories, `templates/`).
- Write all four templates (entity, concept, source-summary, comparison) with the standard frontmatter and structure.
- Create wiki scaffolds: `wiki/index.md` (empty category headers), `wiki/log.md` (empty), `wiki/synthesis.md` (frontmatter + placeholder).
- Generate `CLAUDE.md` with all specifications, guidance sections, and an empty Wiki Conventions section.
- Initialize git with a `.gitignore` that excludes Obsidian workspace files.
- Verify Obsidian CLI availability. Test key commands: template creation, search scoping, graph commands, callout search, link traversal. Document any fallbacks in CLAUDE.md based on test results.
- Scaffold `purpose.md` at the vault root from template. The human fills it in; the LLM reads it but never writes to it.
- Write `writing-style.md` at the vault root with the full content from the Writing Style Reference section above. The agent reads it on demand when drafting prose; the human edits it if the conventions need to change.
- No domain-specific customization needed — the training period and Wiki Conventions handle domain adaptation.
- Commit the initial scaffold.

**Available tools:**

| Operation | CLI approach | Direct approach |
|-----------|-------------|-----------------|
| Create pages | `obsidian create name="..." path=... template=...` | Direct file I/O |
| Search | `obsidian search query="..." path=wiki` | `grep -ri "..." wiki/` |
| Find orphans | `obsidian orphans` | Parse files and wikilinks |
| Find backlinks | `obsidian backlinks file="..."` | `grep -rl "\[\[...\]\]" wiki/` |
| Find outgoing links | `obsidian links file="..."` | Parse wikilinks from file |

Phase 1.4 tests both approaches for each operation and documents which works best.

Additional: `git` for initialization and initial commit.

### Ingest

**Goal:** Extract knowledge from a new source and integrate it into the wiki — creating new pages and revising existing ones so the wiki reflects everything it's been fed.

**Principles:**
- If the source is a PDF, convert it to markdown first using `pymupdf4llm`. Store the converted `.md` alongside the original in `raw/` (e.g., `raw/paper.pdf` stays immutable, `raw/paper.md` is the derived conversion). The source summary's `raw_path` points to the original PDF; ingest from the converted markdown.
- Read `purpose.md` (if populated) for context on what the human is trying to learn. Let it steer what to extract, which pages to create, and how to frame content.
- Read the source. Before writing any pages, present the human with: (1) key takeaways from the source, (2) planned new pages (name and type), (3) existing pages that will be updated and what changes, (4) potential contradictions with existing wiki content. Proceed after human approval. In batch mode or when the human signals to proceed without review, skip the pre-check.
- Search the wiki for existing relevant pages before creating new ones. Avoid duplicates.
- Create a source summary page in `wiki/sources/`. Create or update entity and concept pages as warranted by the source content.
- Every claim extracted from the source is typed: direct extractions are `[!source]` with a link to the source summary page. Inferences are `[!analysis]`. Claims the source makes without evidence are `[!unverified]`. Questions raised but not answered are `[!gap]`.
- Compute the SHA256 hash of the raw source file (via `shasum -a 256`) and store it in the source summary's `raw_hash` frontmatter field. On re-ingest, compare the current file's hash against the stored `raw_hash`. If unchanged, report "no changes detected" and skip. If changed, proceed with a targeted update.
- Track provenance: every page created or updated records the source in its frontmatter `sources` list.
- When new information contradicts existing wiki content, surface the disagreement explicitly. Do not smooth contradictions into false coherence.
- Update `wiki/index.md` with entries for new pages and revised TLDRs for updated pages.
- Update `wiki/synthesis.md` — consider what the new source changes about the big picture.
- Append an entry to `wiki/log.md`.
- Commit via git.
- For long sources (books, lengthy reports), ingest chapter by chapter or section by section. Each chunk gets its own source-summary page. This produces better extraction than ingesting a full document at once.

**Available tools:**

| Operation | CLI approach | Direct approach |
|-----------|-------------|-----------------|
| Find existing pages | `obsidian search query="<terms>" path=wiki` | `grep -ri "<terms>" wiki/` |
| Search with context | `obsidian search:context query="<terms>"` | `grep -ri -C 3 "<terms>" wiki/` |
| Convert PDF | — | `pymupdf4llm` |
| Compute source hash | — | `shasum -a 256 <file>` |
| Read/write pages | — | Direct file I/O |

Phase 1.4 determines which approach works best for each operation. The agent uses whichever is more reliable.

### Query

**Goal:** Answer a question using the wiki's accumulated knowledge. Cite sources. Distinguish what the wiki says from what the LLM infers. Optionally file valuable answers back into the wiki so insights compound.

**Principles:**
- Read `purpose.md` (if populated) to understand the human's research direction and emphasis.
- Read `wiki/index.md` to identify candidate pages. Search for specifics.
- Read relevant pages. Follow links via backlinks and outgoing links to discover related content.
- Synthesize an answer with citations to specific wiki pages. Distinguish sourced claims from inferences.
- If the answer is valuable (a comparison, a synthesis, a connection), consider filing it as a new page in the appropriate wiki directory. This is how explorations compound.
- If the query reveals gaps, stale content, or missing connections — update affected wiki pages as a side effect (dual output).
- Answers can take different forms depending on the question: a markdown page (default), a comparison table, a Marp slide deck, or other formats as appropriate. The agent chooses the format that best serves the question.
- If a new page is created or existing pages are updated, update the index and append to the log.

**Available tools:**

| Operation | CLI approach | Direct approach |
|-----------|-------------|-----------------|
| Full-text search | `obsidian search query="<terms>" path=wiki` | `grep -ri "<terms>" wiki/` |
| Search with context | `obsidian search:context query="<terms>"` | `grep -ri -C 3 "<terms>" wiki/` |
| Find backlinks | `obsidian backlinks file="<page>"` | `grep -rl "\[\[<page>\]\]" wiki/` |
| Find outgoing links | `obsidian links file="<page>"` | Parse wikilinks from file content |
| Read pages | — | Direct file I/O |

### Lint

**Goal:** Health-check the wiki. Find structural problems, schema violations, and conceptual gaps. Report findings; apply fixes only with human approval.

**Principles — structural checks:**
- Find orphan pages (no incoming links): `obsidian orphans`
- Find dead-end pages (no outgoing links): `obsidian deadends`
- Find unresolved links (wikilinks pointing to non-existent pages): `obsidian unresolved`
- Scan for `[!unverified]` claims — assess whether any can now be verified or should be removed.
- Scan for `[!gap]` claims — assess whether new sources or existing wiki content could fill them.

**Principles — schema checks:**
- **Frontmatter completeness.** Every wiki page has the required fields for its `type`: the core fields (`type`, `sources`, `created`, `updated`, `status`, `tags`) on all; `entity_type` on entities; `raw_path` and `raw_hash` on source-summaries; `subjects` on comparisons. Dates are ISO 8601. `sources`, `tags`, and `subjects` are YAML lists, not strings. `sources` and `subjects` entries are wikilinks.
- **TLDR position.** `> [!tldr]` is the first content block immediately after frontmatter on every wiki page. The index extractor depends on this.
- **Page naming.** Filenames use Title Case with spaces, no disallowed special characters, and match their wikilink text exactly.
- **Bare claims.** Scan for factual or analytical prose outside typed callout blocks — paragraphs in entity/concept/comparison pages that aren't list items, table rows, section headings, or inside a `> [!...]` block. Report as candidates, not verdicts — the heuristic will have false positives. `synthesis.md` is exempt (prose is implicitly analysis per its `type`).
- **Index consistency.**
  - Every file under `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/comparisons/` has an entry in `wiki/index.md`.
  - Every index entry resolves to an existing file.
  - Each entry's source count matches `len(sources)` in the page's frontmatter.
  - Each entry's TLDR matches the page's `[!tldr]` text.
- **Source drift.** For each source-summary page, recompute SHA256 of the file at `raw_path` and compare against the stored `raw_hash`. Flag mismatches — the source has changed since ingest and pages citing it may be stale.

**Principles — claim-audit sampling:**
- Select 2-3 `[!source]` claims at random, preferring claims not audited in recent lint log entries (rotate coverage over time).
- Read the cited source summary and trace to the raw source. Verify the claim is actually supported. Report discrepancies.
- Record the audited claim references (page + line or heading) in the lint log entry so future passes can rotate.

**Principles — conceptual review:**
- Produce specific findings, not vague suggestions. Surface concrete weak spots such as:
  - Entities or concepts with only one cited source (thinly corroborated).
  - Pages with `[!source]` callouts but no `[!analysis]` (sourced facts never integrated into the wiki's understanding).
  - Hub pages (5+ backlinks) whose `updated` date is more than 30 days old.
  - `[!gap]` callouts a targeted web search or new source could answer.
  - Entity/concept pairs that co-occur in multiple sources but aren't cross-linked.
- Present these as "Suggested Investigations" — specific next steps naming the pages and gaps, not generic recommendations.
- This is what makes lint a knowledge-building operation, not just janitorial.

**Report format:** Summary organized by category (orphans, dead ends, unresolved links, schema violations, source drift, bare-claim candidates, unverified claims, gaps, audit findings, conceptual suggestions). Recommended actions listed. No fixes applied without human approval.

**Log append.** Every lint pass appends an entry to `wiki/log.md` with the date, a findings summary, and the audited claim references.

**Available tools:**

| Operation | CLI approach | Direct approach |
|-----------|-------------|-----------------|
| Find orphans | `obsidian orphans` | Parse all files, collect wikilinks, diff against filenames |
| Find dead ends | `obsidian deadends` | Parse all files, find pages with no outgoing wikilinks |
| Find unresolved links | `obsidian unresolved` | Collect all wikilinks, diff against existing filenames |
| Find unverified claims | `obsidian search:context query="[!unverified]"` | `grep -r "\[!unverified\]" wiki/` |
| Find gaps | `obsidian search:context query="[!gap]"` | `grep -r "\[!gap\]" wiki/` |
| Find source claims | `obsidian search:context query="[!source]"` | `grep -r "\[!source\]" wiki/` |
| Find backlinks | `obsidian backlinks file="<page>"` | `grep -rl "\[\[<page>\]\]" wiki/` |
| Validate frontmatter | — | Parse YAML front-matter block, check required fields by `type` |
| Check TLDR position | — | Read line after closing `---`, verify it begins `> [!tldr]` |
| Recompute source hash | — | `shasum -a 256 <raw_path>`, compare to stored `raw_hash` |
| Detect bare-claim prose | — | `grep` paragraphs outside callout blocks in entity/concept/comparison pages |
| Read pages | — | Direct file I/O |

---

## The Skill File (CLAUDE.md)

The schema document loaded by Claude Code. Organized into two clearly separated sections: specifications (strict data contracts) and guidance (principles and goals).

```markdown
# LLM Wiki Schema

You maintain a personal knowledge wiki in this Obsidian vault.

## Your Role

You are the writer. The human is the editor-in-chief. You propose changes;
the human directs, reviews, and corrects.

You co-maintain this schema. When you learn something about the domain,
discover a better pattern, or receive a correction — update the
"Wiki Conventions" section at the bottom of this file.

## Specifications (Strict)

These data contracts enable tooling. Do not deviate from them.

### Vault Layout

- `raw/` — Immutable source documents. Read from here, never write
  (except converted `.md` files derived from non-markdown sources).
- `wiki/` — Your knowledge base. You own this directory entirely.
  - `wiki/index.md` — Content catalog. Update on every ingest.
  - `wiki/log.md` — Chronological operation log. Append on every operation.
  - `wiki/synthesis.md` — Evolving high-level synthesis. Revise on every ingest.
  - `wiki/entities/` — Entity pages (people, orgs, tools, places).
  - `wiki/concepts/` — Concept pages (ideas, theories, patterns).
  - `wiki/sources/` — Source summary pages (one per raw source).
  - `wiki/comparisons/` — Analysis and comparison pages.
- `templates/` — Page templates. Use as starting points for new pages.
- `purpose.md` — Human-owned research direction. Read for context
  during ingest and query. Never modify this file.

### Frontmatter (Required on Every Wiki Page)

type: entity | concept | source-summary | comparison | synthesis
sources: []          # Wikilinks to source summary pages
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
status: current | stale
tags: []

Additional by type:
- entity: entity_type (string)
- source-summary: raw_path (string), raw_hash (string, SHA256 of raw source)
- comparison: subjects (list of wikilinks)

### TLDR (Required)

Every wiki page: `> [!tldr]` as the first content block after frontmatter.
One sentence. The index extracts this.

### Claim Typing (Required)

- `> [!source]` — Fact from a source. MUST include `[[source]]` link.
- `> [!analysis]` — Your inference. MUST show reasoning.
- `> [!unverified]` — No authoritative source. Flagged for verification.
- `> [!gap]` — Explicitly missing. NEVER fill with a guess.

If you are paraphrasing, synthesizing, or inferring — even if it seems
obvious — use `[!analysis]`, not `[!source]`.

When multiple sources support the same claim, cite all of them:
`> [!source] Claim text. [[Source A]], [[Source B]], [[Source C]]`

### Cross-References

All cross-references use wikilinks: `[[Page Name]]`.
Not markdown links. The graph depends on this.

### Page Naming

Page filenames use Title Case with spaces: `Transformer Architecture.md`,
linked as `[[Transformer Architecture]]`. The filename must match the
wikilink text exactly — Obsidian resolves links by filename.

No special characters beyond spaces and hyphens. If a page name is
ambiguous, disambiguate with a parenthetical: `Mercury (Planet).md`.

### Index Format

`wiki/index.md`: one wikilink + parenthetical source count + one-line
TLDR per page, organized by category (Entities, Concepts, Sources,
Comparisons). Example: `- [[Page Name]] (3) — One-line TLDR.`
The number is the count of entries in the page's `sources: []` list.
Keep each entry under ~30 words. The index must remain small enough to read in full at
the start of every query and ingest operation. When the index becomes
unwieldy, split into per-category indexes.
Rule of thumb: split when the index exceeds ~100 entries.

### Log Format

`wiki/log.md`: append-only. Each entry:
`### [YYYY-MM-DD] operation | description`
Log every ingest, every query that generates a page, every lint pass.

### Other Conventions

- Tags in frontmatter, not inline.
- Dates in ISO 8601.
- One page per entity. Search before creating to avoid duplicates.
- When sources disagree, surface the disagreement explicitly.
- Prefer targeted updates over full page rewrites.
- For source-summary pages, provenance comes from `raw_path`.
  The `sources` field is typically `[]` unless the summary draws on
  other source-summary pages (e.g., a review paper referencing
  earlier sources already in the wiki).
- Every ingest and query updates the wiki — not just answers the
  immediate question. Index, log, and synthesis updates are part of
  the deliverable, not afterthoughts.
- If a page grows past ~1,500 words, consider splitting it. An entity
  page might spawn a dedicated comparison, timeline, or sub-topic page.
  Each sub-page gets its own frontmatter, TLDR, and index entry.

## Guidance (Flexible)

These describe goals and principles. Use judgment about how to achieve them.

### Writing Style

Apply to prose on every wiki page. See `writing-style.md` for examples and
before/after pairs.

- **Funnel structure.** Each page, section, and paragraph leads with its
  conclusion. A reader skimming first sentences should get the full story.
- **Plain language, short sentences.** Prefer concrete, everyday words.
  Split sentences with more than one clause doing real work.
- **No hedging stacks.** One qualifier max ("this suggests X"), not
  "this might potentially suggest X could possibly be Y."
- **Emdashes sparingly.** At most one emdash pair per paragraph. Use
  commas, colons, or periods otherwise. Use hyphens (not emdashes or
  en-dashes) for numeric ranges (0.70-0.80).
- **Define acronyms on first use per page.** Wiki pages are read standalone.
- **Name recurring concepts.** Give compact labels on first introduction
  so later references stay short.
- **Lead in to tables and figures.** Tell the reader what to look for.
  Caption as `**Table N.** ...` / `**Figure N.** ...`.
- **Anchor thresholds to names.** "Corroboration threshold (≥ 3 cited
  sources)" not bare "≥ 3."
- **State assumptions explicitly.** Bullet them before analysis that
  rests on them.
- **Consistent numbers.** Pick a rounding convention per page. Commas in
  thousands (18,000). Spell out numbers under 10 in prose unless grouped
  with larger numbers.

For `comparisons/` and `synthesis.md`: translate findings into practical
implications ("so what"), and qualify cross-source comparisons when the
sources differ in scope or method.

### Ingest

Your goal is to extract knowledge from a source and integrate it into the
wiki. Read `purpose.md` for context on the human's research direction.
Read the source. Before writing any pages, present the human with:
(1) key takeaways, (2) planned new pages, (3) existing pages to update,
(4) potential contradictions. Proceed after approval. In batch mode or
when the human signals to proceed, skip the pre-check. Then update
the wiki — creating new pages and revising existing ones as needed.
Track provenance. Surface contradictions. Update the index, synthesis,
and log when done. Commit via git.

If the source is a PDF, convert it to markdown first using `pymupdf4llm`.
Store the converted `.md` alongside the original in `raw/`. The source
summary's `raw_path` points to the original file; ingest from the
converted markdown. The original PDF stays immutable.

For long sources (books, lengthy reports), ingest chapter by chapter or
section by section. Each chunk gets its own source-summary page. This
produces better extraction than ingesting a full document at once.

For sources with images or diagrams: ensure attachments are stored in
`raw/assets/`. Reference images in source-summary pages using standard
Obsidian image embeds (`![[image.png]]`). When an image contains
information relevant to the wiki (a diagram, chart, or table), describe
its content in text nearby so the information is searchable and
available to future queries.

### Training Period

For the first ~10 ingests, the human should review every created and
updated page — not just spot-check. Corrections get filed to Wiki
Conventions immediately. This is what bootstraps the schema flywheel:
each correction makes the next ingest better, and the conventions
accumulate domain-specific patterns that no upfront design can
anticipate. As the Wiki Conventions section fills and corrections
become rare, the human can shift to periodic review.

### Query

Your goal is to answer questions using the wiki's accumulated knowledge.
Read `purpose.md` for context on the human's research direction.
Search the index and wiki, read relevant pages, follow links. Cite
specific pages. Distinguish sourced claims from your inferences. If the
answer is valuable, file it as a new page. If you find gaps or stale
content, update affected pages.

Answers can take different forms: markdown page, comparison table,
Marp slide deck, or other formats as appropriate.

### Lint

Your goal is to health-check the wiki — structurally, schema-wise, and
conceptually. Check for orphans, dead ends, unresolved links, unverified
claims, and gaps.

Validate schema: frontmatter completeness per `type` (core fields plus
per-type fields; ISO 8601 dates; `sources`/`tags`/`subjects` as YAML
lists of the right shape); TLDR is the first content block after
frontmatter on every page; filenames are Title Case and match wikilink
text; index consistency (every wiki page has an entry, every entry
resolves to an existing file, source counts match `len(sources)`, TLDRs
match). For each source-summary, recompute `raw_hash` against the file
at `raw_path` and flag drift. Flag prose that looks like a factual or
analytical claim but sits outside a typed callout — report as candidates,
not verdicts (`synthesis.md` is exempt).

Select 2-3 `[!source]` claims at random, preferring claims not audited
in recent lint log entries, trace them to cited sources, and verify
they are actually supported. Record the audited claim references in
the lint log entry so coverage rotates.

For the conceptual pass, name specific weak spots: thinly-sourced pages
(one cited source), pages with sourced facts but no `[!analysis]`, hub
pages (5+ backlinks) with `updated` older than 30 days, unanswered
`[!gap]` callouts, and entity/concept pairs that co-occur in sources
but aren't cross-linked. Present these as specific next steps, not
generic suggestions.

Report findings by category. Append a log entry including the audited
claim references. Apply fixes only with human approval.

### Synthesis

`wiki/synthesis.md` is your evolving thesis — a standalone summary of
everything the wiki knows. Revise it on every ingest. Keep it readable
and under ~1,000 words. It should reflect the current state of the wiki's
knowledge, not just the latest source.

Synthesis is analytical by nature — its `type: synthesis` signals that
all content represents your integrated understanding. Write in prose
without per-claim callout wrappers. If you reference a specific source
directly, use a `[!source]` callout for that claim. Otherwise, the page
is implicitly `[!analysis]`.

## Wiki Conventions

<!-- Maintained by the agent. Add learned patterns, domain-specific
     conventions, corrections from the human, and workflow refinements.
     Format: date, convention, context. -->
```

---

## Scaling Plan

The design above works at personal scale (~100 sources, hundreds of pages) with no infrastructure beyond Obsidian, git, and the LLM's native capabilities. When concrete bottlenecks appear, add infrastructure in this order:

### When search becomes insufficient

The `obsidian search` commands provide full-text search. The index file serves as a curated entry point. If search results become noisy at scale:

1. **Per-category indexes.** Split `wiki/index.md` into `wiki/entities/index.md`, `wiki/concepts/index.md`, etc. Read only the relevant category index per query.
2. **Tag-based navigation.** Use `obsidian tags` and `obsidian tag name=<tag>` to navigate by topic.
3. **Dedicated search engine.** Add [qmd](https://github.com/tobi/qmd) or a SQLite FTS5 index for hybrid search. Keep markdown as source of truth; treat search indexes as rebuildable caches.

### When staleness management becomes burdensome

At small scale, the LLM can check for staleness by comparing source modification dates to page `updated` dates during lint. At larger scale:

1. **Hash-based staleness.** Add a script that computes SHA-256 hashes for source files and compares against stored references.
2. **Lazy recompilation.** Don't recompile all stale pages at once. Recompile each the next time it's accessed by a query.
3. **Diff-based ingest.** When a source is updated (not new), diff it to identify what changed. Update only affected wiki pages.

### When compilation quality becomes a concern

1. **Periodic audit.** Sample random wiki pages per lint pass. Read the page and its cited sources. Check whether claims are actually supported.
2. **Wiki + RAG verification.** When answering a query, verify the wiki's answer against raw sources directly (not just wiki pages).

---

## What This Proposal Deliberately Excludes

- **Multi-model verification.** 4x cost for marginal accuracy at personal scale.
- **Cryptographic receipts.** Solving a problem personal wikis don't have.
- **Formal ontologies.** OWL-RL and SPARQL add a second knowledge management problem.
- **Multi-agent coordination.** Unproven at single-agent scale.
- **Knowledge graph databases.** Wikilinks are an implicit graph. Making it explicit adds infrastructure without clear benefit at personal scale.
- **Autonomous operation.** No cron-based maintenance. Errors compound without human review.
- **Shell scripts in V1.** The LLM performs hash computation, index building, and staleness checking natively. Scripts are added when automation is needed at scale.

---

## Deliverables

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Skill file / schema (specifications + guidance) |
| `templates/entity.md` | Template for entity pages |
| `templates/concept.md` | Template for concept pages |
| `templates/source-summary.md` | Template for source summary pages |
| `templates/comparison.md` | Template for comparison/analysis pages |
| `wiki/index.md` | Content catalog (scaffold) |
| `wiki/log.md` | Chronological operation log (scaffold) |
| `wiki/synthesis.md` | Evolving high-level synthesis (scaffold) |
| `purpose.md` | Human-owned research direction (scaffold) |
| `writing-style.md` | Writing style reference (agent reads for detail) |

Total: 1 skill file, 4 templates, 3 wiki scaffolds, 1 human-owned file, 1 style reference. External dependencies: Obsidian, git, pymupdf4llm, and standard Unix tools.

These deliverables are domain-agnostic. The Init operation produces the same 10 files for any new wiki — a cooking wiki, a research wiki, a software architecture wiki. Domain-specific adaptation happens during the training period as the agent and human co-evolve the Wiki Conventions section of CLAUDE.md. Each wiki instance is an independent vault with its own git history, its own evolved schema, and its own compiled knowledge.
