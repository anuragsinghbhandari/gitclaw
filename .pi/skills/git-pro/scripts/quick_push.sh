#!/bin/bash
# Commit and push all current changes
MESSAGE=$1

if [ -z "$MESSAGE" ]; then
  echo "Error: No commit message provided."
  exit 1
fi

git add .
git commit -m "$MESSAGE"
git push origin $(git rev-parse --abbrev-ref HEAD)
