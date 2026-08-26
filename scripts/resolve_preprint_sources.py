#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

from common import PROCESSED, RAW, read_csv, write_csv, write_json

DATASET = "ai-conferences/ICML2026"
ROWS_API = "https://datasets-server.huggingface.co/rows"
FIELDS = [
    "paper_id",
    "conference",
    "openreview_id",
    "title",
    "arxiv_id",
    "preprint_url",
    "locator_source",
    "locator_method",
    "version_status",
]


def fetch_rows(refresh: bool) -> list[dict[str, object]]:
    snapshot = RAW / "icml_2026_secondary_arxiv_locator.json"
    if snapshot.exists() and not refresh:
        return json.loads(snapshot.read_text(encoding="utf-8"))

    rows: list[dict[str, object]] = []
    offset = 0
    page_size = 100
    total = None
    while total is None or offset < total:
        query = urllib.parse.urlencode(
            {
                "dataset": DATASET,
                "config": "default",
                "split": "train",
                "offset": offset,
                "length": page_size,
            }
        )
        request = urllib.request.Request(
            f"{ROWS_API}?{query}",
            headers={"User-Agent": "elite-ml-paper-anatomy-2026/1.0"},
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            page = json.load(response)
        total = int(page["num_rows_total"])
        batch = [entry["row"] for entry in page["rows"]]
        rows.extend(batch)
        offset += len(batch)
        if not batch:
            break
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    snapshot.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resolve provisional arXiv locators without replacing official conference PDF URLs."
    )
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()

    catalog = [row for row in read_csv(PROCESSED / "papers.csv") if row["conference"] == "ICML"]
    secondary = {str(row["paper_id"]): row for row in fetch_rows(args.refresh)}
    resolved: list[dict[str, object]] = []
    failures: dict[str, str] = {}
    for paper in catalog:
        match = secondary.get(paper["openreview_id"])
        arxiv_id = str(match.get("arxiv_id") or "").strip() if match else ""
        if not arxiv_id:
            failures[paper["paper_id"]] = "no arXiv id in secondary OpenReview-id locator"
            continue
        resolved.append(
            {
                "paper_id": paper["paper_id"],
                "conference": paper["conference"],
                "openreview_id": paper["openreview_id"],
                "title": paper["title"],
                "arxiv_id": arxiv_id,
                "preprint_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "locator_source": f"https://huggingface.co/datasets/{DATASET}",
                "locator_method": str(match.get("arxiv_id_source") or "unspecified"),
                "version_status": "provisional_preprint_not_official_camera_ready",
            }
        )
    write_csv(PROCESSED / "preprint_sources.csv", resolved, FIELDS)
    write_json(PROCESSED / "preprint_source_failures.json", failures)
    print(f"resolved={len(resolved)}/{len(catalog)} failures={len(failures)}")


if __name__ == "__main__":
    main()
