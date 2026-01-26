# Claude Agents Configuration

This directory contains specialized Claude agent configurations for the pyflix repository.

## Available Agents

### Code Editor Agent (`code-editor.md`)
Specialized for Python code editing with pyflix-specific conventions.

### Code Reviewer Agent (`reviewer.md`)
Reviews code changes for quality, security, and adherence to standards.

### Documentation Agent (`documenter.md`)
Maintains and generates documentation following the docs-first approach.

### Research Agent (`researcher.md`)
Conducts web research for libraries, best practices, and solutions.

## Usage

Claude automatically loads these configurations based on the task context. Each agent has specific expertise and follows the protocols defined in `docs/agent-instructions/`.

## Configuration Format

Each `.md` file contains:
- Agent identity and specialization
- Key responsibilities
- Pyflix-specific guidelines
- Integration with docs/

## Related Documentation

- See `docs/agent-instructions/` for shared protocols
- See `claude.md` in repository root for base configuration
