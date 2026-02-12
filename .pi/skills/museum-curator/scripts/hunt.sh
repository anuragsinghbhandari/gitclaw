#!/bin/bash
# Hunt for weirdness in the codebase

echo "Searching for the strange and the hacky..."

# Search for common hacky keywords
grep -rnE "HACK|WTF|MAGIC|CRAP|SHIT|DAMN|WOW|OHNO|FIXME|TODO|XXX" . --exclude-dir={node_modules,.git} --exclude=bun.lock --exclude=package-lock.json

# Search for long lines (potential complexity)
echo "Looking for suspiciously long lines..."
find . -type f -name "*.ts" -o -name "*.py" -o -name "*.js" | xargs wc -L | sort -nr | head -n 5

# Search for deep nesting
echo "Looking for deep nesting..."
find . -not -path '*/.*' -type d | awk -F'/' '{print NF, $0}' | sort -nr | head -n 5
