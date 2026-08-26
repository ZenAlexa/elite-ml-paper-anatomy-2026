#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

from common import FIELDS, PDFS, PROCESSED, ROOT, read_csv, write_csv, write_json

MANIFEST_FIELDS = [
    "paper_id",
    "openreview_id",
    "pdf_url",
    "pdf_path",
    "status",
    "bytes",
    "pages",
    "pdf_version",
    "error",
]


def pdf_info(path: Path) -> dict[str, str]:
    process = subprocess.run(
        ["pdfinfo", str(path)], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60
    )
    if process.returncode:
        raise RuntimeError(process.stderr.strip() or f"pdfinfo exited {process.returncode}")
    values: dict[str, str] = {}
    for line in process.stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    if int(values.get("Pages", "0")) < 1:
        raise RuntimeError("pdfinfo returned no pages")
    return values


def download(row: dict[str, str], refresh: bool, attempts: int = 5) -> dict[str, str]:
    destination = ROOT / row["pdf_path"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "paper_id": row["paper_id"],
        "openreview_id": row["openreview_id"],
        "pdf_url": row["pdf_url"],
        "pdf_path": row["pdf_path"],
        "status": "failed",
        "bytes": "0",
        "pages": "0",
        "pdf_version": "",
        "error": "",
    }
    try:
        if destination.exists() and not refresh:
            info = pdf_info(destination)
            if destination.read_bytes()[:5] != b"%PDF-":
                raise RuntimeError("cached file does not begin with %PDF-")
        else:
            error: Exception | None = None
            for attempt in range(attempts):
                temporary = destination.with_suffix(".pdf.part")
                try:
                    request = urllib.request.Request(
                        row["pdf_url"],
                        headers={
                            "User-Agent": "elite-ml-paper-anatomy-2026/1.0",
                            "Accept": "application/pdf,*/*;q=0.8",
                        },
                    )
                    with urllib.request.urlopen(request, timeout=180) as response, temporary.open("wb") as handle:
                        first = response.read(8192)
                        if not first.startswith(b"%PDF-"):
                            raise RuntimeError(
                                f"non-PDF response: content-type={response.headers.get('Content-Type')} prefix={first[:80]!r}"
                            )
                        handle.write(first)
                        while True:
                            chunk = response.read(1024 * 1024)
                            if not chunk:
                                break
                            handle.write(chunk)
                    temporary.replace(destination)
                    info = pdf_info(destination)
                    break
                except Exception as exc:
                    error = exc
                    if temporary.exists():
                        temporary.unlink()
                    time.sleep(2.0 * (attempt + 1))
            else:
                raise RuntimeError(str(error))
        result.update(
            {
                "status": "verified",
                "bytes": str(destination.stat().st_size),
                "pages": info.get("Pages", "0"),
                "pdf_version": info.get("PDF version", ""),
            }
        )
    except Exception as exc:
        result["error"] = str(exc)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--conference", action="append", default=[])
    args = parser.parse_args()
    rows = read_csv(PROCESSED / "papers.csv")
    if args.conference:
        conferences = set(args.conference)
        rows = [row for row in rows if row["conference"] in conferences]
    if args.paper_id:
        requested = set(args.paper_id)
        rows = [row for row in rows if row["paper_id"] in requested]
        missing = requested - {row["paper_id"] for row in rows}
        if missing:
            raise SystemExit(f"unknown paper ids: {sorted(missing)}")
    free_bytes = shutil.disk_usage(ROOT).free
    if free_bytes < 2 * 1024**3:
        raise SystemExit(f"less than 2 GiB free; refusing corpus download ({free_bytes} bytes available)")

    manifest_path = PROCESSED / "pdf_manifest.csv"
    existing = {row["paper_id"]: row for row in read_csv(manifest_path)} if manifest_path.exists() else {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(download, row, args.refresh): row for row in rows}
        failures = 0
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            existing[result["paper_id"]] = result
            failures += result["status"] != "verified"
            if index % 25 == 0 or index == len(futures):
                print(f"PDFs {index}/{len(futures)}; failures={failures}", flush=True)
                write_csv(manifest_path, existing.values(), MANIFEST_FIELDS)

    all_catalog_rows = read_csv(PROCESSED / "papers.csv")
    for row in all_catalog_rows:
        if row["paper_id"] in existing:
            row["pdf_status"] = existing[row["paper_id"]]["status"]
    write_csv(PROCESSED / "papers.csv", all_catalog_rows, FIELDS)
    write_csv(manifest_path, sorted(existing.values(), key=lambda row: row["paper_id"]), MANIFEST_FIELDS)
    failed = {paper_id: row["error"] for paper_id, row in existing.items() if row["status"] != "verified"}
    write_json(PROCESSED / "pdf_failures.json", failed)
    if failed:
        raise SystemExit(f"{len(failed)} PDF files failed verification; inspect data/processed/pdf_failures.json")


if __name__ == "__main__":
    main()
