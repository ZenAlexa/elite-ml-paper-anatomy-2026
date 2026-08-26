#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path

from acquire_pdfs import download
from common import PROCESSED, read_csv, write_csv


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", default="ICML")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    rows = [row for row in read_csv(PROCESSED / "papers.csv") if row["conference"] == args.conference]
    if args.paper_id:
        requested = set(args.paper_id)
        rows = [row for row in rows if row["paper_id"] in requested]
    else:
        rows = rows[args.start : args.start + args.count]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for index, row in enumerate(rows, 1):
        action_row = dict(row)
        action_row["pdf_path"] = str(args.output_dir / f"{row['paper_id']}.pdf")
        # download() resolves paths relative to ROOT; absolute paths remain absolute.
        result = download(action_row, refresh=True)
        results.append(result)
        print(f"{index}/{len(rows)} {row['paper_id']} {result['status']}", flush=True)
    write_csv(args.output_dir / "manifest.csv", results, list(results[0].keys()) if results else [])
    failures = [row for row in results if row["status"] != "verified"]
    if failures:
        for row in failures:
            print(f"FAILED {row['paper_id']}: {row['error']}")
        raise SystemExit(f"{len(failures)} downloads failed")


if __name__ == "__main__":
    main()
