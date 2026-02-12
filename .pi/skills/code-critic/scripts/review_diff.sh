#!/bin/bash
# Get the diff of the current branch against a base branch (default: main)
BASE_BRANCH=${1:-main}

if ! git rev-parse --verify "$BASE_BRANCH" >/dev/null 2>&1; then
  # Try origin/main if main doesn't exist locally
  if git rev-parse --verify "origin/$BASE_BRANCH" >/dev/null 2>&1; then
    BASE_BRANCH="origin/$BASE_BRANCH"
  else
    echo "Error: Base branch '$BASE_BRANCH' not found."
    exit 1
  fi
fi

git diff "$BASE_BRANCH"...HEAD
