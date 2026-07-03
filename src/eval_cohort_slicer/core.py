from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Cohort:
    name: str
    cases: int
    pass_rate: float
    average_score: float


def load_results(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def field_value(record: dict, field: str) -> str:
    metadata = record.get("metadata", {})
    if isinstance(metadata, dict) and field in metadata:
        return str(metadata[field])
    return str(record.get(field, "unknown"))


def slice_cohorts(records: list[dict], field: str, min_cases: int = 1) -> list[Cohort]:
    buckets: dict[str, list[dict]] = {}
    for record in records:
        buckets.setdefault(field_value(record, field), []).append(record)
    cohorts: list[Cohort] = []
    for name, rows in buckets.items():
        if len(rows) < min_cases:
            continue
        passes = sum(1 for row in rows if bool(row.get("passed", False)))
        scores = [float(row.get("score", 0.0) or 0.0) for row in rows]
        cohorts.append(Cohort(name, len(rows), passes / len(rows), sum(scores) / len(scores)))
    return sorted(cohorts, key=lambda item: (item.pass_rate, item.average_score, item.name))


def render_table(cohorts: list[Cohort]) -> str:
    lines = ["cohort\tcases\tpass_rate\tavg_score"]
    for cohort in cohorts:
        lines.append(f"{cohort.name}\t{cohort.cases}\t{cohort.pass_rate:.2f}\t{cohort.average_score:.3f}")
    return "\n".join(lines) + "\n"


def render_json(cohorts: list[Cohort]) -> str:
    return json.dumps([asdict(cohort) for cohort in cohorts], indent=2)
