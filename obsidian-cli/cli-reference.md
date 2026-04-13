# Obsidian CLI Reference

> Source: https://obsidian.md/cli and https://obsidian.md/help/cli

## Overview

"Anything you can do in Obsidian you can do from the command line." The Obsidian CLI enables programmatic interaction with your vault through terminal commands for automation, scripting, and external tool integration.

Obsidian CLI requires the Obsidian app to be running. If Obsidian is not running, the first command you run launches Obsidian. Looking to sync without the desktop app? See [Headless Sync](headless-sync.md).

## Installation

### Requirements

- Obsidian 1.12.7+ installer

### Steps

1. Go to **Settings** -> **General**.
2. Enable **Command line interface**.
3. Follow the prompt to register Obsidian CLI.

### Platform-specific details

- **macOS**: Creates a symlink at `/usr/local/bin/obsidian` (requires admin privileges)
- **Windows**: Installs `Obsidian.com` terminal redirector alongside `Obsidian.exe`
- **Linux**: Copies binary to `~/.local/bin/obsidian` (ensure this directory is in PATH)

## Getting Started

Obsidian CLI supports both single commands and a terminal user interface (TUI) with interactive help and autocomplete.

### Run a command

Run an individual command without opening the TUI:

```shell
# Run the help command
obsidian help
```

### Use the terminal interface

Use the TUI by entering `obsidian`. Subsequent commands can be entered without `obsidian`.

```shell
# Open the TUI, then run help
obsidian
help
```

The TUI supports autocomplete, command history, and reverse search. Use `Ctrl+R` to search your command history.

## Parameters and Flags

**Parameters** take values in the format `parameter=value`. If the value has spaces, wrap it in quotes:

```shell
obsidian search query="meeting notes"
```

For multiline content, use `\n` for newlines and `\t` for tabs in parameter values.

**Flags** are boolean switches with no value. Include them to turn them on:

```shell
obsidian tasks todo
```

### Vault Targeting

When your terminal's current directory is a vault folder, that vault is used automatically. Otherwise, the active vault applies. To specify a different vault explicitly, use `vault=<name>` or `vault=<id>` as the first parameter before your command:

```shell
obsidian vault=Notes daily
obsidian vault="My Vault" search query="test"
```

In the TUI, switch vaults with `vault:open <name>`.

### File Targeting

Many commands accept parameters to specify target files. If neither is provided, the command targets the active file:

- `file=<name>` - resolves files using wikilink logic, matching by name without requiring full paths or extensions
- `path=<path>` - requires exact paths from the vault root (e.g., `folder/note.md`)

These approaches are interchangeable when file names are unique.

### Output Copying

Add `--copy` to any command to copy the output to the clipboard:

```shell
read --copy
search query="TODO" --copy
```

---

## Command Reference

### General

#### `help`

Display available commands or help for a specific command.

**Parameters:**
- `<command>` - show help for a specific command

#### `version`

Show Obsidian version.

#### `reload`

Reload the app window.

#### `restart`

Restart the app.

---

### Bases

#### `bases`

List all `.base` files in the vault.

#### `base:views`

List views in the current base file.

#### `base:create`

Create a new item in a base. Defaults to the active base view if no file is specified.

**Parameters:**
- `file=<name>` - base file name
- `path=<path>` - base file path
- `view=<name>` - view name
- `name=<name>` - new file name
- `content=<text>` - initial content

**Flags:**
- `open` - open file after creating
- `newtab` - open in new tab

#### `base:query`

Query a base and return results.

**Parameters:**
- `file=<name>` - base file name
- `path=<path>` - base file path
- `view=<name>` - view name to query
- `format=json|csv|tsv|md|paths` - output format (default: json)

---

### Bookmarks

#### `bookmarks`

List bookmarks.

**Parameters:**
- `format=json|tsv|csv` - output format (default: tsv)

**Flags:**
- `total` - return bookmark count
- `verbose` - include bookmark types

#### `bookmark`

Add a bookmark.

**Parameters:**
- `file=<path>` - file to bookmark
- `subpath=<subpath>` - subpath (heading or block) within file
- `folder=<path>` - folder to bookmark
- `search=<query>` - search query to bookmark
- `url=<url>` - URL to bookmark
- `title=<title>` - bookmark title

---

### Command Palette

#### `commands`

List available command IDs.

