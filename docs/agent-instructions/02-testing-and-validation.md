# Testing & Validation Protocol

Testing is not optional. This document establishes mandatory testing requirements for all code contributions.

## The 90% Rule

**Minimum 90% code coverage is required for all new and modified code.**

This applies to:
- New features
- Bug fixes
- Refactoring
- Any code that can be executed

### Exceptions (Require Documentation):
- Configuration files
- Third-party integration points (mock instead)
- Hardware-dependent code (document why)

## Test-Driven Development

### The TDD Cycle
```
1. Write a failing test that defines desired behavior
2. Write minimum code to pass the test
3. Refactor while keeping tests green
4. Repeat
```

### When Writing New Features:
```
Step 1: Understand the specification
Step 2: Write test cases from specification
Step 3: Implement until tests pass
Step 4: Refactor and add edge case tests
Step 5: Verify coverage meets 90% threshold
```

### When Fixing Bugs:
```
Step 1: Write a test that reproduces the bug
Step 2: Verify test fails
Step 3: Fix the bug
Step 4: Verify test passes
Step 5: Ensure no regression in other tests
```

## Test Categories

### Unit Tests
- Test individual functions/methods in isolation
- Mock external dependencies
- Fast execution (< 1 second per test)
- Location: `tests/unit/`

### Integration Tests
- Test component interactions
- May use real dependencies (database, filesystem)
- Slower but more realistic
- Location: `tests/integration/`

### End-to-End Tests
- Test complete user workflows
- Full system execution
- Slowest but highest confidence
- Location: `tests/e2e/`

## Test File Organization

```
tests/
├── __init__.py
├── conftest.py          # Shared fixtures
├── unit/
│   ├── __init__.py
│   ├── test_moov.py
│   ├── test_strategy.py
│   └── test_helpers.py
├── integration/
│   ├── __init__.py
│   └── test_torrent_flow.py
└── e2e/
    ├── __init__.py
    └── test_streaming.py
```

## Testing Tools & Configuration

### pytest (Primary Test Framework)
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=torrent --cov=utils --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_moov.py

# Run tests matching pattern
pytest -k "test_strategy"
```

### Coverage Requirements
```ini
# pyproject.toml or setup.cfg
[tool.coverage.run]
source = ["torrent", "utils"]
branch = true

[tool.coverage.report]
fail_under = 90
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
```

## Self-Correction Protocol

Agents must verify their own work before committing.

### Step 1: Run Tests Locally
```bash
./scripts/validate.sh
```

### Step 2: Check Coverage
```bash
pytest --cov --cov-fail-under=90
```

### Step 3: Analyze Failures
If tests fail:
1. Read the error message completely
2. Identify the root cause
3. Fix the issue
4. Run tests again
5. Repeat until green

### Step 4: Review Coverage Report
```bash
pytest --cov --cov-report=html
# Open htmlcov/index.html to see uncovered lines
```

For uncovered lines:
1. Determine if line should be tested
2. Write test to cover it
3. Mark with `# pragma: no cover` only if truly untestable

## Writing Good Tests

### Test Naming Convention
```python
def test_[function_name]_[scenario]_[expected_result]():
    """Test that [behavior] when [condition]."""
    pass

# Examples:
def test_have_moov_returns_true_when_moov_before_mdat():
    """Test that have_moov returns True when moov atom precedes mdat."""
    pass

def test_get_settings_creates_default_when_missing():
    """Test that get_settings creates default config when file doesn't exist."""
    pass
```

### Test Structure (AAA Pattern)
```python
def test_example():
    # Arrange: Set up test data and conditions
    input_data = create_test_data()
    expected = "expected result"
    
    # Act: Execute the code under test
    result = function_under_test(input_data)
    
    # Assert: Verify the result
    assert result == expected
```

### What to Test
- **Happy path**: Normal, expected inputs
- **Edge cases**: Boundary values, empty inputs, None
- **Error cases**: Invalid inputs, exceptions
- **State changes**: Side effects, mutations

### What NOT to Test
- Third-party library internals
- Language features (Python itself)
- Simple getters/setters with no logic

## Mocking Guidelines

### When to Mock
- External services (APIs, databases)
- Filesystem operations (when not testing them directly)
- Time-dependent code
- Random number generation

### How to Mock
```python
from unittest.mock import Mock, patch

def test_with_mock():
    # Using patch decorator
    with patch('module.external_function') as mock_func:
        mock_func.return_value = "mocked result"
        result = function_that_uses_external()
        assert result == "expected"
        mock_func.assert_called_once_with("expected_arg")
```

## Pre-Commit Checklist

Before committing code:

- [ ] All tests pass (`pytest`)
- [ ] Coverage ≥ 90% (`pytest --cov --cov-fail-under=90`)
- [ ] New code has corresponding tests
- [ ] No skipped tests without explanation
- [ ] No tests marked `@pytest.mark.skip` long-term
- [ ] Tests are deterministic (no flaky tests)
- [ ] Tests run in reasonable time (< 5 min total)

## Handling Test Failures in CI

If CI fails:
1. **Do not ignore** the failure
2. Pull the latest changes
3. Run tests locally
4. Identify the failing test
5. Determine if failure is due to your changes
6. Fix the issue or investigate existing bug
7. Push fix and verify CI passes
