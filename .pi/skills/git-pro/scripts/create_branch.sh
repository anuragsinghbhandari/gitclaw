#!/bin/bash
# Create and switch to a new branch
BRANCH_NAME=$1

if [ -z "$BRANCH_NAME" ]; then
  echo "Error: No branch name provided."
  exit 1
fi

git checkout -b "$BRANCH_NAME"
git push -u origin "$BRANCH_NAME"
