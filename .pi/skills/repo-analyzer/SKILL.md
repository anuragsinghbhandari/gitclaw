---
name: repo-analyzer
description: Analyze and understand the structure of a repository. Use when you first arrive in a new codebase or need to locate entry points, configuration files, and overall project organization.
---

# Repo Analyzer

## Overview

This skill helps you quickly orient yourself in a new codebase. It provides tools to visualize the directory structure and identify critical files.

## Tasks

### 1. Visualization
- **Map Tree**: Use `scripts/map_tree.sh [depth]` to see the project structure (default depth 2). It automatically ignores common noise like `node_modules` and `.git`.

### 2. Exploration
- **Find Entry Points**: Use `scripts/find_entry_points.sh` to locate main application files and configuration files.
- **Search for Patterns**: Use `grep` or `rg` to find specific keywords across the codebase.

## Workflow: Orientation
1. Run `scripts/map_tree.sh` to see the high-level layout.
2. Run `scripts/find_entry_points.sh` to identify where the app starts.
3. Read the `package.json` or `requirements.txt` to understand dependencies.
4. Search for "TODO" or "FIXME" to find areas needing attention.
