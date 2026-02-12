---
name: performance-auditor
description: Audit repository performance and benchmark commands. Use when you need to find large files that might slow down the build or measure the execution time of scripts and tests.
---

# Performance Auditor

## Overview

This skill helps identify performance bottlenecks in the codebase or build process.

## Tasks

### 1. Storage Analysis
- **Check File Sizes**: Run `scripts/check_file_sizes.sh` to find the largest files in the repository (ignoring node_modules and .git).

### 2. Benchmarking
- **Benchmark Command**: Run `scripts/benchmark_command.sh <command>` to execute a command 3 times and see the wall-clock time for each run.

## Workflow: Optimization
1. Identify large assets that could be compressed or moved to LFS.
2. Benchmark slow tests or build steps to establish a baseline.
3. Apply optimizations and re-benchmark to verify improvements.
