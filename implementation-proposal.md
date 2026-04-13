# Proposal: LLM Wiki for Obsidian via Claude Code

A concrete implementation of the LLM Wiki pattern as a Claude Code skill backed by the Obsidian CLI and a small set of supporting shell scripts.

---

## Design Principles

1. **Markdown is the source of truth.** No databases, no embeddings, no infrastructure beyond Obsidian and git. SQLite indexing is deferred until the wiki exceeds ~200 pages.
2. **The Obsidian CLI is the only interface to the vault.** All reads, writes, searches, and metadata operations go through `obsidian` commands. No direct filesystem manipulation of vault files.
3. **Epistemic integrity over convenience.** Every wiki claim is typed (Source, Analysis, Unverified, Gap). Provenance is tracked via source hashes in frontmatter. The system knows what it doesn't know.
4. **Human as editor-in-chief.** The LLM writes; the human reviews, directs, and corrects. Corrections feed back into the schema so mistakes don't recur.
5. **Complexity is added only when earned.** Start with schema conventions and shell scripts. Add infrastructure (search engines, databases) only when concrete failures demand it.

---

## Prerequisites

- **Obsidian 1.12.7+** with the CLI enabled (Settings > General > Command line interface)
- **Obsidian desktop app running** (the CLI communicates with the running app)
- **Claude Code** with skill file loaded
- **Git** initialized in the vault root (for version history and provenance)
- **`shasum`** available (standard on macOS/Linux; for source hash tracking)

---

## Vault Structure

```
vault/
  raw/                          # Layer 1: Immutable source documents
    assets/                     # Downloaded images, PDFs
    <source-files>.md           # Clipped articles, papers, notes
  wiki/                         # Layer 2: LLM-generated knowledge base
    index.md                    # Content catalog (token-budgeted)
    entities/                   # Entity pages (people, orgs, tools, etc.)
    concepts/                   # Concept pages (ideas, theories, patterns)
    sources/                    # Source summary pages (one per raw source)
    comparisons/                # Comparison and analysis pages
    synthesis.md                # Evolving high-level synthesis
  templates/                    # Obsidian templates for each page type
    entity.md
    concept.md
    source-summary.md
    comparison.md
  scripts/                      # Supporting shell scripts
    hash-sources.sh
    check-stale.sh
    build-index.sh
  CLAUDE.md                     # Layer 3: Schema (skill + conventions)
```

### Why This Structure

- **`raw/`** is never modified by the LLM. It's the source of truth the human curates.
- **`wiki/`** is entirely LLM-owned. The human reads it; the LLM writes and maintains it.
- **`templates/`** are Obsidian templates the LLM uses via `obsidian create ... template=<name>`.
- **`scripts/`** are lightweight shell scripts for operations the CLI doesn't natively support (hashing, staleness checks).
- **`CLAUDE.md`** is the schema — loaded automatically by Claude Code. It defines conventions, workflows, and accumulated corrections.

---

## Templates

Each page type has a template enforcing consistent structure. Templates include a required TLDR, claim-typed sections, and frontmatter for provenance tracking.

### Entity Template (`templates/entity.md`)

```markdown
---
type: entity
entity_type: ""
sources: []
source_hashes: {}
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
source_hashes: {}
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
source_hash: ""
ingested: "{{date}}"
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
source_hashes: {}
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

---

## Claim Types

Every substantive claim in the wiki uses one of four Obsidian callout types. This is the primary epistemic integrity mechanism.

| Callout | Meaning | Rule |
|---------|---------|------|
| `> [!source]` | Verbatim or closely paraphrased fact | Must include `[[source]]` link. If you can't cite it, it's not a Source. |
| `> [!analysis]` | Inference drawn from sourced facts | Must show reasoning. Must link to the Source claims it's derived from. |
| `> [!unverified]` | Claim without an authoritative source | Flagged for future verification. Never present as fact. |
| `> [!gap]` | Explicitly missing knowledge | Never fill with a plausible guess. Exists to mark what the wiki doesn't know. |

**The critical distinction is Source vs. Analysis.** If the LLM is paraphrasing, synthesizing, or inferring — even if it feels obvious — it's Analysis, not Source. This prevents the most common failure mode: the wiki presenting an LLM inference as a sourced fact.

---

## Supporting Scripts

### `scripts/hash-sources.sh`

Generates SHA-256 hashes for all files in `raw/`. Outputs a manifest that the skill uses to detect source changes.

```bash
#!/bin/bash
# Usage: ./scripts/hash-sources.sh [vault_path]
# Output: JSON manifest of source file hashes to stdout

