#!/bin/bash
REPO=$1
COMMAND=$2

if [ -z "$REPO" ]; then
  echo "Usage: $0 <repo_owner/repo_name> [command]"
  exit 1
fi

DIR="temp_clones/$(echo $REPO | sed 's/\//_/g')"
mkdir -p temp_clones

echo "Cloning $REPO into $DIR..."
if [ -n "$GH_PAT" ]; then
    gh repo clone "$REPO" "$DIR" -- --depth 1
else
    gh repo clone "$REPO" "$DIR" -- --depth 1 2>/dev/null || git clone "https://github.com/$REPO.git" "$DIR" --depth 1
fi

cd "$DIR" || exit 1

if [ -z "$COMMAND" ]; then
  echo "Cloned successfully. Contents:"
  ls -F
else
  echo "Running command: $COMMAND"
  eval "$COMMAND"
fi
