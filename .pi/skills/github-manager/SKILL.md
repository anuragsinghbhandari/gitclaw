---
name: github-manager
description: Manage GitHub issues, pull requests, and repository data. Use when you need to list, view, create, or update issues and PRs, or search through repository history and metadata using the `gh` CLI.
---

# GitHub Manager

## Overview

This skill provides a structured way to interact with GitHub repositories using the `gh` CLI. It's designed to streamline issue management, PR reviews, and repository exploration.

## Task-Based Capabilities

### 1. Issue Management
Use these scripts to interact with issues.

- **List Issues**: Use `scripts/list_issues.sh [label]` to see recent issues.
- **Get Comments**: Use `scripts/get_issue_comments.sh <issue_number>` to read the full conversation of an issue.

### 2. Repository Information
- **View Repo**: `gh repo view` to see the README and general info.
- **Search Code**: `gh search code <query>` to find specific patterns across the repo.

## References

See [references/gh_cli_cheatsheet.md](references/gh_cli_cheatsheet.md) for a quick guide to common `gh` commands.
