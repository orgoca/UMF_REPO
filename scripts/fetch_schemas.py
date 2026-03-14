"""Fetch canonical UMF JSON Schema artifacts from umfspec.org.

This script downloads schema JSON payloads from direct endpoints
(e.g. https://umfspec.org/schemas/recipe.schema.json) and writes them
into `schemas/`.

Usage:
    python scripts/fetch_schemas.py

This is intended to keep this repository in sync with the official hosted
specification.
"""

from __future__ import annotations

import json
from pathlib import Path

import requests


SCHEMAS = [
    "recipe",
    "ingredient",
    "technique",
    "chef",
    "collection",
    "menu",
    "product",
    "vendor",
    "service",
]

BASE_URL = "https://umfspec.org/schemas"


def fetch_schema(schema_name: str, destination: Path) -> None:
    json_url = f"{BASE_URL}/{schema_name}.schema.json"
    page_url = f"{BASE_URL}/{schema_name}"

    print(f"Fetching {json_url}")
    resp = requests.get(json_url, timeout=30)

    # Fallback for legacy hosting layouts that may only serve schema pages.
    if resp.status_code == 404:
        print(f"Direct JSON not found, falling back to {page_url}")
        resp = requests.get(page_url, timeout=30)

    resp.raise_for_status()

    try:
        schema_obj = resp.json()
    except ValueError as exc:
        raise ValueError(f"Expected JSON from {resp.url}, but got non-JSON content") from exc

    destination.write_text(
        json.dumps(schema_obj, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {destination}")


def main() -> None:
    out_dir = Path(__file__).resolve().parent.parent / "schemas"

    out_dir.mkdir(parents=True, exist_ok=True)

    for name in SCHEMAS:
        dest = out_dir / f"{name}.schema.json"
        fetch_schema(name, dest)


if __name__ == "__main__":
    main()
