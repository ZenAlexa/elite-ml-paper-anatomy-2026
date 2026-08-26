#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import concurrent.futures
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

from common import FIELDS, PROCESSED, RAW, clean_html, read_csv, write_csv, write_json


def retrieve(url: str, attempts: int = 4) -> str:
    error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "elite-ml-paper-anatomy-2026/1.0", "Accept": "text/html,*/*"},
            )
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.read().decode("utf-8", errors="replace")
        except Exception as exc:
            error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"failed to retrieve {url}: {error}")


def hydrate(row: dict[str, str], refresh: bool) -> tuple[str, dict[str, str] | None, str | None]:
    cache = RAW / "paper_pages" / f"{row['paper_id']}.html"
    try:
        if refresh or not cache.exists():
            page = retrieve(row["official_event_url"])
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(page, encoding="utf-8")
        else:
            page = cache.read_text(encoding="utf-8")
        match = re.search(r'https://openreview\.net/forum\?id=([A-Za-z0-9_-]+)', page)
        if not match:
            return row["paper_id"], None, "official event page has no OpenReview forum link"
        forum_id = match.group(1)
        abstract_match = re.search(
            r'<div class="abstract-text-inner">(.*?)</div>', page, flags=re.I | re.S
        )
        hydrated = dict(row)
        hydrated["openreview_id"] = forum_id
        hydrated["openreview_url"] = f"https://openreview.net/forum?id={forum_id}"
        hydrated["pdf_url"] = f"https://openreview.net/pdf?id={forum_id}"
        hydrated["pdf_source_type"] = "openreview_forum_endpoint"
        hydrated["pdf_path"] = f"corpus/pdfs/{row['paper_id']}.pdf"
        hydrated["abstract"] = clean_html(abstract_match.group(1)) if abstract_match else ""
        return row["paper_id"], hydrated, None
    except Exception as exc:  # error is persisted and surfaced after all futures finish
        return row["paper_id"], None, str(exc)


def flag_set(row: dict[str, str]) -> set[str]:
    return {flag for flag in row["selection_flags"].split("|") if flag}


def deduplicate(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    by_forum: dict[tuple[str, str], list[dict[str, str]]] = collections.defaultdict(list)
    for row in rows:
        if not row["openreview_id"]:
            raise RuntimeError(f"cannot deduplicate unhydrated row {row['paper_id']}")
        by_forum[(row["conference"], row["openreview_id"])].append(row)

    output: list[dict[str, str]] = []
    aliases: list[dict[str, str]] = []
    for (_, forum_id), candidates in by_forum.items():
        # Oral pages contain the presentation title and supersede an older spotlight-poster title.
        chosen = max(
            candidates,
            key=lambda row: (
                "outstanding" in flag_set(row),
                "oral" in flag_set(row),
                "spotlight" in flag_set(row),
            ),
        )
        merged = dict(chosen)
        flags = set().union(*(flag_set(row) for row in candidates))
        merged["selection_flags"] = "|".join(
            flag for flag in ("outstanding", "oral", "spotlight") if flag in flags
        )
        merged["analysis_stratum"] = next(
            flag for flag in ("outstanding", "oral", "spotlight") if flag in flags
        )
        output.append(merged)
        for row in candidates:
            if row["paper_id"] == chosen["paper_id"]:
                continue
            aliases.append(
                {
                    "conference": row["conference"],
                    "openreview_id": forum_id,
                    "kept_paper_id": chosen["paper_id"],
                    "kept_title": chosen["title"],
                    "dropped_paper_id": row["paper_id"],
                    "alternate_official_title": row["title"],
                    "alternate_event_url": row["official_event_url"],
                    "reason": "same_openreview_forum",
                }
            )
    output.sort(key=lambda row: (row["conference"], row["analysis_stratum"], row["title"]))
    return output, aliases


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    rows = read_csv(PROCESSED / "papers.csv")
    results: dict[str, dict[str, str]] = {}
    failures: dict[str, str] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(hydrate, row, args.refresh): row["paper_id"] for row in rows}
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            paper_id, record, error = future.result()
            if error:
                failures[paper_id] = error
            elif record:
                results[paper_id] = record
            if index % 50 == 0 or index == len(futures):
                print(f"hydrated {index}/{len(futures)}; failures={len(failures)}", flush=True)
    hydrated_output = [results.get(row["paper_id"], row) for row in rows]
    output, aliases = deduplicate(hydrated_output)
    write_csv(PROCESSED / "papers.csv", output, FIELDS)
    write_csv(
        PROCESSED / "aliases.csv",
        aliases,
        [
            "conference",
            "openreview_id",
            "kept_paper_id",
            "kept_title",
            "dropped_paper_id",
            "alternate_official_title",
            "alternate_event_url",
            "reason",
        ],
    )
    abstract_rows = [
        {"paper_id": row["paper_id"], "abstract": results.get(row["paper_id"], {}).get("abstract", "")}
        for row in output
    ]
    write_json(PROCESSED / "abstracts.json", abstract_rows)
    write_json(PROCESSED / "hydration_failures.json", failures)
    if failures:
        raise SystemExit(f"{len(failures)} papers could not be hydrated; inspect data/processed/hydration_failures.json")
    status_path = PROCESSED / "corpus_status.json"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    counts = collections.Counter((row["conference"], row["analysis_stratum"]) for row in output)
    status["paper_count"] = len(output)
    status["counts"] = {
        f"{conference.lower()}_{stratum}": count
        for (conference, stratum), count in sorted(counts.items())
    }
    status["deduplicated_by_openreview_id"] = len(aliases)
    write_json(status_path, status)
    print(f"deduplicated corpus: {len(output)} papers; aliases={len(aliases)}")


if __name__ == "__main__":
    main()
