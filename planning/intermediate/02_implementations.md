# Implementations Synthesis

A thematic synthesis of 178 implementations shared in the comments on Karpathy's LLM Wiki gist. Grouped by architectural approach, with commentary on patterns and tradeoffs that emerged.

---

## By the Numbers

Within a week of the gist's publication, 178 comments shared concrete implementations. The breakdown:

- **~50 CLI tools** implementing the full ingest/compile/query/lint cycle
- **~35 agent skills** packaged for Claude Code, OpenClaw, Cursor, or Codex
- **~15 Obsidian plugins or integrations**
- **~10 MCP servers** exposing the wiki as a tool interface
- **~10 web apps** with browser-based UIs
- **~10 frameworks/libraries** focused on a specific layer (provenance, search, multi-agent)
- The rest: mobile apps, browser extensions, conceptual writeups, domain-specific adaptations

The dominant stack: **markdown files + git**, often with an optional Obsidian viewer. The dominant language: **TypeScript/Node.js**, followed by Python, then Go.

---

## 1. The Filesystem Majority

The overwhelming majority of implementations stayed faithful to the gist's core premise: the wiki is a directory of markdown files. No database, no embeddings, no infrastructure beyond the filesystem.

Representative examples:

- [068.md](comments/068.md) — **CRATE** (@GuiminChen): Python CLI with `compile`, `ask`, `lint`, `ingest` commands. Three-layer directory structure (`raw/`, `wiki/`, `schema/`). File-first, Obsidian-compatible.
- [128.md](comments/128.md) — **agent-wiki** (@originlabs-app): Pure markdown, no database, no embeddings. 5 slash commands for the full workflow. Works with any LLM agent.
- [198.md](comments/198.md) — **llm-wiki-vault** (@MirkoSon): Zero dependencies — just git + bash. Provenance tracking on every page, zero-token linting (validation without using LLM tokens).
- [305.md](comments/305.md) — **llmwiki-cli** (@doum1004): Exposes filesystem primitives (read, write, search, index, list, commit) for LLM agents. No orchestration layer — the LLM drives the workflow via shell commands.
- [073.md](comments/073.md) — **llm-wiki** (@hellohejinyu): Node.js CLI with multi-step ReAct agent for retrieval, automatic cross-linking, zero vendor lock-in. Works with any OpenAI-compatible provider including Ollama.

**What this means:** The simplest implementations are surprisingly effective. A well-structured markdown directory with an index file and a disciplined schema is enough for personal-scale knowledge bases (~100 sources, hundreds of pages). The filesystem approach fails not at storage but at retrieval — finding the right page among hundreds without a search engine.

---

## 2. The Scaling Cliff: Databases and Search Engines

Multiple builders reported hitting a wall where the index-file-as-navigation approach stopped working. Their solutions diverged:

**SQLite as the escape hatch:**
- [092.md](comments/092.md) — **ra-h_os** (@bradwmorris): After 6-12 months of filesystem experience, moved to SQLite. Found it "the best abstraction for agents at scale."
- [054.md](comments/054.md) — **Binder** (@mpazik): Flipped the model entirely — structured data in a SQLite transaction log that *renders* as markdown. Edits in any editor flow back into the data layer.
- [264.md](comments/264.md) — **WikiMind** (@manavgup): Python/FastAPI + React. Typed JSON contract (not free-form markdown) makes output stable across LLM providers. Lint becomes a SQL query, not a fuzzy re-read.

**Hybrid search (BM25 + vectors):**
- [178.md](comments/178.md) — **OMEGA** (@singularityjason): Local semantic search over markdown. 95.4% on LongMemEval at 50ms retrieval. Obsidian plugin so the compile/ingest pattern stays the same — OMEGA just replaces the index file as the query gateway.
- [084.md](comments/084.md) — **Palinode** (@Paul-Kyle): Git-versioned markdown with 18 MCP tools. Hybrid BM25 + vector search via SQLite-vec. 227 files, 2,230 indexed chunks in production.
- [061.md](comments/061.md) — **LENS** (@flyersworder): Extracts cross-paper knowledge structures (contradiction matrix, architecture catalog). SQLite + FTS5 + sqlite-vec backend.

