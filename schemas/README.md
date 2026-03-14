# UMF Schemas

This directory contains the canonical UMF JSON Schemas.

## Contract

- Files in this folder are authoritative for the corresponding UMF release.
- Changes require pull request review.
- Tags define immutable snapshots for downstream consumers.

## Current Schemas

- `recipe.schema.json`
- `ingredient.schema.json`
- `technique.schema.json`
- `chef.schema.json`
- `collection.schema.json`
- `menu.schema.json`
- `product.schema.json`
- `vendor.schema.json`
- `service.schema.json`

## Consumer Guidance

1. Pin to a tagged release.
2. Validate payloads with a Draft 2020-12 compatible validator.
3. Treat major upgrades as migration events.

## Maintainer Guidance

When modifying a schema:

1. Keep intent explicit in PR notes.
2. Classify compatibility impact.
3. Update examples and docs when semantics change.
