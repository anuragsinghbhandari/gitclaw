#!/bin/bash
# Run a command 3 times and report the average time
COMMAND=$@
if [ -z "$COMMAND" ]; then
  echo "Usage: $0 <command>"
  exit 1
fi

echo "Benchmarking: $COMMAND"
for i in {1..3}; do
  echo -n "Run $i: "
  /usr/bin/time -f "%e seconds" $COMMAND
done
