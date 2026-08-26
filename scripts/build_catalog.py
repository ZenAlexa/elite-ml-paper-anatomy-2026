#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

from common import FIELDS, RAW, PROCESSED, clean_html, fetch, normalize_title, stable_paper_id, write_csv, write_json

SOURCES = {
    "iclr_events": "https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json",
    "iclr_orals": "https://iclr.cc/virtual/2026/events/oral",
    "iclr_awards": "https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/",
    "icml_spotlights": "https://icml.cc/virtual/2026/events/2026SpotlightPosters",
    "icml_orals": "https://icml.cc/virtual/2026/events/oral",
    "icml_awards": "https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/",
    "neurips_cfp": "https://neurips.cc/Conferences/2026/CallForPapers",
}

OUTSTANDING_TITLES = {
    "ICLR": {
        "Transformers are Inherently Succinct",
        "LLMs Get Lost In Multi-Turn Conversation",
    },
    "ICML": {
        "The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models",
        "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions",
    },
}

def snapshot_sources(refresh: bool) -> dict[str, Path]:
    suffixes = {
        "iclr_events": "json",
        "iclr_orals": "html",
        "iclr_awards": "html",
        "icml_spotlights": "html",
        "icml_orals": "html",
        "icml_awards": "html",
        "neurips_cfp": "html",
    }
    paths = {}
    for name, url in SOURCES.items():
        paths[name] = fetch(url, RAW / f"{name}.{suffixes[name]}", refresh=refresh)
    return paths


def verify_award_pages(paths: dict[str, Path]) -> None:
    for conference, key in (("ICLR", "iclr_awards"), ("ICML", "icml_awards")):
        page = clean_html(paths[key].read_text(encoding="utf-8"))
        missing = [title for title in OUTSTANDING_TITLES[conference] if title not in page]
        if missing:
            raise RuntimeError(f"{conference} official award page is missing locked titles: {missing}")


def parse_event_cards(page: str, expected_kind: str) -> list[dict[str, str]]:
    starts = list(re.finditer(r'<div class="event-card[^>]*"\s+id="event-(\d+)"', page, re.I))
    rows: list[dict[str, str]] = []
    for index, start in enumerate(starts):
        block = page[start.start() : starts[index + 1].start() if index + 1 < len(starts) else len(page)]
        title_match = re.search(
            r'<h3 class="event-title">\s*<a href="([^"]+)">(.*?)</a>', block, re.I | re.S
        )
        if not title_match:
            continue
        href = title_match.group(1)
        if f"/virtual/2026/{expected_kind}/" not in href:
            continue
        title = clean_html(title_match.group(2))
        speakers_match = re.search(r'<div class="event-speakers">(.*?)</div>', block, re.I | re.S)
        speakers = clean_html(speakers_match.group(1)) if speakers_match else ""
        rows.append(
            {
                "event_id": start.group(1),
                "href": href,
                "title": title,
                "authors": speakers.replace(" ⋅ ", "|"),
            }
        )
    return rows


def blank_record(conference: str, title: str) -> dict[str, object]:
    return {
        "paper_id": stable_paper_id(conference, title),
        "conference": conference,
        "year": 2026,
        "title": title,
        "authors": "",
        "analysis_stratum": "",
        "selection_flags": set(),
        "official_event_id": "",
        "official_event_url": "",
        "official_source_url": "",
        "openreview_id": "",
        "openreview_url": "",
        "pdf_url": "",
        "pdf_source_type": "",
        "pdf_path": "",
        "pdf_status": "not_requested",
    }


