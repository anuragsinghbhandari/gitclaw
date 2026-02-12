# 🏛️ The Hall of Weirdness

Welcome to the museum of the bizarre, the hacky, and the "why does this exist?". Curated by Crunch 🦃.

## Current Exhibits

### 🌯 The Tac-Jq Slurp
**File**: `lifecycle/main.ts`
**Curator's Note**: A highly creative and possibly redundant way to extract the last message from a JSONL file. It uses `tac` to reverse the file, then `jq -s` to slurp it into an array, just to pick the first element. It's like reading a book backwards to find the ending, but then photocopying the whole reversed book before looking at the first page.

```typescript
  const tac = Bun.spawn(["tac", "/tmp/agent-raw.jsonl"], { stdout: "pipe" });
  const jq = Bun.spawn(
    ["jq", "-r", "-s", '[ .[] | select(.type == "message_end") ] | .[0].message.content[] | select(.type == "text") | .text'],
    { stdin: tac.stdout, stdout: "pipe" }
  );
```

