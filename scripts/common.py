#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import unicodedata
import urllib.request
from functools import lru_cache
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "official"
PROCESSED = ROOT / "data" / "processed"
PDFS = ROOT / "corpus" / "pdfs"
TEXT = ROOT / "corpus" / "text"

FIELDS = [
    "paper_id",
    "conference",
    "year",
    "title",
    "authors",
    "analysis_stratum",
    "selection_flags",
    "official_event_id",
    "official_event_url",
    "official_source_url",
    "openreview_id",
    "openreview_url",
    "pdf_url",
    "pdf_source_type",
    "pdf_path",
    "pdf_status",
]


def fetch(url: str, destination: Path, refresh: bool = False) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.stat().st_size > 0 and not refresh:
        return destination
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "elite-ml-paper-anatomy-2026/1.0 (+https://github.com/ZenAlexa/elite-ml-paper-anatomy-2026)",
            "Accept": "text/html,application/json,application/pdf;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        payload = response.read()
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_bytes(payload)
    temporary.replace(destination)
    return destination


def normalize_title(title: str) -> str:
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", ascii_title.lower())


def clean_html(fragment: str) -> str:
    fragment = re.sub(r"<script\b.*?</script>", " ", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<style\b.*?</style>", " ", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return " ".join(html.unescape(fragment).split())


def stable_paper_id(conference: str, title: str) -> str:
    digest = hashlib.sha256(normalize_title(title).encode()).hexdigest()[:12]
    return f"{conference.lower()}-2026-{digest}"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: Iterable[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


@lru_cache(maxsize=1)
def reading_required_keys() -> set[str]:
    schema = json.loads((ROOT / "schemas" / "deep-read.schema.json").read_text(encoding="utf-8"))
    return set(schema["required"])


def load_complete_reading(paper_id: str) -> dict[str, object] | None:
    json_path = ROOT / "readings" / f"{paper_id}.json"
    markdown_path = ROOT / "readings" / f"{paper_id}.md"
    if not json_path.exists() or not markdown_path.exists():
        return None
    try:
        value = json.loads(json_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(value, dict):
        return None
    if value.get("paper_id") != paper_id or not reading_required_keys().issubset(value):
        return None
    return value
