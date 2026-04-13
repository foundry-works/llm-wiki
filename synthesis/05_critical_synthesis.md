# LLM Wiki: Core Challenges & Promising Solutions

A critical assessment of the ideas in `llm-wiki-ideas.md`. Each challenge is evaluated for severity. Each proposed solution is evaluated for plausibility, feasibility, effectiveness, and complexity. The goal: separate what matters from what's overengineered, and surface a practical priority stack.

---

## The Six Core Challenges

Ranked by severity — how much damage they cause if left unaddressed.

### 1. Epistemic Integrity (Critical)

**The risk:** A wiki mistake doesn't reset like a stateless hallucination — it persists and becomes a prior that future compilations build on. Over time, compounding errors can make the wiki actively harmful: confidently wrong, with the confidence itself sourced from its own earlier mistakes.

**Why it's the top priority:** Every other feature of the wiki — scaling, search, multi-agent, provenance — is worthless if the wiki's content can't be trusted. A well-organized, fast-searching, beautifully indexed wiki that's full of subtly wrong syntheses is worse than no wiki at all, because you'll act on it.

**An inconvenient finding:** ETH Zurich research showed LLM-generated context files hurt agent performance in 5 of 8 settings ([344.md](comments/344.md)). This doesn't just suggest "be careful" — it suggests the entire premise needs guardrails. The wiki is an LLM-generated context file that persists indefinitely. If the LLM is generating context that makes itself dumber, the system has a negative feedback loop baked in.

**What makes this hard:** The failure mode is silent. A wiki page that confidently merges two sources into a coherent synthesis, when the sources actually disagree, looks correct on inspection. You'd need to go back to the raw sources to catch it — which is precisely the work the wiki was supposed to eliminate.

### 2. Staleness (High)

**The risk:** Sources change. The wiki pages derived from them don't know it. 15 pages can be silently wrong because a single source was updated.

**Why it matters:** Unlike epistemic integrity (where the error originates in the compilation step), staleness is structural — even perfect compilation goes stale. The wiki's value proposition is that knowledge is "compiled once and kept current." Without staleness detection, the "kept current" part is aspirational, not actual.

**What makes this hard:** Detection is solved (hash the sources, compare on access). The hard part is the recompilation policy. Eager recompilation (re-derive all dependent pages immediately) is expensive and may recompile pages no one ever reads again. Lazy recompilation (recompile on next access) means stale pages persist until someone stumbles into them.

### 3. Retrieval at Scale (High)

**The risk:** The index-file approach stops working past ~200 pages. The LLM can't navigate the wiki, so it can't find relevant pages, so its answers degrade — not because the knowledge isn't there, but because it can't find it.

**Why it matters:** This is the most commonly reported concrete failure. Multiple independent builders hit this wall at roughly the same page count.

**What makes it tractable:** Unlike the first two challenges, this one has proven solutions. SQLite FTS5 for keyword search, sqlite-vec for semantic search, or structure-aware tree traversal. The question isn't "can we solve it" but "when should we add the infrastructure."

### 4. Compilation Quality at Scale (Medium, Unknown)

**The risk:** Even with good retrieval, does the *quality of synthesis* degrade as the wiki grows? When the LLM is updating a page that touches 30 other pages, does it lose coherence? Does it introduce subtle inconsistencies because it can't hold the full wiki in context?

**Why it's uncertain:** No one in the thread reported this as a concrete failure. It's a theoretical concern extrapolated from context window limitations. But it's also the kind of failure that's hard to detect — you'd need to systematically audit synthesis quality at different wiki sizes, and no one has done that.

**Why it still matters:** If compilation quality degrades silently at scale, then the wiki's compounding value proposition has a hidden ceiling. You build 500 pages thinking your knowledge base is getting richer, but past page 300, each new ingest is introducing more inconsistency than knowledge.

### 5. Human Disengagement (Medium)

**The risk:** The Generation Effect — outsourcing the writing to an LLM means you don't process the material as deeply, so you understand it less, even though you "have" it in your wiki.

**Why it's medium, not high:** The critique is cognitively valid but practically overstated. The gist's claim isn't "you'll understand the material as deeply as if you wrote it yourself." It's "you'll have a maintained knowledge base instead of an abandoned one." For most use cases — research reference, project knowledge, competitive analysis — a maintained index you understand at 70% depth beats a hand-written wiki you abandoned at 15% coverage. The tradeoff is real, but the gist is already on the right side of it for most users.

**Where it does matter:** For domains where deep personal understanding is the point — studying for exams, developing original research theses, building intuition in a new field — the Generation Effect critique has teeth. In these cases, the wiki is a crutch that prevents the learning it's supposed to support.

