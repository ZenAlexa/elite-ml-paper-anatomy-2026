#!/usr/bin/env python3
"""Acquire compact public visual-source files selected by source discovery."""

from __future__ import annotations

import argparse
import base64
import csv
import io
import json
import subprocess
import tarfile
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path, PurePosixPath
from urllib.parse import quote, urljoin, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "reports" / "tables" / "visual_source_inventory.csv"
OUTPUT = ROOT / "reports" / "tables" / "visual_source_files_local.csv"
SOURCE_ROOT = ROOT / "corpus" / "visual_sources"
CODE_EXTENSIONS = {".py", ".ipynb", ".r", ".jl", ".m", ".tex", ".tikz", ".pgf"}
ASSET_EXTENSIONS = {
    ".svg", ".eps", ".pdf", ".png", ".jpg", ".jpeg",
    ".csv", ".json", ".yaml", ".yml", ".sty", ".cls", ".mplstyle",
}
ALLOWED_EXTENSIONS = CODE_EXTENSIONS | ASSET_EXTENSIONS
USER_AGENT = "elite-ml-paper-anatomy-2026/1.0 (visual-source research)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--max-files-per-paper", type=int, default=12)
    parser.add_argument("--max-bytes", type=int, default=1_500_000)
    return parser.parse_args()


def read_inventory() -> list[dict[str, str]]:
    with INVENTORY.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rank_path(path: str) -> tuple[int, int, int, str]:
    suffix = PurePosixPath(path).suffix.lower()
    lower = path.lower()
    return (
        0 if suffix in CODE_EXTENSIONS else 1,
        0 if any(token in lower for token in ("plot", "figure", "visual", "table", "paper", "latex")) else 1,
        len(path),
        lower,
    )


