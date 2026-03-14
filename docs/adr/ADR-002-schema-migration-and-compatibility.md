# ADR-002: Schema Migration and Backward Compatibility

- Status: Accepted
- Date: 2026-03-14
- Owners: UMF maintainers

## Context

UMF historically used `formatVersion`.
Paper and downstream implementers use `schema_version`.
A compatibility strategy is required to avoid breaking existing producers/consumers.

## Decision

1. Canonical field name.
   `schema_version` is the canonical version identifier for new implementations.

2. Backward compatibility alias.
   `formatVersion` remains supported as a legacy alias for compatibility during migration.

3. Transitional acceptance.
   During the transition window, documents are valid if they contain either:
   - `schema_version`, or
   - `formatVersion`

4. SemVer policy.
   - Patch: clarifications and non-breaking fixes.
   - Minor: additive schema changes.
   - Major: breaking changes, including alias removals.

5. Deprecation path.
   Removal of `formatVersion` requires a major release and explicit migration guidance.

## Consequences

- Implementers can migrate without immediate breakage.
- Documentation and examples should prefer `schema_version`.
- CI and release notes must flag deprecation state clearly.
