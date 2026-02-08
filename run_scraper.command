#!/bin/bash
# Double-click to run the scraper (run_scraper.py)

cd "$(dirname "$0")"
export TMPDIR="$(pwd)/.tmp"
mkdir -p "$TMPDIR"
echo "🔍 Running scraper..."
.venv/bin/python3 run_scraper.py
echo ""
echo "Done! Press any key to close."
read -n 1
