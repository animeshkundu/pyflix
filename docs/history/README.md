# History & Handoffs

This directory documents completed work, handoffs between agents/developers, and deprecated approaches. It serves as a historical record and prevents duplication of effort.

## Purpose

1. **Handoff Documentation**: Record context when work transitions between agents
2. **Deprecated Logic**: Explain why approaches were abandoned
3. **Learning Repository**: Document lessons learned
4. **Audit Trail**: Track who worked on what and when

## Document Types

### Handoff Notes
Created when:
- An agent completes a task that another agent will continue
- A developer hands off work to an AI agent
- Work is paused and will be resumed later

Template:
```markdown
# Handoff: [Task Name]

## Date: YYYY-MM-DD

## Author
[Agent/Developer name]

## Work Completed
- Item 1
- Item 2

## Work Remaining
- Item 1
- Item 2

## Context & Notes
Important information for the next person/agent.

## Files Modified
- `path/to/file.py`

## Open Questions
- Question 1?
```

### Deprecated Logic
Created when:
- An approach is abandoned in favor of a better solution
- Code is removed but the reasoning should be preserved
- A feature is sunset

Template:
```markdown
# Deprecated: [Feature/Approach Name]

## Date Deprecated: YYYY-MM-DD

## Original Purpose
What this was meant to do.

## Reason for Deprecation
Why we stopped using this approach.

## Replacement
What replaced it (if applicable).

## Related ADR
Link to ADR if one exists.
```

## For AI Agents

1. **Check history before starting new work** - similar work may have been attempted
2. **Create handoff notes** when completing partial work
3. **Document deprecated approaches** when removing code
4. **Link to history docs** in commits and PRs

## Index

| Document | Type | Date |
|----------|------|------|
| [2026-01-26-ai-scaffolding.md](./2026-01-26-ai-scaffolding.md) | Handoff | 2026-01-26 |
