#!/usr/bin/env bash
# Create release zips in the repository root (ignored by git). See PROJECT_MAP.md.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
cd "$ROOT"
rm -f applypilot.ai-complete.zip applypilot.ai-source.zip
zip -rq applypilot.ai-complete.zip . \
  -x "./applypilot.ai-complete.zip" \
  -x "./applypilot.ai-source.zip" \
  -x "./applypilot.ai-project.zip"
git archive --format=zip -o applypilot.ai-source.zip HEAD
ls -lh applypilot.ai-complete.zip applypilot.ai-source.zip
echo "Done. Archives written under: $ROOT"
