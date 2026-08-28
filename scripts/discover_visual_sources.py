#!/usr/bin/env python3
"""Discover public paper repositories and compact figure/table source files."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data" / "processed" / "analysis_sample.csv"
PAPERS = ROOT / "data" / "processed" / "papers.csv"
OUTPUT = ROOT / "reports" / "tables" / "visual_source_inventory.csv"

REPO_RE = re.compile(
    r"(?:https?://)?(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)",
    re.IGNORECASE,
)
CODE_CONTEXT_RE = re.compile(
    r"(?:our\s+(?:code|implementation)|code\s+is\s+(?:available|released)|"
    r"implementation\s+is\s+available|project\s+(?:page|website)|"
    r"available\s+at|source\s+code|github\s+repository)",
    re.IGNORECASE,
)
REFERENCE_CONTEXT_RE = re.compile(
    r"(?:we\s+(?:use|adopt|follow)|baseline|built\s+on|based\s+on|"
    r"implementation\s+of|code\s+from)",
    re.IGNORECASE,
)
VISUAL_PATH_RE = re.compile(
    r"(?:^|/)(?:fig(?:ure)?s?|plots?|charts?|visual(?:ization)?s?|tables?|paper|latex)(?:/|[_-]|\.)",
    re.IGNORECASE,
)
VISUAL_NAME_RE = re.compile(
    r"(?:^|[_./-])(?:plot|fig(?:ure)?|chart|visual|table|diagram|heatmap|ablation|qualitative|pareto)(?:s|ting|ter|[_./-]|$)",
    re.IGNORECASE,
)
RESULT_PATH_RE = re.compile(r"(?:^|/)(?:results?|metrics?|analysis|evaluation)(?:/|[_-]|\.)", re.I)
VISUAL_EXTENSIONS = {
    ".py",
    ".ipynb",
    ".r",
    ".jl",
    ".m",
    ".tex",
    ".tikz",
    ".pgf",
    ".svg",
    ".eps",
    ".pdf",
    ".csv",
    ".json",
    ".yaml",
    ".yml",
}
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "is",
    "of",
    "on",
    "the",
    "to",
    "with",
    "via",
    "using",
    "model",
    "models",
    "method",
    "methods",
    "learning",
}
AGGREGATOR_RE = re.compile(r"(?:^|/)(?:awesome|daily[-_]?arxiv|paper[-_]?list|papers?[-_]?with[-_]?code)", re.I)
NONAUTHOR_REPO_RE = re.compile(
    r"(?:awesome|survey|review|literature|paper[-_]?list|papers?|reading[-_]?group|"
    r"reproduction|course|final[-_]?project|article|radar)",
    re.I,
)


@dataclass(frozen=True)
class Candidate:
    repository: str
    score: float
    context: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Skip GitHub API resolution.")
    parser.add_argument("--workers", type=int, default=6)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def paper_text_path(paper_id: str) -> Path | None:
    for directory in (ROOT / "corpus" / "text", ROOT / "corpus" / "preprint_text"):
        path = directory / f"{paper_id}.txt"
        if path.exists():
            return path
    return None


def title_tokens(title: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", title.lower())
        if len(token) > 2 and token not in STOPWORDS
    }


def normalize_repo(owner: str, name: str) -> str | None:
    clean = name.rstrip(".,;:!?)]}\"'")
    clean = re.sub(r"\.git$", "", clean, flags=re.IGNORECASE)
    if clean.lower() in {"issues", "pull", "tree", "blob", "releases"}:
        return None
    if not clean or clean.startswith("_"):
        return None
    return f"{owner}/{clean}"


def discover_candidates(text: str, title: str) -> list[Candidate]:
    tokens = title_tokens(title)
    by_repo: dict[str, Candidate] = {}
    for match in REPO_RE.finditer(text):
        repository = normalize_repo(match.group(1), match.group(2))
        if repository is None:
            continue
        context = re.sub(r"\s+", " ", text[max(0, match.start() - 260) : match.end() + 260]).strip()
        repo_tokens = title_tokens(repository.replace("/", " ").replace("-", " ").replace("_", " "))
        overlap = len(tokens & repo_tokens)
        score = float(overlap * 3)
        if CODE_CONTEXT_RE.search(context):
            score += 12
        if REFERENCE_CONTEXT_RE.search(context):
            score -= 3
        if match.start() < 9000:
            score += 2
        if repository.lower() in {"openai/gym", "karpathy/nanogpt", "lm-sys/fastchat"}:
            score -= 4
        candidate = Candidate(repository, score, context[:700])
        previous = by_repo.get(repository.lower())
        if previous is None or candidate.score > previous.score:
            by_repo[repository.lower()] = candidate
    return sorted(by_repo.values(), key=lambda candidate: (-candidate.score, candidate.repository.lower()))


def gh_json(arguments: list[str]) -> object | None:
    completed = subprocess.run(
        ["gh", *arguments],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
        timeout=45,
    )
    if completed.returncode != 0 or not completed.stdout.strip():
        return None
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError:
        return None


def gh_text(arguments: list[str]) -> str:
    completed = subprocess.run(
        ["gh", *arguments],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
        timeout=45,
    )
    return completed.stdout if completed.returncode == 0 else ""


def search_title(title: str) -> list[str]:
    query = re.sub(r"[$\\{}]", " ", title)
    result = gh_json(
        [
            "search",
            "repos",
            query,
            "--match",
            "name,description,readme",
            "--limit",
            "5",
            "--json",
            "fullName,description,updatedAt",
        ]
    )
    if not isinstance(result, list):
        return []
    return [str(item["fullName"]) for item in result if item.get("fullName")]


def repository_title_evidence(repository: str, title: str) -> tuple[bool, str]:
    if AGGREGATOR_RE.search(repository) or NONAUTHOR_REPO_RE.search(repository):
        return False, "aggregator repository"
    metadata = gh_json(["api", f"repos/{repository}"])
    if not isinstance(metadata, dict):
        return False, "repository unresolved"
    readme = gh_text(["api", f"repos/{repository}/readme", "-H", "Accept: application/vnd.github.raw+json"])
    metadata_text = " ".join(
        str(value or "")
        for value in (
            metadata.get("name"),
            metadata.get("description"),
            metadata.get("homepage"),
        )
    )
    evidence_text = f"{metadata_text} {readme[:50000]}"
    normalized_title = " ".join(re.findall(r"[a-z0-9]+", title.lower()))
    normalized_evidence = " ".join(re.findall(r"[a-z0-9]+", evidence_text.lower()))
    tokens = title_tokens(title)
    evidence_tokens = set(re.findall(r"[a-z0-9]+", evidence_text.lower()))
    metadata_tokens = set(re.findall(r"[a-z0-9]+", metadata_text.lower()))
    overlap = tokens & evidence_tokens
    recall = len(overlap) / max(1, len(tokens))
    exact = normalized_title in normalized_evidence
    normalized_metadata = " ".join(re.findall(r"[a-z0-9]+", metadata_text.lower()))
    metadata_exact = normalized_title in normalized_metadata
    lead = title.split(":", 1)[0]
    lead_tokens = {token for token in title_tokens(lead) if len(token) >= 4}
    anchor_overlap = lead_tokens & metadata_tokens
    if not lead_tokens:
        anchor_overlap = tokens & metadata_tokens
    distinctive = sorted(overlap)
    verified = metadata_exact or (
        exact
        and bool(anchor_overlap)
        and len(overlap) >= 4
        and recall >= 0.55
    )
    reason = (
        f"metadata_title_exact={int(metadata_exact)}; readme_title_exact={int(exact)}; "
        f"token_recall={recall:.3f}; anchors={','.join(sorted(anchor_overlap)[:6])}; "
        f"matched={','.join(distinctive[:12])}"
    )
    return verified, reason


def visual_files(repository: str) -> tuple[str, str, list[str]]:
    metadata = gh_json(["api", f"repos/{repository}"])
    if not isinstance(metadata, dict):
        return "unresolved", "", []
    branch = str(metadata.get("default_branch") or "")
    if not branch:
        return "repository_without_visual_source", "", []
    tree = gh_json(["api", f"repos/{repository}/git/trees/{branch}?recursive=1"])
    if not isinstance(tree, dict):
        return "repository_without_visual_source", branch, []
    candidates: list[str] = []
    for item in tree.get("tree", []):
        if item.get("type") != "blob":
            continue
        path = str(item.get("path") or "")
        suffix = Path(path).suffix.lower()
        if suffix not in VISUAL_EXTENSIONS:
            continue
        if VISUAL_PATH_RE.search(path) or VISUAL_NAME_RE.search(path) or (
            RESULT_PATH_RE.search(path) and suffix in {".csv", ".json", ".yaml", ".yml"}
        ):
            candidates.append(path)
    ranked = sorted(
        set(candidates),
        key=lambda path: (
            0 if Path(path).suffix.lower() in {".py", ".ipynb", ".r", ".tex", ".tikz", ".pgf"} else 1,
            0 if VISUAL_NAME_RE.search(Path(path).stem) else 1,
            len(path),
            path.lower(),
        ),
    )
    status = "partial_visual_source" if ranked else "repository_without_visual_source"
    if any(Path(path).suffix.lower() in {".py", ".ipynb", ".r", ".jl", ".m", ".tikz", ".pgf"} for path in ranked):
        status = "exact_visual_source"
    elif any(Path(path).suffix.lower() == ".tex" for path in ranked):
        status = "paper_source_only"
    return status, branch, ranked[:40]


def resolve(row: dict[str, object]) -> dict[str, object]:
    candidates = list(row["candidates"])
    selected = ""
    method = ""
    verification = ""
    for candidate in candidates:
        if candidate.score < 8:
            break
        verified, reason = repository_title_evidence(candidate.repository, str(row["title"]))
        # A first-party code statement in the paper is stronger than repository
        # naming: project repositories frequently use only an acronym.
        explicit = candidate.score >= 12 and bool(CODE_CONTEXT_RE.search(candidate.context))
        if verified or explicit:
            selected = candidate.repository
            method = "explicit_pdf_url"
            verification = f"{reason}; explicit_code_context={int(explicit)}"
            break
    searched: list[str] = []
    if not selected:
        searched = search_title(str(row["title"]))
        for repository in searched:
            verified, reason = repository_title_evidence(repository, str(row["title"]))
            if verified:
                selected = repository
                method = "github_title_search_verified"
                verification = reason
                break
    if not selected:
        return {**row, "selected": "", "selection_method": "", "verification": "", "status": "no_public_source_found", "branch": "", "files": [], "searched": searched}
    status, branch, files = visual_files(selected)
    return {**row, "selected": selected, "selection_method": method, "verification": verification, "status": status, "branch": branch, "files": files, "searched": searched}


def main() -> None:
    args = parse_args()
    paper_by_id = {row["paper_id"]: row for row in read_csv(PAPERS)}
    rows: list[dict[str, object]] = []
    for sample in read_csv(SAMPLE):
        paper_id = sample["paper_id"]
        if not (ROOT / "readings" / f"{paper_id}.json").exists():
            continue
        metadata = paper_by_id[paper_id]
        text_path = paper_text_path(paper_id)
        text = text_path.read_text(encoding="utf-8", errors="ignore") if text_path else ""
        candidates = discover_candidates(text, metadata["title"])
        rows.append(
            {
                "paper_id": paper_id,
                "conference": sample["conference"],
                "title": metadata["title"],
                "candidates": candidates,
                "text_path": str(text_path.relative_to(ROOT)) if text_path else "",
            }
        )

    if not args.offline:
        resolved: list[dict[str, object]] = []
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {executor.submit(resolve, row): row["paper_id"] for row in rows}
            for index, future in enumerate(as_completed(futures), start=1):
                resolved.append(future.result())
                if index % 25 == 0:
                    print(f"resolved {index}/{len(futures)}")
                    time.sleep(0.15)
        rows = sorted(resolved, key=lambda row: str(row["paper_id"]))
    else:
        rows = [
            {
                **row,
                "selected": row["candidates"][0].repository if row["candidates"] else "",
                "selection_method": "offline_top_candidate" if row["candidates"] else "",
                "verification": "",
                "status": "unresolved" if row["candidates"] else "no_public_source_found",
                "branch": "",
                "files": [],
                "searched": [],
            }
            for row in rows
        ]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "paper_id",
        "conference",
        "title",
        "discovery_status",
        "discovered_repository",
        "discovery_method",
        "discovery_evidence",
        "default_branch",
        "candidate_repositories",
        "candidate_scores",
        "search_repositories",
        "visual_source_files",
        "best_pdf_context",
        "text_path",
    ]
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            candidates = list(row["candidates"])
            writer.writerow(
                {
                    "paper_id": row["paper_id"],
                    "conference": row["conference"],
                    "title": row["title"],
                    "discovery_status": row["status"],
                    "discovered_repository": row["selected"],
                    "discovery_method": row["selection_method"],
                    "discovery_evidence": row["verification"],
                    "default_branch": row["branch"],
                    "candidate_repositories": "|".join(candidate.repository for candidate in candidates),
                    "candidate_scores": "|".join(f"{candidate.score:g}" for candidate in candidates),
                    "search_repositories": "|".join(row["searched"]),
                    "visual_source_files": "|".join(row["files"]),
                    "best_pdf_context": candidates[0].context if candidates else "",
                    "text_path": row["text_path"],
                }
            )
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(rows)} papers)")


if __name__ == "__main__":
    main()
