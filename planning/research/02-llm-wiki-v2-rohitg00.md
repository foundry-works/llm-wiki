# LLM Wiki v2 — Extending Karpathy's Pattern with AgentMemory Lessons

**Source:** https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2

## Core Foundation

Extends Andrej Karpathy's original LLM Wiki concept with production lessons from building agentmemory. The fundamental insight remains: "stop re-deriving, start compiling" through systematic knowledge accumulation rather than ephemeral RAG retrieval.

## Key Extensions Beyond Original

### Memory Lifecycle Management

The original treated all wiki content as permanently equal. Version 2 introduces:

**Confidence Scoring**: Facts carry metadata indicating source count, recency, and contradiction status. A claim like "Project X uses Redis" tracks how many sources confirm it, when last verified, and its confidence level (e.g., 0.85).

**Supersession**: New information explicitly replaces outdated claims with preserved version history, creating "version control for knowledge."

**Retention Curves**: Following Ebbinghaus principles, facts decay without reinforcement but reset upon confirmation. Architecture decisions decay slowly; transient bugs decay faster.

**Consolidation Tiers**:
- Working memory (recent observations)
- Episodic memory (session summaries)
- Semantic memory (cross-session facts)
- Procedural memory (workflows and patterns)

### Knowledge Graph Architecture

Beyond flat markdown pages, the system uses:

**Entity Extraction**: Types include people, projects, libraries, concepts, files, and decisions with attributes and relationships.

**Typed Relationships**: "Uses," "depends on," "contradicts," "caused," "fixed," "supersedes" carry semantic weight beyond generic links.

**Graph Traversal**: Queries like "upgrade impact analysis" walk outward through relevant edges rather than keyword matching alone.

## Scaling Solutions

### Hybrid Search Strategy

Three complementary retrieval streams:
- **BM25**: Keyword matching with stemming and synonym expansion
- **Vector Search**: Semantic similarity via embeddings
- **Graph Traversal**: Entity-aware relationship walking

Results fuse using reciprocal rank fusion. The single-file index breaks around 200-500 documents; hybrid search scales beyond.

### Quality and Self-Correction

- Automated scoring of all LLM-generated content
- Self-healing lint operations (fixing orphan pages, broken references)
- Automatic contradiction resolution with timestamp-based authority ranking
- Human override capability for all corrections

## Operations and Automation

Event-driven hooks replace manual workflows:
- Auto-ingest on new sources
- Context injection at session start
- Compression and filing at session end
- Contradiction detection on memory writes
- Scheduled lint and consolidation

## Multi-Agent and Collaboration

**Mesh Sync**: Last-write-wins with timestamp resolution and manual override for conflicts.

**Scoping**: Distinguishes personal knowledge from shared team knowledge, with promotion pathways.

**Coordination**: Lightweight tracking of who works on what to prevent duplicate effort.

## Privacy and Governance

- Automatic sensitive data filtering during ingestion
- Complete audit trails for all operations
- Reversible bulk operations on mature content
- Governance controls for merging and deletion

## The Schema as Core Product

The schema document (encoding entity types, relationships, ingestion rules, quality standards, contradiction handling, and consolidation schedules) is described as more valuable than the wiki itself, functioning as a transferable blueprint for knowledge work in similar domains.

## Implementation Spectrum

The pattern scales from minimal viable (raw sources + wiki pages + index + schema) through lifecycle management, graph structure, automation, scaling infrastructure, and multi-agent collaboration—each layer optional based on needs.
