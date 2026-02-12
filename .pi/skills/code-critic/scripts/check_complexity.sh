#!/bin/bash
# Find files longer than a certain number of lines
# Usage: ./check_complexity.sh [max_lines] [directory]

MAX_LINES=${1:-300}
TARGET_DIR=${2:-.}

find "$TARGET_DIR" -type f -not -path '*/.*' -not -path '*/node_modules/*' -exec wc -l {} + | sort -nr | awk -v max="$MAX_LINES" '$1 > max {print $0}'
