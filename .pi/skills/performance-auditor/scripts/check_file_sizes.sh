#!/bin/bash
# Find the 10 largest files in the repository
find . -type f -not -path '*/.*' -not -path '*/node_modules/*' -exec du -h {} + | sort -hr | head -n 10
