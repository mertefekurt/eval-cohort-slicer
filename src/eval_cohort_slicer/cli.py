from __future__ import annotations

import argparse
from pathlib import Path

from eval_cohort_slicer.core import load_results, render_json, render_table, slice_cohorts


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Slice eval results by cohort.")
    parser.add_argument("jsonl", type=Path)
    parser.add_argument("--by", required=True)
    parser.add_argument("--min-cases", type=int, default=1)
    parser.add_argument("--json", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cohorts = slice_cohorts(load_results(args.jsonl), args.by, args.min_cases)
    print(render_json(cohorts) if args.json else render_table(cohorts), end="")
    return 0
