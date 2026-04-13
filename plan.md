# Implementation Plan

Implements the proposal in `implementation-proposal.md`. Eight deliverable files (1 skill file, 4 templates, 3 scripts), a vault directory structure, and a tested end-to-end workflow.

---

## Phase 0: Prerequisites & Environment

**Goal:** Confirm the toolchain works before writing any code.

### 0.1 Verify Obsidian CLI

Obsidian 1.12.7+ required. The CLI must be enabled in Settings > General > Command line interface. On macOS this installs a symlink at `/usr/local/bin/obsidian`.

Verification:
```bash
obsidian version
```

If the command isn't found, the CLI isn't registered. Follow Obsidian's setup prompt.

### 0.2 Verify Git and shasum

```bash
git --version
shasum --version
```

Both should be available on any macOS or Linux system. If not, install via Homebrew or package manager.

### 0.3 Choose or Create the Vault

Either use an existing Obsidian vault or create a new one. The vault must be open in the Obsidian desktop app for CLI commands to work.

If creating a new vault: create it via Obsidian's UI (File > Open another vault > Create new vault). Note the path.

### 0.4 Configure Obsidian Settings

In the Obsidian desktop app:
- **Settings > Files and links > Default location for new notes:** "In the folder specified below" -> `wiki/`
- **Settings > Files and links > Attachment folder path:** `raw/assets/`
- **Settings > Templates > Template folder location:** `templates/`
- **Settings > Core plugins:** Enable Templates plugin if not already enabled

### 0.5 Initialize Git

```bash
cd /path/to/vault
git init
```

Create a `.gitignore`:
```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.trash/
```

Initial commit:
```bash
git add .gitignore
git commit -m "Initialize vault"
```

---

## Phase 1: Vault Directory Structure

**Goal:** Create the directory layout from the proposal.

**Depends on:** Phase 0

### 1.1 Create Directories

```bash
cd /path/to/vault
mkdir -p raw/assets
mkdir -p wiki/entities
mkdir -p wiki/concepts
mkdir -p wiki/sources
mkdir -p wiki/comparisons
mkdir -p templates
mkdir -p scripts
```

### 1.2 Create Index Scaffold

Create `wiki/index.md` with the initial structure:

```markdown
# Wiki Index

## Entities

## Concepts

## Sources

## Comparisons
```

### 1.3 Create Synthesis Scaffold

Create `wiki/synthesis.md`:

```markdown
---
type: synthesis
updated: ""
status: current
---

> [!tldr]
> High-level synthesis of the wiki's knowledge. Updated as the wiki grows.

## Overview

*No content yet. This page will be updated after the first few sources are ingested.*
```

### 1.4 Commit Structure

```bash
git add -A
git commit -m "Create vault directory structure"
```

---

## Phase 2: Templates

**Goal:** Create the four page templates and verify they work with the Obsidian CLI.

**Depends on:** Phase 1

### 2.1 Write Entity Template

Create `templates/entity.md` with the content from the proposal: frontmatter (type, entity_type, sources, source_hashes, created, updated, status, tags), TLDR callout, Overview section with source/analysis callouts, Relationships section, Open Questions section with gap callout.

### 2.2 Write Concept Template

Create `templates/concept.md`: frontmatter, TLDR, Definition, Key Claims (with all four callout types demonstrated), Connections, Contradictions & Tensions, Open Questions.

### 2.3 Write Source Summary Template

Create `templates/source-summary.md`: frontmatter (including raw_path and source_hash), TLDR, Key Takeaways, Entities Mentioned, Concepts Covered, Notes.

### 2.4 Write Comparison Template

Create `templates/comparison.md`: frontmatter (including subjects list), TLDR, Comparison table, Analysis, Open Questions.

### 2.5 Verify Template Creation via CLI

Test that the Obsidian CLI can create pages from templates:

```bash
obsidian create name="Test Entity" path=wiki/entities template=entity
obsidian read path="wiki/entities/Test Entity.md"
```

Verify:
- The page was created in the correct directory
- Frontmatter is intact
- Template content (callouts, sections) rendered correctly
- `{{date}}` variables were resolved

If `template=` doesn't work as expected, fallback plan: read the template via `obsidian template:read name=entity`, then create the page via `obsidian create` with the template content passed directly. Document whichever approach works in CLAUDE.md.

