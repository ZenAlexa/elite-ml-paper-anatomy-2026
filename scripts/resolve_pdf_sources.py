#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path

from common import FIELDS, PROCESSED, RAW, clean_html, fetch, normalize_title, read_csv, write_csv, write_json

ICLR_INDEX = "https://proceedings.iclr.cc/paper_files/paper/2026"
ICML_HASH_INDEX = (
    "https://huggingface.co/datasets/Drbellamy/icml-2026/resolve/main/data/papers.csv?download=true"
)


def iclr_urls(path: Path) -> dict[str, str]:
    page = path.read_text(encoding="utf-8")
    output: dict[str, str] = {}
    for match in re.finditer(
        r'href="/paper_files/paper/2026/hash/([0-9a-f]+)-Abstract-Conference\.html">(.*?)</a>',
        page,
        flags=re.I | re.S,
    ):
        title = clean_html(match.group(2))
        digest = match.group(1)
        output[normalize_title(title)] = (
            f"https://proceedings.iclr.cc/paper_files/paper/2026/file/{digest}-Paper-Conference.pdf"
        )
    return output


def icml_urls(path: Path) -> dict[str, str]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        return {
            row["openreview"].split("id=", 1)[1]: row["pdf"]
            for row in rows
            if row.get("track") == "main_conference"
            and row.get("openreview", "").startswith("https://openreview.net/forum?id=")
            and row.get("pdf", "").startswith("https://openreview.net/pdf/")
        }


def main() -> None:
    iclr_path = fetch(ICLR_INDEX, RAW / "iclr_proceedings_2026.html")
    icml_path = fetch(ICML_HASH_INDEX, RAW / "icml_2026_hf_paper_index.csv")
    by_title = iclr_urls(iclr_path)
    by_forum = icml_urls(icml_path)
    rows = read_csv(PROCESSED / "papers.csv")
    failures: dict[str, str] = {}
    for row in rows:
        if row["conference"] == "ICLR":
            url = by_title.get(normalize_title(row["title"]))
            source_type = "iclr_official_proceedings"
        else:
            url = by_forum.get(row["openreview_id"])
            source_type = "openreview_content_hash"
        if not url:
            failures[row["paper_id"]] = "no exact proceedings/content-hash PDF mapping"
            continue
        row["pdf_url"] = url
        row["pdf_source_type"] = source_type
    write_csv(PROCESSED / "papers.csv", rows, FIELDS)
    write_json(PROCESSED / "pdf_source_resolution_failures.json", failures)
    print(f"resolved={len(rows) - len(failures)}/{len(rows)} failures={len(failures)}")
    if failures:
        raise SystemExit("PDF source mapping is incomplete")


if __name__ == "__main__":
    main()
