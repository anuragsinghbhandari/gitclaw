#!/bin/bash
# Check for inconsistent file naming (kebab-case vs camelCase)
# Usage: ./check_naming.sh

echo "Files with camelCase (potential issues if project uses kebab-case):"
find . -type f -name "*[a-z][A-Z]*" -not -path '*/node_modules/*' -not -path '*/.git/*'

echo ""
echo "Files with underscores (potential issues if project uses kebab-case):"
find . -type f -name "*_*" -not -path '*/node_modules/*' -not -path '*/.git/*'
