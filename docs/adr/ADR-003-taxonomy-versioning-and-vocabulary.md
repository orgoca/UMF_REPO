# ADR-003: Taxonomy Versioning and Controlled Vocabulary Expansion

- Status: Accepted
- Date: 2026-03-14
- Owners: UMF maintainers

## Context

Deterministic dietary and category logic requires a stable controlled vocabulary.
UMF needs a versioned ingredient taxonomy artifact and explicit expansion rules.

## Decision

1. Standalone artifact.
   Ingredient taxonomy is maintained as a discrete versioned artifact:
   `taxonomy/ingredient-taxonomy.v<major>.<minor>.<patch>.json`

2. Baseline.
   Taxonomy v1.0.0 defines:
   - 18 top-level categories
   - 130 controlled leaf nodes

3. Recipe coupling.
   Recipe documents SHOULD declare `meta.taxonomy_version_used`.
   `ingredient_categories` values must be taxonomy leaf IDs.

4. Dietary presets.
   Named dietary presets are controlled in:
   `taxonomy/dietary-presets.v<major>.<minor>.<patch>.json`

5. Change policy.
   - Patch: typo/docs fixes, no semantic meaning changes.
   - Minor: additive leaf/category introduction, no removals.
   - Major: removals, renames, semantic reinterpretations.

6. Stability rule.
   Existing leaf IDs are immutable across minor/patch releases.
   Semantic reinterpretation of an existing leaf requires a major release.

## Consequences

- Dietary logic can be deterministic and reproducible.
- Taxonomy changes become auditable and release-bound.
- Implementers can pin taxonomy versions independently from schema versions.
