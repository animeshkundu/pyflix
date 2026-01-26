# ADR 0001: AI-Enabled Repository Structure

## Status

Accepted

## Date

2026-01-26

## Context

The pyflix repository needed restructuring to support AI-driven development workflows (Agentic Coding). Multiple AI agents work on this codebase, and without clear protocols and documentation, they risk:
- Making inconsistent decisions
- Duplicating work
- Breaking existing functionality
- Not following established patterns

Key requirements identified:
1. Documentation must drive implementation (specs before code)
2. All architectural decisions must be traceable
3. AI agents need clear instructions and context
4. Validation must be automated and reliable
5. Multiple agents need coordination protocols

## Decision

We will structure the repository with the following documentation-driven approach:

### Documentation Hierarchy (`docs/`)
```
docs/
├── adrs/           # Architecture Decision Records (this document)
├── specs/          # Technical specifications (write BEFORE code)
├── architecture/   # System diagrams (Mermaid.js)
├── history/        # Handoffs and deprecated logic
└── agent-instructions/  # AI agent protocols
```

### Agent Configuration
- `.github/copilot-instructions.md` - GitHub Copilot context
- `claude.md` - Claude AI context
- `.github/instructions/` - Path-specific instructions
- `.claude/agents/` - Specialized agent configurations

### Automation
- `scripts/validate.sh` - Local validation (lint + test)
- `.github/workflows/ci.yml` - CI/CD pipeline
- `.github/workflows/pages.yml` - Website deployment

### Core Principles
1. **Docs = Code**: No implementation without specification
2. **Research First**: Validate approaches via web search
3. **Test Everything**: 90% minimum coverage
4. **Automate Repetition**: Script repeated tasks

## Consequences

### Positive

- Clear protocols for AI agents working on the codebase
- Traceable architectural decisions via ADRs
- Consistent code quality through automated validation
- Searchable history of changes and deprecations
- SEO-optimized public website for project visibility

### Negative

- Initial overhead to set up documentation structure
- Agents must read documentation before acting (added latency)
- Maintaining documentation requires discipline
- Some existing code lacks corresponding specifications

### Neutral

- Structure mirrors enterprise software practices
- Can be adapted as GitHub agent features evolve
- Website requires periodic content updates

## Related

- [Agent Instructions README](../agent-instructions/README.md)
- [Core Philosophy](../agent-instructions/00-core-philosophy.md)
- [Testing Protocol](../agent-instructions/02-testing-and-validation.md)
