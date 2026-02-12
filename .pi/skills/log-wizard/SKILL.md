---
name: log-wizard
description: Parse and analyze log files to find errors, exceptions, and failures. Use when debugging build logs, application logs, or any large text file containing system output.
---

# Log Wizard

## Overview

Log Wizard helps you find the needle in the haystack of large log files. It uses pattern matching to highlight critical issues.

## Tasks

### 1. Log Analysis
- **Analyze Log**: Use `python3 scripts/analyze_logs.py <file>` to extract errors, failures, and exceptions from a log file.

### 2. Tail and Follow
- Use `tail -f` for real-time monitoring.
- Use `grep -C 5 "Error"` to see context around errors.

## Tips
- Always check the last 100 lines of a failing CI log first.
- Search for "timestamp" to see where processes got stuck.
