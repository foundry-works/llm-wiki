# Semantic Graphs: LLM Wiki at Enterprise Scale (Epsilla)

**Source:** https://www.epsilla.com/blogs/llm-wiki-kills-rag-karpathy-enterprise-semantic-graph

## Core Argument

While Karpathy's LLM Wiki conceptual approach is revolutionary, local Markdown files managed through Obsidian are unsuitable for enterprise environments. Semantic graphs are the enterprise-grade evolution.

## Karpathy's Three-Phase Model

1. **Ingestion**: Raw materials deposited without preprocessing
2. **Compilation**: LLMs synthesize into structured entries with backlinks
3. **Active Maintenance**: AI agents identify inconsistencies, discover missing info, suggest connections

## Critical Enterprise Weaknesses of Local Files

- **Access Control**: File systems can't implement granular RBAC
- **Auditability**: Git lacks compliance-grade audit trails
- **Scalability**: Millions of documents create prohibitive I/O constraints
- **Security**: Text files enable trivial IP theft

## Epsilla's Semantic Graph Solution

- **Structured Nodes**: Concept representations with summaries and metadata (vs opaque vectors)
- **Labeled Relationships**: Explicit connections ("CITES," "AUTHORED") preserving context
- **Enterprise Governance**: RBAC with immutable audit logging (ClawTrace)
- **Agentic Services**: Production compilation via AgentStudio, real-time organizational ingestion

## Looking Forward

By 2026, MCP standardizes how agents interact with structured knowledge. Agents will traverse rich semantic graphs for multi-step insights while maintaining auditability and access governance — representing the true enterprise evolution of the wiki pattern.
