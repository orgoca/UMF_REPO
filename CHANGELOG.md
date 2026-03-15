# Changelog

All notable changes to this repository are documented in this file.

## [Unreleased]

### Added

- ADR set:
  - ADR-001 canonical lineage promotion policy
  - ADR-002 schema migration/backward compatibility strategy
  - ADR-003 taxonomy versioning and controlled vocabulary rules
- Standalone taxonomy artifacts:
  - `taxonomy/ingredient-taxonomy.v1.0.0.json`
  - `taxonomy/dietary-presets.v1.0.0.json`
- Schema updates for governance and determinism:
  - `isCanonical` on lineage objects
  - `schema_version` migration path with `formatVersion` alias support
  - Controlled `ingredient_categories` vocabulary in `recipe.schema.json`
  - Controlled dietary preset vocabulary
- CI workflow to validate story examples against schemas.

### Changed

- Story examples updated to include schema version migration fields and taxonomy version linkage.
- `technique.schema.json` redesigned to pedagogy-first structure:
  - `meta` block with difficulty/category/timeEstimate
  - `purpose`, `prerequisites`, `equipment`
  - instructional `steps[]` with `sensory_cue`, `timing`, and `why`
  - first-class `failure_modes[]`, `sensory_checkpoints[]`, and `variations[]`
  - removal of recipe-only concerns from technique modeling (servings/plating/scaling semantics)
- Lineage relationship enum in `technique.schema.json` normalized to remove `adapted_from` and use `adaptation_of` consistently with other UMF schemas.

## [1.0.0] - 2026-03-14

### Added

- Initial canonical UMF repository baseline:
  - 9 entity schemas
  - Governance and contribution documentation
  - Cohesive, cross-linked story examples