### 6. Autonomous Error Compounding (Medium)

**The risk:** Many implementations push toward full autonomy — cron-based maintenance, autopilot ingest, autonomous research loops. Autonomy amplifies Challenge #1: errors compound faster when no human is reviewing.

**Why it's listed separately:** The gist itself emphasizes human involvement. The push toward autonomy comes from the community, not the pattern. But it's a natural evolution — if the LLM can maintain the wiki, why not let it run unsupervised? The answer is: because errors compound, and the error rate isn't zero.

---

## Solution Assessment

### Tier 1: High Impact, Low Complexity (Implement First)

These are schema conventions or lightweight mechanisms that directly address core challenges with minimal infrastructure cost.

**1. Claim Typing** (addresses: Epistemic Integrity)

Four claim types as a schema convention: **Source** (verbatim quote with citation), **Analysis** (inference with reasoning shown), **Unverified** (no authoritative source yet), **Gap** (explicitly missing). The Analysis/Unverified split is the key innovation — it forces the LLM to distinguish between "I found this stated explicitly" and "I'm inferring this."

- *Feasibility:* Trivially implementable — just add the convention to the schema. No infrastructure needed.
- *Effectiveness:* Production-tested over 6 months ([374.md](comments/374.md)). The team that built it reported the Analysis/Unverified split "earned its keep."
- *Complexity:* Near zero. It's a markdown convention.
- *Limitation:* Relies on the LLM correctly classifying its own claims. LLMs are imperfect at this — they can present an inference as a source-backed fact. Claim typing reduces the rate but doesn't eliminate it.

**2. Source Hash Tracking** (addresses: Staleness)

Store a content hash of each source file at compilation time. On query, check the hash. Mismatch = stale.

- *Feasibility:* A few lines of code per ingest. Store hashes in page frontmatter or a separate manifest.
- *Effectiveness:* Deterministic staleness detection. No false negatives — if the source changed, you know.
- *Complexity:* Minimal. SHA-256 hashing is a standard library call.
- *Limitation:* Detection only. You still need a recompilation strategy (see Tier 2).

**3. Entity Type Templates** (addresses: Compilation Quality, Wiki Structure)

One template per entity type, not one generic template. Seven types as production-tested sweet spot.

- *Feasibility:* Schema convention. Define the templates, include them in the schema document.
- *Effectiveness:* Constrains the LLM's output format, reducing drift and inconsistency across pages. Makes lint checkable — a page that doesn't match its template is structurally wrong.
- *Complexity:* Low. The upfront work is designing the templates; after that, it's self-reinforcing.
- *Limitation:* Requires knowing your entity types upfront. The gist's advice to let the schema co-evolve is in mild tension with this — you may need to redesign templates as the wiki matures.

**4. TLDRs + Index Token Budgets** (addresses: Retrieval, Token Efficiency)

Add a TLDR to the top of every wiki page. Give the index a token budget (L0 ~200 tokens through L3 5-20K). Keep the index surgically small.

- *Feasibility:* Schema conventions. No tooling needed.
- *Effectiveness:* TLDRs let the LLM decide whether to read a full page without spending tokens on it. Index budgets prevent context window bloat — critical for Claude Code, where compaction silently drops deprioritized content.
- *Complexity:* Near zero.
- *Limitation:* TLDRs are themselves LLM-generated and can be wrong. But a wrong TLDR is much less dangerous than a wrong full page — it just leads to reading the wrong page, not acting on wrong facts.

**5. "LLM Proposes Diffs, Not Overwrites"** (addresses: Epistemic Integrity, Human Oversight)

Every wiki edit is proposed as a diff, not a wholesale page rewrite. The human (or a review step) sees what changed and can approve or reject.

