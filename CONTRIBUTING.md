# Contributing to UMF

Thanks for your interest in contributing! This project aims to be a community-maintained reference implementation of the Ummi Markup Format (UMF) standard.

## ✅ How to contribute

1. **Fork the repository** and create a branch for your change.
2. **Run tests and validation** before submitting a PR.
3. **Open a Pull Request**, explaining your changes and why they are needed.

## 🧰 Development workflow

- Use `python -m venv .venv` and `pip install -r requirements.txt`.
- Run `python scripts/fetch_schemas.py` to sync the latest official schemas.
- Validate a sample document using the scripts in `scripts/`.

## 🧩 Schema changes

UMF is a schema-versioned standard. If you want to propose schema changes, update the JSON Schema artifacts in `schemas/` and document the reason in a pull request.

If your changes affect interoperability or require a new schema version, open an issue first to discuss the proposal.

## 📬 Reporting issues

Please open an issue if you:

- Find a discrepancy between the schema files and the official site
- Discover a bug in the validation scripts
- Have a suggestion for improving documentation or tooling

Thanks for helping make UMF better! 🙌
