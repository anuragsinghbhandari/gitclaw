#!/usr/bin/env python3
import sys
import os

def add_exhibit(name, file_path, description):
    museum_path = "MUSEUM.md"
    
    with open(file_path, 'r') as f:
        content = f.read()
        # Just grab the first 10 lines for the exhibit snippet
        lines = content.split('\n')[:15]
        snippet = '\n'.join(lines)

    exhibit = f"""
### {name}
**File**: `{file_path}`
**Curator's Note**: {description}

```typescript
{snippet}
...
```
"""
    
    with open(museum_path, 'a') as f:
        f.write(exhibit)
    
    print(f"Added exhibit '{name}' to {museum_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: add_exhibit.py <name> <file_path> <description>")
        sys.exit(1)
    
    add_exhibit(sys.argv[1], sys.argv[2], sys.argv[3])
