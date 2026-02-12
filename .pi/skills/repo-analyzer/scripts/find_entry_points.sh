#!/bin/bash
# Find common entry points and configuration files
echo "--- Entry Points ---"
find . -maxdepth 2 \( -name "index.*" -o -name "main.*" -o -name "app.*" -o -name "server.*" \) -not -path "*/node_modules/*"

echo -e "\n--- Config Files ---"
find . -maxdepth 2 \( -name "package.json" -o -name "requirements.txt" -o -name "pyproject.toml" -o -name "webpack.config.js" -o -name ".env.example" \) -not -path "*/node_modules/*"
