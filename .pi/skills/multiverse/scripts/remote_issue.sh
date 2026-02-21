#!/bin/bash
REPO=$1
TITLE=$2
BODY=$3

if [ -z "$REPO" ] || [ -z "$TITLE" ]; then
  echo "Usage: $0 <repo_owner/repo_name> <title> [body]"
  exit 1
fi

gh issue create -R "$REPO" -t "$TITLE" -b "$BODY"
