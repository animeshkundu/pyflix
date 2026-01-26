# Agent Instructions

This directory contains protocols and guidelines that AI agents **MUST** follow when working on the pyflix codebase. These instructions ensure consistent, high-quality contributions.

## Required Reading

Before performing any work on this repository, agents must read the following files **in order**:

| Order | File | Purpose |
|-------|------|---------|
| 1 | [00-core-philosophy.md](./00-core-philosophy.md) | Fundamental principles and working model |
| 2 | [01-research-and-web.md](./01-research-and-web.md) | Research requirements and validation |
| 3 | [02-testing-and-validation.md](./02-testing-and-validation.md) | Testing standards and coverage requirements |
| 4 | [03-tooling-and-pipelines.md](./03-tooling-and-pipelines.md) | CI/CD and automation requirements |

## Quick Reference

### Before Writing Code
- [ ] Read relevant specification in `docs/specs/`
- [ ] Check `docs/adrs/` for related decisions
- [ ] Search the web for current best practices
- [ ] Write or update specification if needed

### While Writing Code
- [ ] Write tests alongside implementation
- [ ] Follow existing code patterns
- [ ] Run `./scripts/validate.sh` frequently
- [ ] Document significant decisions

### After Writing Code
- [ ] Ensure 90%+ test coverage
- [ ] Update relevant documentation
- [ ] Create handoff note if work is incomplete
- [ ] Update `docs/history/` if deprecating code

## Key Principles Summary

1. **Docs = Code**: Documentation drives implementation
2. **Research First**: Validate approaches before coding
3. **Test Everything**: Minimum 90% coverage
4. **Automate Repetition**: Script any repeated task
5. **Trace Decisions**: Record all significant choices