VAULT="${1:-.}"
RAW_DIR="$VAULT/raw"

if [ ! -d "$RAW_DIR" ]; then
  echo '{}' 
  exit 0
fi

echo "{"
first=true
find "$RAW_DIR" -type f ! -name '.DS_Store' ! -path '*/.git/*' | sort | while read -r file; do
  rel_path="${file#$VAULT/}"
  hash=$(shasum -a 256 "$file" | cut -d' ' -f1)
  if [ "$first" = true ]; then
    first=false
  else
    echo ","
  fi
  printf '  "%s": "%s"' "$rel_path" "$hash"
done
echo ""
echo "}"
```

### `scripts/check-stale.sh`

Compares current source hashes against the hashes stored in wiki page frontmatter. Reports which wiki pages reference changed sources.

```bash
#!/bin/bash
# Usage: ./scripts/check-stale.sh [vault_path]
# Output: List of wiki pages with stale source references

VAULT="${1:-.}"
WIKI_DIR="$VAULT/wiki"
MANIFEST=$(bash "$VAULT/scripts/hash-sources.sh" "$VAULT")

stale_count=0

find "$WIKI_DIR" -name '*.md' -type f | sort | while read -r page; do
  rel_page="${page#$VAULT/}"
  
  # Extract source_hash entries from frontmatter
  in_frontmatter=false
  in_hashes=false
  while IFS= read -r line; do
    if [ "$line" = "---" ]; then
      if [ "$in_frontmatter" = true ]; then
        break
      fi
      in_frontmatter=true
      continue
    fi
    
    if [ "$in_frontmatter" = true ]; then
      case "$line" in
        source_hashes:*) in_hashes=true ;;
        *:*) 
          if [ "$in_hashes" = true ]; then
            # Check if this is a nested key (indented) or a new top-level key
            case "$line" in
              "  "*)
                src=$(echo "$line" | sed 's/^ *//' | cut -d: -f1 | tr -d '"')
                stored_hash=$(echo "$line" | cut -d: -f2- | tr -d ' "')
                current_hash=$(echo "$MANIFEST" | grep "\"$src\"" | cut -d: -f2 | tr -d ' ",')
                if [ -n "$current_hash" ] && [ "$stored_hash" != "$current_hash" ]; then
                  echo "STALE: $rel_page (source changed: $src)"
                  stale_count=$((stale_count + 1))
                fi
                ;;
              *) in_hashes=false ;;
            esac
          fi
          ;;
      esac
    fi
  done < "$page"
done

if [ "$stale_count" = 0 ]; then
  echo "No stale pages detected."
fi
```

### `scripts/build-index.sh`

Rebuilds the index from wiki page frontmatter and TLDRs. Used as a fallback when the index drifts from actual content.

```bash
#!/bin/bash
# Usage: ./scripts/build-index.sh [vault_path]
# Output: Markdown index content to stdout

VAULT="${1:-.}"
WIKI_DIR="$VAULT/wiki"

echo "# Wiki Index"
echo ""
echo "Auto-generated from page frontmatter. $(date '+%Y-%m-%d %H:%M')."
echo ""

for category in entities concepts sources comparisons; do
  dir="$WIKI_DIR/$category"
  [ ! -d "$dir" ] && continue
  
  echo "## ${category^}"
  echo ""
  
  find "$dir" -name '*.md' -type f | sort | while read -r file; do
    name=$(basename "$file" .md)
    rel_path="${file#$VAULT/}"
    
    # Extract TLDR from file (first line after > [!tldr])
    tldr=$(awk '/\[!tldr\]/{getline; gsub(/^> ?/, ""); print; exit}' "$file")
    
    if [ -n "$tldr" ]; then
      echo "- [[$name]] — $tldr"
    else
      echo "- [[$name]]"
    fi
  done
  
  echo ""
