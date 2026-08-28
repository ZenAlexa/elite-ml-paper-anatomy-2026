#!/usr/bin/env python3
"""Build the paper-level visual-audit index from schema-valid audits."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

import jsonschema

from common import PROCESSED, ROOT, load_complete_reading, read_csv


AUDIT_DIR = ROOT / "visual_audits"
OUTPUT_CSV = ROOT / "reports" / "tables" / "visual_audit_index.csv"
OUTPUT_MD = ROOT / "reports" / "visual_audit_index.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, default=250)
    parser.add_argument("--allow-partial", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    samples = [
        row
        for row in read_csv(PROCESSED / "analysis_sample.csv")
        if load_complete_reading(row["paper_id"]) is not None
    ]
    if len(samples) != args.target:
        raise SystemExit(f"expected {args.target} checkpoint papers; found {len(samples)}")
    metadata = {row["paper_id"]: row for row in read_csv(PROCESSED / "papers.csv")}
    schema = json.loads((ROOT / "schemas" / "visual-audit.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    rows: list[dict[str, object]] = []
    for sample in samples:
        paper_id = sample["paper_id"]
        path = AUDIT_DIR / f"{paper_id}.json"
        if not path.exists():
            continue
        audit = json.loads(path.read_text(encoding="utf-8"))
        validator.validate(audit)
        figures = audit["figures"]
        tables = audit["tables"]
        paper = metadata[paper_id]
        rows.append(
            {
                "paper_id": paper_id,
                "conference": sample["conference"],
                "analysis_stratum": sample["analysis_stratum"],
                "title": paper["title"],
                "figures": len(figures),
                "tables": len(tables),
                "main_visuals": sum(item["placement"] == "main" for item in figures + tables),
                "appendix_visuals": sum(item["placement"] == "appendix" for item in figures + tables),
                "source_status": audit["source_acquisition"]["status"],
                "selected_repository": audit["source_acquisition"]["selected_repository"] or "",
                "markdown": f"visual_audits/{paper_id}.md",
                "json": f"visual_audits/{paper_id}.json",
                "paper_url": paper["openreview_url"] or paper["official_event_url"],
            }
        )
    if not args.allow_partial and len(rows) != args.target:
        raise SystemExit(f"visual index requires {args.target} audits; found {len(rows)}")
    rows.sort(key=lambda row: (str(row["conference"]), str(row["analysis_stratum"]), str(row["title"])))
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]) if rows else ["paper_id"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        "# 250 篇论文视觉审计索引",
        "",
        "本索引连接逐篇 Figure/Table 深度审计、结构化 JSON、论文页面和公开视觉源码状态。",
        "",
        f"当前包含 **{len(rows)}** 篇论文。",
        "",
        "| 会议 | 层级 | 论文 | 图 | 表 | 正文对象 | 附录对象 | 视觉源码 |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        source = str(row["source_status"])
        repository = str(row["selected_repository"])
        if repository:
            repository_url = repository if repository.startswith(("http://", "https://")) else f"https://github.com/{repository}"
            repository_label = re.sub(r"^https?://github\.com/", "", repository).rstrip("/")
            source += f" · [{repository_label}]({repository_url})"
        lines.append(
            "| {conference} | {stratum} | [{title}](../{markdown}) | {figures} | {tables} | "
            "{main_visuals} | {appendix_visuals} | {source} |".format(
                conference=row["conference"],
                stratum=row["analysis_stratum"],
                title=str(row["title"]).replace("|", "\\|"),
                markdown=row["markdown"],
                figures=row["figures"],
                tables=row["tables"],
                main_visuals=row["main_visuals"],
                appendix_visuals=row["appendix_visuals"],
                source=source.replace("|", "\\|"),
            )
        )
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"papers": len(rows), "markdown": str(OUTPUT_MD.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
