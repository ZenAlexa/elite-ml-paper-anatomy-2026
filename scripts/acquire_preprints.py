#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import shutil

from acquire_pdfs import MANIFEST_FIELDS, download
from common import PROCESSED, ROOT, read_csv, write_csv, write_json


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Acquire provisional arXiv PDFs without changing official-PDF coverage."
    )
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--paper-id", action="append", default=[])
    args = parser.parse_args()

    sources = read_csv(PROCESSED / "preprint_sources.csv")
    if args.paper_id:
        requested = set(args.paper_id)
        sources = [row for row in sources if row["paper_id"] in requested]
        missing = requested - {row["paper_id"] for row in sources}
        if missing:
            raise SystemExit(f"paper ids without a preprint source: {sorted(missing)}")
    rows = [
        {
            "paper_id": row["paper_id"],
            "openreview_id": row["openreview_id"],
            "pdf_url": row["preprint_url"],
            "pdf_path": f"corpus/preprints/{row['paper_id']}.pdf",
        }
        for row in sources
    ]
    free_bytes = shutil.disk_usage(ROOT).free
    if free_bytes < 2 * 1024**3:
        raise SystemExit(f"less than 2 GiB free; refusing preprint download ({free_bytes} bytes available)")

    manifest_path = PROCESSED / "preprint_manifest.csv"
    existing = {row["paper_id"]: row for row in read_csv(manifest_path)} if manifest_path.exists() else {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(download, row, args.refresh): row for row in rows}
        failures = 0
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            existing[result["paper_id"]] = result
            failures += result["status"] != "verified"
            if index % 25 == 0 or index == len(futures):
                print(f"preprints {index}/{len(futures)}; failures={failures}", flush=True)
                write_csv(manifest_path, existing.values(), MANIFEST_FIELDS)

    write_csv(manifest_path, sorted(existing.values(), key=lambda row: row["paper_id"]), MANIFEST_FIELDS)
    failed = {paper_id: row["error"] for paper_id, row in existing.items() if row["status"] != "verified"}
    write_json(PROCESSED / "preprint_failures.json", failed)
    if failed:
        raise SystemExit(f"{len(failed)} preprints failed verification; inspect preprint_failures.json")


if __name__ == "__main__":
    main()
