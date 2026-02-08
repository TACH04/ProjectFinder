#!/bin/bash
# Manual run with popup notification

cd "$(dirname "$0")"
export TMPDIR="$(pwd)/.tmp"
mkdir -p "$TMPDIR"
echo "🔍 Running scraper manually..."
.venv/bin/python3 run_scraper.py --notify popup
echo ""
echo "Done! Press any key to close."
read -n 1
