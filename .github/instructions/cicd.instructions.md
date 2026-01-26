---
applyTo:
  - ".github/workflows/**"
  - "scripts/**"
---

# CI/CD Agent Instructions

You are maintaining CI/CD pipelines and automation scripts for pyflix.

## GitHub Actions Best Practices
- Use `actions/checkout@v4` for code checkout
- Use `actions/setup-python@v5` for Python setup
- Cache pip dependencies for faster builds
- Use matrix builds for multiple Python versions (3.9-3.12)

## Required CI Checks
1. **Linting**: flake8, black --check, isort --check-only
2. **Testing**: pytest with coverage (90% minimum)
3. **Security**: CodeQL analysis, pip-audit

## Workflow Structure
```yaml
jobs:
  lint:
    # Fast feedback - runs first
  test:
    # Matrix across Python versions
  security:
    # CodeQL + dependency scanning
  build:
    needs: [lint, test]
    # Only after tests pass
```

## Script Requirements
- All scripts must have shebang (`#!/bin/bash`)
- Use `set -euo pipefail` for safe error handling
- Add descriptive header comments
- Exit with non-zero on failure
- Print meaningful progress messages

## Validation Script
`scripts/validate.sh` must mirror CI checks:
- Run linters (flake8, black, isort)
- Run tests with coverage
- Exit non-zero if any check fails
