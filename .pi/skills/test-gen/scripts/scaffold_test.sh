#!/bin/bash
# Generate a basic test scaffold for a given file
# Usage: ./scaffold_test.sh <source_file>

FILE=$1
if [ ! -f "$FILE" ]; then
  echo "File not found: $FILE"
  exit 1
fi

EXTENSION="${FILE##*.}"
BASENAME=$(basename "$FILE")
FILENAME="${BASENAME%.*}"

case "$EXTENSION" in
  js|ts)
    cat <<EOF
import { describe, it, expect } from 'vitest';
import * as target from './$BASENAME';

describe('$FILENAME', () => {
  it('should be defined', () => {
    expect(target).toBeDefined();
  });
});
EOF
    ;;
  py)
    cat <<EOF
import unittest
import $FILENAME

class Test${FILENAME^}(unittest.TestCase):
    def test_exists(self):
        self.assertIsNotNone($FILENAME)

if __name__ == '__main__':
    unittest.main()
EOF
    ;;
  *)
    echo "Unsupported extension: $EXTENSION"
    ;;
esac
