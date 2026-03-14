"""Validate UMF JSON documents against the official schemas.

Example:
    python scripts/validate_recipe.py examples/recipe-example.json

The script loads `schemas/recipe.schema.json` by default and validates the
provided document.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver


def validate(json_path: Path, schema_path: Path) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    document = json.loads(json_path.read_text(encoding="utf-8"))

    resolver = RefResolver(base_uri=f"file://{schema_path.resolve()}", referrer=schema)
    validator = Draft202012Validator(schema, resolver=resolver)

    errors = sorted(validator.iter_errors(document), key=lambda e: e.path)
    if not errors:
        print("OK: Document is valid.")
        return

    print(f"ERROR: {len(errors)} validation error(s):")
    for err in errors:
        path = ".".join(str(p) for p in err.path) or "<root>"
        print(f"- {path}: {err.message}")
    raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a UMF JSON document against a schema.")
    parser.add_argument("document", type=Path, help="Path to the JSON document to validate")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schemas" / "recipe.schema.json",
        help="Schema to validate against",
    )

    args = parser.parse_args()

    validate(args.document, args.schema)


if __name__ == "__main__":
    main()
