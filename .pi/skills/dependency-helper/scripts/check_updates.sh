#!/bin/bash
# Check for updates in various package managers
if [ -f "package.json" ]; then
  echo "--- NPM Updates ---"
  npm outdated
fi

if [ -f "requirements.txt" ]; then
  echo "--- Pip Updates (checking via pip list) ---"
  pip list --outdated
fi

if [ -f "Cargo.toml" ]; then
  echo "--- Cargo Updates ---"
  cargo outdated 2>/dev/null || echo "cargo-outdated not installed"
fi