done
```

---

## Operations

The three core operations from the gist, implemented through the Obsidian CLI.

### Ingest

Process a new source document into the wiki. This is the primary knowledge-building operation.

**Workflow:**

1. **Hash the source.** Run `scripts/hash-sources.sh` to get the current hash of the new source file.

2. **Read the source.** Use `obsidian read path=raw/<source-file>` to read the full source content.

3. **Discuss with human.** Summarize key takeaways. Ask the human what to emphasize, what's important, what connects to existing wiki content. (This step is skippable for batch ingest, but recommended for deliberate knowledge building.)

4. **Search for existing relevant pages.** Use `obsidian search query="<key terms>" path=wiki` and `obsidian search:context query="<key terms>" path=wiki` to find pages that need updating.

5. **Create the source summary page.** Use `obsidian create name="<source-name>" path=wiki/sources template=source-summary`. Then use `obsidian property:set` to populate frontmatter fields (`raw_path`, `source_hash`, `tags`). Use `obsidian append` to write the page body.

6. **Create or update entity pages.** For each entity mentioned in the source:
   - Search: `obsidian search query="<entity name>" path=wiki/entities`
   - If no existing page: `obsidian create name="<entity>" path=wiki/entities template=entity`
   - If existing page: `obsidian read path=wiki/entities/<entity>.md`, then apply targeted updates via `obsidian append` or by reading, modifying, and writing back.
   - Update frontmatter: `obsidian property:set file="<entity>" name=sources value="<updated list>"` and record the source hash.

7. **Create or update concept pages.** Same pattern as entities but in `wiki/concepts/`.

8. **Update the index.** Read `wiki/index.md`, add entries for new pages, update summaries for modified pages.

9. **Log via git.** Commit all changes with a message describing what was ingested.

**Claim typing discipline during ingest:**
- Direct extractions from the source -> `> [!source]` with `[[source-summary-page]]` link
- Connections or inferences the LLM draws -> `> [!analysis]` with reasoning
- Claims the source makes without evidence -> `> [!unverified]`
- Questions raised but not answered -> `> [!gap]`

**Key CLI commands used:**
```bash
obsidian read path=raw/article.md
obsidian create name="Entity Name" path=wiki/entities template=entity
obsidian property:set file="Entity Name" name=source_hash value='{"raw/article.md": "abc123..."}'
obsidian property:set file="Entity Name" name=sources value="[[article-summary]]"
obsidian property:set file="Entity Name" name=updated value="2026-04-13"
obsidian append file="Entity Name" content="> [!source] Key fact\n> Extracted fact. [[article-summary]]"
obsidian search query="relevant term" path=wiki
obsidian read path=wiki/entities/existing-entity.md
```

### Query

Ask a question against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer.

**Workflow:**

1. **Search the index.** Read `wiki/index.md` to identify candidate pages.

2. **Search for specifics.** Use `obsidian search query="<terms>" path=wiki` and `obsidian search:context query="<terms>" path=wiki` to find pages the index might miss.

3. **Read relevant pages.** Use `obsidian read` on the most relevant pages (guided by TLDRs in the index).

4. **Follow links.** Use `obsidian backlinks file="<page>"` and `obsidian links file="<page>"` to discover related pages.

5. **Synthesize an answer.** Cite wiki pages. Distinguish between what the wiki says (sourced) and what the LLM infers (analysis).

6. **Optionally file the answer back.** If the query produced a valuable comparison, analysis, or synthesis, create a new page in `wiki/comparisons/` or `wiki/concepts/` so the insight compounds.

7. **Dual output.** If the query revealed gaps, outdated claims, or missing connections — update the relevant wiki pages as a side effect.

**Key CLI commands used:**
```bash
obsidian read path=wiki/index.md
obsidian search query="machine learning" path=wiki format=json
obsidian search:context query="transformer architecture" path=wiki
obsidian read path=wiki/concepts/transformers.md
obsidian backlinks file="transformers"
obsidian links file="transformers"
```

### Lint

Health-check the wiki. Run periodically (weekly, or after a batch of ingests).

**Workflow:**

1. **Check staleness.** Run `scripts/check-stale.sh` to find pages with outdated source references.

2. **Find orphans.** Use `obsidian orphans` to find pages with no incoming links.

3. **Find dead ends.** Use `obsidian deadends` to find pages with no outgoing links.

4. **Find unresolved links.** Use `obsidian unresolved` to find wikilinks pointing to non-existent pages.

5. **Scan for unverified claims.** Use `obsidian search:context query="[!unverified]" path=wiki` to find all unverified claims. Assess whether any can now be verified or should be removed.

6. **Scan for gaps.** Use `obsidian search:context query="[!gap]" path=wiki` to collect all stated gaps. Assess whether new sources could fill them.

7. **Check index consistency.** Run `scripts/build-index.sh` and compare with current `wiki/index.md`. Flag discrepancies.

8. **Review hub pages.** Use `obsidian backlinks file="<page>" --total` on major pages to identify over-connected hubs that may need splitting.

9. **Report findings.** Present a summary: stale pages, orphans, dead ends, unresolved links, unverified claims, gaps, and recommended actions.

10. **Apply fixes.** With human approval, update stale pages, link orphans, create pages for unresolved links, resolve or remove unverified claims.

**Key CLI commands used:**
```bash
bash scripts/check-stale.sh /path/to/vault
obsidian orphans format=json
obsidian deadends format=json
obsidian unresolved format=json
obsidian search:context query="[!unverified]" path=wiki
obsidian search:context query="[!gap]" path=wiki
obsidian backlinks file="important-concept" --total
```

---

## The Skill File (CLAUDE.md)

The schema document loaded by Claude Code. This is the operational core — it tells the LLM how to behave.

```markdown
# LLM Wiki Schema