def build_iclr(path: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = [row for row in payload["results"] if row.get("decision") == "Accept (Oral)"]
    by_uid: dict[str, list[dict[str, object]]] = collections.defaultdict(list)
    for row in rows:
        by_uid[str(row["uid"])].append(row)

    papers: list[dict[str, object]] = []
    for candidates in by_uid.values():
        chosen = next((row for row in candidates if row.get("eventtype") == "Oral"), candidates[0])
        title = str(chosen["name"]).strip()
        record = blank_record("ICLR", title)
        record["authors"] = "|".join(str(author["fullname"]) for author in chosen.get("authors", []))
        record["selection_flags"].add("oral")
        if normalize_title(title) in {normalize_title(x) for x in OUTSTANDING_TITLES["ICLR"]}:
            record["selection_flags"].add("outstanding")
        record["official_event_id"] = str(chosen["id"])
        event_kind = "oral" if chosen.get("eventtype") == "Oral" else "poster"
        record["official_event_url"] = f"https://iclr.cc/virtual/2026/{event_kind}/{chosen['id']}"
        record["official_source_url"] = SOURCES["iclr_events"]
        papers.append(record)

    observed_awards = {normalize_title(str(row["title"])) for row in papers if "outstanding" in row["selection_flags"]}
    expected_awards = {normalize_title(title) for title in OUTSTANDING_TITLES["ICLR"]}
    if observed_awards != expected_awards:
        raise RuntimeError(f"ICLR Outstanding papers are not all present in Oral corpus: {expected_awards - observed_awards}")
    return papers, []


def build_icml(spotlight_path: Path, oral_path: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    spotlight_rows = parse_event_cards(spotlight_path.read_text(encoding="utf-8"), "poster")
    oral_rows = parse_event_cards(oral_path.read_text(encoding="utf-8"), "oral")
    exclusions: list[dict[str, object]] = []

    def eligible(row: dict[str, str], flag: str, source_url: str) -> bool:
        if row["title"].lower().startswith("position:"):
            exclusions.append(
                {
                    "conference": "ICML",
                    "year": 2026,
                    "title": row["title"],
                    "official_event_id": row["event_id"],
                    "selection_flag": flag,
                    "reason": "position_paper_track",
                    "official_source_url": source_url,
                }
            )
            return False
        return True

    merged: dict[str, dict[str, object]] = {}
    for flag, rows, source_url in (
        ("spotlight", spotlight_rows, SOURCES["icml_spotlights"]),
        ("oral", oral_rows, SOURCES["icml_orals"]),
    ):
        for row in rows:
            if not eligible(row, flag, source_url):
                continue
            key = normalize_title(row["title"])
            record = merged.setdefault(key, blank_record("ICML", row["title"]))
            record["selection_flags"].add(flag)
            if row["authors"] and not record["authors"]:
                record["authors"] = row["authors"]
            # Prefer the oral landing page when the paper has both records.
            if flag == "oral" or not record["official_event_id"]:
                record["official_event_id"] = row["event_id"]
                record["official_event_url"] = f"https://icml.cc{row['href']}"
                record["official_source_url"] = source_url

    award_keys = {normalize_title(title) for title in OUTSTANDING_TITLES["ICML"]}
    for key, record in merged.items():
        if key in award_keys:
            record["selection_flags"].add("outstanding")
    observed_awards = {key for key, record in merged.items() if "outstanding" in record["selection_flags"]}
    if observed_awards != award_keys:
        raise RuntimeError(f"ICML Outstanding papers are not all present in Oral/Spotlight corpus: {award_keys - observed_awards}")
    return list(merged.values()), exclusions


def finalize(records: list[dict[str, object]]) -> list[dict[str, object]]:
    for record in records:
        flags = set(record["selection_flags"])
        record["analysis_stratum"] = next(flag for flag in ("outstanding", "oral", "spotlight") if flag in flags)
        record["selection_flags"] = "|".join(flag for flag in ("outstanding", "oral", "spotlight") if flag in flags)
    return sorted(records, key=lambda row: (str(row["conference"]), str(row["analysis_stratum"]), str(row["title"])))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="refresh official source snapshots")
    args = parser.parse_args()
    paths = snapshot_sources(args.refresh)
    verify_award_pages(paths)
    iclr, iclr_exclusions = build_iclr(paths["iclr_events"])
    icml, icml_exclusions = build_icml(paths["icml_spotlights"], paths["icml_orals"])
    records = finalize(iclr + icml)
    write_csv(PROCESSED / "papers.csv", records, FIELDS)
    write_csv(
        PROCESSED / "exclusions.csv",
        iclr_exclusions + icml_exclusions,
        ["conference", "year", "title", "official_event_id", "selection_flag", "reason", "official_source_url"],
    )
    counts = collections.Counter((str(row["conference"]), str(row["analysis_stratum"])) for row in records)
    status = {
        "schema_version": "corpus-status.v1",
        "as_of_utc": "2026-08-26T14:28:58Z",
        "observed_conferences": ["ICLR", "ICML"],
        "pending_conferences": {
            "NeurIPS": {
                "status": "not_yet_observed",
                "author_notification": "2026-09-24 AoE",
                "source": SOURCES["neurips_cfp"],
            }
        },
        "paper_count": len(records),
        "counts": {f"{conference.lower()}_{stratum}": count for (conference, stratum), count in sorted(counts.items())},
        "official_sources": SOURCES,
    }
    write_json(PROCESSED / "corpus_status.json", status)
    print(json.dumps(status, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
