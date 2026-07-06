# Eval Cohort Slicer

Slice evaluation JSONL by a cohort field so weak segments do not disappear inside aggregate scores.

![Eval Cohort Slicer cover](assets/readme-cover.svg)

## Example

The sample data includes `metadata.language`; slice it to compare English and Turkish cases.

```bash
git clone https://github.com/mertefekurt/eval-cohort-slicer.git
cd eval-cohort-slicer
python -m pip install -e ".[dev]"
eval-cohort-slicer examples/eval.jsonl --by language
eval-cohort-slicer examples/eval.jsonl --by language --json
```

## Output idea

The table is meant for quick review; JSON is meant for notebooks, dashboards, or CI artifacts.
