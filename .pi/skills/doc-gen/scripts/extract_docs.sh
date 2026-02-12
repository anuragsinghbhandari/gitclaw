#!/bin/bash
# Extract JSDoc/Docstrings from a file
# Usage: ./extract_docs.sh <file>

FILE=$1
if [ ! -f "$FILE" ]; then
  echo "File not found: $FILE"
  exit 1
fi

EXTENSION="${FILE##*.}"

case "$EXTENSION" in
  js|ts)
    # Extract blocks starting with /** and ending with */
    sed -n '/\/\*\*/,/\*\//p' "$FILE"
    ;;
  py)
    # Extract blocks between triple quotes
    sed -n '/"""/,/"""/p' "$FILE"
    ;;
  *)
    echo "Unsupported extension: $EXTENSION"
    ;;
esac