You maintain a personal knowledge wiki in this Obsidian vault.

## Your Role

You are the writer. The human is the editor-in-chief. You propose changes;
the human directs, reviews, and corrects. Every correction you receive
should inform how you handle similar situations in the future — update
the "Accumulated Corrections" section at the bottom of this file.

## Vault Structure

- `raw/` — Immutable source documents. You read from here, never write.
- `wiki/` — Your knowledge base. You own this directory entirely.
  - `wiki/index.md` — Content catalog. Update on every ingest.
  - `wiki/entities/` — Entity pages (people, orgs, tools, places).
  - `wiki/concepts/` — Concept pages (ideas, theories, patterns).
  - `wiki/sources/` — Source summary pages (one per raw source).
  - `wiki/comparisons/` — Analysis and comparison pages.
  - `wiki/synthesis.md` — Evolving high-level synthesis.
- `templates/` — Page templates. Use via `obsidian create ... template=<name>`.
- `scripts/` — Shell scripts for hashing and staleness checks.

## Operations

### Ingest (`/ingest <source-file>`)
1. Hash the source: `bash scripts/hash-sources.sh .`
2. Read: `obsidian read path=raw/<file>`
3. Discuss key takeaways with the human (unless batch mode).
4. Search for existing relevant pages:
   `obsidian search query="<terms>" path=wiki`
5. Create source summary in `wiki/sources/` using `source-summary` template.
6. Create or update entity pages in `wiki/entities/`.
7. Create or update concept pages in `wiki/concepts/`.
8. Store source hash in frontmatter of every page you create or update.
9. Update `wiki/index.md`.
10. Commit via git.

### Query (`/query <question>`)
1. Read `wiki/index.md` for candidate pages.
2. Search: `obsidian search query="<terms>" path=wiki`
3. Read relevant pages. Follow links via `obsidian backlinks`/`obsidian links`.
4. Synthesize answer with citations.
5. If the answer is valuable, file it as a new page.
6. If you discover gaps or stale content, update affected pages (dual output).

### Lint (`/lint`)
1. Run `bash scripts/check-stale.sh .`
2. Run `obsidian orphans`, `obsidian deadends`, `obsidian unresolved`.
3. Search for `[!unverified]` and `[!gap]` callouts.
4. Compare `scripts/build-index.sh` output against `wiki/index.md`.
5. Report findings. Apply fixes only with human approval.

## Claim Typing (Mandatory)

Every substantive claim uses one of these callout types:

- `> [!source]` — Fact directly from a source. MUST include `[[source]]` link.
- `> [!analysis]` — Your inference. MUST show reasoning.
- `> [!unverified]` — No authoritative source. Flagged for verification.
- `> [!gap]` — Explicitly missing. NEVER fill with a guess.

If you are paraphrasing, synthesizing, or inferring — even if it seems
obvious — use `[!analysis]`, not `[!source]`.

## Provenance Rules

- Every wiki page records its source files and their SHA-256 hashes
  in frontmatter (`sources`, `source_hashes`).
- When updating a page from a new source, add the new source and hash.
- Never remove old source references — they are the page's provenance chain.
- When a source hash doesn't match current, mark the page
  `status: stale` in frontmatter.