**Parameters:**
- `filter=<prefix>` - filter by ID prefix

#### `command`

Execute an Obsidian command.

**Parameters:**
- `id=<command-id>` - (required) command ID to execute

#### `hotkeys`

List hotkeys for all commands.

**Parameters:**
- `format=json|tsv|csv` - output format (default: tsv)

**Flags:**
- `total` - return hotkey count
- `verbose` - show if hotkey is custom

#### `hotkey`

Get hotkey for a command.

**Parameters:**
- `id=<command-id>` - (required) command ID

**Flags:**
- `verbose` - show if custom or default

---

### Daily Notes

#### `daily`

Open daily note.

**Parameters:**
- `paneType=tab|split|window` - pane type to open in

#### `daily:path`

Get daily note path. Returns the expected path even if the file hasn't been created yet.

#### `daily:read`

Read daily note contents.

#### `daily:append`

Append content to daily note.

**Parameters:**
- `content=<text>` - (required) content to append
- `paneType=tab|split|window` - pane type to open in

**Flags:**
- `inline` - append without newline
- `open` - open file after adding

**Example:**
```shell
obsidian daily:append content="- [ ] Buy groceries"
```

#### `daily:prepend`

Prepend content to daily note.

**Parameters:**
- `content=<text>` - (required) content to prepend
- `paneType=tab|split|window` - pane type to open in

**Flags:**
- `inline` - prepend without newline
- `open` - open file after adding

---

### File History

#### `diff`

List or compare versions from local file recovery and Sync. Versions are numbered from newest to oldest.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `from=<n>` - version number to diff from
- `to=<n>` - version number to diff to
- `filter=local|sync` - filter by version source

**Examples:**
```shell
# List all versions of the active file
diff

# List all versions of a specific file
diff file=Recipe

# Compare the latest version to the current file
diff file=Recipe from=1

# Compare two versions
diff file=Recipe from=2 to=1

# Only show Sync versions
diff filter=sync
```

#### `history`

List versions from file recovery only.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

#### `history:list`

List all files with local history.

#### `history:read`

Read a local history version.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `version=<n>` - version number (default: 1)

#### `history:restore`

Restore a local history version.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `version=<n>` - (required) version number

#### `history:open`

Open file recovery.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

---

### Files and Folders

#### `file`

