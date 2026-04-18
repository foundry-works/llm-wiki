# Schemas and Specifications

## AGENTS.md (OpenAI)

**Source:** https://github.com/openai/openai-agents-python/blob/main/AGENTS.md

OpenAI's specification for agent configuration files. Defines how AI agents read project context, directory layouts, and behavioral instructions. Used by Codex and compatible agents as the standard project-level instruction file.

## CLAUDE.md (Anthropic)

**Source:** https://docs.anthropic.com/en/docs/claude-code/memory

Anthropic's specification for Claude Code project memory. Defines how Claude reads project context, remembers conventions, and maintains behavioral consistency across sessions. The schema file that most LLM Wiki implementations use to define wiki structure, conventions, and workflows.

## MEMORY.md (claude-obsidian)

**Source:** https://github.com/AgriciDaniel/claude-obsidian

Memory specification used by the claude-obsidian project for persisting session context. Enables hot cache system that maintains recent context between Claude Code sessions.

## Key Insight

These schema files (CLAUDE.md, AGENTS.md, MEMORY.md) are the "rules layer" that makes the LLM Wiki pattern work. They tell the LLM how to structure the wiki, what operations to perform, and what conventions to follow. Multiple implementations in the ecosystem describe the schema as "more valuable than the wiki itself" — a transferable blueprint for knowledge work.
