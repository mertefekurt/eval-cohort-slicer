<p align="center">
  <img src="assets/readme-cover.svg" alt="Eval Cohort Slicer cover" width="100%" />
</p>

# Eval Cohort Slicer

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

Slice evaluation results by cohort and surface weak segments.

## Good for

- quick local checks around evaluation work
- small CI jobs where a readable report is enough
- review workflows that need deterministic output
- examples based on `examples/eval.jsonl`

## Run it

```bash
python -m pip install -e ".[dev]"
eval-cohort-slicer examples/eval.jsonl
```

## Project notes

- Command: `eval-cohort-slicer`
- Language: Python
- Python: `>=3.11`
- Tests: `pytest`

## Layout

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```

## Check locally

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m eval_cohort_slicer --help
```
