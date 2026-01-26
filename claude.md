# Pyflix AI Agent Instructions

You are an AI assistant working on the **pyflix** repository—a Python library for torrent streaming that powers [torrent-dl](https://github.com/animeshkundu/torrent-dl).

## Before You Begin

**MANDATORY**: Read the following documentation before responding to any request:

1. `docs/agent-instructions/` - Agent protocols and requirements
2. `docs/adrs/` - Past architectural decisions
3. `docs/specs/` - Feature specifications

## Technology Stack

- **Language**: Python 3.x
- **Core Functionality**: Torrent streaming, video atom manipulation
- **Key Dependencies**: libtorrent, qtfaststart, PyYAML
- **Testing**: pytest with pytest-cov
- **Linting**: flake8, black, isort

## Project Structure

```
pyflix/
├── torrent/              # Core torrent handling
│   ├── moov.py           # Video MOOV atom detection
│   └── strategy.py       # Download strategy engine
├── utils/                # Utility modules
│   ├── helpers.py        # Common helper functions
│   ├── settings.py       # Configuration management
│   ├── logger.py         # Logging setup
│   └── output.py         # Output formatting
├── docs/                 # Documentation (THE BRAIN)
├── scripts/              # Automation scripts
└── tests/                # Test suite
```

## Core Principles

### 1. Documentation First
- **Never** write code without a specification in `docs/specs/`
- **Always** check `docs/adrs/` before making architectural changes
- **Update** documentation when implementation changes

### 2. Research Before Coding
- **Search the internet** to verify library APIs and best practices
- **Do not hallucinate** API signatures, configuration options, or URLs
- **Validate** dependency versions before adding or updating

### 3. Test Everything
- **90% minimum** code coverage required
- **Write tests first** or alongside implementation
- **Run `./scripts/validate.sh`** before committing

### 4. Automate Repetition
- If you perform a task twice, **create a script** for it
- Use existing scripts in `scripts/` directory
- Add new scripts following established patterns

## Workflow Requirements

### When Adding Features
1. Check if a spec exists in `docs/specs/`; create one if not
2. Review relevant ADRs in `docs/adrs/`
3. Research current best practices
4. Write tests alongside implementation
5. Update architecture docs if structure changes
6. Run validation: `./scripts/validate.sh`

### When Fixing Bugs
1. Write a test that reproduces the bug
2. Fix the bug
3. Verify test passes
4. Update spec if behavior changed
5. Run full test suite

### When Refactoring
1. Ensure tests exist for affected code
2. Make incremental changes
3. Run tests after each change
4. Update architecture diagrams

## Code Style

- Follow PEP 8 with Black formatting
- Use type hints where practical
- Prefer explicit over implicit
- Write descriptive function/variable names
- Add docstrings to public functions

```python
# Good
def have_moov(video_file: str) -> bool:
    """Check if video file has MOOV atom before MDAT.
    
    Args:
        video_file: Path to the video file to analyze
        
    Returns:
        True if MOOV atom is properly positioned, False otherwise
    """
    pass

# Avoid
def check(f):
    pass
```

## Error Handling

- Use specific exception types
- Log errors with context
- Provide actionable error messages
- Don't silence exceptions without reason

```python
# Good
try:
    result = process_video(path)
except VideoProcessingError as e:
    log.error("Failed to process video %s: %s", path, e)
    raise
except FileNotFoundError:
    log.error("Video file not found: %s", path)
    raise VideoNotFoundError(path) from None

# Avoid
try:
    result = process_video(path)
except:
    pass
```

## Testing Guidelines

- Use pytest fixtures for common setup
- Mock external dependencies
- Test edge cases and error conditions
- Name tests descriptively

```python
# Good test name
def test_have_moov_returns_false_when_file_not_found():
    pass

# Avoid
def test_moov():
    pass
```

## Validation Commands

```bash
# Run all checks
./scripts/validate.sh

# Run tests only
pytest

# Run tests with coverage
pytest --cov=torrent --cov=utils --cov-report=term-missing

# Run linting
flake8 torrent utils
black --check torrent utils
```

## Important Notes

- **Do not** modify files in `.github/agents/` or `.claude/agents/`
- **Do not** commit secrets or credentials
- **Do not** add dependencies without security review
- **Always** run validation before committing
- **Document** any deviations from these guidelines with rationale

## Getting Help

If you're unsure about:
- **Architecture**: Check `docs/adrs/` and `docs/architecture/`
- **Feature behavior**: Check `docs/specs/`
- **Past decisions**: Check `docs/history/`
- **Current state**: Search the codebase and recent commits
- **External APIs**: Search the internet—don't guess

Remember: **When in doubt, research and document.**
