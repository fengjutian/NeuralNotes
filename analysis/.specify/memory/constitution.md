# Python Project Constitution

## Core Principles

### I. PEP 8 Coding Standards (NON-NEGOTIABLE)
All code MUST adhere to PEP 8 guidelines, including:
- Indentation: 4 spaces per level
- Line length: Maximum 79 characters per line
- Naming conventions: snake_case for functions/variables, PascalCase for classes
- Import organization: standard library → third-party → local imports
- Whitespace rules: No trailing whitespace, blank lines between functions

### II. Type Annotations (NON-NEGOTIABLE)
Every function MUST include complete type hints:
- All function parameters MUST have type annotations
- Return types MUST be explicitly declared
- Use Union types where applicable (e.g., `Union[str, None]`)
- Complex types should use type aliases for readability
- Runtime type checking via `mypy --strict` must pass without errors

### III. Test-Driven Development (NON-NEGOTIABLE)
Core functionality MUST follow TDD principles:
- Tests written BEFORE implementation
- Red-Green-Refactor cycle strictly enforced
- Minimum 80% code coverage for all new code
- Test files named: `test_<module_name>.py`
- All tests must be isolated and independent

### IV. Virtual Environment Isolation
Development MUST use isolated environments:
- Use `venv` or `conda` for dependency management
- requirements.txt or pyproject.toml for dependency specification
- No system site-packages in production environments
- Dependencies version-pinned for reproducibility

### V. Documentation Standards
Comprehensive documentation is mandatory:
- Every public function MUST have a docstring (Google style)
- Module-level docstrings describing purpose and usage
- README.md with installation, usage, and examples
- Inline comments for complex logic only (code should be self-documenting)

## Additional Constraints

### Security Requirements
- No hardcoded credentials or API keys
- Environment variables for sensitive configuration
- Input validation on all user-facing functions
- Dependencies scanned for vulnerabilities (use `safety` or `pip-audit`)

### Performance Standards
- No blocking operations in async contexts
- Resource cleanup in finally blocks
- Efficient algorithms preferred (document trade-offs if suboptimal)
- Logging at appropriate levels (DEBUG, INFO, WARNING, ERROR)

## Development Workflow

### Code Review Process
- All PRs require at least one reviewer approval
- CI/CD pipeline must pass: linting, type-checking, tests
- Coverage report must not decrease below threshold
- Documentation updates for API changes

### Quality Gates
- Pre-commit hooks: flake8, mypy, pytest
- Branch protection: no direct commits to main
- Changelog maintained for each release
- Version bump follows Semantic Versioning (MAJOR.MINOR.PATCH)

## Governance

### Amendment Procedure
- Constitution changes require pull request with detailed rationale
- Breaking changes to principles require MAJOR version bump
- New principles can be added with MINOR version bump
- Clarifications and wording fixes are PATCH updates
- All changes must be documented in version history

### Compliance Requirements
- All code MUST pass linter before commit
- All tests MUST pass before merge
- Type checking MUST pass without errors
- Documentation MUST be updated alongside code changes
- Constitution supersedes all other development practices

**Version**: 1.0.0 | **Ratified**: 2025-07-19 | **Last Amended**: 2025-07-19