Show file info (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Example output:**
```
path       Notes/Recipe.md
name       Recipe
extension  md
size       1024
created    1700000000000
modified   1700001000000
```

#### `files`

List files in the vault.

**Parameters:**
- `folder=<path>` - filter by folder
- `ext=<extension>` - filter by extension

**Flags:**
- `total` - return file count

#### `folder`

Show folder info.

**Parameters:**
- `path=<path>` - (required) folder path
- `info=files|folders|size` - return specific info only

#### `folders`

List folders in the vault.

**Parameters:**
- `folder=<path>` - filter by parent folder

**Flags:**
- `total` - return folder count

#### `open`

Open a file.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Flags:**
- `newtab` - open in new tab

#### `create`

Create or overwrite a file.

**Parameters:**
- `name=<name>` - file name
- `path=<path>` - file path
- `content=<text>` - initial content
- `template=<name>` - template to use

**Flags:**
- `overwrite` - overwrite if file exists
- `open` - open file after creating
- `newtab` - open in new tab

**Example:**
```shell
obsidian create name="Trip to Paris" template=Travel
```

#### `read`

Read file contents (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

#### `append`

Append content to a file (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `content=<text>` - (required) content to append

**Flags:**
- `inline` - append without newline

#### `prepend`

Prepend content after frontmatter (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `content=<text>` - (required) content to prepend

**Flags:**
- `inline` - prepend without newline

#### `move`

Move or rename a file (default: active file). Automatically updates internal links if enabled in vault settings.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `to=<path>` - (required) destination folder or path

#### `rename`

Rename a file (default: active file). File extension is preserved automatically if omitted. Automatically updates internal links if enabled in vault settings.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `name=<name>` - (required) new file name

#### `delete`

Delete a file (default: active file, trash by default).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Flags:**
- `permanent` - skip trash, delete permanently

---

### Links

#### `backlinks`

List backlinks to a file (default: active file).

**Parameters:**
- `file=<name>` - target file name
- `path=<path>` - target file path
- `format=json|tsv|csv` - output format (default: tsv)

**Flags:**
- `counts` - include link counts
- `total` - return backlink count

#### `links`

List outgoing links from a file (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Flags:**
- `total` - return link count

#### `unresolved`

List unresolved links in vault.

**Parameters:**
- `format=json|tsv|csv` - output format (default: tsv)

**Flags:**
- `total` - return unresolved link count
- `counts` - include link counts
- `verbose` - include source files

#### `orphans`

List files with no incoming links.

**Flags:**
- `total` - return orphan count

#### `deadends`

List files with no outgoing links.

**Flags:**
- `total` - return dead-end count

---

### Outline

#### `outline`

Show headings for the current file.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `format=tree|md|json` - output format (default: tree)

**Flags:**
- `total` - return heading count

---

### Plugins

#### `plugins`

List installed plugins.

**Parameters:**
- `filter=core|community` - filter by plugin type
- `format=json|tsv|csv` - output format (default: tsv)

**Flags:**
- `versions` - include version numbers

#### `plugins:enabled`

List enabled plugins.

**Parameters:**
- `filter=core|community` - filter by plugin type
- `format=json|tsv|csv` - output format (default: tsv)

**Flags:**
- `versions` - include version numbers

#### `plugins:restrict`

Toggle or check restricted mode.

**Flags:**
- `on` - enable restricted mode
- `off` - disable restricted mode

#### `plugin`

Get plugin info.

**Parameters:**
- `id=<plugin-id>` - (required) plugin ID

#### `plugin:enable`

Enable a plugin.

**Parameters:**
- `id=<id>` - (required) plugin ID
- `filter=core|community` - plugin type

#### `plugin:disable`

Disable a plugin.

**Parameters:**
- `id=<id>` - (required) plugin ID
- `filter=core|community` - plugin type

#### `plugin:install`

Install a community plugin.

**Parameters:**
- `id=<id>` - (required) plugin ID

**Flags:**
- `enable` - enable after install

#### `plugin:uninstall`

Uninstall a community plugin.

**Parameters:**
- `id=<id>` - (required) plugin ID

#### `plugin:reload`

Reload a plugin (for developers).

**Parameters:**
- `id=<id>` - (required) plugin ID

**Example:**
```shell
obsidian plugin:reload id=my-plugin
```

---

### Properties

#### `aliases`

List aliases in the vault. Use `active` or `file`/`path` to show aliases for a specific file.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Flags:**
- `total` - return alias count
- `verbose` - include file paths
- `active` - show aliases for active file

#### `properties`

List properties in the vault. Use `active` or `file`/`path` to show properties for a specific file.

**Parameters:**
- `file=<name>` - show properties for file
- `path=<path>` - show properties for path
- `name=<name>` - get specific property count
- `sort=count` - sort by count (default: name)
- `format=yaml|json|tsv` - output format (default: yaml)

**Flags:**
- `total` - return property count
- `counts` - include occurrence counts
- `active` - show properties for active file

#### `property:set`

Set a property on a file (default: active file).

**Parameters:**
- `name=<name>` - (required) property name
- `value=<value>` - (required) property value
- `type=text|list|number|checkbox|date|datetime` - property type
- `file=<name>` - file name
- `path=<path>` - file path

#### `property:remove`

Remove a property from a file (default: active file).

**Parameters:**
- `name=<name>` - (required) property name
- `file=<name>` - file name
- `path=<path>` - file path

#### `property:read`

Read a property value from a file (default: active file).

**Parameters:**
- `name=<name>` - (required) property name
- `file=<name>` - file name
- `path=<path>` - file path

---

### Publish

#### `publish:site`

Show publish site info (slug, URL).

#### `publish:list`

List published files.

**Flags:**
- `total` - return published file count

#### `publish:status`

List publish changes.

**Flags:**
- `total` - return change count
- `new` - show new files only
- `changed` - show changed files only
- `deleted` - show deleted files only

#### `publish:add`

Publish a file or all changed files (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Flags:**
- `changed` - publish all changed files

#### `publish:remove`

Unpublish a file (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

#### `publish:open`

Open file on published site (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

---

### Random Notes

#### `random`

Open a random note.

**Parameters:**
- `folder=<path>` - limit to folder

**Flags:**
- `newtab` - open in new tab

#### `random:read`

Read a random note (includes path).

**Parameters:**
- `folder=<path>` - limit to folder

---

### Search

#### `search`

Search vault for text. Returns matching file paths.

**Parameters:**
- `query=<text>` - (required) search query
- `path=<folder>` - limit to folder
- `limit=<n>` - max files
- `format=text|json` - output format (default: text)

**Flags:**
- `total` - return match count
- `case` - case sensitive

**Example:**
```shell
obsidian search query="meeting notes"
```

#### `search:context`

Search with matching line context. Returns grep-style `path:line: text` output.

**Parameters:**
- `query=<text>` - (required) search query
- `path=<folder>` - limit to folder
- `limit=<n>` - max files
- `format=text|json` - output format (default: text)

**Flags:**
- `case` - case sensitive

#### `search:open`

Open search view.

**Parameters:**
- `query=<text>` - initial search query

---

### Sync

#### `sync`

Pause or resume sync.

**Flags:**
- `on` - resume sync
- `off` - pause sync

#### `sync:status`

Show sync status and usage.

#### `sync:history`

List sync version history for a file (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Flags:**
- `total` - return version count

#### `sync:read`

Read a sync version (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `version=<n>` - (required) version number

#### `sync:restore`

Restore a sync version (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `version=<n>` - (required) version number

#### `sync:open`

Open sync history (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

#### `sync:deleted`

List deleted files in sync.

**Flags:**
- `total` - return deleted file count

---

### Tags

#### `tags`

List tags in the vault. Use `active` or `file`/`path` to show tags for a specific file.

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path
- `sort=count` - sort by count (default: name)
- `format=json|tsv|csv` - output format (default: tsv)

**Flags:**
- `total` - return tag count
- `counts` - include tag counts
- `active` - show tags for active file

**Example:**
```shell
obsidian tags counts
```

#### `tag`

Get tag info.

**Parameters:**
- `name=<tag>` - (required) tag name

**Flags:**
- `total` - return occurrence count
- `verbose` - include file list and count

---

### Tasks

#### `tasks`

List tasks in the vault. Use `active` or `file`/`path` to show tasks for a specific file.

**Parameters:**
- `file=<name>` - filter by file name
- `path=<path>` - filter by file path
- `status="<char>"` - filter by status character
- `format=json|tsv|csv` - output format (default: text)

**Flags:**
- `total` - return task count
- `done` - show completed tasks
- `todo` - show incomplete tasks
- `verbose` - group by file with line numbers
- `active` - show tasks for active file
- `daily` - show tasks from daily note

**Examples:**
```shell
# List all tasks in the vault
tasks

# List incomplete tasks in the vault
tasks todo

# List completed tasks from a specific file
tasks file=Recipe done

# List tasks from today's daily note
tasks daily

# Count tasks in daily note
tasks daily total

# List tasks with file paths and line numbers
tasks verbose

# Filter by custom status (quote special chars)
tasks 'status=?'
```

#### `task`

Show or update a task.

**Parameters:**
- `ref=<path:line>` - task reference (path:line)
- `file=<name>` - file name
- `path=<path>` - file path
- `line=<n>` - line number
- `status="<char>"` - set status character

**Flags:**
- `toggle` - toggle task status
- `daily` - daily note
- `done` - mark as done
- `todo` - mark as todo

**Examples:**
```shell
# Show task info
task file=Recipe line=8
task ref="Recipe.md:8"

# Toggle task completion
task ref="Recipe.md:8" toggle

# Toggle task in daily note
task daily line=3 toggle

# Set task status
task file=Recipe line=8 done      # -> [x]
task file=Recipe line=8 todo      # -> [ ]
task file=Recipe line=8 status=-  # -> [-]
task daily line=3 done            # Mark daily note task as done
```

---

### Templates

#### `templates`

List templates.

**Flags:**
- `total` - return template count

#### `template:read`

Read template content.

**Parameters:**
- `name=<template>` - (required) template name
- `title=<title>` - title for variable resolution

**Flags:**
- `resolve` - resolve template variables (`{{date}}`, `{{time}}`, `{{title}}`)

#### `template:insert`

Insert template into active file.

**Parameters:**
- `name=<template>` - (required) template name

Use `create path=<path> template=<name>` to create a file with a template.

---

### Themes and Snippets

#### `themes`

List installed themes.

**Flags:**
- `versions` - include version numbers

#### `theme`

Show active theme or get info.

**Parameters:**
- `name=<name>` - theme name for details

#### `theme:set`

Set active theme.

**Parameters:**
- `name=<name>` - (required) theme name (empty for default)

#### `theme:install`

Install a community theme.

**Parameters:**
- `name=<name>` - (required) theme name

**Flags:**
- `enable` - activate after install

#### `theme:uninstall`

Uninstall a theme.

**Parameters:**
- `name=<name>` - (required) theme name

#### `snippets`

List installed CSS snippets.

#### `snippets:enabled`

List enabled CSS snippets.

#### `snippet:enable`

Enable a CSS snippet.

**Parameters:**
- `name=<name>` - (required) snippet name

#### `snippet:disable`

Disable a CSS snippet.

**Parameters:**
- `name=<name>` - (required) snippet name

---

### Unique Notes

#### `unique`

Create unique note.

**Parameters:**
- `name=<text>` - note name
- `content=<text>` - initial content
- `paneType=tab|split|window` - pane type to open in

**Flags:**
- `open` - open file after creating

---

### Vault

#### `vault`

Show vault info.

**Parameters:**
- `info=name|path|files|folders|size` - return specific info only

#### `vaults`

List known vaults.

**Flags:**
- `total` - return vault count
- `verbose` - include vault paths

#### `vault:open`

Switch to a different vault (TUI only).

**Parameters:**
- `name=<name>` - (required) vault name

---

### Web Viewer

#### `web`

Open URL in web viewer.

**Parameters:**
- `url=<url>` - (required) URL to open

**Flags:**
- `newtab` - open in new tab

---

### Wordcount

#### `wordcount`

Count words and characters (default: active file).

**Parameters:**
- `file=<name>` - file name
- `path=<path>` - file path

**Flags:**
- `words` - return word count only
- `characters` - return character count only

---

### Workspace

#### `workspace`

Show workspace tree.

**Flags:**
- `ids` - include workspace item IDs

#### `workspaces`

List saved workspaces.

**Flags:**
- `total` - return workspace count

#### `workspace:save`

Save current layout as workspace.

**Parameters:**
- `name=<name>` - workspace name

#### `workspace:load`

Load a saved workspace.

**Parameters:**
- `name=<name>` - (required) workspace name

#### `workspace:delete`

Delete a saved workspace.

**Parameters:**
- `name=<name>` - (required) workspace name

#### `tabs`

List open tabs.

**Flags:**
- `ids` - include tab IDs

#### `tab:open`

Open a new tab.

**Parameters:**
- `group=<id>` - tab group ID
- `file=<path>` - file to open
- `view=<type>` - view type to open

#### `recents`

List recently opened files.

**Flags:**
- `total` - return recent file count

---

### Developer Commands

Commands to help you develop community plugins and themes.

#### `devtools`

Toggle Electron dev tools.

#### `dev:debug`

Attach/detach Chrome DevTools Protocol debugger.

**Flags:**
- `on` - attach debugger
- `off` - detach debugger

#### `dev:cdp`

Run a Chrome DevTools Protocol command.

**Parameters:**
- `method=<CDP.method>` - (required) CDP method to call
- `params=<json>` - method parameters as JSON

#### `dev:errors`

Show captured JavaScript errors.

**Flags:**
- `clear` - clear the error buffer

#### `dev:screenshot`

Take a screenshot (returns base64 PNG).

**Parameters:**
- `path=<filename>` - output file path

**Example:**
```shell
obsidian dev:screenshot path=screenshot.png
```

#### `dev:console`

Show captured console messages.

**Parameters:**
- `limit=<n>` - max messages to show (default 50)
- `level=log|warn|error|info|debug` - filter by log level

**Flags:**
- `clear` - clear the console buffer

#### `dev:css`

Inspect CSS with source locations.

**Parameters:**
- `selector=<css>` - (required) CSS selector
- `prop=<name>` - filter by property name

#### `dev:dom`

Query DOM elements.

**Parameters:**
- `selector=<css>` - (required) CSS selector
- `attr=<name>` - get attribute value
- `css=<prop>` - get CSS property value

**Flags:**
- `total` - return element count
- `text` - return text content
- `inner` - return innerHTML instead of outerHTML
- `all` - return all matches instead of first

#### `dev:mobile`

Toggle mobile emulation.

**Flags:**
- `on` - enable mobile emulation
- `off` - disable mobile emulation

#### `eval`

Execute JavaScript and return result.

**Parameters:**
- `code=<javascript>` - (required) JavaScript code to execute

**Example:**
```shell
obsidian eval code="app.vault.getFiles().length"
```

---

## Keyboard Shortcuts

These shortcuts are available in the TUI.

### Navigation

| Action | Shortcut |
| --- | --- |
| Move cursor left | `←` / `Ctrl+B` |
| Move cursor right (accepts suggestion at end of line) | `→` / `Ctrl+F` |
| Jump to start of line | `Ctrl+A` |
| Jump to end of line | `Ctrl+E` |
| Move back one word | `Alt+B` |
| Move forward one word | `Alt+F` |

### Editing

| Action | Shortcut |
| --- | --- |
| Delete to start of line | `Ctrl+U` |
| Delete to end of line | `Ctrl+K` |
| Delete previous word | `Ctrl+W` / `Alt+Backspace` |

### Autocomplete

| Action | Shortcut |
| --- | --- |
| Enter suggestion mode / accept selected suggestion | `Tab` |
| Exit suggestion mode | `Shift+Tab` |
| Enter suggestion mode (from fresh input) | `↓` |
| Accept first/selected suggestion (at end of line) | `→` |

### History

| Action | Shortcut |
| --- | --- |
| Previous history entry / navigate suggestions up | `↑` / `Ctrl+P` |
| Next history entry / navigate suggestions down | `↓` / `Ctrl+N` |
| Reverse history search (type to filter, `Ctrl+R` to cycle) | `Ctrl+R` |

### Other

| Action | Shortcut |
| --- | --- |
| Execute command or accept suggestion | `Enter` |
| Undo autocomplete / exit suggestion mode / clear input | `Escape` |
| Clear screen | `Ctrl+L` |
| Exit | `Ctrl+C` / `Ctrl+D` |

---

## Troubleshooting

If you are having trouble running Obsidian CLI:

- Make sure you are using the latest Obsidian installer version (1.12.7 or above).
- If you just updated Obsidian from an earlier version, turn off the CLI setting and turn it back on again, then allow Obsidian to perform the automatic PATH registration.
- Restart your terminal after registering the CLI for the PATH changes to take effect.
- Obsidian must be running. The CLI connects to the running Obsidian instance.

### Windows

Obsidian CLI on Windows requires the Obsidian 1.12.7+ installer.

Windows uses a terminal redirector that connects Obsidian to stdin/stdout properly. This is necessary because Obsidian normally runs as a GUI app which is incompatible with terminal outputs on Windows. When you install Obsidian 1.12.7+ the `Obsidian.com` terminal redirector will be added in the folder where you installed the `Obsidian.exe` file.

The CLI registration adds Obsidian into your user's PATH variable, which only takes effect after you restart the terminal.

### macOS

The CLI registration creates a symlink at `/usr/local/bin/obsidian` pointing to the CLI binary bundled inside the app. This requires administrator privileges -- you will be prompted via a system dialog.

Check that the symlink exists and points to the correct binary:

```shell
ls -l /usr/local/bin/obsidian
```

If the symlink is missing, create it manually:

```shell
sudo ln -sf /Applications/Obsidian.app/Contents/MacOS/obsidian-cli /usr/local/bin/obsidian
```

> **Note:** If you previously registered the CLI with an older version of Obsidian, you may have a leftover PATH entry in `~/.zprofile`. The new registration process removes this automatically, but if it remains, you can safely delete the lines starting with `# Added by Obsidian` from `~/.zprofile`.

### Linux

The CLI registration copies the CLI binary to `~/.local/bin/obsidian`. This is done because some Linux installation methods run from temporary directories that cannot be symlinked persistently.

Make sure `~/.local/bin` is in your PATH. Add the following to your `~/.bashrc` or `~/.zshrc` if it isn't:

```shell
export PATH="$PATH:$HOME/.local/bin"
```

Check that the binary exists:

```shell
ls -l ~/.local/bin/obsidian
```

If the binary is missing, copy it manually from the Obsidian installation directory:

```shell
cp /path/to/Obsidian/obsidian-cli ~/.local/bin/obsidian
chmod 755 ~/.local/bin/obsidian
```
