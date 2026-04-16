# LLM Knowledge Bases (DAIR.AI Academy)

**Source:** https://academy.dair.ai/blog/llm-knowledge-bases-karpathy

## Overview

Discusses Andrej Karpathy's innovative approach to building personal knowledge bases powered by LLMs, emphasizing a practical system that avoids traditional RAG pipelines and vector databases.

## Core Architecture — Four Continuous Phases

### Phase 1: Ingest

Raw data enters from multiple sources including web articles (via Obsidian Web Clipper), academic papers from arXiv, GitHub repositories, and datasets. All materials initially land in a `raw/` staging directory.

### Phase 2: Compile

The LLM reads from the raw directory and constructs a structured wiki featuring:
- Index files summarizing all documents as query entry points
- Approximately 100 concept articles (~400K words total) organized topically with cross-references
- Derived outputs including Marp presentations, matplotlib visualizations, and documented query responses
- Automatically maintained link graphs identifying connections between concepts

### Phase 3: Query and Enhance

Users interact with the knowledge base through Obsidian IDE for browsing, a Q&A agent for complex research questions, and a basic search engine accessible via web UI or CLI. Critically, all query outputs feed back into the wiki.

### Phase 4: Lint and Maintain

The LLM performs health checks, identifies inconsistencies, discovers missing information through web search, and suggests new article opportunities.

## Key Advantages

"At personal knowledge base scale (~100 articles), the index files + LLM context window are sufficient for retrieval" without vector databases. Additional benefits include cumulative query exploration and minimal manual wiki editing.

## Implementation Tools

Required components remain straightforward: Obsidian as IDE, Obsidian Web Clipper for ingestion, context-capable LLMs, and markdown directory structures.

## Author's Adaptation

Elvis Saravia describes a personalized variant using automated paper curation and the qmd CLI tool for semantic indexing, creating an interactive research visualization system for agent-powered discovery.