def parse_github_repository(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None
    return f"{parts[0]}/{parts[1].removesuffix('.git')}"


def arxiv_identifier(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.netloc.lower() not in {"arxiv.org", "www.arxiv.org", "export.arxiv.org"}:
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2 or parts[0] not in {"abs", "src", "e-print", "pdf"}:
        return None
    return parts[1].removesuffix(".pdf")


def read_url(url: str, max_bytes: int, timeout: int = 120) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    chunks: list[bytes] = []
    total = 0
    with urlopen(request, timeout=timeout) as response:
        while True:
            chunk = response.read(1 << 20)
            if not chunk:
                break
            total += len(chunk)
            if total > max_bytes:
                raise ValueError("download exceeds byte limit")
            chunks.append(chunk)
    return b"".join(chunks)


def external_repository_token(repository_url: str) -> str:
    parsed = urlparse(repository_url)
    path = "__".join(part for part in parsed.path.split("/") if part)
    return "__".join(part for part in (parsed.netloc, path) if part)


def write_external_file(
    paper_id: str,
    repository_url: str,
    source_path: str,
    content: bytes,
) -> str:
    destination = SOURCE_ROOT / paper_id / external_repository_token(repository_url) / PurePosixPath(source_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)
    return str(destination.relative_to(ROOT))


def fetch_arxiv_group(task: tuple[str, str, tuple[str, ...], int]) -> list[dict[str, object]]:
    paper_id, repository_url, requested_paths, max_bytes = task
    identifier = arxiv_identifier(repository_url)
    base = {
        "paper_id": paper_id,
        "repository": repository_url,
        "branch": identifier or "",
        "local_path": "",
        "bytes": "",
        "origin": "manual_audit",
    }
    if not identifier:
        return [{**base, "source_path": path, "status": "unsupported_repository"} for path in requested_paths]
    try:
        package = read_url(f"https://export.arxiv.org/e-print/{identifier}", max(80_000_000, max_bytes))
    except Exception:
        try:
            package = read_url(f"https://arxiv.org/e-print/{identifier}", max(80_000_000, max_bytes))
        except Exception:
            return [{**base, "source_path": path, "status": "fetch_failed"} for path in requested_paths]

    members: dict[str, bytes] = {}
    try:
        with tarfile.open(fileobj=io.BytesIO(package), mode="r:*") as archive:
            for member in archive.getmembers():
                if not member.isfile():
                    continue
                normalized = member.name.lstrip("./")
                if member.size > max_bytes:
                    continue
                extracted = archive.extractfile(member)
                if extracted is not None:
                    members[normalized] = extracted.read(max_bytes + 1)
    except tarfile.TarError:
        try:
            with zipfile.ZipFile(io.BytesIO(package)) as archive:
                for info in archive.infolist():
                    if info.is_dir() or info.file_size > max_bytes:
                        continue
                    members[info.filename.lstrip("./")] = archive.read(info, pwd=None)
        except zipfile.BadZipFile:
            members = {}

    results: list[dict[str, object]] = []
    for source_path in requested_paths:
        normalized = source_path.lstrip("./")
        matches = [name for name in members if name == normalized or name.endswith("/" + normalized)]
        if not matches:
            results.append({**base, "source_path": source_path, "status": "path_not_found"})
            continue
        member_name = min(matches, key=lambda name: (len(name), name))
        content = members[member_name]
        if len(content) > max_bytes:
            results.append({**base, "source_path": source_path, "bytes": len(content), "status": "skipped_large"})
            continue
        local_path = write_external_file(paper_id, repository_url, source_path, content)
        results.append(
            {
                **base,
                "source_path": source_path,
                "local_path": local_path,
                "bytes": len(content),
                "status": "acquired",
            }
        )
    return results


def fetch_direct_file(task: tuple[str, str, str, int]) -> dict[str, object]:
    paper_id, repository_url, source_path, max_bytes = task
    base = {
        "paper_id": paper_id,
        "repository": repository_url,
        "branch": "",
        "source_path": source_path,
        "local_path": "",
        "bytes": "",
        "origin": "manual_audit",
    }
    target_url = urljoin(repository_url.rstrip("/") + "/", source_path)
    try:
        content = read_url(target_url, max_bytes)
    except ValueError:
        return {**base, "status": "skipped_large"}
    except Exception:
        return {**base, "status": "fetch_failed"}
    local_path = write_external_file(paper_id, repository_url, source_path, content)
    return {**base, "local_path": local_path, "bytes": len(content), "status": "acquired"}


def default_branch(repository: str) -> str | None:
    completed = subprocess.run(
        ["gh", "api", f"repos/{repository}", "--jq", ".default_branch"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=60,
    )
    branch = completed.stdout.strip()
    return branch if completed.returncode == 0 and branch else None


def fetch_file(task: tuple[str, str, str, str, int, str]) -> dict[str, object]:
    paper_id, repository, branch, source_path, max_bytes, origin = task
    endpoint = f"repos/{repository}/contents/{quote(source_path, safe='/')}?ref={quote(branch)}"
    completed = subprocess.run(
        ["gh", "api", endpoint],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=60,
    )
    base = {
        "paper_id": paper_id,
        "repository": repository,
        "branch": branch,
        "source_path": source_path,
        "local_path": "",
        "bytes": "",
        "status": "",
        "origin": origin,
    }
    if completed.returncode != 0:
        return {**base, "status": "fetch_failed"}
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return {**base, "status": "invalid_response"}
    size = int(payload.get("size") or 0)
    if size > max_bytes:
        return {**base, "bytes": size, "status": "skipped_large"}
    encoded = payload.get("content")
    if not isinstance(encoded, str):
        return {**base, "bytes": size, "status": "content_unavailable"}
    try:
        content = base64.b64decode(encoded)
    except ValueError:
        return {**base, "bytes": size, "status": "decode_failed"}
    if len(content) > max_bytes:
        return {**base, "bytes": len(content), "status": "skipped_large"}
    relative = Path(paper_id) / repository.replace("/", "__") / PurePosixPath(source_path)
    destination = SOURCE_ROOT / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)
    return {
        **base,
        "local_path": str(destination.relative_to(ROOT)),
        "bytes": len(content),
        "status": "acquired",
    }


def main() -> None:
    args = parse_args()
    candidates: dict[tuple[str, str, str], str] = {}
    branch_by_repository: dict[str, str] = {}
    for row in read_inventory():
        repository = row.get("discovered_repository", "")
        branch = row.get("default_branch", "")
        if not repository or not branch:
            continue
        branch_by_repository[repository] = branch
        paths = [path for path in row.get("visual_source_files", "").split("|") if path]
        paths = [path for path in paths if PurePosixPath(path).suffix.lower() in CODE_EXTENSIONS | ASSET_EXTENSIONS]
        for source_path in paths:
            candidates[(row["paper_id"], repository, source_path)] = "automated_inventory"

    external_candidates: dict[tuple[str, str], set[str]] = {}
    for audit_path in sorted((ROOT / "visual_audits").glob("*.json")):
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        paper_id = audit["paper_id"]
        for item in audit["source_acquisition"]["visual_source_files"]:
            repository = parse_github_repository(item.get("repository_url", ""))
            source_path = item.get("path", "").strip().lstrip("/")
            if PurePosixPath(source_path).suffix.lower() not in ALLOWED_EXTENSIONS:
                continue
            if repository:
                candidates[(paper_id, repository, source_path)] = "manual_audit"
            else:
                repository_url = item.get("repository_url", "").strip()
                if repository_url:
                    external_candidates.setdefault((paper_id, repository_url), set()).add(source_path)

    repositories = sorted({repository for _, repository, _ in candidates})
    unresolved_repositories = [repository for repository in repositories if repository not in branch_by_repository]
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(default_branch, repository): repository
            for repository in unresolved_repositories
        }
        for future in as_completed(futures):
            repository = futures[future]
            branch = future.result()
            if branch:
                branch_by_repository[repository] = branch

    ranked_by_paper: dict[str, list[tuple[str, str, str]]] = {}
    for paper_id, repository, source_path in candidates:
        if repository not in branch_by_repository:
            continue
        ranked_by_paper.setdefault(paper_id, []).append((repository, source_path, candidates[(paper_id, repository, source_path)]))
    tasks: list[tuple[str, str, str, str, int, str]] = []
    for paper_id, items in ranked_by_paper.items():
        for repository, source_path, origin in sorted(
            items,
            key=lambda item: (0 if item[2] == "manual_audit" else 1, *rank_path(item[1])),
        )[: args.max_files_per_paper]:
            tasks.append((paper_id, repository, branch_by_repository[repository], source_path, args.max_bytes, origin))

    results: list[dict[str, object]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(fetch_file, task) for task in tasks]
        for index, future in enumerate(as_completed(futures), start=1):
            results.append(future.result())
            if index % 50 == 0:
                print(f"acquired/resolved {index}/{len(futures)} source files")

    arxiv_tasks: list[tuple[str, str, tuple[str, ...], int]] = []
    direct_tasks: list[tuple[str, str, str, int]] = []
    for (paper_id, repository_url), paths in external_candidates.items():
        selected_paths = tuple(sorted(paths, key=rank_path)[: args.max_files_per_paper])
        if arxiv_identifier(repository_url):
            arxiv_tasks.append((paper_id, repository_url, selected_paths, args.max_bytes))
        else:
            direct_tasks.extend((paper_id, repository_url, path, args.max_bytes) for path in selected_paths)
    with ThreadPoolExecutor(max_workers=min(4, max(1, args.workers))) as executor:
        futures = [executor.submit(fetch_arxiv_group, task) for task in arxiv_tasks]
        futures.extend(executor.submit(fetch_direct_file, task) for task in direct_tasks)
        for future in as_completed(futures):
            value = future.result()
            if isinstance(value, list):
                results.extend(value)
            else:
                results.append(value)
    results.sort(key=lambda row: (str(row["paper_id"]), str(row["source_path"])))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["paper_id", "repository", "branch", "source_path", "local_path", "bytes", "status", "origin"]
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(results)
    acquired = sum(row["status"] == "acquired" for row in results)
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({acquired}/{len(results)} files acquired)")


if __name__ == "__main__":
    main()