- *Feasibility:* Schema convention + workflow change. Tell the LLM to output proposed changes in a structured format before committing.
- *Effectiveness:* Makes every edit reviewable. Prevents the silent rewrite problem where an ingest changes 15 pages and you can't tell what's different.
- *Complexity:* Low, but adds friction to every ingest. For supervised workflows (the gist's preference), this is fine. For autonomous workflows, it becomes a bottleneck.
- *Limitation:* Review fatigue. If every ingest touches 15 pages and each has a diff to review, the human will start rubber-stamping.

**6. "Every Task Produces Two Outputs"** (addresses: Wiki Maintenance)

The deliverable and wiki updates, always. The wiki gets updated as a side effect of normal work, not as a separate maintenance task.

- *Feasibility:* Behavioral convention in the schema. The LLM produces the answer to your question *and* updates relevant wiki pages in the same operation.
- *Effectiveness:* Solves the maintenance problem at its root — the wiki never falls behind because it's updated continuously.
- *Complexity:* Near zero. It's a prompt instruction.
- *Limitation:* Increases token usage per task (you're paying for wiki updates you didn't explicitly ask for). For expensive models, this adds up.

### Tier 2: High Impact, Moderate Complexity (Implement When Needed)

These require some infrastructure but solve problems that will eventually become blocking.

**7. Lazy Recompilation with Stale Markers** (addresses: Staleness, Cascading Invalidation)

When a source changes, mark all derived pages as "potentially stale" (via the hash tracking from Tier 1). Don't recompile immediately. When a stale page is accessed (by a query or during a lint pass), recompile it then.

- *Feasibility:* Requires: (a) a dependency map (which pages derive from which sources), (b) a mechanism to mark pages stale, (c) a recompilation trigger on access. The dependency map is the hardest part — it needs to be maintained during ingest.
- *Effectiveness:* Avoids wasted recompilation of pages no one reads. Ensures any page you *do* read is fresh.
- *Complexity:* Moderate. The dependency map adds bookkeeping to every ingest.
- *Limitation:* Stale pages persist until accessed. If a stale page is linked from a non-stale page, the non-stale page's cross-references may be misleading. A compromise: run a periodic lint pass that recompiles the most-linked stale pages.

**8. SQLite as Index** (addresses: Retrieval at Scale)

Keep markdown as source of truth. Index page metadata, TLDRs, tags, and content in SQLite. Query the index instead of the index file.

- *Feasibility:* SQLite is a single file, zero-server, available in every language. FTS5 for keyword search is built in.
- *Effectiveness:* Production-validated after 6-12 months of filesystem experience ([092.md](comments/092.md)). Scales well past the ~200-page ceiling.
- *Complexity:* Moderate. You need: an indexing step after each ingest, a search tool the LLM can invoke, and a sync mechanism to keep the index consistent with the markdown files.
- *Limitation:* You now have two sources of truth — the markdown files and the SQLite index. They can get out of sync. Treat the index as a cache: if it's wrong, rebuild from markdown.
- *When to add it:* When the index file exceeds the LLM's comfortable context window, or when you notice the LLM failing to find relevant pages.

**9. Diff-Based Ingest** (addresses: Token Efficiency, Compilation Quality)

When a source changes, use `git diff` to identify what actually changed, then only update wiki pages affected by the changes.

- *Feasibility:* Requires git for raw sources and a dependency map (same as #7).
- *Effectiveness:* Dramatically reduces the scope of each ingest. Instead of re-reading and re-processing an entire source, the LLM focuses on what changed. Cheaper, faster, and less likely to introduce new errors in unchanged sections.
- *Complexity:* Moderate. The LLM needs to interpret diffs correctly, which is a skill it generally has.
- *Limitation:* Misses indirect effects. A change in Section 3 of a source might invalidate a synthesis that combined Section 3 with Section 7 — but the diff only shows Section 3 changed.

**10. Training Period (30-Day Human Review)** (addresses: Epistemic Integrity, Autonomous Error Compounding)

For the first ~30 days, a human reviews every wiki write. The LLM learns the human's conventions, correction patterns, and quality standards. After the training period, automated linting takes over.

- *Feasibility:* No infrastructure needed — it's a workflow discipline. The schema accumulates corrections naturally.
- *Effectiveness:* Builds the schema's correction history, which is the real flywheel ([156.md](comments/156.md)). The LLM's wiki writes improve as the schema captures more conventions.
- *Complexity:* Low infrastructure, high time investment. 30 days of review is a real commitment.
- *Limitation:* The quality ceiling is set by the LLM's ability to generalize from corrections. Some error types keep recurring despite corrections in the schema.

### Tier 3: Interesting but Overengineered (Defer or Skip)

These solutions solve real problems but at a complexity cost that exceeds their benefit for most users.

**Multi-Model Verification** — Running 4 frontier LLMs on every claim is 4x the API cost for marginal accuracy gains. Models from the same training paradigm share blind spots, so "4 models agree" doesn't mean "correct." The cost-benefit works only for high-stakes shared knowledge bases (legal, medical, financial). For personal wikis: not worth it.

**Cryptographic Receipts** — Solving a problem almost no one has. Proving to a third party that a specific model generated a specific wiki page matters for auditable, regulated, or adversarial contexts. For personal or team wikis where trust is established by other means: unnecessary complexity.

**Formal Ontologies (OWL-RL, SPARQL)** — Deterministic reasoning without LLM calls is elegant. But OWL-RL requires formal ontology design — a specialized skill that most wiki users don't have and most domains don't need. The maintenance cost of the ontology itself (keeping it consistent with the evolving wiki) is a second knowledge management problem on top of the first one.

**Consensus Voting with Signed Commits** — RSA-PSS signed knowledge commits, 75% thresholds, Devil's Advocate roles. This is enterprise-grade coordination infrastructure for a pattern that's barely proven at personal scale. Multi-agent wikis are an interesting future direction, but the unsolved problem there is consistency of style and categorization, not cryptographic trust. Git + PR review already provides adequate coordination for teams.

**Knowledge Graphs with Typed Edges** — Making the implicit wikilink graph explicit (typed edges, community detection, contradiction propagation) enables operations that flat markdown can't support. But for most personal wikis, those operations aren't needed. The wikilink graph is sufficient. When it isn't — for cross-paper research analysis or large-scale contradiction tracking — a lightweight approach (frontmatter tags for edge types) is better than a graph database.

**Identity-Aware Filtering** — Same sources producing different wiki pages per role (founder vs. engineer). Multiplicative in wiki size and maintenance cost. The value is real for team wikis with genuinely different audiences, but the simpler approach is to have one wiki with role-tagged sections, not N parallel wikis.

**Social Knowledge Networks** — A compelling vision: personal knowledge graphs with public sections, git-based forking, cross-validation. But the coordination and trust problems are unsolved even for single-agent wikis. Building a social layer on top of an unstable foundation is premature.

---

## Underappreciated Findings

Three results from the thread that deserve more attention than they got.

**1. Wiki + RAG Combined Never Lost**

Head-to-head tests across 7 evaluation rounds ([320.md](comments/320.md)) found that using the wiki for context and RAG for verification always outperformed either alone. This challenges the gist's anti-RAG framing. The gist positions the wiki as a replacement for RAG. The evidence suggests it's a complement. The practical implication: don't discard your RAG infrastructure when you build a wiki — use the wiki to provide compiled context and RAG to verify against raw sources.

**2. The Ingestion Gap**

The same head-to-head study found that a mostly-finished wiki performed 17% worse than a fully compiled one. This means you can't half-build a wiki and expect partial value — the cross-references and synthesis that make the wiki useful only emerge when coverage is sufficiently complete. Implication: commit to building the wiki for a domain or don't start. A wiki at 60% coverage may be worse than no wiki.

**3. The Compaction Problem**

Claude Code silently drops deprioritized content when context gets too long ([372.md](comments/372.md)). Rules set at session start can stop applying mid-session. This is an operational issue that affects every Claude Code-based wiki implementation. It means the index must be surgically small, the schema must fit in a tight token budget, and long sessions will degrade wiki maintenance quality. This isn't a design flaw in the wiki pattern — it's a constraint of the current tooling that the pattern must work within.

---

## Priority Stack

For someone building an LLM wiki today, the recommended implementation order:

### Phase 1: Foundation (Day 1)

Costs nothing but schema conventions. Addresses epistemic integrity and structure.

1. Add claim typing to the schema (Source / Analysis / Unverified / Gap)
2. Define entity type templates (start with 3-5, expand to ~7 as the domain clarifies)
3. Add TLDRs as a required element on every wiki page
4. Set an index token budget and enforce it
5. Schema convention: "LLM proposes diffs, not overwrites" for all wiki edits
6. Schema convention: "Every task produces two outputs — the deliverable and wiki updates"

### Phase 2: Provenance (Week 2-4)

Low-cost infrastructure that solves staleness detection.

7. Implement source hash tracking (hash stored in page frontmatter)
8. Build a source-to-page dependency map (maintained during ingest)
9. Add stale markers — when a source hash changes, mark derived pages
10. Human reviews all wiki writes during this period (the training period)

### Phase 3: Scaling Infrastructure (When Needed)

Add only when the index file stops working or token costs become a concern.

11. Implement diff-based ingest (update only changed pages)
12. Add SQLite indexing (FTS5 for keyword search)
13. Add lazy recompilation (recompile stale pages on access)
14. Consider hybrid search (BM25 + vectors) if semantic retrieval is insufficient

### Phase 4: Advanced (If the Domain Demands It)

These are worth the complexity only for specific use cases.

15. Multi-model spot-checking (not full verification — periodic audits of random pages)
16. The `reflect` step (for research wikis where understanding structural evolution matters)
17. Decision-based learning loops (for operational wikis: PM, trading, project management)
18. Wiki + RAG verification (use RAG to verify wiki answers against raw sources)

### What to Skip

Unless you have a specific, concrete reason:

- Formal ontologies and SPARQL
- Cryptographic receipt chains
- Multi-agent consensus protocols
- Identity-aware role filtering
- Social knowledge networks
- Parallel provenance layers (git history is sufficient for most users)
