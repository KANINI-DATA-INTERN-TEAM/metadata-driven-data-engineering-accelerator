# Contributing

## Branch naming

- Exploration: `sandbox/<name>-prototype`
- Feature: `feature/<short-description>`
- Bug fix: `fix/<short-description>`
- Tests: `test/<short-description>`
- Documentation: `docs/<short-description>`

Examples: `feature/metadata-config`, `feature/bronze-ingestion`, `test/scd2-idempotency`.

## Rules

- Never commit directly to `main`.
- Keep PRs focused and explain what changed and how it was tested.
- Add tests for behavior changes.
- Do not commit credentials, tokens, local `.env` files, generated Delta tables, or non-approved data.
- Do not merge sandbox branches into `main`.
- PR authors must not approve their own PR.
- Reviewers should check correctness, tests, backward compatibility, and documentation.

## Pull request checklist

- [ ] Scope and behavior are described.
- [ ] Tests added/updated where appropriate.
- [ ] `pytest` passes locally.
- [ ] `ruff check .` passes locally.
- [ ] No secrets or unapproved data included.
- [ ] Documentation/config examples updated if needed.