**Deterministic (no LLM needed for search):**
- [244.md](comments/244.md) — **TreeSearch** (@shibing624): Structure-aware tree search using heading hierarchy. Zero ML models. 5,000 docs in under 10ms. Pure CPU.
- [219.md](comments/219.md) — **codesight** (@Houseofmvps): No LLM at all — deterministic extraction using TypeScript compiler APIs and regex for 25+ frameworks. Runs in 200ms. Cannot hallucinate.
- [235.md](comments/235.md) — **blink-query** (@arpitnath): DNS-inspired typed records (SUMMARY, META, SOURCE, ALIAS, COLLECTION). 83x faster than grep on 14k files. Agent reads ~242x fewer files.

**The pattern:** Filesystem works up to ~200 pages. Past that, you need either search infrastructure (OMEGA, Palinode) or a database (ra-h_os, WikiMind). The most pragmatic approach: keep markdown as the source of truth but index it in SQLite for retrieval.

---

## 3. Provenance: The Most Interesting Innovation

The thread's deepest architectural innovation was structural provenance — tracking not just what the wiki knows but *which source produced each claim and whether that source has changed*.

- [085.md](comments/085.md) — **Freelance** (@Jwcjwc12): Every proposition records source files and their content hashes at compilation time. Queries validate freshness via hash checks. Stale = mismatch. Query-time compilation fills the gap between what's known and what's new. Git branching works for free — switch branches, different propositions light up as valid.
- [038.md](comments/038.md) — **Veritas Acta** (@tomjwxf): Multi-model verification — routes questions to 4 frontier LLMs, synthesizes into Knowledge Units with agreement/dispute tracking. Cryptographic receipt chain so every unit is verifiable offline.
- [084.md](comments/084.md) — **Palinode** (@Paul-Kyle): Git-versioned markdown with `git blame` on every fact. Deterministic executor validates LLM-proposed operations (KEEP, UPDATE, MERGE, SUPERSEDE, ARCHIVE) as JSON before committing.
- [089.md](comments/089.md) — **Anamnesis** (@gayawellness): Separate provenance layer running alongside the wiki. "The wiki is the codebase, Anamnesis is the git log." Tracks how knowledge was compiled, why decisions were made, what superseded what.
- [123.md](comments/123.md) — **paper-spec** (@viberesearch): Git-native research provenance. SHA-256 hashing on every source at ingest. Every idea gets a commit — creating timestamped proofs of discovery, priority, and derivation.

**Why this matters:** Without provenance, the wiki can silently go stale. A source changes, and 15 wiki pages derived from it are now wrong but don't know it. Hash-based provenance makes staleness detectable. Cryptographic receipts make it auditable. This is the clearest architectural gap in the original gist.

---

## 4. Agent Skills: The Fastest Adoption Path

The simplest way to adopt the pattern: install a pre-packaged skill into your existing agent.

- [043.md](comments/043.md) — **wiki-skills** (@kfchou): Claude Code skill files implementing the pattern.
- [045.md](comments/045.md) — **karpathy-kb** (@pedronauck): Another Claude Code skill.
- [080.md](comments/080.md) — **karpathy-llm-wiki** (@john-ver): One-command install via `npx clawhub@latest install`.
- [315.md](comments/315.md) — **claude-obsidian** (@AgriciDaniel): Hot cache (~500 tokens for session continuity), `[!contradiction]` callouts instead of silent overwrites, 8-category lint, `/autoresearch` for autonomous exploration.
- [345.md](comments/345.md) — **memory-toolkit** (@IlyaGorsky): Addresses Claude Code's auto-memory compaction problem. PreCompact hook saves state before compaction. Haiku watcher extracts decisions every 3 minutes. Nothing writes without human approval.
- [342.md](comments/342.md) — **llm-project-wiki** (@akash-r34): Applies the pattern to software codebases. Diff-based ingest via `git diff` — only refreshes pages affected by actual changes. Rewrites CLAUDE.md so Claude checks the wiki before opening source files.

**The tradeoff:** Skills are easy to install but limited in scope. They work within the constraints of their host agent (context window, tool access, session persistence). The more ambitious implementations needed to break out of the skill model into standalone CLI tools or MCP servers.

---

## 5. Knowledge Graphs: Beyond Flat Files

Several implementations added explicit graph structures on top of or instead of flat markdown:

