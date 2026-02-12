#!/bin/bash
# Find functions/classes without documentation
# Usage: ./check_undocumented.sh <file>

FILE=$1
if [ ! -f "$FILE" ]; then
  echo "File not found: $FILE"
  exit 1
fi

EXTENSION="${FILE##*.}"

case "$EXTENSION" in
  js|ts)
    # Look for export function/const/class NOT preceded by /**
    # This is a very rough regex approach
    grep -B 1 -E "export (function|const|class)" "$FILE" | grep -v "/\*\*" | grep -E "export (function|const|class)"
    ;;
  py)
    # Look for def/class NOT preceded by """
    grep -B 1 -E "^(def|class)" "$FILE" | grep -v "\"\"\"" | grep -E "^(def|class)"
    ;;
  *)
    echo "Unsupported extension: $EXTENSION"
    ;;
esac