Clean up:
```bash
obsidian delete path="wiki/entities/Test Entity.md"
```

### 2.6 Commit Templates

```bash
git add templates/
git commit -m "Add page templates (entity, concept, source-summary, comparison)"
```

---

## Phase 3: Supporting Scripts

**Goal:** Write and test the three shell scripts.

**Depends on:** Phase 1 (can run in parallel with Phase 2)

### 3.1 Write hash-sources.sh

Create `scripts/hash-sources.sh` from the proposal. This script:
- Takes an optional vault path argument (defaults to `.`)
- Finds all files in `raw/` (excluding .DS_Store and .git)
- Outputs a JSON manifest of `{ "raw/filename": "sha256hash" }` to stdout

Make executable: `chmod +x scripts/hash-sources.sh`

### 3.2 Test hash-sources.sh

Drop a test file into `raw/`:
```bash
echo "Test source content" > raw/test-source.md
bash scripts/hash-sources.sh .
```

Expected output: valid JSON with one entry for `raw/test-source.md` and its SHA-256 hash.

Verify the hash is correct:
```bash
shasum -a 256 raw/test-source.md
```

Edge cases to test:
- Empty `raw/` directory (should output `{}`)
- Files with spaces in names
- Subdirectories within `raw/`
- Binary files (images in `raw/assets/`)

### 3.3 Write check-stale.sh

Create `scripts/check-stale.sh` from the proposal. This script:
- Takes an optional vault path argument
- Runs `hash-sources.sh` to get current hashes
- Reads frontmatter from each wiki page to find stored `source_hashes`
- Compares stored vs. current hashes
- Reports any mismatches as stale pages

Make executable: `chmod +x scripts/check-stale.sh`

### 3.4 Test check-stale.sh

This requires a wiki page with `source_hashes` in its frontmatter. Create a minimal test page:

```bash
obsidian create name="Test Stale" path=wiki/sources content="Test page"
obsidian property:set file="Test Stale" name=source_hashes value='{"raw/test-source.md": "known-bad-hash"}'
```

Run:
```bash
bash scripts/check-stale.sh .
```

