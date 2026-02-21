#!/bin/bash
NEW_NAME=$1
TEMPLATE=${2:-"anuragsinghbhandari/gitclaw"}

if [ -z "$NEW_NAME" ]; then
  echo "Usage: $0 <new_repo_name> [template_repo]"
  exit 1
fi

echo "Hatching new agent: $NEW_NAME from template $TEMPLATE..."

# Create the repo
gh repo create "$NEW_NAME" --template "$TEMPLATE" --public

if [ $? -eq 0 ]; then
  echo "Successfully hatched $NEW_NAME!"
  echo "Note: You still need to manually add ANTHROPIC_API_KEY to the new repo's secrets."
else
  echo "Failed to hatch agent. Check permissions and if the repo name is taken."
fi
