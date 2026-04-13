# Questions Synthesis

A thematic synthesis of questions raised in the comments on Karpathy's LLM Wiki gist. Questions are grouped by theme, with commentary drawing on answers that emerged elsewhere in the thread.

---

## 1. Error Handling & Trust

The most substantive cluster of questions concerns what happens when the wiki gets things wrong — and the fact that, unlike a stateless LLM, mistakes here persist and compound.

- [002.md](comments/002.md) — @alinawab: *"What's the failure mode? Where does it start fighting you?"*
- [308.md](comments/308.md) — @Shagun0402: *"We're trading ephemeral hallucinations for persistent errors. If a wiki incorrectly links two concepts, that mistake becomes a prior that future generations build on."* Asks how to debug and evaluate these systems over time — especially when errors compound instead of resetting per prompt.
- [318.md](comments/318.md) — @XingwenZhang: *"With knowledge grows, how to manage them efficiently and avoid memory drift?"*
- [087.md](comments/087.md) — @barrygfox: *"Change in file hash invalidates all propositions derived from that file?"* — responding to a comment about source provenance tracking, and raising the question of cascading invalidation.
- [291.md](comments/291.md) — @jaychia: Notes that knowledge curation (not search) is the real data problem for AI, implying the wiki's correctness bottleneck is in the compilation step.

**What emerged in the thread:** Several implementations attacked this directly. The Freelance project ([085.md](comments/085.md)) tracks content hashes per source file so stale propositions are detected at query time. @bendetro ([088.md](comments/088.md)) proposed adding a `reflect` step to the loop — `ingest -> compile -> reflect -> query -> lint` — where the wiki records not just what changed but *why*, creating decision records as first-class pages. Multiple commenters converged on the idea that provenance tracking (knowing which source produced which claim) is the missing structural piece.

The gist's own `lint` operation partially addresses this, but the thread suggests lint alone isn't sufficient — you also need structural provenance so the system can trace errors back to their source rather than just scanning for surface contradictions.

---

## 2. Scaling

How far does this pattern stretch before it breaks?

- [035.md](comments/035.md) — @adagoral: *"I have complex PDFs (tables, images, columns), 100-300 technical manuals x 12 — is this idea still feasible for enterprise data?"*
- [155.md](comments/155.md) — @chipsageSupport: Wants to build a semiconductor wiki locally on an Intel Ultra 7 with 32GB RAM. Asks which local LLM to use.
- [318.md](comments/318.md) — @XingwenZhang: *"How to manage them efficiently and avoid the memory drift?"* — the scaling question framed as a maintenance problem.

**What emerged in the thread:** Karpathy's gist says the index-file approach "works surprisingly well at moderate scale (~100 sources, ~hundreds of pages)." Beyond that, the thread splits. Some built full search engines (qmd, OMEGA, RTFM with FTS5 + vector search). Others moved the index into SQLite ([092.md](comments/092.md)) after finding the filesystem approach stopped scaling. @xoai ([097.md](comments/097.md)) reported that sage-wiki needed multi-pass pipelines and ontology enforcement to stay coherent at scale. The consensus: the pattern works well up to a few hundred pages with just an index file; past that, you need proper search infrastructure and more aggressive lint.

For enterprise-scale PDFs, the thread offered no definitive answer, but several comments pointed to PDF-to-markdown conversion (anyformat-ai, Obsidian Web Clipper) as the necessary first step, with the wiki consuming the converted markdown rather than raw PDFs.

---

## 3. Wiki Structure & Organization

Practical questions about how to structure the wiki itself.

- [003.md](comments/003.md) — @alinawab: *"How do you decide when to create a new page vs. edit an existing one?"*
- [141.md](comments/141.md) — @Lukaschub: *"Instead of one massive single index file, I set up a federated organization — each major track has its own index.md."*
- [091.md](comments/091.md) — @rjbudzynski: *"Shouldn't index.md and log.md rather be database tables, in SQLite, DuckDB, whatever?"*
- [280.md](comments/280.md) — @ats-bcon: *"Don't you think you will need some kind of type schema to classify information?"*
- [360.md](comments/360.md) — @RonanCodes: *"How many instances would you recommend? Personal vs. work? One per project? If multiple, do you cross-query between them?"*
- [026.md](comments/026.md) — @MironV: *"Do you have any rules on periodic cleaning and pruning of the artifacts so they don't get unwieldy?"*

