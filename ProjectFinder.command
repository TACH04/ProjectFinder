#!/bin/bash
# Double-click this file to run ProjectFinder manually

cd "$(dirname "$0")"
echo "🔍 Running ProjectFinder..."
.venv/bin/python3 main.py
echo ""
echo "Done! Press any key to close."
read -n 1