- [099.md](comments/099.md) — **thinking-mcp** (@H179922): Models cognition, not just knowledge. 8,000+ nodes with typed edges (supports, contradicts, evolved_into, depends_on). Temporal decay model — values hold, ideas fade fast.
- [212.md](comments/212.md) — **SwarmVault** (@waydelyle): The most aggressively iterated project in the thread (4 major updates: [212.md](comments/212.md), [257.md](comments/257.md), [284.md](comments/284.md), [327.md](comments/327.md)). TypeScript CLI with knowledge graph, community detection, god-node analysis, contradiction edges, 50+ format ingest, YouTube transcript pulling, hybrid search.
- [333.md](comments/333.md) — **Cortex** (@abbacusgroup): Formal OWL-RL ontology with SPARQL graph store. Deterministic reasoning — no LLM calls for inference. Transitive chain tracing (A supersedes B supersedes C → A supersedes C).
- [301.md](comments/301.md) — **LLM Wikidata** (@QipengGuo): ChromaDB-based entity linking to prevent duplicate nodes at scale.
- [262.md](comments/262.md) — **celestix-ifr** (@emil-celestix): Embedding graph where the query vector *mutates at each hop* (induced-fit retrieval). On HotpotQA with 5.2M articles: all traditional RAG scored 0% Hit@20 on multi-hop questions; this found targets.
- [259.md](comments/259.md) — **grover** (@ClayGendron): Cross-references stored as persistent graph edges in `/.connections`, not inline text. Graph traversal (pagerank, neighborhood) for discovery.

**The pattern:** Flat markdown with wikilinks is a graph — just an implicit one. These implementations make the graph explicit, which enables operations markdown alone can't support: community detection, contradiction propagation, causal tracing, and multi-hop retrieval.

---

## 6. Multi-Agent Coordination

The wiki pattern assumes a single agent. Several implementations tackled what happens when multiple agents share a wiki:

