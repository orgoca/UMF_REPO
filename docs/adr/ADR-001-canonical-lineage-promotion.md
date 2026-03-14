# ADR-001: Canonical Lineage Promotion Policy

- Status: Accepted
- Date: 2026-03-14
- Owners: UMF maintainers

## Context

UMF lineage edges encode provenance between variants (`derived_from`, `adaptation_of`, `translation_of`, etc.).
Implementations need a deterministic way to distinguish ordinary provenance from canonical lineage assertions.

## Decision

1. Canonical lineage is explicit.
   Canonical status is represented by `isCanonical: true` on a lineage edge.

2. Presence of a lineage edge alone is not canonical.
   Implementations MUST NOT infer canonical status from edge presence.

3. Promotion window.
   A lineage edge is eligible for canonical promotion after a 14-day public review window with no unresolved governance objections.

4. Promotion authority.
   Only maintainers (or delegated governance role) may set `isCanonical: true`.

5. Co-occurrence rules.
   - At most one lineage relationship per `(source, target)` pair.
   - If both `translation_of` and `adaptation_of` could apply to the same source, `translation_of` takes precedence.

## Consequences

- Canonical assertions are reviewable and auditable.
- Tooling can compute canonical graphs deterministically.
- Implementations must preserve `isCanonical` semantics when transforming documents.

## Compliance Notes

- Schemas include optional `isCanonical` on lineage edge objects.
- Validation beyond JSON Schema (pair uniqueness and precedence) should be enforced by CI/policy checks.
