---
name: refactor-bot
description: Tools for automated refactoring and codebase cleanup. Use when renaming things, moving files, or consolidating logic.
---

# 🤖 Refactor Bot

Refactor Bot helps you transform the codebase efficiently and consistently.

## Tasks

### 1. Global Search & Replace
- **Bulk Replace**: Run `scripts/search_replace.sh <search_pattern> <replace_pattern> [ext]` to perform a search and replace across the project. Use with caution!

### 2. Consistency Checks
- **Naming Consistency**: Run `scripts/check_naming.sh` to find files that don't match common naming conventions (camelCase vs snake_case vs kebab-case).

### 3. Redundancy Detection
- **Duplicate Lines**: Run `scripts/find_duplicates.sh <min_occurrences>` to find lines of code that appear frequently, suggesting potential for extraction into components or utilities.

## Workflow: Refactoring
1. Identify a pattern to refactor (e.g., a duplicated utility).
2. Use `search_replace.sh` to update call sites.
3. Use `check_naming.sh` to ensure any new files follow project conventions.