## Index Rules

- `wiki/index.md` lists every wiki page with its TLDR.
- Keep the index under ~3,000 tokens. If it exceeds this, split into
  per-category sections with collapsed details.
- Every page MUST have a `> [!tldr]` as its first content block.

## Conventions

- One page per entity. Use `obsidian search` before creating to avoid duplicates.
- Use wikilinks (`[[Page Name]]`) for all cross-references.
- Tags in frontmatter, not inline.
- Dates in ISO 8601 (`2026-04-13`).
- When sources disagree, surface the disagreement explicitly. Do not
  smooth contradictions into false coherence.
- Prefer targeted updates (append, property:set) over full page rewrites.

## Accumulated Corrections

<!-- Add corrections here as the human provides feedback.
     Format: date, what was wrong, what to do instead. -->
```

---

## Scaling Plan

The design above works at personal scale (~100 sources, ~hundreds of pages) with no infrastructure beyond Obsidian, git, and shell scripts. When concrete bottlenecks appear, add infrastructure in this order:

### When the index file stops working (~200+ pages)

The `obsidian search` and `obsidian search:context` commands provide full-text search without additional infrastructure. The index file serves as a curated, token-efficient entry point — not the only search mechanism. If search results become noisy:

1. **Federated indexes.** Split `wiki/index.md` into per-category indexes (`wiki/entities/index.md`, `wiki/concepts/index.md`). Read only the relevant category index per query.
2. **Tag-based navigation.** Use `obsidian tags` and `obsidian tag name=<tag>` to navigate by topic rather than by page listing.
3. **SQLite FTS5 index.** Add a `scripts/build-sqlite-index.sh` that indexes page content, TLDRs, and frontmatter into SQLite with FTS5. Query the index via a `scripts/search-wiki.sh` wrapper. Keep markdown as source of truth; treat SQLite as a rebuildable cache.

### When staleness management becomes burdensome

1. **Lazy recompilation.** When `check-stale.sh` reports stale pages, don't recompile all of them immediately. Recompile each page the next time it's accessed by a query. Add a lint task that recompiles the most-linked stale pages proactively.
2. **Diff-based ingest.** When a source is updated (not new), use `git diff` on the source to identify what changed, then update only the affected wiki pages. This requires the dependency map already tracked in frontmatter (`sources` field).

### When compilation quality becomes a concern

1. **Periodic audit.** Sample 5-10 random wiki pages per lint pass. Read the page and its cited sources. Check whether the claims are actually supported. This is manual but catches the silent degradation that automated lint misses.
2. **Wiki + RAG verification.** When answering a query, verify the wiki's answer against the raw sources directly (read the relevant raw files, not just the wiki pages). This is the "combined" approach that outperformed either alone in head-to-head tests.

---

## What This Proposal Deliberately Excludes

- **Multi-model verification.** 4x cost for marginal accuracy. Not worth it at personal scale.
- **Cryptographic receipts.** Solving a problem personal wikis don't have.
- **Formal ontologies.** OWL-RL and SPARQL require specialized knowledge and add a second knowledge management problem.
- **Multi-agent coordination.** Consensus voting, trust tiers, contamination firewalls. The pattern is unproven at single-agent scale; multi-agent is premature.
- **Knowledge graph databases.** Wikilinks are an implicit graph. Making it explicit adds infrastructure without clear benefit at personal scale.
- **Identity-aware role filtering.** Multiplicative in wiki size and maintenance.
- **Autonomous operation.** No cron-based maintenance, no autopilot. Errors compound faster without human review. The human stays in the loop.

---

## Deliverables

| File | Purpose |
|------|---------|
| `CLAUDE.md` | The skill file / schema. Loaded by Claude Code automatically. |
| `templates/entity.md` | Template for entity pages. |
| `templates/concept.md` | Template for concept pages. |
| `templates/source-summary.md` | Template for source summary pages. |
| `templates/comparison.md` | Template for comparison/analysis pages. |
| `scripts/hash-sources.sh` | SHA-256 hash manifest for raw sources. |
| `scripts/check-stale.sh` | Staleness checker (compares current hashes to stored). |
| `scripts/build-index.sh` | Index rebuilder from page frontmatter + TLDRs. |

Total: 1 skill file, 4 templates, 3 scripts. No external dependencies beyond Obsidian, git, and standard Unix tools.
