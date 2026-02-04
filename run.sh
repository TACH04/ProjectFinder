#!/bin/bash
# Run the scraper with proper temp directory
cd "$(dirname "$0")"
export TMPDIR="$(pwd)/.tmp"
mkdir -p "$TMPDIR"
.venv/bin/python3 main.py "$@"
