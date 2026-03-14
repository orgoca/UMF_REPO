# UMF Specification (Docs)

This folder contains extracted documentation for the **Ummi Markup Format (UMF)**.

## Overview

UMF is an open, schema-versioned data standard that represents culinary knowledge as a **typed knowledge graph** rather than a flat document.

Key concepts include:

- **Nine entity types**: Recipe, Ingredient, Technique, Chef, Collection, Menu, Product, Vendor, Service
- **Provenance & Lineage**: Recipes and other entities form directed acyclic graphs capturing adaptation, variation, and translation relationships
- **Deterministic Dietary Logic**: Dietary filters are computed against a controlled ingredient taxonomy (not keyword heuristics)
- **Schema Governance**: Versioned schema artifacts and Architecture Decision Records (ADRs)

## How to Use

1. Fetch the latest schemas: `python scripts/fetch_schemas.py`
2. Validate documents against the schemas (see `scripts/validate_recipe.py`)
3. Read the full spec at https://umfspec.org/docs

## Additional Resources

- Website: https://umfspec.org/
- Schemas: https://umfspec.org/schemas
- Playground: https://umfspec.org/playground
- Contribution guidelines: [CONTRIBUTING.md](../CONTRIBUTING.md)
