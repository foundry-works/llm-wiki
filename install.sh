#!/usr/bin/env sh
# Install the LLM Wiki.
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/tylerburleigh/llm-wiki/main/install.sh | sh
#
# Clones the repo to $LLM_WIKI_DIR (default: ~/.local/share/llm-wiki) and
# symlinks scripts/new-wiki.sh to $LLM_WIKI_BIN/llm-wiki-new (default:
# ~/.local/bin). Re-running updates the clone in place.

set -eu

REPO="${LLM_WIKI_REPO:-https://github.com/tylerburleigh/llm-wiki.git}"
CLONE_DIR="${LLM_WIKI_DIR:-$HOME/.local/share/llm-wiki}"
BIN_DIR="${LLM_WIKI_BIN:-$HOME/.local/bin}"

if [ -d "$CLONE_DIR/.git" ]; then
  echo "Updating $CLONE_DIR"
  git -C "$CLONE_DIR" pull --ff-only
else
  echo "Cloning $REPO -> $CLONE_DIR"
  mkdir -p "$(dirname "$CLONE_DIR")"
  git clone --depth 1 "$REPO" "$CLONE_DIR"
fi

mkdir -p "$BIN_DIR"
ln -sf "$CLONE_DIR/scripts/new-wiki.sh" "$BIN_DIR/llm-wiki-new"

case ":$PATH:" in
  *":$BIN_DIR:"*) PATH_NOTE="" ;;
  *) PATH_NOTE="
Add this to your shell profile (~/.zshrc, ~/.bashrc) if it isn't already:
  export PATH=\"$BIN_DIR:\$PATH\"
" ;;
esac

cat <<EOF

Installed:
  repo:     $CLONE_DIR
  launcher: $BIN_DIR/llm-wiki-new -> scripts/new-wiki.sh
$PATH_NOTE
Next steps:
  1. llm-wiki-new ~/wikis/my-wiki --git
  2. cd ~/wikis/my-wiki
  3. Edit purpose.md with your research direction.
  4. Drop a source (PDF or markdown) into raw/.
  5. Launch Claude Code and run: /wiki-ingest raw/<your-source>
EOF
