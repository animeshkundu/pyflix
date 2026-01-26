# pyflix

[![CI](https://github.com/animeshkundu/pyflix/actions/workflows/ci.yml/badge.svg)](https://github.com/animeshkundu/pyflix/actions/workflows/ci.yml)

The torrent streaming library that powers [torrent-dl](https://github.com/animeshkundu/torrent-dl).

## Features

- Sequential download for video streaming
- MOOV atom detection for optimal playback
- Configurable download strategies
- Daemon mode support

## Installation

```bash
pip install -r requirements.txt
```

## Development Setup

```bash
# Set up development environment
./scripts/setup-dev.sh

# Activate virtual environment
source venv/bin/activate

# Run validation checks
./scripts/validate.sh
```

## Project Structure

```
pyflix/
├── torrent/              # Core torrent handling
│   ├── moov.py           # Video MOOV atom detection
│   └── strategy.py       # Download strategy engine
├── utils/                # Utility modules
├── docs/                 # Documentation (see below)
├── scripts/              # Automation scripts
└── tests/                # Test suite
```

## Documentation

This repository follows a documentation-first approach:

| Directory | Purpose |
|-----------|---------|
| [docs/specs/](docs/specs/) | Technical specifications |
| [docs/adrs/](docs/adrs/) | Architecture Decision Records |
| [docs/architecture/](docs/architecture/) | System diagrams |
| [docs/agent-instructions/](docs/agent-instructions/) | AI agent protocols |

## For AI Agents

Before making changes, read:
1. [Agent Instructions](docs/agent-instructions/)
2. [Architecture Decisions](docs/adrs/)
3. [Technical Specs](docs/specs/)

## Contributing

1. Write/update specification in `docs/specs/`
2. Write tests alongside implementation
3. Run `./scripts/validate.sh`
4. Update documentation

## License

See [LICENSE](LICENSE) for details.
