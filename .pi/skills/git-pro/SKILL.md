---
name: git-pro
description: Advanced git operations including committing, pushing, and branch management. Use this when you need to persist changes to the remote repository.
---

# 🛠️ Git Pro

This skill allows the agent to manage the repository's git state, commit changes, and push to the remote origin.

## Core Tasks

### 1. Quick Commit & Push
Persist your current changes to the current branch.
```bash
./.pi/skills/git-pro/scripts/quick_push.sh "Commit message"
```

### 2. Feature Branching
Create a new branch for a specific task.
```bash
./.pi/skills/git-pro/scripts/create_branch.sh "branch-name"
```

### 3. Undo/Reset
Clean up the working directory if something went wrong.
```bash
git reset --hard HEAD
```

## Safety Guidelines
- Always check `git status` before committing.
- Ensure commit messages are descriptive.
- Don't push to `main` without permission (unless it's a hotfix or you're Crunchy).
