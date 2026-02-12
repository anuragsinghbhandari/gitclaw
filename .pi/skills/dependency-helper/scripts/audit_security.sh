#!/bin/bash
# Run security audits
if [ -f "package.json" ]; then
  echo "--- NPM Audit ---"
  npm audit
fi

if [ -f "requirements.txt" ]; then
  echo "--- Pip Audit ---"
  pip-audit 2>/dev/null || echo "pip-audit not installed"
fi
