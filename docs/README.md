# Documentation Hub

This `docs/` folder is the **central knowledge base** for the pyflix repository. All agents and developers must reference and maintain this documentation as the source of truth.

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| [`adrs/`](./adrs/) | Architecture Decision Records - Historical context for all major technical decisions |
| [`specs/`](./specs/) | Technical Specifications - Detailed requirements that must be written **before** code |
| [`architecture/`](./architecture/) | System Diagrams & High-Level Design - Visual representations using Mermaid.js |
| [`history/`](./history/) | Handoffs & Deprecated Logic - Record of completed work and deprecated approaches |
| [`agent-instructions/`](./agent-instructions/) | AI Agent Protocols - Instructions for AI agents working on this codebase |

## Key Principles

1. **Documentation First**: No code changes without corresponding documentation updates
2. **Specs Before Code**: Technical specifications must be written and reviewed before implementation
3. **Decision Traceability**: All architectural decisions are recorded with context and rationale
4. **Living Documentation**: Keep docs in sync with the codebase at all times

## For AI Agents

Before making any changes:
1. Read the relevant specification in `specs/`
2. Check `adrs/` for past decisions that may affect your work
3. Follow protocols in `agent-instructions/`
4. Update documentation as you work
