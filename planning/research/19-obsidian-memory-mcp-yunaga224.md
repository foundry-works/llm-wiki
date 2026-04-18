# obsidian-memory-mcp (YuNaga224)

**Source:** https://github.com/YuNaga224/obsidian-memory-mcp
**Stars:** 23 | **Languages:** TypeScript 69.1%, JavaScript 30.9% | **License:** MIT

## Description

MCP server that persists AI memories as individual Markdown files, enabling visualization through Obsidian's graph view. Transforms Anthropic's original JSON-based memory system into Obsidian-compatible format.

## Core Features

- Markdown storage: each entity saved as separate .md file
- Obsidian graph integration using `[[link]]` syntax
- Knowledge management: entities, observations, relationships
- Search across stored memories
- YAML frontmatter metadata

## Available Tools

- create_entities, create_relations, add_observations
- delete_entities, delete_observations, delete_relations
- read_graph, search_nodes, open_nodes

## Architecture

TypeScript/Node.js. Claude Desktop integration via JSON config. Generates markdown files with YAML frontmatter and Obsidian-compatible links.

## What Makes It Unique

Individual markdown files (vs centralized JSON) suited for Obsidian's graph visualization. Each memory becomes a visible node in the knowledge graph.
