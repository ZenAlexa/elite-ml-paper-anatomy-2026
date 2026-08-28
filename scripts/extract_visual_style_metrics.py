#!/usr/bin/env python3
"""Extract reproducible PDF-level and object-level visual style measurements."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import pdfplumber
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
VISUALS = ROOT / "reports" / "tables" / "visual_inventory.csv"
PAPERS = ROOT / "data" / "processed" / "papers.csv"
OBJECT_OUTPUT = ROOT / "reports" / "tables" / "visual_object_auto_metrics.csv"
PAPER_OUTPUT = ROOT / "reports" / "tables" / "visual_paper_auto_metrics.csv"

FINDING_RE = re.compile(
    r"\b(?:outperform|improv|higher|lower|achiev|show|demonstrat|indicat|reveal|"
    r"best|highest|lowest|superior|reduce|increase|decrease|remain|consistent)",
    re.IGNORECASE,
)
SETUP_RE = re.compile(r"\b(?:dataset|task|model|benchmark|setting|across|under|using|compare|evaluation)\b", re.I)
ENCODING_RE = re.compile(r"\b(?:color|line|shade|bar|marker|panel|left|right|top|bottom|axis|row|column)\b", re.I)
UNCERTAINTY_RE = re.compile(r"\b(?:error|standard deviation|standard error|confidence|interval|shaded|quantile|variance)\b", re.I)
APPENDIX_RE = re.compile(r"\b(?:appendix|supplement)\b", re.I)
TYPE_PATTERNS = {
    "line": r"\b(?:line|curve|trajectory|trend|convergence|scaling)\b|折线|曲线|轨迹|趋势",
    "bar": r"\b(?:bar|histogram)\b|条形|柱状|直方",
    "scatter": r"\b(?:scatter|correlation)\b|散点|相关图",
    "heatmap": r"\b(?:heatmap|heat map)\b|热力|热图",
    "box": r"\bbox(?:plot)?\b",
    "violin": r"\bviolin\b",
    "matrix": r"\b(?:matrix|confusion)\b|矩阵",
    "network": r"\b(?:network|graph structure|node|edge)\b|网络图|节点|边",
    "tree": r"\b(?:tree|hierarchy)\b|树图|层级",
    "pipeline": r"\b(?:pipeline|workflow|framework|overview|procedure)\b|流程|管线|框架|总览",
    "architecture": r"\b(?:architecture|module|encoder|decoder|backbone)\b|架构|模块|编码器|解码器",
    "conceptual_diagram": r"\b(?:illustration|schematic|conceptual|diagram)\b|示意|机制图|概念图",
    "qualitative_grid": r"\b(?:qualitative|visual results|generated|examples?|samples?|outputs?)\b|定性|案例|示例|样例",
    "image_montage": r"\b(?:images?|videos?|frames?|montage)\b|图像|视频|帧|拼图",
    "screenshot": r"\b(?:screenshot|interface|webpage)\b",
    "map": r"\bmap\b",
    "pareto": r"\bpareto\b",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--resolution", type=int, default=96)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def clean_font(font: str) -> str:
    return re.sub(r"^[A-Z]{6}\+", "", font)


def is_bold(font: str) -> bool:
    return bool(re.search(r"bold|demi|semi|medi|black", font, re.I))


def median_or_blank(values: list[float]) -> float | str:
    return round(statistics.median(values), 3) if values else ""


def find_caption(lines: list[dict[str, Any]], label: str) -> tuple[list[dict[str, Any]], int | None]:
    label_key = compact(label)
    variants = {label_key}
    number = re.search(r"\d+", label_key)
    if number:
        variants.add(compact(f"fig {number.group()}"))
    starts: list[int] = []
    contains: list[int] = []
    for index, line in enumerate(lines):
        key = compact(str(line["text"]))
        if any(key.startswith(variant) for variant in variants):
            starts.append(index)
        elif any(variant in key for variant in variants):
            contains.append(index)
    if not starts and not contains:
        return [], None
    start = starts[0] if starts else contains[0]
    caption = [lines[start]]
    base_chars = lines[start].get("chars") or []
    base_size = statistics.median(float(char["size"]) for char in base_chars) if base_chars else 9.0
    full_width = float(lines[start]["x1"]) - float(lines[start]["x0"]) > 260
    base_center = (float(lines[start]["x0"]) + float(lines[start]["x1"])) / 2
    for candidate in lines[start + 1 : start + 9]:
        previous = caption[-1]
        gap = float(candidate["top"]) - float(previous["bottom"])
        chars = candidate.get("chars") or []
        size = statistics.median(float(char["size"]) for char in chars) if chars else base_size
        center = (float(candidate["x0"]) + float(candidate["x1"])) / 2
        # Caption lines are normally set solid; the first body line after a
        # caption is separated by a paragraph-sized gap.  A permissive bound
        # here silently absorbs body prose and corrupts caption statistics.
        if gap > max(5.25, base_size * 0.58):
            break
        if size > base_size + 1.6:
            break
        if not full_width and abs(center - base_center) > 175:
            break
        text = str(candidate["text"]).strip()
        if re.match(r"^(?:\d+(?:\.\d+)*\s+)?[A-Z][A-Z\s]{4,}$", text):
            break
        caption.append(candidate)
    return caption, start


def caption_metrics(page: Any, caption: list[dict[str, Any]]) -> dict[str, object]:
    if not caption:
        return {
            "caption_found": 0,
            "caption_text": "",
            "caption_words": "",
            "caption_sentences": "",
            "caption_fonts": "",
            "caption_font_size_median": "",
            "caption_headline_bold": "",
            "caption_has_setup": "",
            "caption_has_encoding_key": "",
            "caption_has_main_finding": "",
            "caption_has_uncertainty_definition": "",
            "caption_has_appendix_pointer": "",
            "caption_self_contained_score": "",
        }
    raw_box = caption_bbox(caption)
    box = (
        (
            max(float(page.bbox[0]), raw_box[0]),
            max(float(page.bbox[1]), raw_box[1]),
            min(float(page.bbox[2]), raw_box[2]),
            min(float(page.bbox[3]), raw_box[3]),
        )
        if raw_box
        else None
    )
    extracted = page.crop(box).extract_text(x_tolerance=2, y_tolerance=3) if box else ""
    text = re.sub(r"\s+", " ", extracted or " ".join(str(line["text"]).strip() for line in caption)).strip()
    chars = [char for line in caption for char in (line.get("chars") or []) if str(char.get("text", "")).strip()]
    fonts = Counter(clean_font(str(char.get("fontname", ""))) for char in chars)
    sizes = [float(char["size"]) for char in chars if char.get("size")]
    colon = next((index for index, char in enumerate(chars) if char.get("text") == ":"), -1)
    period = next((index for index, char in enumerate(chars[colon + 1 :], start=colon + 1) if char.get("text") == "."), len(chars))
    headline_chars = chars[colon + 1 : period] if colon >= 0 else chars[: min(80, len(chars))]
    bold_share = sum(is_bold(str(char.get("fontname", ""))) for char in headline_chars) / max(1, len(headline_chars))
    setup = bool(SETUP_RE.search(text))
    encoding = bool(ENCODING_RE.search(text))
    finding = bool(FINDING_RE.search(text))
    uncertainty = bool(UNCERTAINTY_RE.search(text))
    score = int(setup) + int(encoding) + int(finding) + int(uncertainty)
    return {
        "caption_found": 1,
        "caption_text": re.sub(r"\s+", " ", text),
        "caption_words": len(re.findall(r"\b\w+[\w'-]*\b", text)),
        "caption_sentences": len(re.findall(r"[.!?](?:\s|$)", text)) or 1,
        "caption_fonts": "|".join(font for font, _ in fonts.most_common(5)),
        "caption_font_size_median": median_or_blank(sizes),
        "caption_headline_bold": int(bold_share >= 0.55),
        "caption_has_setup": int(setup),
        "caption_has_encoding_key": int(encoding),
        "caption_has_main_finding": int(finding),
        "caption_has_uncertainty_definition": int(uncertainty),
        "caption_has_appendix_pointer": int(bool(APPENDIX_RE.search(text))),
        "caption_self_contained_score": score,
    }


def caption_bbox(caption: list[dict[str, Any]]) -> tuple[float, float, float, float] | None:
    if not caption:
        return None
    return (
        min(float(line["x0"]) for line in caption),
        min(float(line["top"]) for line in caption),
        max(float(line["x1"]) for line in caption),
        max(float(line["bottom"]) for line in caption),
    )


def object_bbox(
    page: Any,
    kind: str,
    caption: list[dict[str, Any]],
    detected_tables: list[Any] | None = None,
) -> tuple[float, float, float, float] | None:
    box = caption_bbox(caption)
    if box is None:
        return None
    x0, top, x1, bottom = box
    center = (x0 + x1) / 2
    full = x1 - x0 > page.width * 0.52
    if full:
        left, right = max(18.0, x0 - 18), min(float(page.width) - 18, x1 + 18)
    elif center < page.width / 2:
        left, right = 24.0, page.width / 2 - 5
    else:
        left, right = page.width / 2 + 5, page.width - 24.0
    if kind == "figure":
        return (left, max(20.0, top - page.height * 0.39), right, max(22.0, top - 2))
    tables = [table.bbox for table in (detected_tables or [])]
    below = [bbox for bbox in tables if bbox[1] >= top - 3 and bbox[0] < right and bbox[2] > left]
    if below:
        nearest = min(below, key=lambda bbox: abs(float(bbox[1]) - bottom))
        return tuple(float(value) for value in nearest)
    return (left, min(page.height - 22, bottom + 2), right, min(page.height - 20, bottom + page.height * 0.32))


def width_class(page: Any, box: tuple[float, float, float, float] | None) -> str:
    if box is None:
        return "unknown"
    ratio = (box[2] - box[0]) / page.width
    if ratio >= 0.78:
        return "page_width"
    if ratio >= 0.56:
        return "double_column"
    if ratio >= 0.34:
        return "single_column"
    return "inset"


def internal_typography(page: Any, box: tuple[float, float, float, float] | None) -> tuple[str, float | str, float | str, float | str]:
    if box is None:
        return "", "", "", ""
    chars = [
        char
        for char in page.chars
        if float(char["x0"]) >= box[0]
        and float(char["x1"]) <= box[2]
        and float(char["top"]) >= box[1]
        and float(char["bottom"]) <= box[3]
        and str(char.get("text", "")).strip()
    ]
    fonts = Counter(clean_font(str(char.get("fontname", ""))) for char in chars)
    sizes = [float(char["size"]) for char in chars if char.get("size")]
    return (
        "|".join(font for font, _ in fonts.most_common(6)),
        round(min(sizes), 3) if sizes else "",
        median_or_blank(sizes),
        round(max(sizes), 3) if sizes else "",
    )


def palette_metrics(
    page: Any,
    page_image: Image.Image | None,
    box: tuple[float, float, float, float] | None,
) -> tuple[str, int | str, str, float | str]:
    if box is None or box[2] <= box[0] or box[3] <= box[1]:
        return "", "", "", ""
    if page_image is None:
        return "", "", "", ""
    scale_x = page_image.width / float(page.width)
    scale_y = page_image.height / float(page.height)
    crop_box = (
        max(0, int(box[0] * scale_x)),
        max(0, int(box[1] * scale_y)),
        min(page_image.width, int(math.ceil(box[2] * scale_x))),
        min(page_image.height, int(math.ceil(box[3] * scale_y))),
    )
    if crop_box[2] <= crop_box[0] or crop_box[3] <= crop_box[1]:
        return "", "", "", ""
    image = page_image.crop(crop_box).convert("RGB")
    image.thumbnail((600, 600), Image.Resampling.LANCZOS)
    pixels = list(image.get_flattened_data())
    nonwhite = [pixel for pixel in pixels if min(pixel) < 244]
    if not nonwhite:
        return "grayscale", 0, "", 1.0
    chromatic = [pixel for pixel in nonwhite if max(pixel) - min(pixel) >= 16 and max(pixel) >= 55]
    chromatic_share = len(chromatic) / len(nonwhite)
    if chromatic_share < 0.025:
        return "grayscale", 0, "", round(chromatic_share, 4)
    strip = Image.new("RGB", (len(chromatic), 1))
    strip.putdata(chromatic)
    quantized = strip.quantize(colors=10, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette() or []
    colors = quantized.getcolors() or []
    ranked: list[tuple[int, str]] = []
    for count, index in colors:
        offset = index * 3
        rgb = tuple(palette[offset : offset + 3])
        if len(rgb) != 3:
            continue
        ranked.append((count, "#" + "".join(f"{value:02X}" for value in rgb)))
    ranked.sort(reverse=True)
    threshold = max(2, int(len(chromatic) * 0.018))
    selected = [hex_value for count, hex_value in ranked if count >= threshold][:8]
    if not selected:
        selected = [hex_value for _, hex_value in ranked[:3]]
    return "color", len(selected), "|".join(selected), round(chromatic_share, 4)


def classify_types(text: str, kind: str) -> str:
    if kind != "figure":
        return "table"
    types = [name for name, pattern in TYPE_PATTERNS.items() if re.search(pattern, text, re.I)]
    return "|".join(types or ["other"])


def panel_count(text: str) -> int:
    labels = set(re.findall(r"\(([a-z])\)", text.lower()))
    return max(1, len(labels))


def object_panel_count(page: Any, box: tuple[float, float, float, float] | None, caption_text: str) -> int:
    labels = set(re.findall(r"\(([a-z])\)", caption_text.lower()))
    if box is not None:
        try:
            inside = page.crop(box).extract_text(x_tolerance=2, y_tolerance=3) or ""
            labels.update(re.findall(r"(?:^|\s)\(?([a-z])\)(?=\s|$|[A-Z])", inside.lower()))
        except Exception:
            pass
    return max(1, len(labels))


def complexity_score(types: str, panels: int, caption_words: int | str, purpose: str) -> int:
    score = 1
    if panels >= 2:
        score += 1
    if panels >= 5:
        score += 1
    if any(token in types for token in ("heatmap", "matrix", "network", "qualitative_grid", "image_montage")):
        score += 1
    if isinstance(caption_words, int) and caption_words >= 80:
        score += 1
    if len(purpose) >= 180:
        score += 1
    return min(5, score)


def table_geometry(
    page: Any,
    box: tuple[float, float, float, float] | None,
    detected_tables: list[Any] | None = None,
) -> tuple[int | str, int | str, int | str]:
    if box is None:
        return "", "", ""
    try:
        candidates = [
            table
            for table in (detected_tables or [])
            if abs(float(table.bbox[0]) - box[0]) < 12
            and abs(float(table.bbox[1]) - box[1]) < 12
            and abs(float(table.bbox[2]) - box[2]) < 12
        ]
        if not candidates:
            return "", "", ""
        extracted = candidates[0].extract()
        rows = len(extracted)
        columns = max((len(row) for row in extracted), default=0)
        header_levels = 1
        if rows >= 2 and any(cell is None or "\n" in str(cell) for cell in extracted[0]):
            header_levels = 2
        return rows or "", columns or "", header_levels
    except Exception:
        return "", "", ""


def pdf_fonts(pdf_path: Path) -> list[str]:
    completed = subprocess.run(
        ["pdffonts", str(pdf_path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
        timeout=30,
    )
    if completed.returncode != 0:
        return []
    fonts = []
    for line in completed.stdout.splitlines()[2:]:
        fields = line.split()
        if fields:
            fonts.append(clean_font(fields[0]))
    return sorted(set(fonts))


def resolve_pdf_path(paper_id: str, metadata: dict[str, str]) -> Path:
    candidates = [metadata.get("pdf_path", "")]
    reading_path = ROOT / "readings" / f"{paper_id}.json"
    if reading_path.exists():
        reading = json.loads(reading_path.read_text(encoding="utf-8"))
        source_files = reading.get("source_files")
        if isinstance(source_files, dict):
            candidates.append(str(source_files.get("pdf", "")))
    candidates.extend((f"corpus/pdfs/{paper_id}.pdf", f"corpus/preprints/{paper_id}.pdf"))
    for candidate in candidates:
        if candidate and (ROOT / candidate).exists():
            return ROOT / candidate
    raise FileNotFoundError(f"no local PDF found for {paper_id}: {candidates}")


def main() -> None:
    args = parse_args()
    selected_ids = set(args.paper_id)
    paper_meta = {row["paper_id"]: row for row in read_csv(PAPERS)}
    visual_rows = [row for row in read_csv(VISUALS) if row["kind"] in {"figure", "table"}]
    if selected_ids:
        visual_rows = [row for row in visual_rows if row["paper_id"] in selected_ids]
    by_paper: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in visual_rows:
        by_paper[row["paper_id"]].append(row)

    object_rows: list[dict[str, object]] = []
    paper_rows: list[dict[str, object]] = []
    for paper_index, (paper_id, objects) in enumerate(sorted(by_paper.items()), start=1):
        pdf_path = resolve_pdf_path(paper_id, paper_meta[paper_id])
        counters: Counter[str] = Counter()
        caption_words: list[int] = []
        internal_sizes: list[float] = []
        palette_counter: Counter[str] = Counter()
        with pdfplumber.open(pdf_path) as pdf:
            objects_by_page: dict[int, list[dict[str, str]]] = defaultdict(list)
            for visual in objects:
                objects_by_page[int(float(visual["page"]))].append(visual)
            for page_number, page_objects in sorted(objects_by_page.items()):
                if not 1 <= page_number <= len(pdf.pages):
                    continue
                page = pdf.pages[page_number - 1]
                lines = page.extract_text_lines(return_chars=True)
                detected_tables = page.find_tables() if any(item["kind"] == "table" for item in page_objects) else []
                try:
                    page_image = page.to_image(resolution=args.resolution, antialias=True).original.convert("RGB")
                except Exception:
                    page_image = None
                for visual in sorted(page_objects, key=lambda row: (row["kind"], row["label"])):
                    caption, _ = find_caption(lines, visual["label"])
                    caption_data = caption_metrics(page, caption)
                    box = object_bbox(page, visual["kind"], caption, detected_tables)
                    fonts, size_min, size_median, size_max = internal_typography(page, box)
                    color_mode, color_count, palette, chromatic_share = palette_metrics(page, page_image, box)
                    text = f"{caption_data['caption_text']} {visual['purpose']}"
                    types = classify_types(text, visual["kind"])
                    panels = object_panel_count(page, box, str(caption_data["caption_text"]))
                    complexity = complexity_score(types, panels, caption_data["caption_words"], visual["purpose"])
                    table_rows, table_columns, header_levels = (
                        table_geometry(page, box, detected_tables) if visual["kind"] == "table" else ("", "", "")
                    )
                    if caption_data["caption_found"]:
                        counters["caption_found"] += 1
                        caption_words.append(int(caption_data["caption_words"]))
                        for field in (
                            "caption_headline_bold",
                            "caption_has_setup",
                            "caption_has_encoding_key",
                            "caption_has_main_finding",
                            "caption_has_uncertainty_definition",
                            "caption_has_appendix_pointer",
                        ):
                            counters[field] += int(caption_data[field])
                    if isinstance(size_median, float):
                        internal_sizes.append(size_median)
                    for color in str(palette).split("|"):
                        if color:
                            palette_counter[color] += 1
                    counters[f"kind_{visual['kind']}"] += 1
                    counters[f"module_{visual['module']}"] += 1
                    counters[f"width_{width_class(page, box)}"] += 1
                    counters[f"color_{color_mode}"] += 1
                    for figure_type in types.split("|"):
                        counters[f"type_{figure_type}"] += 1
                    object_rows.append(
                        {
                            "paper_id": paper_id,
                            "conference": visual["conference"],
                            "analysis_stratum": visual["analysis_stratum"],
                            "sample_cohort": visual["sample_cohort"],
                            "kind": visual["kind"],
                            "module": visual["module"],
                            "placement": "appendix" if visual["module"] == "appendix" else "main",
                            "label": visual["label"],
                            "page": page_number,
                            "purpose": visual["purpose"],
                            "width": width_class(page, box),
                            "bbox": "|".join(f"{value:.2f}" for value in box) if box else "",
                            "types_auto": types,
                            "panels_auto": panels,
                            "complexity_auto": complexity,
                            **caption_data,
                            "internal_fonts": fonts,
                            "internal_font_size_min": size_min,
                            "internal_font_size_median": size_median,
                            "internal_font_size_max": size_max,
                            "color_mode_auto": color_mode,
                            "color_count_auto": color_count,
                            "palette_hex_auto": palette,
                            "chromatic_pixel_share": chromatic_share,
                            "table_rows_auto": table_rows,
                            "table_columns_auto": table_columns,
                            "table_header_levels_auto": header_levels,
                        }
                    )
                if page_image is not None:
                    page_image.close()
                flush_cache = getattr(page, "flush_cache", None)
                if callable(flush_cache):
                    flush_cache()
        total = len(objects)
        found = counters["caption_found"]
        paper_rows.append(
            {
                "paper_id": paper_id,
                "conference": objects[0]["conference"],
                "analysis_stratum": objects[0]["analysis_stratum"],
                "sample_cohort": objects[0]["sample_cohort"],
                "figures": counters["kind_figure"],
                "tables": counters["kind_table"],
                "visual_objects": total,
                "caption_found": found,
                "caption_coverage": round(found / total, 6) if total else 0,
                "caption_words_mean": round(statistics.fmean(caption_words), 3) if caption_words else "",
                "caption_words_median": median_or_blank([float(value) for value in caption_words]),
                "caption_headline_bold_share": round(counters["caption_headline_bold"] / found, 6) if found else "",
                "caption_setup_share": round(counters["caption_has_setup"] / found, 6) if found else "",
                "caption_encoding_key_share": round(counters["caption_has_encoding_key"] / found, 6) if found else "",
                "caption_main_finding_share": round(counters["caption_has_main_finding"] / found, 6) if found else "",
                "caption_uncertainty_share": round(counters["caption_has_uncertainty_definition"] / found, 6) if found else "",
                "internal_font_size_median": median_or_blank(internal_sizes),
                "dominant_palette_hex": "|".join(color for color, _ in palette_counter.most_common(8)),
                "color_object_share": round(counters["color_color"] / total, 6) if total else 0,
                "single_column_share": round(counters["width_single_column"] / total, 6) if total else 0,
                "page_or_double_width_share": round((counters["width_page_width"] + counters["width_double_column"]) / total, 6) if total else 0,
                "pdf_fonts": "|".join(pdf_fonts(pdf_path)),
            }
        )
        if paper_index % 20 == 0:
            print(f"processed {paper_index}/{len(by_paper)} papers")
    if object_rows:
        write_csv(OBJECT_OUTPUT, object_rows)
    if paper_rows:
        write_csv(PAPER_OUTPUT, paper_rows)
    print(f"wrote {OBJECT_OUTPUT.relative_to(ROOT)} ({len(object_rows)} objects)")
    print(f"wrote {PAPER_OUTPUT.relative_to(ROOT)} ({len(paper_rows)} papers)")


if __name__ == "__main__":
    main()
