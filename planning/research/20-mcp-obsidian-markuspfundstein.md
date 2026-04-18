# mcp-obsidian (MarkusPfundstein)

**Source:** https://github.com/MarkusPfundstein/mcp-obsidian
**Stars:** 3.4k | **Forks:** 392 | **Language:** Python | **License:** MIT

## Description

MCP server enabling Claude to interact with Obsidian via the Local REST API community plugin. Strong community adoption for AI-powered note management.

## Available Tools

- Vault file enumeration and directory browsing
- Individual file content retrieval
- Full-vault text search
- Content insertion relative to headings or block references
- File appending and deletion operations

## Architecture

Python MCP server using stdio communication. REST API client for Obsidian. Environment-based config (API key, host, port). Default: port 27124, host 127.0.0.1.

## How It Works

1. User obtains API key from Obsidian REST API plugin
2. Settings via environment variables or .env files
3. Claude sends tool calls over MCP; server translates to REST API requests

## What Makes It Unique

- Most popular MCP-Obsidian integration (3.4k stars)
- MCP Inspector debugging support
- Flexible deployment (local dev or published uvx)
- Natural language interface for vault operations
