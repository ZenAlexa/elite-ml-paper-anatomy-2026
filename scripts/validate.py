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

MODULES = {
    "abstract",
    "introduction",
    "related_work",
    "method",
    "theory",
    "experimental_design",
    "results",
    "ablation",
    "conclusion",
    "limitations",
    "appendix",
    "other",
}


def iter_evidence(value: object):
    if isinstance(value, dict):
        if {"page", "section", "anchor", "basis"}.issubset(value):
            yield value
        for child in value.values():
            yield from iter_evidence(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_evidence(child)


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    catalog = {row["paper_id"]: row for row in papers}
    schema = json.loads((ROOT / "schemas" / "deep-read.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    ids = [row["paper_id"] for row in papers]
    if len(ids) != len(set(ids)):
        errors.append("duplicate paper_id in papers.csv")
    forums = [row["openreview_id"] for row in papers]
    if len(forums) != len(set(forums)):
        errors.append("duplicate OpenReview forum after hydration")
    sample_path = PROCESSED / "analysis_sample.csv"
    if sample_path.exists():
        sample = read_csv(sample_path)
        sample_ids = [row["paper_id"] for row in sample]
        if len(sample) != 400 or len(sample_ids) != len(set(sample_ids)):
            errors.append("analysis sample must contain 400 unique papers")
        unknown = sorted(set(sample_ids) - set(catalog))
        if unknown:
            errors.append(f"analysis sample contains unknown paper ids: {unknown}")
        expected_groups = {
            ("ICLR", "outstanding"): 2,
            ("ICLR", "oral"): 198,
            ("ICML", "outstanding"): 2,
            ("ICML", "oral"): 99,
            ("ICML", "spotlight"): 99,
        }
        actual_groups = {
            group: sum(
                row["conference"] == group[0] and row["analysis_stratum"] == group[1]
                for row in sample
            )
            for group in expected_groups
        }
        if actual_groups != expected_groups:
            errors.append(f"analysis sample group counts mismatch: {actual_groups}")
        expected_cohort_groups = {
            ("foundation_200", "ICLR", "outstanding"): 2,
            ("foundation_200", "ICLR", "oral"): 98,
            ("foundation_200", "ICML", "outstanding"): 2,
            ("foundation_200", "ICML", "oral"): 49,
            ("foundation_200", "ICML", "spotlight"): 49,
            ("replication_200", "ICLR", "oral"): 100,
            ("replication_200", "ICML", "oral"): 50,
            ("replication_200", "ICML", "spotlight"): 50,
        }
        actual_cohort_groups = {
            group: sum(
                row.get("sample_cohort") == group[0]
                and row["conference"] == group[1]
                and row["analysis_stratum"] == group[2]
                for row in sample
            )
            for group in expected_cohort_groups
        }
        if actual_cohort_groups != expected_cohort_groups:
            errors.append(f"analysis sample cohort counts mismatch: {actual_cohort_groups}")
        for sample_row in sample:
            source_path = ROOT / sample_row["source_path"]
            if not source_path.exists() or source_path.read_bytes()[:5] != b"%PDF-":
                errors.append(f"analysis sample source missing or invalid: {sample_row['paper_id']}")
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
            source_files = value.get("source_files", {})
            if str(source_files.get("pdf", "")).startswith("corpus/preprints/"):
                if source_files.get("source_kind") != "verified_preprint" or not source_files.get("source_url"):
                    errors.append(f"preprint reading source metadata incomplete: {row['paper_id']}")
            if not (ROOT / "readings" / f"{row['paper_id']}.md").exists():
                errors.append(f"reading Markdown missing: {row['paper_id']}")
            modules = [item.get("module") for item in value.get("module_metrics", [])]
            if set(modules) != MODULES or len(modules) != len(set(modules)):
                errors.append(
                    f"reading {row['paper_id']} must contain each semantic module exactly once"
                )
            coverage = value.get("evidence_coverage", {})
            if coverage.get("status") != "complete" or coverage.get("substantive_claims") != coverage.get(
                "claims_with_page_evidence"
            ):
                errors.append(f"reading {row['paper_id']} has incomplete evidence coverage")
            pdf_pages = value.get("page_map", {}).get("pdf_pages")
            if isinstance(pdf_pages, (int, float)):
                for evidence in iter_evidence(value):
                    if evidence["page"] > pdf_pages:
                        errors.append(
                            f"reading {row['paper_id']} evidence page {evidence['page']} exceeds PDF pages {pdf_pages}"
                        )
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
