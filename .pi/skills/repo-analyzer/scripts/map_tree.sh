#!/bin/bash
# Show a depth-limited directory tree, ignoring common noise
DEPTH=${1:-2}
tree -L "$DEPTH" -I "node_modules|.git|.venv|__pycache__|dist|build"
