#!/usr/bin/env python3
"""Extract source-exact plotting and table style literals from acquired files."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "reports" / "tables" / "visual_source_files_local.csv"
OUTPUT = ROOT / "reports" / "tables" / "visual_source_style_metrics.csv"
SOURCE_TEXT_EXTENSIONS = {
    ".py", ".ipynb", ".r", ".jl", ".m", ".tex", ".tikz", ".pgf",
    ".svg", ".eps", ".csv", ".json", ".yaml", ".yml", ".sty", ".cls", ".mplstyle",
}

HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")
TEX_HEX_RE = re.compile(r"\\definecolor\{[^}]+\}\{HTML\}\{([0-9A-Fa-f]{6})\}", re.I)
FIGSIZE_RE = re.compile(r"figsize\s*=\s*\(?\s*([0-9.]+)\s*,\s*([0-9.]+)")
FONT_RE = re.compile(r"(?:font(?:size|_size)|fontsize|font\.size)\s*[=:]\s*[\"']?([0-9.]+)", re.I)
TEX_FONT_RE = re.compile(r"\\fontsize\s*\{([0-9.]+)\}", re.I)
LINE_RE = re.compile(r"(?:linewidth|line_width|lw)\s*[=:]\s*([0-9.]+)", re.I)
TEX_LINE_RE = re.compile(r"line\s+width\s*=\s*([0-9.]+)\s*pt", re.I)
DPI_RE = re.compile(r"(?:dpi|savefig\.dpi)\s*[=:]\s*([0-9.]+)", re.I)
ALPHA_RE = re.compile(r"alpha\s*[=:]\s*([0-9.]+)", re.I)
MARKER_RE = re.compile(r"marker\s*[=:]\s*[\"']([^\"']+)[\"']", re.I)
STYLE_RE = re.compile(r"(?:plt\.style\.use|sns\.set_(?:theme|style)|style\s*=)\s*\(?[\"']([^\"']+)[\"']", re.I)


def read_manifest() -> list[dict[str, str]]:
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def source_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() != ".ipynb":
        return text
    try:
        notebook = json.loads(text)
    except json.JSONDecodeError:
        return text
    return "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook.get("cells", [])
        if cell.get("cell_type") == "code"
    )


def values(pattern: re.Pattern[str], text: str) -> list[str]:
    found = []
    for match in pattern.finditer(text):
        value = "x".join(match.groups()) if len(match.groups()) > 1 else match.group(1)
        if value not in found:
            found.append(value)
    return found


def tools(text: str, suffix: str) -> list[str]:
    detected = []
    patterns = {
        "matplotlib": r"(?:matplotlib|pyplot|plt\.)",
        "seaborn": r"(?:seaborn|sns\.)",
        "plotly": r"(?:plotly|px\.|go\.)",
        "pandas": r"(?:pandas|pd\.)",
        "tikz": r"(?:\\begin\{tikzpicture\}|\\draw|\.tikz)",
        "pgfplots": r"(?:\\begin\{axis\}|pgfplots)",
        "graphviz": r"(?:graphviz|Digraph\()",
        "latex": r"(?:\\begin\{table|\\includegraphics|\\toprule|\\midrule)",
    }
    for name, pattern in patterns.items():
        if re.search(pattern, text, re.I):
            detected.append(name)
    if suffix in {".tex", ".tikz", ".pgf"} and "latex" not in detected:
        detected.append("latex")
    return detected


def main() -> None:
    rows = []
    for item in read_manifest():
        if item["status"] != "acquired" or not item["local_path"]:
            continue
        path = ROOT / item["local_path"]
        if path.suffix.lower() not in SOURCE_TEXT_EXTENSIONS:
            continue
        text = source_text(path)
        lower = text.lower()
        colors = set(HEX_RE.findall(text))
        colors.update(f"#{value}" for value in TEX_HEX_RE.findall(text))
        font_sizes = values(FONT_RE, text)
        font_sizes.extend(value for value in values(TEX_FONT_RE, text) if value not in font_sizes)
        line_widths = values(LINE_RE, text)
        line_widths.extend(value for value in values(TEX_LINE_RE, text) if value not in line_widths)
        rows.append(
            {
                "paper_id": item["paper_id"],
                "repository": item["repository"],
                "source_path": item["source_path"],
                "suffix": path.suffix.lower(),
                "tools": "|".join(tools(text, path.suffix.lower())),
                "hex_colors": "|".join(sorted(colors, key=str.lower)),
                "figsizes_inches": "|".join(values(FIGSIZE_RE, text)),
                "font_sizes_pt": "|".join(font_sizes),
                "line_widths_pt": "|".join(line_widths),
                "alpha_values": "|".join(values(ALPHA_RE, text)),
                "marker_literals": "|".join(values(MARKER_RE, text)),
                "style_literals": "|".join(values(STYLE_RE, text)),
                "dpi_values": "|".join(values(DPI_RE, text)),
                "uses_grid": int(bool(re.search(r"(?:\.grid\(|grid\s*=\s*True)", text, re.I))),
                "uses_legend": int(bool(re.search(r"(?:\.legend\(|legend\s*=)", text, re.I))),
                "uses_errorbar": int(bool(re.search(r"(?:errorbar|yerr\s*=|xerr\s*=)", text, re.I))),
                "uses_fill_between": int("fill_between" in lower),
                "uses_log_axis": int(bool(re.search(r"(?:set_[xy]scale\s*\(\s*[\"']log|loglog|semilog[xy])", text, re.I))),
                "uses_booktabs": int(bool(re.search(r"\\(?:toprule|midrule|bottomrule)", text))),
                "uses_resizebox": int("\\resizebox" in text),
                "uses_small_font": int(bool(re.search(r"\\(?:small|footnotesize|scriptsize|tiny)\b", text))),
                "export_formats": "|".join(
                    sorted(
                        set(re.findall(r"savefig\s*\([^\n]*?[\"'][^\"']+\.(pdf|svg|png|eps)[\"']", text, re.I)),
                        key=str.lower,
                    )
                ),
            }
        )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(rows)} source files)")


if __name__ == "__main__":
    main()
