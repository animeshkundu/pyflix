# Research & Web Access Protocol

AI agents have access to the internet and **MUST** use it to validate approaches, discover best practices, and avoid hallucinating APIs or patterns.

## Core Principle: Internet is First-Class

Web search is not optional—it is a required step in the development process. The internet provides:
- Current library versions and API documentation
- Community-validated best practices
- Security advisories and known issues
- Alternative approaches and trade-offs

## When to Search

### Always Search For:
1. **Library Usage**: Before using any library, verify the current API
2. **Version Compatibility**: Check compatible versions for dependencies
3. **Security Concerns**: Look for known vulnerabilities
4. **Best Practices**: Validate your approach against current standards
5. **Error Messages**: When encountering unfamiliar errors

### Search Triggers:
- Starting work on a new feature
- Using a library not recently validated
- Implementing security-sensitive code
- Encountering an error you don't immediately recognize
- Making architectural decisions

## Research Protocol

### Step 1: Identify What to Research
```
Before implementing [feature], I need to verify:
- [ ] Library [X] API for [functionality]
- [ ] Current best practice for [pattern]
- [ ] Security considerations for [area]
```

### Step 2: Conduct Research
Use web search with specific queries:
```
Good: "Python 3.11 asyncio best practices 2024"
Bad: "how to do async"

Good: "pytest-cov minimum coverage configuration"
Bad: "test coverage"

Good: "libtorrent-python streaming video API"
Bad: "torrent library"
```

### Step 3: Validate Information
- Cross-reference multiple sources
- Prefer official documentation
- Check dates—prefer recent information
- Verify with code examples when possible

### Step 4: Document Findings
Record research results in your work:
```python
# Per https://docs.python.org/3/library/asyncio-task.html
# Using asyncio.create_task() for concurrent operations
```

## Information Saturation

Continue researching until you reach **information saturation**:

### Signs of Saturation:
- Multiple sources agree on the approach
- You understand the trade-offs
- You can explain why alternatives were rejected
- Official documentation confirms your understanding

### Signs You Need More Research:
- Sources contradict each other
- You're unsure about edge cases
- Security implications are unclear
- You can't find recent information

## Validation Requirements

### Before Using Any Dependency:
```
1. Search: "[package name] latest version"
2. Search: "[package name] security vulnerabilities"
3. Search: "[package name] Python [version] compatibility"
4. Verify: Package is actively maintained (recent commits/releases)
```

### Before Implementing Patterns:
```
1. Search: "[pattern name] Python best practices [current year]"
2. Search: "[pattern name] pitfalls" or "[pattern name] anti-patterns"
3. Verify: Pattern is appropriate for use case
4. Document: Why this pattern was chosen
```

### Before Security-Sensitive Code:
```
1. Search: "[topic] security best practices"
2. Search: "[topic] OWASP guidelines"
3. Search: "[topic] common vulnerabilities"
4. Verify: Implementation follows security guidelines
```

## Hallucination Prevention

### DO NOT:
- Assume API signatures without verification
- Guess library behavior
- Invent configuration options
- Make up URL patterns or endpoints
- Assume default values

### DO:
- Verify every API call against documentation
- Test assumptions with minimal code
- Quote or link to sources
- Admit uncertainty and research further
- Ask for clarification when documentation is ambiguous

## Research Documentation

When research informs a decision, document it:

### In Code Comments:
```python
# Approach based on: https://realpython.com/python-logging/
# Alternative considered: structlog (rejected due to dependency constraints)
```

### In ADRs:
```markdown
## Research Summary
- Source 1: [link] - Key finding
- Source 2: [link] - Key finding
- Decision based on: [rationale]
```

### In Specs:
```markdown
## Technical Background
Based on research conducted [date]:
- Current best practice is X
- Library Y is recommended for Z
- Security consideration: W
```

## Search Query Templates

### For Python Libraries:
```
"[library] Python [version] documentation"
"[library] [feature] example"
"[library] changelog breaking changes"
```

### For Patterns:
```
"[pattern] Python implementation"
"[pattern] pros cons"
"when to use [pattern] vs [alternative]"
```

### For Debugging:
```
"[error message]" (exact match)
"[library] [error type] cause"
"[framework] [behavior] not working"
```

### For Security:
```
"[technology] security best practices [year]"
"[vulnerability type] prevention Python"
"[library] CVE"
```
