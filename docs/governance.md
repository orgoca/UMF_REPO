# UMF Governance

This document defines how the UMF specification evolves.

## Canonical Source

The canonical source for UMF is this git repository.

- Schema truth lives in `schemas/`.
- Behavioral and process truth lives in `docs/`.
- Published website assets must be generated from repository releases.

## Decision Process

Changes are proposed through issues and pull requests.

Expected process:

1. Problem framing.
2. Proposed schema or semantics change.
3. Compatibility review.
4. Maintainer approval.
5. Release tagging and publication.

## Compatibility Rules

- Backwards-compatible additions target a minor release.
- Breaking changes target a major release.
- Editorial clarifications target a patch release.

Any ambiguity should be resolved in favor of explicit migration guidance.

## Release Discipline

Each release should include:

- Immutable git tag.
- Complete schema set in `schemas/`.
- Documentation updates needed to interpret that release.
- Publication to `umfspec.org` from the same tag.

## Conflict Resolution

If website behavior disagrees with repository artifacts:

1. Treat repository artifacts as authoritative.
2. File an issue describing the mismatch.
3. Correct publication pipeline and regenerate site content.
