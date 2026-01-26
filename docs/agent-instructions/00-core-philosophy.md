# Core Philosophy: Documentation-Driven Development

This document establishes the fundamental principles that govern all AI agent work on this codebase.

## The Prime Directive: Docs = Code

**Documentation is not an afterthought—it is the specification that drives implementation.**

### Principle 1: Specification First

No code is written without a corresponding specification in `docs/specs/`. This ensures:
- Clear understanding of requirements before implementation
- Traceable decisions
- Consistent behavior across agent sessions

**Process:**
```
1. Receive task
2. Check if specification exists in docs/specs/
3. If no spec exists → Create spec first → Get approval
4. If spec exists → Verify understanding → Implement
5. Update spec with any implementation learnings
```

### Principle 2: Sync Protocol

After completing any work:
1. Update relevant documentation to match implementation
2. Add entry to `docs/history/` documenting what was done
3. Update architecture diagrams if structure changed
4. Create handoff note if work is incomplete

**Never leave documentation out of sync with code.**

## The CEO Model: Agent Hierarchy

When multiple agents work on a codebase, one agent acts as the **CEO** (orchestrator) and others are **Workers**.

### CEO Agent Responsibilities
- Understand the overall task and break it into sub-tasks
- Assign work to worker agents with clear specifications
- Review and integrate worker output
- Ensure documentation consistency
- Make final decisions on conflicts

### Worker Agent Responsibilities
- Execute assigned tasks within defined scope
- Report blockers immediately
- Document decisions made during implementation
- Stay within specification boundaries
- Request CEO clarification when ambiguous

### Communication Protocol
```
CEO → Worker: Clear task specification + context
Worker → CEO: Implementation + documentation updates + blockers
CEO → Worker: Approval or revision request
```

## First Principles Reasoning

Before implementing any solution:

### Step 1: Understand the Problem
- What is the actual problem being solved?
- What are the constraints?
- What does success look like?

### Step 2: Research Existing Solutions
- Has this been solved before in this codebase?
- What are industry best practices?
- What are the trade-offs of different approaches?

### Step 3: Plan Before Coding
- Write pseudocode or outline the approach
- Identify edge cases
- Consider testing strategy
- Document assumptions

### Step 4: Implement Incrementally
- Start with the simplest working solution
- Add complexity only when necessary
- Test at each step
- Document as you go

### Step 5: Validate Thoroughly
- Run all tests
- Verify against specification
- Check for regressions
- Review documentation completeness

## Deep Thinking Requirements

For any non-trivial task, agents must demonstrate:

1. **Context Understanding**: Show awareness of how the change fits into the larger system
2. **Impact Analysis**: Identify what else might be affected
3. **Alternative Consideration**: Document at least one alternative approach considered
4. **Risk Assessment**: Identify potential issues or edge cases
5. **Rollback Plan**: Know how to undo the change if needed

## Documentation Maintenance

### When to Update Documentation
- Adding a new feature → Update specs, architecture
- Fixing a bug → Update spec if behavior changes
- Refactoring → Update architecture diagrams
- Deprecating code → Create history document
- Any breaking change → Create ADR

### Documentation Quality Standards
- Clear, concise language
- Code examples where helpful
- Links to related documents
- Current and accurate information
- Proper formatting (Markdown)

## Checklist Before Committing

- [ ] Specification exists and is up-to-date
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Architecture diagrams current
- [ ] ADR created if architectural decision made
- [ ] No hardcoded values without explanation
- [ ] Error handling implemented
- [ ] Logging appropriate for debugging
