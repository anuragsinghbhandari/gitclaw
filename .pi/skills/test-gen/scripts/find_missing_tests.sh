#!/bin/bash
# Find source files that don't have a corresponding test file
# Usage: ./find_missing_tests.sh [src_dir] [test_dir]

SRC_DIR=${1:-.}
TEST_DIR=${2:-.}

# Very basic heuristic: looks for .js/.ts/.py files and checks if a .test.js / _test.py etc exists
find "$SRC_DIR" -type f \( -name "*.js" -o -name "*.ts" -o -name "*.py" \) \
  -not -path "*/node_modules/*" \
  -not -path "*/test/*" \
  -not -path "*/tests/*" \
  -not -name "*.test.*" \
  -not -name "test_*" | while read -r file; do
    filename=$(basename "$file")
    basename="${filename%.*}"
    # Check if a test file exists anywhere in TEST_DIR
    if ! find "$TEST_DIR" -name "*$basename*test*" -o -name "test_$basename*" | grep -q .; then
      echo "Missing test for: $file"
    fi
done
