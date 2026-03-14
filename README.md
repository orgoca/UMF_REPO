# UMF Specification

Ummi Markup Format (UMF) is an open, schema-versioned standard for representing culinary knowledge as a typed knowledge graph.

UMF is designed for builders who need recipe data that is interoperable, testable, and reusable across products.

## Why UMF Exists

Most recipe formats are document-like and hard to compose across systems.

UMF treats culinary knowledge as structured entities and relationships so teams can:

- Share data between apps without brittle transformations.
- Track provenance, adaptations, and lineage explicitly.
- Build deterministic dietary and taxonomy logic.
- Evolve models through versioned schemas instead of ad hoc payload drift.

## Core Model

UMF currently defines nine first-class entities:

- `recipe`
- `ingredient`
- `technique`
- `chef`
- `collection`
- `menu`
- `product`
- `vendor`
- `service`

Relationships between these entities encode how culinary knowledge is created, organized, and operationalized.

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

## Example Payload

See [examples/recipe-example.json](./examples/recipe-example.json) for a reference document.

## How To Adopt UMF

1. Choose a release tag.
2. Use schemas from `schemas/` for that tag.
3. Validate producer and consumer payloads in CI with a Draft 2020-12 compatible validator.
4. Upgrade intentionally between schema versions.

## Versioning

UMF uses semantic intent:

- Patch: editorial/non-breaking fixes.
- Minor: backwards-compatible additions.
- Major: breaking changes with migration impact.

## Repository Layout

- `schemas/`: JSON Schema artifacts.
- `docs/`: specification and governance docs.
- `examples/`: sample UMF documents.

## Contributing

- Contribution guide: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Governance: [docs/governance.md](./docs/governance.md)
- Code of conduct: [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

## License

Released under [CC BY 4.0](./LICENSE).
