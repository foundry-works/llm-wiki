#!/usr/bin/env bash

set -euo pipefail

# Resolve this script's real location, following symlinks (e.g. when
# invoked via ~/.local/bin/llm-wiki-doctor -> scripts/wiki-doctor.sh).
SOURCE="${BASH_SOURCE[0]}"
while [[ -L "$SOURCE" ]]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  [[ "$SOURCE" != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(cd -P "$(dirname "$SOURCE")" && pwd)"
exec "$SCRIPT_DIR/../wiki-base/scripts/wiki-doctor.sh" "${1:-.}"
