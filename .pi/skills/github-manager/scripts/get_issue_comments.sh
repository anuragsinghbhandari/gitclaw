#!/bin/bash
# Get comments for a specific issue
ISSUE_NUMBER=$1
if [ -z "$ISSUE_NUMBER" ]; then
  echo "Usage: $0 <issue-number>"
  exit 1
fi
gh issue view "$ISSUE_NUMBER" --comments
