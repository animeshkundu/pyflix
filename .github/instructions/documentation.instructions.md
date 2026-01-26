---
applyTo:
  - "docs/**/*.md"
  - "*.md"
  - "**/*.md"
excludeAgent:
  - code-review
---

# Documentation Agent Instructions

You are maintaining documentation for the pyflix Python library.

## Documentation Structure
- `docs/adrs/` - Architecture Decision Records
- `docs/specs/` - Technical Specifications
- `docs/architecture/` - System diagrams (Mermaid.js)
- `docs/history/` - Handoffs and deprecated logic
- `docs/agent-instructions/` - AI agent protocols

## Documentation Principles
1. **Docs = Code**: Documentation drives implementation
2. **Spec First**: Write specifications before code
3. **Keep Updated**: Sync docs with code changes
4. **Use Mermaid**: For all diagrams (version-controlled, GitHub-rendered)

## Markdown Style
- Use ATX-style headers (`#`, `##`, `###`)
- Use fenced code blocks with language hints
- Add alt-text to images
- Use relative links for internal references

## ADR Format
```markdown
# ADR NNNN: [Title]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Date
YYYY-MM-DD

## Context
[Problem description]

## Decision
[What was decided]

## Consequences
### Positive
- ...
### Negative
- ...
```

## Specification Format
```markdown
# Feature: [Name]

## Overview
[High-level description]

## Requirements
- REQ-1: ...
- REQ-2: ...

## API
[Interface details]

## Examples
[Usage examples]

## Testing Strategy
[How to verify]
```
