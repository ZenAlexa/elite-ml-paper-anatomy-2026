#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from common import PDFS, PROCESSED, ROOT, read_csv

READING_KEYS = {
    "schema_version",
    "paper_id",
    "bibliography",
    "source_files",
    "page_map",
    "module_metrics",
    "abstract_sentences",
    "visual_inventory",
    "equation_theory_inventory",
    "experimental_design",
    "claim_closure",
    "appendix_inventory",
    "limitations",
    "final_judgment",
    "evidence_coverage",
}


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    schema = json.loads((ROOT / "schemas" / "deep-read.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    ids = [row["paper_id"] for row in papers]
    if len(ids) != len(set(ids)):
        errors.append("duplicate paper_id in papers.csv")
    forums = [row["openreview_id"] for row in papers]
    if len(forums) != len(set(forums)):
        errors.append("duplicate OpenReview forum after hydration")
    for row in papers:
        if row["pdf_status"] == "verified":
            path = ROOT / row["pdf_path"]
            if not path.exists() or path.read_bytes()[:5] != b"%PDF-":
                errors.append(f"verified PDF missing or invalid: {row['paper_id']}")
        reading = ROOT / "readings" / f"{row['paper_id']}.json"
        if reading.exists():
            try:
                value = json.loads(reading.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid reading JSON {row['paper_id']}: {exc}")
                continue
            missing = READING_KEYS - set(value)
            if missing:
                errors.append(f"reading {row['paper_id']} missing keys: {sorted(missing)}")
            if value.get("paper_id") != row["paper_id"]:
                errors.append(f"reading paper_id mismatch: {row['paper_id']}")
            if not (ROOT / "readings" / f"{row['paper_id']}.md").exists():
                errors.append(f"reading Markdown missing: {row['paper_id']}")
            for issue in validator.iter_errors(value):
                location = ".".join(str(part) for part in issue.absolute_path) or "<root>"
                errors.append(f"reading schema error {row['paper_id']} at {location}: {issue.message}")
    print(
        json.dumps(
            {
                "papers": len(papers),
                "verified_pdfs": sum(row["pdf_status"] == "verified" for row in papers),
                "completed_readings": sum(
                    (ROOT / "readings" / f"{row['paper_id']}.json").exists()
                    and (ROOT / "readings" / f"{row['paper_id']}.md").exists()
                    for row in papers
                ),
                "errors": errors,
            },
            indent=2,
        )
    )
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