**What emerged in the thread:** The new-page-vs-edit question is really about granularity, and the gist is deliberately silent on it — the schema is meant to co-evolve with use. Several implementations introduced entity registries ([382.md](comments/382.md)) to prevent duplicate pages for the same concept. On indexing, the thread was divided: purists argued markdown files + `ls` is enough ([278.md](comments/278.md)), pragmatists moved to SQLite or DuckDB as the wiki grew. On federated vs. monolithic indexes, @Lukaschub's per-project approach was echoed by @RonanCodes's question about multiple instances — the emerging advice was: keep separate wikis per major domain, with the option to cross-reference via links but not a unified index. On pruning, lint is the prescribed mechanism, but the thread surfaced ideas like staleness scoring ([374.md](comments/374.md)) and spaced-repetition review ([162.md](comments/162.md)).

---

## 4. Team Sharing & Collaboration

- [004.md](comments/004.md) — @geetansharora: *"How can I share the knowledge base with my team? Currently we create a RAG and then an MCP server. Should we follow a similar approach?"*

**What emerged in the thread:** Since the wiki is just a git repo of markdown files, the simplest answer is: share the repo. Several implementations went further — @agentic-coop-db ([353.md](comments/353.md)) built a Postgres gateway for multi-agent distributed sharing, and the team-oriented wiki in [297.md](comments/297.md) used git submodules with Claude Code native integration. The MCP approach @geetansharora already uses could sit on top of the wiki as a query layer. The deeper question — access control, who can edit what, review gates — was addressed by implementations like Veritas Acta ([038.md](comments/038.md)) with its review-gated edits and multi-model verification.

---

## 5. Comparisons to Other Approaches

A recurring pattern: people recognizing the idea and asking how it relates to something they already know.

- [114.md](comments/114.md) — @fibrou: *"Is this similar to the Zettelkasten system?"*
- [102.md](comments/102.md) — @WolfgangSenff: *"I wonder if this works better than, or on par with, RAG — because while it feels overly simplistic, humans understand markdown far better than a bunch of numbers."*
- [014.md](comments/014.md) — @tomicz: *"I use Plan mode in Cursor — it sounds similar to that?"*
- [116.md](comments/116.md) — @PlantingProsperity: *"How does this differ from teaching your agent to use iwe-org/iwe?"*
- [193.md](comments/193.md) — @bulawow: *"Isn't this what Microsoft released called RPG-encoder?"*
- [216.md](comments/216.md) — @javi2375: *"How is this different from almost all markdown-based memory solutions in the past year? See: mem-agent-mcp."* Argues the system should run on a small local model, not a cloud LLM.
- [221.md](comments/221.md) — @gourav-sg: *"Are we not trying to build essentially knowledge graphs the same way that WWW conventions have been used?"* Suggests common vocabulary building is the critical missing piece.
- [304.md](comments/304.md) — @manjeetgupta: Asks whether PageIndex (reasoning-based retrieval) can overcome vector-based RAG limitations.

**What emerged in the thread:** The Zettelkasten comparison came up multiple times and was confirmed ([117.md](comments/117.md), [172.md](comments/172.md)) — the pattern *is* a Zettelkasten, with the LLM doing the work humans traditionally do. The key difference from RAG: RAG retrieves and forgets; the wiki compiles and remembers. The difference from Cursor's Plan mode or other agent memory: those are ephemeral working memory; the wiki is persistent compiled knowledge. @WolfgangSenff's intuition that markdown might outperform vector embeddings was validated by [320.md](comments/320.md), which ran head-to-head tests and found that wiki + RAG combined never lost. The thread's answer to "how is this different from X?" is usually: it isn't radically different in form — the insight is that the LLM does the maintenance, so the knowledge base actually gets maintained.

---

## 6. Self-Awareness & Meta-Cognition

The most philosophically interesting questions: can the wiki understand itself?