- [021.md](comments/021.md) — **tracecraft** (@Arrmlet): Coordination layer for multiple LLM agents building a wiki in parallel. Shared memory and task claiming through S3 or HuggingFace buckets.
- [359.md](comments/359.md) — **multi-agent-wiki-toolkit** (@redmizt): 13 extensions for production multi-agent use (6 parallel agents, 50+ sub-agents per session). Capability tokens for identity, three-layer content protection, wiki locking with TTL-based mutual exclusion, contamination firewalls.
- [353.md](comments/353.md) — **agentic-coop-db** (@fheinfling): PostgreSQL gateway enabling multiple agents to share a wiki in a distributed manner.
- [194.md](comments/194.md) — **DPC Messenger** (@mikhashev): Multi-agent knowledge negotiation with consensus voting (75% threshold, Devil's Advocate required). RSA-PSS signed knowledge commits on a tamper-proof DAG.
- [332.md](comments/332.md) — **Automaton Memory System** (@plundrpunk): Multi-agent conflict resolution with relationship-typed links and trust tiers. Consolidation engine that scores, merges, and prunes rather than just appending.
- [125.md](comments/125.md) — **MindOS** (@GeminiLight): 19 agents connected to the same wiki simultaneously — no MCP lock-in. Agent corrections auto-distill into persistent wiki rules.

**The hard problem:** File-level locking is insufficient when agents operate on overlapping concepts. The solutions range from simple (TTL locks) to elaborate (consensus voting, trust tiers, contamination firewalls). No clear winner yet.

---

## 7. Research-Focused Platforms

The wiki pattern is a natural fit for academic research, and several implementations built full research lifecycle tools:

- [285.md](comments/285.md) / [339.md](comments/339.md) — **OmegaWiki** (@skyllwt): The most ambitious. 20 Claude Code skills covering: ingest papers → detect gaps → generate ideas → design experiments → run experiments → write papers → respond to reviewers. Failed experiments stored as anti-repetition memory. 8 entity types, 9 relationship types.
- [061.md](comments/061.md) — **LENS** (@flyersworder): Cross-paper knowledge structures (contradiction matrix, architecture catalog, agentic pattern catalog) rather than per-paper summaries. Canonical vocabulary with guided extraction.
- [123.md](comments/123.md) — **paper-spec** (@viberesearch): Adapts the wiki for research repos with provenance tracking. SHA-256 hashing creates timestamped proofs of discovery.
- [247.md](comments/247.md) — **ScholarAIO** (@ZimoLiao): Wiki as operational substrate — knowledge translated into executable workflows, scripts, and tool interactions. Self-improving research environment.
- [095.md](comments/095.md) — **ELF** (@ProjectEli): Base-delta protocol for incremental experiments. Minimizes researcher documentation fatigue.

---

## 8. Voice, Mobile, and Ambient Capture

Not everyone wants to sit at a desk dropping files into a folder:

- [044.md](comments/044.md) — **Voice-first PKM** (@peas): Record voice memos into Telegram while walking. Whisper transcribes, LLM classifies and routes, synthesizer updates wiki nodes. Strict "no content invention" constraint — LLM is editor only, gaps get `[TODO:]` markers.
- [075.md](comments/075.md) — **Memex** (@sparkleMing): Mobile-first. Daily recordings auto-organized into a P.A.R.A. wiki. Visual cards and pattern discovery.
- [145.md](comments/145.md) — **WALI** (@liamsysmind): Local Mac Mini daemon accepting text, files, and audio from phone or browser. Local ASR, local storage, local search. Claude handles reasoning only.
- [205.md](comments/205.md) — **remember-md** (@codezz): Sources are past AI chat sessions, not articles. Extracts people, decisions, projects, tasks from conversations into a git-synced Obsidian vault.
- [347.md](comments/347.md) — **AIContext** (@AIContextMe): Captures ambient context (browser history, coding sessions, conversations) rather than deliberately curated knowledge. Agent discovers patterns the user never noticed.

---

## 9. Local / Offline Implementations

Multiple implementations validated that the pattern works without cloud LLMs:

- [207.md](comments/207.md) / [340.md](comments/340.md) / [343.md](comments/343.md) — **obsidian-llm-wiki-local** (@kytmanov): Fully offline with Ollama. No cloud dependency.
- [122.md](comments/122.md) — **mel** (@polonski): Gemini 3.1 Pro via Gemini Code Assist. Proves the pattern is model-agnostic.
- [219.md](comments/219.md) — **codesight** (@Houseofmvps): No LLM at all — deterministic extraction via compiler APIs. 200ms, zero API cost.
- [244.md](comments/244.md) — **TreeSearch** (@shibing624): Pure CPU, zero embeddings, millisecond latency.

---

## 10. Domain-Specific Adaptations

The pattern's flexibility showed in its domain-specific applications:

- [051.md](comments/051.md) — **Vibe Sensei** (@VictorVVedtion): AI trading terminal with 52 historical "master guardians" (Soros, Livermore, Buffett) that watch trades and warn in character. Counterfactual tracking measures whether heeded/ignored alerts led to good outcomes.
- [074.md](comments/074.md) — **Centel** (@christianhpoe): Wiki pattern for product managers. Sales, new hires, and customers query product capabilities.
- [064.md](comments/064.md) — **peeps-skill** (@ilyabelikin): People and organizations intelligence.
- [204.md](comments/204.md) — **llm-research-wiki** (@MetamusicX): Academic research in music and philosophy with domain-specific page types (concepts, authors, debates, syntheses). First ingest: 38 interlinked pages from a single source.
- [170.md](comments/170.md) — **llm-fandom** (@vykhand): Auto-extracts entities (characters, locations, organizations) into Fandom-style static wiki sites. Multi-format, multi-provider.
- [342.md](comments/342.md) — **llm-project-wiki** (@akash-r34): Software codebases. Diff-based ingest via `git diff`. Wiki-first development where Claude checks the wiki before opening source files.
- [195.md](comments/195.md) — **llm-wiki for PM** (@junbjnnn): Software project management. Ingests PRDs, meeting notes, API specs, postmortems. Compiles into ADRs, runbooks, entity pages.

---

## Architectural Themes

Looking across all 178 implementations, several tensions emerged:

**Markdown vs. databases.** The gist says markdown. Most implementations agree. But everyone who scaled past ~200 pages either added a search layer on top (OMEGA, blink-query) or moved to a database (ra-h_os, WikiMind). The pragmatic synthesis: markdown as source of truth, SQLite as index.

**Compile-time vs. query-time.** The gist emphasizes compile-time knowledge building. Freelance ([085.md](comments/085.md)) introduced query-time compilation — building knowledge on demand and caching it. This solves the staleness problem (you never serve pre-compiled knowledge without checking freshness) but trades latency.

**Single agent vs. multi-agent.** The pattern works cleanly with one agent. Multi-agent introduces coordination problems (locking, conflict resolution, trust) that the filesystem model doesn't naturally support. The solutions range from "just use git" to elaborate consensus protocols.

**Human in the loop vs. autonomous.** The gist emphasizes human involvement ("I prefer to ingest sources one at a time and stay involved"). Many implementations pushed toward full autonomy — autopilot modes, cron-based maintenance, autonomous research loops. The tension: autonomous systems compound errors as well as knowledge.

**Provenance vs. simplicity.** Hash-based provenance tracking is the thread's most compelling innovation, but it adds complexity. Most implementations didn't include it. The ones that did (Freelance, Palinode, paper-spec) reported significantly better trust and debuggability.
