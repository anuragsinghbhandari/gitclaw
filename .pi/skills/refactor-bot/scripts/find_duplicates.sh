#!/bin/bash
# Find duplicate lines across files (vaguely detects copy-paste)
# Usage: ./find_duplicates.sh [min_lines]

MIN_LINES=${1:-5}

# This is a very rough approximation using find, sort, and uniq
find . -type f -not -path '*/.*' -not -path '*/node_modules/*' -exec cat {} + | sort | uniq -c | sort -nr | awk -v min="$MIN_LINES" '$1 >= min {print $0}' | head -n 20