- [088.md](comments/088.md) — @bendetro: *"Does your wiki know why it's shaped the way it is? Can it trace why one concept became a hub while another stayed peripheral? Can it critique its own evolution?"* Proposes adding a `reflect` step and decision records as first-class wiki pages.
- [017.md](comments/017.md) — @AarushSharmaa: *"Are we building a brain for all our personalized AI Agents?"*
- [063.md](comments/063.md) — @kmeanskaran: Asks about combining LLM-as-a-judge with the wiki architecture — using one LLM to evaluate another's wiki edits.
- [265.md](comments/265.md) — @kenwCoding: Proposes 4D evolutionary knowledge graphs where time is the Z-axis, allowing agents to calculate "causal gradients" of how relationships evolved.

**What emerged in the thread:** @bendetro's `reflect` step was the most concrete proposal — making the wiki record not just what it knows but *how it came to know it*. This is a meaningful extension: most implementations track provenance at the source level (which file produced which claim) but not at the structural level (why this concept has 12 inbound links while that one has 2). The LLM-as-a-judge idea didn't get traction in the thread, but multi-model verification did — Veritas Acta ([038.md](comments/038.md)) uses multiple models to cross-check wiki edits. The 4D knowledge graph idea is ambitious but no implementation attempted it; the closest was the actor-network graph approach in [255.md](comments/255.md) which tracks relationship trajectories.

---

## 7. Tooling & Getting Started

Practical how-do-I-start questions.

- [066.md](comments/066.md) — @tcbhagat: *"How to use it on my Ubuntu desktop PC? What to use and how?"*
- [129.md](comments/129.md) — @cryptopsy0: *"Any alternative to Obsidian for the command line?"*
- [142.md](comments/142.md) — @LeonardoDaviti: *"Anyone tested with local models?"*
- [148.md](comments/148.md) — @mmoustafa8108: *"Hasn't anyone made an implementation in Python?"*
- [225.md](comments/225.md) — @monksy: *"Any work being done on Joplin for this?"*
- [240.md](comments/240.md) — @dolzenko: *"Is there any tool to route all my recorded Codex CLI sessions into something like this?"*
- [232.md](comments/232.md) — @earaizapowerera: Asks how to structure a book for the wiki system (chapters vs. smaller chunks).
- [319.md](comments/319.md) — @jaytxrx: Asks how to feed local inputs to Grok via web without API access.
- [213.md](comments/213.md) — @007bsd: *"Any examples one could refer to?"*
- [227.md](comments/227.md) — @torchy55: *"Can you post how?"*

**What emerged in the thread:** The gist itself answers most of these — Obsidian is just a viewer, the wiki is markdown files + git, any LLM agent works. For command-line alternatives to Obsidian, the thread suggested ekphos ([143.md](comments/143.md)) and noted that Obsidian has its own CLI. For local models, multiple people confirmed success with Gemma 4 ([138.md](comments/138.md), [144.md](comments/144.md)), Ollama ([207.md](comments/207.md)), and sub-20b models via LMStudio ([139.md](comments/139.md)). Python implementations exist in abundance — CRATE ([068.md](comments/068.md)), the Pratiyush llm-wiki, and dozens more in the Implementations section. For routing Codex sessions into a wiki, @jakob1379 ([243.md](comments/243.md) area) suggested a simple bash loop over session transcripts. No Joplin-specific implementation surfaced.

---

## Summary of Open Questions

Some questions from the thread remain genuinely unresolved:

1. **When does the pattern break?** No one reported a clear failure ceiling. The thread suggests ~200+ pages needs proper search, but whether the *compilation* quality degrades at scale (not just retrieval) is untested.

2. **How do you handle cascading invalidation?** If a source changes and 15 wiki pages were derived from it, do you re-derive all 15? Hash-based provenance detects staleness but doesn't prescribe the recompilation strategy.

3. **Can the wiki maintain epistemic humility?** Multiple commenters worried about "false coherence" — the wiki presenting a confident synthesis when the underlying sources actually disagree. Lint helps, but the deeper question is whether an LLM-written wiki can reliably surface its own uncertainty.

4. **What's the right granularity?** New page vs. edit existing, one wiki vs. many, flat vs. hierarchical — these are domain-dependent and the gist intentionally leaves them open. The thread offered competing philosophies but no convergence.

5. **Does this work for teams?** The pattern is designed for personal use. Team-scale adds access control, review gates, and the question of whether multiple LLMs editing the same wiki will maintain consistency. Early implementations exist but are unproven.
