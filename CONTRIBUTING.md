# Contributing To UMF

Thanks for contributing to the Ummi Markup Format (UMF).

This project treats the repository as canonical for schemas and specification docs.

## Ground Rules

- Schema and documentation changes happen by pull request only.
- Direct pushes to protected branches should be disabled.
- Every material change should be reviewable from git history alone.

## Contribution Flow

1. Fork the repository.
2. Create a feature branch.
3. Make focused changes.
4. Open a pull request with rationale and impact.

## Pull Request Expectations

Every PR should include:

1. Problem statement.
2. Proposed change.
3. Compatibility assessment.
4. Migration notes when applicable.
5. Documentation updates when semantics changed.

## Schema Change Checklist

For any file in `schemas/`:

1. Explain whether change is breaking, additive, or editorial.
2. Update examples if payload behavior changed.
3. Keep `$id` and versioning semantics coherent.
4. Confirm JSON remains valid and machine-readable.

## Versioning Guidance

Use semantic intent:

- Patch for non-breaking fixes and clarifications.
- Minor for additive, backwards-compatible changes.
- Major for breaking changes.

If uncertain, open an issue before implementing the change.

## Publication Alignment

The website should publish from repository tags.

If a discrepancy appears between `umfspec.org` and this repository:

1. Open an issue describing the mismatch.
2. Include the exact URLs, commit/tag, and observed behavior.
3. Propose whether to fix repo, site pipeline, or both.

## Reporting Issues

Open an issue for:

- Schema bugs.
- Ambiguous semantics.
- Documentation gaps.
- Release/versioning inconsistencies.

## Community Standards

By participating, you agree to the [Code of Conduct](./CODE_OF_CONDUCT.md).

## Licensing Of Contributions

By submitting a contribution, you agree that your contribution is licensed
under this repository's license model:

- Non-code specification content under [CC BY 4.0](./LICENSE).
- Software code under [MIT](./LICENSE-MIT).
