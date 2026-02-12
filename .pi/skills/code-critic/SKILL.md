---
name: code-critic
description: Automated code review and quality checks. Use when you need to review changes, find TODOs, or identify complex files.
---

# 🧐 Code Critic

This skill helps maintain code quality by identifying potential issues, technical debt, and complexity.

## Tasks

### 1. Review Changes
- **Diff Review**: Run `scripts/review_diff.sh <base_branch>` to get a clean diff of changes between the current branch and the base branch (e.g., `main`).

### 2. Technical Debt
- **Find TODOs**: Run `scripts/find_todos.sh` to locate `TODO`, `FIXME`, and `XXX` markers in the codebase.

### 3. Complexity Analysis
- **Long Files**: Run `scripts/check_complexity.sh <max_lines>` to find files that might be getting too large and are candidates for refactoring.

## Workflow: Code Review
1. Run `review_diff.sh` to see what has changed.
2. Run `find_todos.sh` to see if any new technical debt was introduced.
3. Run `check_complexity.sh` to ensure no files have grown beyond manageable limits.
4. (Optional) Use the LLM to analyze the diff for logic errors or security vulnerabilities.
