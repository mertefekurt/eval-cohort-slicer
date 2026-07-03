from __future__ import annotations

import json

from eval_cohort_slicer.cli import main
from eval_cohort_slicer.core import field_value, render_json, render_table, slice_cohorts

RECORDS = [
    {"score": 1, "passed": True, "metadata": {"lang": "en"}},
    {"score": 0, "passed": False, "metadata": {"lang": "tr"}},
    {"score": 0.5, "passed": True, "metadata": {"lang": "tr"}},
]


def test_field_value_reads_metadata() -> None:
    assert field_value(RECORDS[0], "lang") == "en"


def test_slices_and_sorts_weakest_first() -> None:
    assert slice_cohorts(RECORDS, "lang")[0].name == "tr"


def test_min_cases_filter() -> None:
    assert [c.name for c in slice_cohorts(RECORDS, "lang", min_cases=2)] == ["tr"]


def test_table_header() -> None:
    assert render_table(slice_cohorts(RECORDS, "lang")).startswith("cohort")


def test_json_render() -> None:
    assert json.loads(render_json(slice_cohorts(RECORDS, "lang")))[0]["name"] == "tr"


def test_cli_help(capsys) -> None:
    try:
        main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0
    assert "cohort" in capsys.readouterr().out.lower()
