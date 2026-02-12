#!/bin/bash
# Find TODOs, FIXMEs, and XXXs in the codebase
# Usage: ./find_todos.sh [directory]

TARGET_DIR=${1:-.}

grep -rnE "TODO|FIXME|XXX" "$TARGET_DIR" --exclude-dir={node_modules,.git,state} --exclude={REPORT.md,bun.lock,package-lock.json}
