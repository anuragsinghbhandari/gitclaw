---
name: test-gen
description: Automated test generation and coverage auditing. Use when identifying missing tests or creating new test suites.
---

# 🧪 Test Gen

Test Gen helps ensure your codebase is well-tested and reliable.

## Tasks

### 1. Coverage Audit
- **Find Missing Tests**: Run `scripts/find_missing_tests.sh [src_dir]` to identify source files that lack corresponding test files.

### 2. Test Scaffolding
- **Scaffold Test**: Run `scripts/scaffold_test.sh <source_file>` to generate a basic test template for a given JavaScript, TypeScript, or Python file.

## Workflow: Improving Test Coverage
1. Run `find_missing_tests.sh` to see where the gaps are.
2. For a missing test, run `scaffold_test.sh` to get a starting point.
3. Fill in the specific test cases using the LLM's understanding of the code.
4. Run the tests (using the project's standard test runner) to verify.
