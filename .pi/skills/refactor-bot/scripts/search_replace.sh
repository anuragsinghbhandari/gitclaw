#!/bin/bash
# Global search and replace using sed
# Usage: ./search_replace.sh <search_pattern> <replace_pattern> [file_extension]

PATTERN=$1
REPLACE=$2
EXT=${3:-*}

if [ -z "$PATTERN" ] || [ -z "$REPLACE" ]; then
  echo "Usage: $0 <search_pattern> <replace_pattern> [file_extension]"
  exit 1
fi

# Use find to locate files and sed to replace
find . -type f -name "$EXT" -not -path '*/node_modules/*' -not -path '*/.git/*' -exec sed -i "s/$PATTERN/$REPLACE/g" {} +

echo "Replacement complete."
