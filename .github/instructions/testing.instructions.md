---
applyTo:
  - "tests/**/*.py"
---

# Testing Agent Instructions

You are writing tests for the pyflix Python library.

## Testing Framework
- Use pytest as the test framework
- Use pytest-cov for coverage reporting

## Test Structure
- Place unit tests in `tests/unit/`
- Place integration tests in `tests/integration/`
- Use shared fixtures from `tests/conftest.py`

## Naming Conventions
```python
def test_[function_name]_[scenario]_[expected_result]():
    """Test that [behavior] when [condition]."""
    pass
```

## Test Pattern (AAA)
```python
def test_example():
    # Arrange: Set up test data
    input_data = "test"
    
    # Act: Execute code under test
    result = function_under_test(input_data)
    
    # Assert: Verify result
    assert result == expected
```

## Mocking Guidelines
- Mock external dependencies (file I/O, network, libtorrent)
- Use `unittest.mock.patch` for module-level mocking
- Import modules using `importlib` when direct import causes issues

## Coverage Requirements
- Minimum 90% code coverage
- All public functions must have tests
- Test both success and failure paths
- Test edge cases (empty inputs, None values, boundary conditions)

## Running Tests
```bash
pytest tests/ -v
pytest tests/ --cov=torrent --cov=utils --cov-report=term-missing
```
