# Obsidian Headless Sync

> Source: https://obsidian.md/help/sync/headless

## Overview

Obsidian Sync offers a headless client to sync vaults without using the desktop app. Useful for CI pipelines, agents, and automated workflows. The headless client maintains the same encryption and privacy protections as the desktop app, including end-to-end encryption.

## Requirements

- An active Obsidian Sync subscription
- Back up your data before beginning
- Do **not** run both desktop and headless sync simultaneously on the same device to prevent conflicts

## Installation

```shell
npm install -g obsidian-headless
```

## Platform Support

The package includes native modules for preserving file creation timestamps (birthtime) on Windows and macOS. Prebuilt binaries support:

- **Windows**: x64, ARM64, and 32-bit
- **macOS**: Apple Silicon (ARM64) and Intel (x64)
- **Linux**: Functions normally for synchronization but without birthtime preservation

## Commands

### `ob login`

Authenticate with your Obsidian account.

### `ob sync-list-remote`

List all remote vaults available to your account, including shared vaults.

### `ob sync-list-local`

List locally configured vaults and their paths.

### `ob sync-create-remote`

Create a new remote vault.

```shell
ob sync-create-remote --name "Vault Name" [--encryption <standard|e2ee>] [--password <password>] [--region <region>]
```

**Options:**
- `--name` (required) - vault name
- `--encryption` - `standard` or `e2ee`
- `--password` - end-to-end encryption password
- `--region` - server region

### `ob sync-setup`

Configure a local directory to sync with a remote vault.

```shell
ob sync-setup --vault <id-or-name> [--path <local-path>] [--password <password>] [--device-name <name>] [--config-dir <name>]
```

**Options:**
- `--vault` (required) - remote vault ID or name
- `--path` - local directory (default: current directory)
- `--password` - end-to-end encryption password
- `--device-name` - device identifier in version history
- `--config-dir` - config folder name (default: `.obsidian`)

### `ob sync`

Execute synchronization.

```shell
ob sync [--path <local-path>] [--continuous]
```

**Options:**
- `--path` - local vault path (default: current directory)
- `--continuous` - run continuously, watching for changes

### `ob sync-config`

Manage sync settings.

```shell
ob sync-config [--path <local-path>] [options]
```

**Options:**
- `--path` - local vault path
- `--mode` - sync mode: `bidirectional` (default), `pull-only`, or `mirror-remote`
- `--conflict-strategy` - `merge` or `conflict`
- `--file-types` - attachment types to sync: `image`, `audio`, `video`, `pdf`, `unsupported`
- `--configs` - config categories to sync
- `--excluded-folders` - folders to exclude from sync
- `--device-name` - device identifier
- `--config-dir` - config directory name

### `ob sync-status`

Display current sync status and configuration.

```shell
ob sync-status [--path <local-path>]
```

### `ob sync-unlink`

Disconnect vault from sync and remove credentials.

```shell
ob sync-unlink [--path <local-path>]
```

## Typical Workflow

```shell
# 1. Authenticate
ob login

# 2. List available remote vaults
ob sync-list-remote

# 3. Set up a local directory to sync with a remote vault
ob sync-setup --vault "My Vault" --path ./my-vault

# 4. Configure sync settings (optional)
ob sync-config --path ./my-vault --mode pull-only

# 5. Run sync (one-time)
ob sync --path ./my-vault

# 6. Or run continuously
ob sync --path ./my-vault --continuous
```
