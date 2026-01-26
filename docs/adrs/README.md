# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) that document significant technical and architectural decisions made in the pyflix project.

## What is an ADR?

An ADR is a short document that captures:
- **Context**: The circumstances and constraints that led to the decision
- **Decision**: The specific choice that was made
- **Consequences**: The resulting impact, both positive and negative

## How to Use ADRs

### For Developers
1. Before making a significant architectural decision, check existing ADRs
2. If no relevant ADR exists, create one using the [template](./0000-template.md)
3. ADRs are **immutable** once accepted - create a new ADR to supersede an old one

### For AI Agents
1. **Always** check ADRs before proposing architectural changes
2. Reference relevant ADR numbers in commits and PR descriptions
3. Create new ADRs when introducing significant changes
4. Never modify existing ADRs - create superseding records instead

## ADR Status Lifecycle

- **Proposed**: Under discussion, not yet accepted
- **Accepted**: Decision is final and should be followed
- **Deprecated**: Replaced by a newer ADR (link to successor)
- **Superseded**: Fully replaced (link to successor)

## File Naming Convention

```
NNNN-short-title.md
```

Where `NNNN` is a 4-digit sequence number (e.g., `0001-use-python-3.md`).

## Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0000](./0000-template.md) | ADR Template | Template | - |
| [0001](./0001-ai-enabled-structure.md) | AI-Enabled Repository Structure | Accepted | 2026-01-26 |
