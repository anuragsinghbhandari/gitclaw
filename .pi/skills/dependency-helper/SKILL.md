---
name: dependency-helper
description: Manage and audit project dependencies. Use when checking for outdated packages, security vulnerabilities, or trying to understand the dependency graph of a project (npm, pip, cargo).
---

# Dependency Helper

## Overview

This skill provides utilities to manage project dependencies across different ecosystems. It helps keep packages up-to-date and secure.

## Tasks

### 1. Update Checks
- **Check Updates**: Run `scripts/check_updates.sh` to see which dependencies have newer versions available.

### 2. Security Auditing
- **Audit Security**: Run `scripts/audit_security.sh` to check for known vulnerabilities in your project's dependencies.

## References

### Common Commands
- **NPM**: `npm install`, `npm uninstall`, `npm update`
- **Pip**: `pip install -r requirements.txt`, `pip freeze > requirements.txt`
- **Cargo**: `cargo update`, `cargo add`
