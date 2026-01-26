# GitHub Agents & Instructions Configuration

This directory contains GitHub Copilot agent configurations and custom instructions for the pyflix repository.

## Directory Structure

```
.github/
├── agents/                    # Agent-specific configurations (placeholder)
├── instructions/              # Path-specific instruction files
│   ├── python-code.instructions.md
│   ├── testing.instructions.md
│   ├── documentation.instructions.md
│   └── cicd.instructions.md
├── copilot-instructions.md    # Repository-wide Copilot instructions
└── workflows/                 # GitHub Actions workflows
```

## Custom Instructions

### Path-Specific Instructions

| File | Applies To | Purpose |
|------|-----------|---------|
| `python-code.instructions.md` | `torrent/**/*.py`, `utils/**/*.py` | Python coding standards |
| `testing.instructions.md` | `tests/**/*.py` | Testing guidelines |
| `documentation.instructions.md` | `docs/**/*.md`, `*.md` | Documentation standards |
| `cicd.instructions.md` | `.github/workflows/**`, `scripts/**` | CI/CD best practices |

### Repository-Wide Instructions

The `copilot-instructions.md` file provides general guidance for all Copilot interactions, including:
- Technology stack overview
- Core development principles
- Workflow requirements
- Code style guidelines

## Agent Configurations (Future)

When GitHub releases native agent configuration support, this directory will contain:
- Agent definitions with specific capabilities
- Workflow triggers for automated tasks
- Permission configurations
- Custom agent behaviors

## Related Documentation

- See `docs/agent-instructions/` for detailed agent protocols
- See `.claude/agents/` for Claude-specific configurations
- See `copilot-instructions.md` for base Copilot instructions
