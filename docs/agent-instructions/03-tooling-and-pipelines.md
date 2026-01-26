# Tooling & Pipelines Protocol

This document establishes requirements for automation, tooling, and CI/CD pipelines.

## Core Principle: Automate Repetition

**If you perform a task twice, automate it.**

This applies to:
- Validation steps
- Build processes
- Deployment procedures
- Code quality checks
- Documentation generation

## Tool Creation Guidelines

### When to Create a Tool
- Task is performed more than once
- Task has multiple steps
- Task is error-prone when manual
- Task needs to be reproducible

### Tool Location
```
scripts/
├── validate.sh         # Run all validation (lint, test, coverage)
├── lint.sh             # Run linters only
├── test.sh             # Run tests only
├── build.sh            # Build/package the project
└── setup-dev.sh        # Set up development environment
```

### Tool Standards
Every script must:
1. Have a shebang line (`#!/bin/bash` or `#!/usr/bin/env python3`)
2. Exit with non-zero on failure
3. Print meaningful error messages
4. Be documented (header comment explaining purpose)
5. Be idempotent when possible

### Script Template
```bash
#!/bin/bash
# Description: What this script does
# Usage: ./scripts/script-name.sh [options]
# 
# Options:
#   --verbose    Show detailed output
#   --help       Show this help message

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Script logic here

echo "✓ Task completed successfully"
```

## CI/CD Requirements

### GitHub Actions Workflow Structure
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    # Fast feedback - runs first
    
  test:
    # Comprehensive testing
    
  security:
    # Security scanning
    
  build:
    # Only after tests pass
    needs: [lint, test]
```

### Required CI Checks

#### 1. Linting
- Run on every push and PR
- Block merge if failing
- Include:
  - `flake8` or `ruff` for Python style
  - `black --check` for formatting
  - `isort --check` for import order
  - `mypy` for type checking (if types used)

#### 2. Testing
- Run full test suite
- Require 90% coverage
- Fail if any test fails
- Upload coverage report

#### 3. Security Scanning
- Use CodeQL for static analysis
- Check for vulnerable dependencies
- Scan for secrets in code

#### 4. Build Verification
- Ensure package can be built
- Verify installation works
- Run smoke tests if applicable

### Workflow Best Practices

```yaml
# Use matrix for multiple Python versions
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11', '3.12']

# Cache dependencies
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements*.txt') }}

# Fail fast during testing
strategy:
  fail-fast: true
```

## Local Development Tools

### Validation Script
The `scripts/validate.sh` script should run the same checks as CI:

```bash
#!/bin/bash
# Description: Run all validation checks locally
# Usage: ./scripts/validate.sh

set -euo pipefail

echo "🔍 Running linters..."
flake8 torrent utils
black --check torrent utils
isort --check-only torrent utils

echo "🧪 Running tests with coverage..."
pytest --cov=torrent --cov=utils --cov-report=term-missing --cov-fail-under=90

echo "✓ All checks passed!"
```

### Pre-commit Hooks
Use pre-commit for automatic checks:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

## Prioritized CI/CD Implementation

### Phase 1: Basic (Required)
1. Linting (flake8/ruff)
2. Testing (pytest)
3. Coverage reporting

### Phase 2: Enhanced
1. Security scanning (CodeQL)
2. Dependency vulnerability check
3. Type checking (mypy)

### Phase 3: Advanced
1. Performance benchmarks
2. Documentation building
3. Release automation

## Agent Workflow Integration

### Before Making Changes
```bash
# Ensure you're starting from a clean state
./scripts/validate.sh
```

### After Making Changes
```bash
# Verify changes don't break anything
./scripts/validate.sh
```

### Creating New Tools
When creating a new automation tool:

1. **Identify the need**: Document what manual process is being automated
2. **Write the script**: Follow the script template
3. **Test the script**: Run it multiple times, check edge cases
4. **Document usage**: Add to README or script header
5. **Add to CI**: If the tool should run on every change

## Tool Documentation

Every tool should be documented in:

1. **Script header**: Purpose, usage, options
2. **README.md**: High-level description, when to use
3. **CONTRIBUTING.md**: How to add new tools

### Documentation Template
```markdown
## scripts/[tool-name].sh

**Purpose:** What this tool does

**Usage:**
```bash
./scripts/tool-name.sh [options]
```

**Options:**
- `--verbose`: Show detailed output
- `--dry-run`: Show what would be done without doing it

**Examples:**
```bash
# Basic usage
./scripts/tool-name.sh

# With options
./scripts/tool-name.sh --verbose
```

**Exit Codes:**
- `0`: Success
- `1`: General error
- `2`: Configuration error
```

## Monitoring & Observability

### CI/CD Metrics to Track
- Build time trends
- Test execution time
- Flaky test frequency
- Coverage trends
- Security finding trends

### Status Badges
Add CI status badges to README:
```markdown
![CI](https://github.com/owner/repo/actions/workflows/ci.yml/badge.svg)
![Coverage](https://codecov.io/gh/owner/repo/branch/main/graph/badge.svg)
```
