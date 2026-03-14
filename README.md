# Ummi Markup Format (UMF) — Specification Repository

This repository captures the **Ummi Markup Format (UMF)** specification as a self-contained, professional-grade reference implementation.

UMF is an **open, schema-versioned data standard** for representing culinary knowledge as a **typed knowledge graph**, not a document.

## 📌 What’s Included

- ✅ **JSON Schema artifacts** for UMF entity types (recipes, ingredients, techniques, etc.)
- ✅ **Documentation** extracted from https://umfspec.org/
- ✅ Scripts to **fetch / refresh** the schema artifacts directly from the live website
- ✅ Standard open-source repository infrastructure (LICENSE, CONTRIBUTING, CI templates)

## 🚀 Getting Started

### 1) Install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Fetch the latest schemas from https://umfspec.org

```bash
python scripts/fetch_schemas.py
```

This will populate `schemas/` with the canonical JSON Schema definitions.

### 3) Validate example documents

```bash
python scripts/validate_recipe.py examples/recipe-example.json
```

## 🗂 Project Layout

- `schemas/` — Canonical UMF JSON Schema files
- `docs/` — Spec documentation extracted from umfspec.org
- `scripts/` — Helpers & tooling (schema fetching, validation)

## � UMF Knowledge Graph (ERD)

```mermaid
flowchart TD
    %% ── Controlled Vocabulary nodes ──
    MT([meal_type])
    CT([cuisine_type])

    %% ── Knowledge Layer ──
    subgraph KNOWLEDGE["KNOWLEDGE LAYER"]
        MT
        CT
        Chef
        Recipe
        Technique
        Ingredient
        Taxonomy
    end

    %% ── Curation Layer ──
    subgraph CURATION["CURATION LAYER"]
        Collection
        Menu
    end

    %% ── Commercial Layer ──
    subgraph COMMERCIAL["COMMERCIAL LAYER"]
        Service
        Product
        Vendor
    end

    %% ── Knowledge edges ──
    MT -->|classifies| Recipe
    CT -->|classifies| Recipe
    Chef -->|creates| Recipe
    Recipe -->|uses| Technique
    Recipe -->|uses| Ingredient
    Ingredient -->|classified by| Taxonomy

    %% ── Knowledge → Curation ──
    Recipe -->|grouped into| Collection
    Recipe -->|composed into| Menu

    %% ── Curation → Commercial ──
    Menu -->|executed by| Service

    %% ── Knowledge → Commercial ──
    Ingredient -->|instantiated as| Product

    %% ── Commercial edges ──
    Product -->|sold by| Vendor
    Vendor -->|sources from| Service
```

## �🔖 License

This repo is released under **CC BY 4.0** (same as the original UMF spec).

---

📌 This repository is intended as a canonical, community-friendly home for the UMF standard.
If you want to propose changes, please open an issue or a pull request.
