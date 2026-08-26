#!/usr/bin/env python3
from __future__ import annotations

import re
import unicodedata
from collections import Counter, defaultdict

from common import PROCESSED, ROOT, TEXT, load_complete_reading, read_csv, write_csv

TOKEN = re.compile(r"[a-z][a-z'-]{1,}")
REFERENCES = re.compile(r"(?im)^\s*(?:\d+[. ]+)?references\s*$")
STOPWORDS = {
    "a", "about", "after", "again", "against", "all", "also", "an", "and", "any", "are", "as", "at",
    "be", "because", "been", "before", "being", "between", "both", "but", "by", "can", "could", "did",
    "do", "does", "doing", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having",
    "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "however", "i", "if", "in",
    "into", "is", "it", "its", "itself", "just", "may", "me", "more", "most", "my", "myself", "no", "nor",
    "not", "now", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over",
    "own", "same", "she", "should", "so", "some", "such", "than", "that", "the", "their", "theirs", "them",
    "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until",
    "up", "very", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will",
    "with", "would", "you", "your", "yours", "yourself", "yourselves",
}
RHETORICAL_PATTERNS = {
    "we_propose": r"\bwe propose\b",
    "we_introduce": r"\bwe introduce\b",
    "we_present": r"\bwe present\b",
    "we_show": r"\bwe show\b",
    "we_find": r"\bwe (?:find|found)\b",
    "we_demonstrate": r"\bwe demonstrate\b",
    "we_observe": r"\bwe observe\b",
    "we_establish": r"\bwe establish\b",
    "our_results": r"\bour results?\b",
    "to_our_knowledge": r"\b(?:to the best of )?our knowledge\b",
    "state_of_the_art": r"\bstate[- ]of[- ]the[- ]art\b",
    "significantly": r"\bsignificantly\b",
    "however": r"\bhowever\b",
    "in_contrast": r"\bin contrast\b",
    "suggest": r"\bsuggest(?:s|ed)?\b",
    "limitation": r"\blimitations?\b",
    "first_claim": r"\b(?:the|a|our)?\s*first\b",
    "novel": r"\bnovel\b",
}


def main_body_text(paper_id: str, main_pages: int) -> str:
    text = (TEXT / f"{paper_id}.txt").read_text(encoding="utf-8", errors="replace")
    pages = text.split("\f")
    body = "\n".join(pages[:main_pages])
    reference_match = REFERENCES.search(body)
    if reference_match:
        body = body[: reference_match.start()]
    body = unicodedata.normalize("NFKC", body).lower()
    body = re.sub(r"https?://\S+|www\.\S+", " ", body)
    body = re.sub(r"\S+@\S+", " ", body)
    return body


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    catalog = {row["paper_id"]: row for row in papers}
    documents: list[dict[str, object]] = []
    rhetoric_rows: list[dict[str, object]] = []
    for paper_id, paper in catalog.items():
        reading = load_complete_reading(paper_id)
        if reading is None:
            continue
        body = main_body_text(paper_id, int(float(reading["page_map"]["main_pages"])))
        tokens = TOKEN.findall(body)
        content_tokens = [token for token in tokens if token not in STOPWORDS and len(token) >= 3]
        documents.append(
            {
                "paper_id": paper_id,
                "conference": paper["conference"],
                "analysis_stratum": paper["analysis_stratum"],
                "tokens": tokens,
                "content_tokens": content_tokens,
            }
        )
        for pattern, expression in RHETORICAL_PATTERNS.items():
            count = len(re.findall(expression, body))
            rhetoric_rows.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "pattern": pattern,
                    "count": count,
                    "per_10000_words": round(count / len(tokens) * 10000, 6) if tokens else "",
                }
            )

    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for document in documents:
        groups[(str(document["conference"]), "all")].append(document)
        groups[(str(document["conference"]), str(document["analysis_stratum"]))].append(document)

    frequency_rows: list[dict[str, object]] = []
    ngram_rows: list[dict[str, object]] = []
    for (conference, stratum), group in sorted(groups.items()):
        token_counts: Counter[str] = Counter()
        document_counts: Counter[str] = Counter()
        total_tokens = 0
        ngram_counts: dict[int, Counter[tuple[str, ...]]] = {2: Counter(), 3: Counter()}
        ngram_documents: dict[int, Counter[tuple[str, ...]]] = {2: Counter(), 3: Counter()}
        for document in group:
            tokens = document["content_tokens"]
            token_counts.update(tokens)
            document_counts.update(set(tokens))
            total_tokens += len(document["tokens"])
            for n in (2, 3):
                ngrams = list(zip(*(tokens[offset:] for offset in range(n))))
                ngram_counts[n].update(ngrams)
                ngram_documents[n].update(set(ngrams))
        for token, count in token_counts.most_common(500):
            frequency_rows.append(
                {
                    "conference": conference,
                    "analysis_stratum": stratum,
                    "token": token,
                    "count": count,
                    "document_count": document_counts[token],
                    "document_share": round(document_counts[token] / len(group), 6),
                    "per_10000_all_words": round(count / total_tokens * 10000, 6) if total_tokens else "",
                }
            )
        for n in (2, 3):
            for phrase, count in ngram_counts[n].most_common(500):
                ngram_rows.append(
                    {
                        "conference": conference,
                        "analysis_stratum": stratum,
                        "n": n,
                        "phrase": " ".join(phrase),
                        "count": count,
                        "document_count": ngram_documents[n][phrase],
                        "document_share": round(ngram_documents[n][phrase] / len(group), 6),
                        "per_10000_all_words": round(count / total_tokens * 10000, 6) if total_tokens else "",
                    }
                )

    table_dir = ROOT / "reports" / "tables"
    write_csv(
        table_dir / "lexical_frequencies.csv",
        frequency_rows,
        ["conference", "analysis_stratum", "token", "count", "document_count", "document_share", "per_10000_all_words"],
    )
    write_csv(
        table_dir / "ngram_frequencies.csv",
        ngram_rows,
        ["conference", "analysis_stratum", "n", "phrase", "count", "document_count", "document_share", "per_10000_all_words"],
    )
    write_csv(
        table_dir / "rhetorical_patterns.csv",
        rhetoric_rows,
        ["paper_id", "conference", "analysis_stratum", "pattern", "count", "per_10000_words"],
    )
    print(f"documents={len(documents)} lexical_rows={len(frequency_rows)} ngram_rows={len(ngram_rows)}")


if __name__ == "__main__":
    main()
