# UMF Specification

Canonical schemas and governance for the Ummi Markup Format (UMF).

UMF is an open, schema-versioned data standard for representing culinary knowledge as a typed knowledge graph.

## Repository Contract

This repository is the source of truth for UMF schemas and specification docs.

- `main` and tagged releases are canonical.
- `umfspec.org` is a publication target built from this repository.
- If the website and repository ever diverge, the repository wins.

## What Is In This Repository

- Canonical JSON Schema artifacts for all UMF entity types.
- Human-readable specification docs and governance notes.
- Example payloads for implementation guidance.
- Open-source project infrastructure for contribution and review.

## What Is Not In This Repository

- No schema scraping or sync scripts from the website.
- No generated artifacts that cannot be traced to commits and releases.
- No hidden canonical source outside git.

## Entity Coverage

UMF currently defines nine first-class entity schemas:

- `recipe`
- `ingredient`
- `technique`
- `chef`
- `collection`
- `menu`
- `product`
- `vendor`
- `service`

## UMF Knowledge Graph

```mermaid
%%{init: {"theme":"base"}}%%
flowchart LR
    MT["Meal Type"]
    CT["Cuisine Type"]
    Chef["Chef"]
    Recipe["Recipe"]
    Technique["Technique"]
    Ingredient["Ingredient"]
    Taxonomy["Taxonomy"]
    Collection["Collection"]
    Menu["Menu"]
    Product["Product"]
    Vendor["Vendor"]
    Service["Service"]

    MT -->|classifies| Recipe
    CT -->|classifies| Recipe
    Chef -->|creates| Recipe
    Recipe -->|uses| Technique
    Recipe -->|uses| Ingredient
    Ingredient -->|classified by| Taxonomy
    Recipe -->|grouped into| Collection
    Recipe -->|composed into| Menu
    Menu -->|executed by| Service
    Ingredient -->|instantiated as| Product
    Product -->|sold by| Vendor
    Vendor -->|sources from| Service

    classDef vocab fill:#6B4A2E,stroke:#C49A6C,stroke-width:1.5px,color:#FFFFFF;
    classDef people fill:#1F3A5F,stroke:#88A6D4,stroke-width:1.5px,color:#FFFFFF;
    classDef core fill:#2F6B3A,stroke:#8FCF99,stroke-width:1.8px,color:#FFFFFF;
    classDef method fill:#5F2E6B,stroke:#C79AD4,stroke-width:1.5px,color:#FFFFFF;
    classDef ingredient fill:#6A6B2E,stroke:#D3D48E,stroke-width:1.5px,color:#FFFFFF;
    classDef taxonomy fill:#6A6A6A,stroke:#BFBFBF,stroke-width:1.5px,color:#FFFFFF;
    classDef curation fill:#274A7A,stroke:#90B6E9,stroke-width:1.5px,color:#FFFFFF;
    classDef commercial fill:#2E6B3A,stroke:#8FD29D,stroke-width:1.5px,color:#FFFFFF;
    classDef vendor fill:#6B2E2E,stroke:#D49797,stroke-width:1.5px,color:#FFFFFF;
    classDef service fill:#5A2E6B,stroke:#C99BDA,stroke-width:1.5px,color:#FFFFFF;

    class MT,CT vocab;
    class Chef people;
    class Recipe core;
    class Technique method;
    class Ingredient ingredient;
    class Taxonomy taxonomy;
    class Collection,Menu curation;
    class Product commercial;
    class Vendor vendor;
    class Service service;

    linkStyle 0 stroke:#D19A3E,stroke-width:2px;
    linkStyle 1 stroke:#D19A3E,stroke-width:2px;
    linkStyle 2 stroke:#4A78D1,stroke-width:2px;
    linkStyle 3 stroke:#C07AE8,stroke-width:2px;
    linkStyle 4 stroke:#D2CF34,stroke-width:2px;
    linkStyle 5 stroke:#D3D3D3,stroke-width:2px;
    linkStyle 6 stroke:#2A5FFF,stroke-width:2px;
    linkStyle 7 stroke:#2A5FFF,stroke-width:2px;
    linkStyle 8 stroke:#D38CFF,stroke-width:2px;
    linkStyle 9 stroke:#66D96A,stroke-width:2px;
    linkStyle 10 stroke:#FF4A4A,stroke-width:2px;
    linkStyle 11 stroke:#D38CFF,stroke-width:2px;
```

## Repository Layout

- `schemas/`: Canonical JSON Schema files.
- `docs/`: Specification and governance documentation.
- `examples/`: Example UMF JSON documents.

Important references:

- Schema guide: [schemas/README.md](./schemas/README.md)
- Governance model: [docs/governance.md](./docs/governance.md)

## How To Use The Schemas

Use any JSON Schema Draft 2020-12 compatible validator in your runtime or CI pipeline.

Recommended consumption model:

1. Pin to a release tag.
2. Vendor or reference the schema files from that tag.
3. Validate producer and consumer payloads in CI.
4. Upgrade intentionally between schema versions.

## Change Model

All schema changes must flow through pull requests.

Required for schema PRs:

1. Clear rationale in the PR description.
2. Compatibility impact statement.
3. Example payload changes when behavior changes.
4. Documentation updates in `docs/` when semantics change.

## Versioning And Releases

UMF follows explicit schema versioning.

- Patch: editorial fixes or non-breaking clarifications.
- Minor: backwards-compatible additive schema changes.
- Major: breaking changes requiring migration.

Every released version should map to:

- A git tag.
- A stable schema set in `schemas/`.
- A matching website publication.

## Publication Policy

`umfspec.org` should publish from tagged releases of this repository.

Suggested publication pattern:

1. Merge approved PR into `main`.
2. Create release tag.
3. Publish site artifacts from that exact tag.
4. Keep versioned schema URLs immutable.

## Contributing

Contribution guide: [CONTRIBUTING.md](./CONTRIBUTING.md)

Code of conduct: [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

## License

Released under [CC BY 4.0](./LICENSE).
