# Test Suite for pyflix

This directory contains the test suite for the pyflix library.

## Structure

```
tests/
├── conftest.py          # Shared pytest fixtures
├── unit/                # Unit tests (isolated, fast)
│   ├── test_moov.py
│   ├── test_strategy.py
│   └── test_helpers.py
├── integration/         # Integration tests (component interactions)
│   └── test_torrent_flow.py
└── e2e/                 # End-to-end tests (full workflows)
    └── test_streaming.py
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=torrent --cov=utils --cov-report=term-missing

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/test_moov.py

# Run tests matching pattern
pytest -k "test_have_moov"

# Run with coverage enforcement (90% minimum)
pytest --cov=torrent --cov=utils --cov-fail-under=90
```

## Writing Tests

### Naming Convention
```python
def test_[function_name]_[scenario]_[expected_result]():
    pass
```

### Test Structure (AAA Pattern)
```python
def test_example():
    # Arrange: Set up test data
    input_data = "test"
    
    # Act: Execute code under test
    result = function_under_test(input_data)
    
    # Assert: Verify result
    assert result == expected
```

### Using Fixtures
```python
@pytest.fixture
def sample_video_file(tmp_path):
    """Create a temporary test video file."""
    video = tmp_path / "test.mp4"
    video.write_bytes(b"mock video content")
    return str(video)

def test_with_fixture(sample_video_file):
    result = process_video(sample_video_file)
    assert result is not None
```

## Coverage Requirements

- **Minimum**: 90% code coverage
- **Target**: 95%+ for critical modules

Files excluded from coverage:
- `__init__.py` files
- Test files themselves
- Configuration files
