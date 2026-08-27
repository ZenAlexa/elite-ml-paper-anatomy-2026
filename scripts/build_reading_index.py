#!/usr/bin/env python3
from __future__ import annotations

from common import PROCESSED, ROOT, load_complete_reading, read_csv, write_csv


STRATUM_ORDER = {"outstanding": 0, "oral": 1, "spotlight": 2, "": 3}


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def build_rows() -> list[dict[str, object]]:
    papers = {row["paper_id"]: row for row in read_csv(PROCESSED / "papers.csv")}
    sample = {row["paper_id"]: row for row in read_csv(PROCESSED / "analysis_sample.csv")}
    rows: list[dict[str, object]] = []
    for path in sorted((ROOT / "readings").glob("*.json")):
        paper_id = path.stem
        reading = load_complete_reading(paper_id)
        if reading is None:
            continue
        bibliography = reading["bibliography"]
        source = reading["source_files"]
        sample_row = sample.get(paper_id)
        paper_row = papers.get(paper_id, {})
        selection_flags = bibliography.get("selection_flags", [])
        if isinstance(selection_flags, list):
            selection_flags = "|".join(str(value) for value in selection_flags)
        rows.append(
            {
                "paper_id": paper_id,
                "checkpoint_250": "yes" if sample_row is not None else "no",
                "conference": bibliography["conference"],
                "analysis_stratum": (
                    sample_row.get("analysis_stratum", "")
                    if sample_row
                    else paper_row.get("analysis_stratum", "")
                ),
                "sample_cohort": sample_row.get("sample_cohort", "extended") if sample_row else "extended",
                "title": bibliography["title"],
                "authors": "|".join(str(value) for value in bibliography.get("authors", [])),
                "selection_flags": selection_flags,
                "source_kind": source.get("source_kind", ""),
                "source_url": source.get("source_url", ""),
                "openreview_url": source.get("openreview_url", ""),
                "reading_markdown": f"readings/{paper_id}.md",
                "reading_json": f"readings/{paper_id}.json",
            }
        )
    rows.sort(
        key=lambda row: (
            str(row["checkpoint_250"]) != "yes",
            str(row["conference"]),
            STRATUM_ORDER.get(str(row["analysis_stratum"]), 3),
            str(row["title"]).casefold(),
        )
    )
    return rows


def render_table(rows: list[dict[str, object]]) -> list[str]:
    lines = [
        "| # | 论文 | 等级 | 队列 | 深读 | 数据 | 来源 |",
        "|---:|---|---|---|---|---|---|",
    ]
    for index, row in enumerate(rows, 1):
        paper_id = row["paper_id"]
        source_links = []
        if row["source_url"]:
            source_links.append(f"[PDF]({row['source_url']})")
        if row["openreview_url"]:
            source_links.append(f"[OpenReview]({row['openreview_url']})")
        lines.append(
            "| {index} | {title} | `{stratum}` | `{cohort}` | [MD](../readings/{paper_id}.md) | "
            "[JSON](../readings/{paper_id}.json) | {sources} |".format(
                index=index,
                title=markdown_escape(row["title"]),
                stratum=markdown_escape(row["analysis_stratum"]),
                cohort=markdown_escape(row["sample_cohort"]),
                paper_id=paper_id,
                sources=" · ".join(source_links),
            )
        )
    return lines


def render_markdown(rows: list[dict[str, object]]) -> str:
    checkpoint = [row for row in rows if row["checkpoint_250"] == "yes"]
    extended = [row for row in rows if row["checkpoint_250"] == "no"]
    conference_counts = {
        conference: sum(row["conference"] == conference for row in checkpoint)
        for conference in ("ICLR", "ICML")
    }
    lines = [
        "# 逐篇深读索引",
        "",
        "本页连接论文来源、中文深读备忘和结构化 JSON。250 篇统计总体包含 "
        f"ICLR {conference_counts['ICLR']} 篇与 ICML {conference_counts['ICML']} 篇；"
        f"另有 {len(extended)} 篇扩展阅读。统计总览见 "
        "[`statistical_analysis_250.md`](statistical_analysis_250.md)。",
        "",
        "CSV 索引位于 [`tables/reading_index.csv`](tables/reading_index.csv)。",
        "",
        "## 250 篇统计总体",
    ]
    for conference in ("ICLR", "ICML"):
        subset = [row for row in checkpoint if row["conference"] == conference]
        lines.extend(["", f"### {conference}（{len(subset)} 篇）", ""])
        lines.extend(render_table(subset))
    if extended:
        lines.extend(["", "## 扩展阅读", ""])
        lines.extend(render_table(extended))
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = build_rows()
    checkpoint_count = sum(row["checkpoint_250"] == "yes" for row in rows)
    if checkpoint_count != 250:
        raise SystemExit(f"expected 250 checkpoint readings; found {checkpoint_count}")
    fields = [
        "paper_id",
        "checkpoint_250",
        "conference",
        "analysis_stratum",
        "sample_cohort",
        "title",
        "authors",
        "selection_flags",
        "source_kind",
        "source_url",
        "openreview_url",
        "reading_markdown",
        "reading_json",
    ]
    write_csv(ROOT / "reports" / "tables" / "reading_index.csv", rows, fields)
    (ROOT / "reports" / "reading_index.md").write_text(render_markdown(rows), encoding="utf-8")
    print(f"indexed={len(rows)} checkpoint={checkpoint_count} extended={len(rows) - checkpoint_count}")


if __name__ == "__main__":
    main()
