# Claudian (YishenTu)

**Source:** https://github.com/YishenTu/Claudian
**Languages:** TypeScript 97.3%, CSS 2.4%, JavaScript 0.3%

## Description

Obsidian plugin that integrates AI coding agents — primarily Claude Code — directly into the note-taking vault. Transforms vault into a shared workspace where AI agents can read, write, edit, and search files autonomously.

## Core Features

**Chat & Collaboration:**
- Sidebar chat interface with multi-tab and conversation history
- "Inline Edit" mode with word-level diff previews
- Plan Mode (Shift+Tab) for exploration before implementation

**Prompt & Command System:**
- Slash commands (/) and Skills ($) for reusable templates
- @mention for vault files, subagents, MCP servers, external directories
- Instruction Mode (#) for custom instructions

**External Integrations:**
- MCP server support (stdio, SSE, HTTP)
- Provider flexibility: Claude Code CLI, Codex, Openrouter, Kimi

## Architecture

- **core/**: Provider-neutral runtime with ChatRuntime interface
- **providers/**: Claude SDK adaptor and Codex JSON-RPC transport
- **features/**: Chat sidebar, inline editing, settings UI
- **shared/**: Reusable UI components
- **i18n/**: 10 locale support

## What Makes It Unique

- Not a wiki builder per se, but an Obsidian-native AI agent interface
- Keeps entire vault as the agent's working context
- No telemetry
- MCP server integration and approval workflows
- Supports multiple AI providers
- Desktop platforms only (macOS, Linux, Windows)

## Requirements

- Claude Code CLI or compatible provider
- Obsidian v1.4.5+
