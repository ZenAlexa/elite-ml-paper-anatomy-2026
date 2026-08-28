#!/usr/bin/env python3
"""Validate completed one-paper visual audits and report 250-paper coverage."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema

from common import PROCESSED, ROOT, load_complete_reading, read_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--target", type=int, default=250)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sample = read_csv(PROCESSED / "analysis_sample.csv")
    target_ids = [row["paper_id"] for row in sample if load_complete_reading(row["paper_id"]) is not None]
    if len(target_ids) != args.target:
        raise SystemExit(f"expected {args.target} complete checkpoint readings; found {len(target_ids)}")

    schema = json.loads((ROOT / "schemas" / "visual-audit.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    completed: list[str] = []
    figure_count = 0
    table_count = 0
    source_status: dict[str, int] = {}

    for paper_id in target_ids:
        json_path = ROOT / "visual_audits" / f"{paper_id}.json"
        markdown_path = ROOT / "visual_audits" / f"{paper_id}.md"
        if not json_path.exists() and not markdown_path.exists():
            continue
        if not json_path.exists() or not markdown_path.exists():
            errors.append(f"visual audit pair incomplete: {paper_id}")
            continue
        try:
            audit = json.loads(json_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid visual audit JSON {paper_id}: {exc}")
            continue
        if audit.get("paper_id") != paper_id:
            errors.append(f"visual audit paper_id mismatch: {paper_id}")
        for issue in validator.iter_errors(audit):
            location = ".".join(str(part) for part in issue.absolute_path) or "<root>"
            errors.append(f"visual audit schema error {paper_id} at {location}: {issue.message}")
        objects = [*audit.get("figures", []), *audit.get("tables", [])]
        identities = [(item.get("label"), item.get("page")) for item in objects]
        if len(identities) != len(set(identities)):
            errors.append(f"duplicate visual object label/page: {paper_id}")
        for item in objects:
            caption = item.get("caption", {})
            if not caption.get("text") and (
                caption.get("word_count") != 0
                or caption.get("moves")
                or caption.get("headline_bold")
                or caption.get("self_contained")
                or caption.get("main_finding_stated")
            ):
                errors.append(f"uncaptioned visual has nonempty caption metadata: {paper_id} {item.get('label')}")
        if any(not item.get("evidence_relation") for item in objects):
            errors.append(f"empty visual evidence relation: {paper_id}")
        style = audit.get("paper_style", {})
        figures = audit.get("figures", [])
        tables = audit.get("tables", [])
        expected_figures = int(style.get("main_figures", 0)) + int(style.get("appendix_figures", 0))
        expected_tables = int(style.get("main_tables", 0)) + int(style.get("appendix_tables", 0))
        if expected_figures != len(figures):
            errors.append(f"figure total mismatch {paper_id}: style={expected_figures}, objects={len(figures)}")
        if expected_tables != len(tables):
            errors.append(f"table total mismatch {paper_id}: style={expected_tables}, objects={len(tables)}")
        completed.append(paper_id)
        figure_count += len(figures)
        table_count += len(tables)
        status = str(audit.get("source_acquisition", {}).get("status", "missing"))
        source_status[status] = source_status.get(status, 0) + 1

    if args.require_complete and len(completed) != args.target:
        errors.append(f"complete visual-audit checkpoint requires {args.target}; found {len(completed)}")
    result = {
        "target_papers": args.target,
        "completed_visual_audits": len(completed),
        "remaining_visual_audits": args.target - len(completed),
        "audited_figures": figure_count,
        "audited_tables": table_count,
        "source_status": dict(sorted(source_status.items())),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