Expected: reports `wiki/sources/Test Stale.md` as stale (because the stored hash doesn't match the current hash of `raw/test-source.md`).

Then update the hash to the correct value and re-run. Expected: "No stale pages detected."

**Important:** The frontmatter format for `source_hashes` as a nested YAML object needs to match what `obsidian property:set` actually produces. Test this and adjust the script's parsing if needed. This is the most likely point of friction — YAML nested object parsing in bash is fragile. If the format doesn't work cleanly, consider an alternative: store hashes as a flat string (`source_hash: "abc123"` for single-source pages) and use a separate `scripts/hash-manifest.json` file as the canonical hash store instead of per-page frontmatter.

### 3.5 Write build-index.sh

Create `scripts/build-index.sh` from the proposal. This script:
- Iterates over `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/comparisons/`
- Extracts the TLDR from each page (first line after `> [!tldr]`)
- Outputs a markdown index with wikilinks and TLDRs

Make executable: `chmod +x scripts/build-index.sh`

### 3.6 Test build-index.sh

Using any test pages still in the vault:
```bash
bash scripts/build-index.sh .
```

Expected: markdown output with categorized page listings. Compare against `wiki/index.md` to verify consistency.

### 3.7 Clean Up Test Artifacts

Remove test files:
```bash
obsidian delete path="wiki/sources/Test Stale.md"
rm raw/test-source.md
```

### 3.8 Commit Scripts

```bash
git add scripts/
git commit -m "Add supporting scripts (hash-sources, check-stale, build-index)"
```

---

## Phase 4: The Skill File

**Goal:** Write CLAUDE.md — the schema that governs all LLM behavior.

**Depends on:** Phases 2 and 3 (needs to reference verified template names and script paths)

### 4.1 Write CLAUDE.md

Create `CLAUDE.md` in the vault root with the content from the proposal's "The Skill File" section. This includes:

- Role definition (writer / editor-in-chief)
- Vault structure reference
- Operation workflows (Ingest, Query, Lint) with exact CLI commands
- Claim typing rules (Source, Analysis, Unverified, Gap)
- Provenance rules (source hashes in frontmatter)
- Index rules (token budget, TLDR requirement)
- Conventions (one page per entity, wikilinks, ISO dates, surface disagreements)
- Empty "Accumulated Corrections" section

### 4.2 Adjust CLI Commands Based on Phase 2/3 Findings

If Phase 2 testing revealed that certain CLI patterns don't work as expected (e.g., `template=` parameter, `property:set` with complex values, `path=` filtering on search), update the CLI commands in CLAUDE.md to match what actually works.

Document any workarounds discovered. For example:
- If `obsidian create ... template=entity` doesn't work, document the working alternative
- If `property:set` can't handle nested YAML objects, document the flat hash approach
- If `search ... path=wiki` doesn't filter by path, use `obsidian search query="<terms>" folder=wiki` or an alternative

### 4.3 Commit Skill File

```bash
git add CLAUDE.md
git commit -m "Add CLAUDE.md skill file (wiki schema and conventions)"
```

---

## Phase 5: Smoke Test — Ingest

**Goal:** Run the full ingest workflow end-to-end with a real source document. Verify every step produces the expected result.

**Depends on:** All of Phases 1-4

### 5.1 Add a Test Source

Choose a real source document — a short article or paper (under 5 pages). Copy or clip it into `raw/`. If using Obsidian Web Clipper, clip an article directly.

### 5.2 Run Ingest

Open a Claude Code session in the vault directory. The CLAUDE.md should load automatically. Tell Claude to ingest the source:

```
Ingest the source at raw/<filename>.md
```

### 5.3 Verify Results

After ingest completes, check each expected output:

**Source summary page:**
- Created in `wiki/sources/`?
- Frontmatter populated (raw_path, source_hash, ingested date, tags)?
- TLDR present and accurate?
- Key takeaways use `[!source]` callouts with links?

**Entity pages:**
- Created in `wiki/entities/` for entities mentioned in the source?
- No duplicates (search was performed before creation)?
- Frontmatter includes source reference and hash?
- Claims properly typed (source vs. analysis)?

**Concept pages:**
- Same checks as entity pages, in `wiki/concepts/`.

**Index:**
- `wiki/index.md` updated with new pages?
- TLDRs included?
- Under token budget?

**Provenance:**
- Source hash in frontmatter matches `scripts/hash-sources.sh` output?
- Source references in all created/updated pages?

**Claim typing:**
- No bare claims outside callout blocks?
- Source callouts include `[[source-page]]` links?
- Analysis callouts show reasoning?
- Any uncertain claims marked `[!unverified]`?

### 5.4 Record Issues

Any problems discovered become corrections:
- If the LLM made mistakes, note them for the CLAUDE.md "Accumulated Corrections" section
- If CLI commands behaved unexpectedly, document workarounds in CLAUDE.md
- If templates need adjustment, update them

### 5.5 Commit

```bash
git add -A
git commit -m "First ingest: <source-name>"
```

---

## Phase 6: Smoke Test — Query

**Goal:** Ask a question against the wiki and verify the query workflow.

**Depends on:** Phase 5

### 6.1 Ask a Question

Ask something that requires reading at least 2-3 wiki pages to answer:

```
What are the main themes in the wiki so far?
```

Or a more specific question based on the ingested source.

### 6.2 Verify Results

- Did the LLM read the index first?
- Did it use `obsidian search` to find relevant pages?
- Did it read the relevant pages?
- Did it follow links (backlinks/outgoing links) to discover related content?
- Does the answer cite specific wiki pages?
- Does it distinguish sourced claims from its own inferences?

### 6.3 Verify Dual Output

- Did the LLM update any wiki pages as a side effect of the query?
- If the query revealed gaps, were they marked with `[!gap]`?
- If the answer was valuable, was it filed as a new page?

### 6.4 Record Issues and Commit

Same pattern as Phase 5.

---

## Phase 7: Smoke Test — Lint

**Goal:** Run the lint workflow and verify all checks work.

**Depends on:** Phase 5

### 7.1 Run Lint

```
Run a lint check on the wiki.
```

### 7.2 Verify Each Check

**Staleness:**
- `check-stale.sh` ran without errors?
- Output is meaningful (either reports stale pages or confirms none)?

**Structural health:**
- `obsidian orphans` ran and returned results (or empty)?
- `obsidian deadends` ran?
- `obsidian unresolved` ran?

**Claim scans:**
- Search for `[!unverified]` returned results?
- Search for `[!gap]` returned results?

**Index consistency:**
- `build-index.sh` output was compared to current `wiki/index.md`?
- Discrepancies flagged?

**Report:**
- Summary presented with clear categories?
- Recommended actions listed?
- No fixes applied without human approval?

### 7.3 Record Issues and Commit

Same pattern.

---

## Phase 8: Iteration & Refinement

**Goal:** Stress-test with more sources. Refine the schema based on real use.

**Depends on:** Phases 5-7

### 8.1 Ingest 3-5 More Sources

Choose sources that are related (overlapping entities/concepts) to test cross-referencing behavior. At least one source should introduce information that contradicts or updates a claim from an earlier source.

After each ingest, review:
- Are cross-references being created correctly?
- Is the LLM finding and updating existing pages (not creating duplicates)?
- Are contradictions surfaced (not smoothed)?
- Is the index staying manageable?

### 8.2 Test Source Update (Staleness)

Modify one of the raw sources (change some content). Then:
1. Run `bash scripts/check-stale.sh .` — should report stale pages
2. Tell Claude to re-ingest the updated source
3. Verify that affected pages are updated and hashes are refreshed

### 8.3 Update CLAUDE.md with Corrections

Review the "Accumulated Corrections" section. By this point there should be several entries based on mistakes caught during Phases 5-8. These corrections are the schema's learning mechanism — they prevent the same mistakes in future sessions.

### 8.4 Assess Template Fitness

After 4-6 sources, review whether the four templates cover the domain. Common adjustments:
- Do you need additional entity subtypes (the `entity_type` field)?
- Are the concept page sections right for your domain?
- Does the comparison template work for the kinds of comparisons you're making?
- Do you need a fifth template for a page type that keeps coming up?

Adjust templates if needed. Update CLAUDE.md to reference any changes.

### 8.5 Final Commit

```bash
git add -A
git commit -m "Complete initial wiki buildout (<N> sources, <M> wiki pages)"
```

---

## Dependency Graph

```
Phase 0 (Prerequisites)
  |
  v
Phase 1 (Directory Structure)
  |
  +-----------+-----------+
  |           |           |
  v           v           |
Phase 2     Phase 3       |
(Templates) (Scripts)     |
  |           |           |
  +-----------+           |
  |                       |
  v                       |
Phase 4 (CLAUDE.md) <-----+
  |
  v
Phase 5 (Smoke: Ingest)
  |
  +-------+
  |       |
  v       v
Phase 6  Phase 7
(Query)  (Lint)
  |       |
  +-------+
  |
  v
Phase 8 (Iteration)
```

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| `obsidian create ... template=` doesn't work as expected | Medium | Medium | Test in Phase 2.5. Fallback: read template content, pass to create directly. |
| `obsidian property:set` can't handle nested YAML (source_hashes) | High | Medium | Test in Phase 3.4. Fallback: flat `source_hash` string for single-source pages, separate manifest file for multi-source. |
| `obsidian search ... path=wiki` doesn't filter by path | Medium | Low | Test in Phase 2.5. Fallback: use `folder=wiki` parameter. |
| Obsidian desktop app not running when scripts execute | Low | High | Scripts are called from Claude Code during interactive sessions when Obsidian is open. Document requirement clearly. |
| TLDR extraction in build-index.sh fails on edge cases | Medium | Low | Test with various callout formats. Adjust awk pattern if needed. |
| Hash-sources.sh slow on large raw/ directories | Low | Low | Only affects vaults with hundreds of source files. Optimize with caching if needed. |
| Claude Code context compaction drops CLAUDE.md conventions mid-session | Medium | High | Keep CLAUDE.md concise. Keep index under token budget. For long sessions, remind Claude to re-read CLAUDE.md. |

---

## Success Criteria

The implementation is complete when:

1. All 8 deliverable files exist and are committed to git
2. A source has been ingested end-to-end with correct claim typing and provenance
3. A query has been answered using wiki content with proper citations
4. A lint pass has run all checks and produced a coherent report
5. At least one source update has been detected as stale and recompiled
6. CLAUDE.md has at least one accumulated correction from real use
7. The wiki has 4+ sources ingested with cross-referenced entity and concept pages
