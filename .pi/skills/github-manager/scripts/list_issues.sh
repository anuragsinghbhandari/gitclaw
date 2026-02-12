#!/bin/bash
# List recent issues with an optional label
LABEL=$1
if [ -n "$LABEL" ]; then
  gh issue list --label "$LABEL" --limit 10
else
  gh issue list --limit 10
fi
