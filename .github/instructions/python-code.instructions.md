---
applyTo:
  - "torrent/**/*.py"
  - "utils/**/*.py"
---

# Python Code Agent Instructions

You are working on the pyflix Python library - a torrent streaming library.

## Code Style
- Follow PEP 8 with max line length of 120 characters
- Use descriptive variable and function names
- Add docstrings to all public functions and classes
- Use type hints where practical

## Module Structure
- `torrent/` - Core torrent handling (moov detection, download strategies)
- `utils/` - Utility modules (helpers, settings, streaming server)

## Key Patterns
- Use logging module for all output, not print statements
- Handle exceptions explicitly with specific exception types
- Import from Pyflix namespace (e.g., `from Pyflix.utils.settings import ...`)

## Testing Requirements
- All new code must have corresponding tests in `tests/unit/`
- Mock external dependencies (libtorrent, qtfaststart, etc.)
- Use pytest fixtures for common setup
- Maintain minimum 90% coverage

## Validation
Always run `./scripts/validate.sh` before committing.
