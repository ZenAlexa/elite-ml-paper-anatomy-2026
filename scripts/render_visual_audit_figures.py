#!/usr/bin/env python3
"""Render paper-normalized summary figures for the 250-paper visual audit."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from templates.visuals.iclr_style import (  # noqa: E402
    PALETTE,
    apply_iclr_style,
    figure_size,
    panel_label,
    save_figure,
    style_axis,
)


TABLES = ROOT / "reports" / "tables"
FIGURES = ROOT / "reports" / "figures"


def read_csv(name: str) -> list[dict[str, str]]:
    with (TABLES / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def save(fig: plt.Figure, stem: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    for suffix in (".svg", ".pdf"):
        save_figure(fig, FIGURES / f"{stem}{suffix}", close=False)
    plt.close(fig)


def object_count_figure() -> None:
    rows = read_csv("visual_audit_paper_summary.csv")
    apply_iclr_style()
    fig, axes = plt.subplots(1, 2, figsize=figure_size("full", aspect=0.43))
    count_fields = ["main_figures", "main_tables", "appendix_figures", "appendix_tables"]
    labels = ["Main\nfigures", "Main\ntables", "Appendix\nfigures", "Appendix\ntables"]
    values = [[float(row[field]) for row in rows] for field in count_fields]
    box = axes[0].boxplot(values, tick_labels=labels, widths=0.58, patch_artist=True, showfliers=False)
    colors = [PALETTE["blue"], PALETTE["orange"], PALETTE["blue"], PALETTE["orange"]]
    hatches = ["", "//", "..", "xx"]
    for patch, color, hatch in zip(box["boxes"], colors, hatches):
        patch.set(facecolor=color, alpha=0.25, edgecolor=color, hatch=hatch, linewidth=0.8)
    for median in box["medians"]:
        median.set(color=PALETTE["gray"], linewidth=1.2)
    axes[0].set_ylabel("Objects per paper")
    style_axis(axes[0], grid="y")
    panel_label(axes[0], "a")

    statuses: dict[str, int] = {}
    for row in rows:
        statuses[row["source_status"]] = statuses.get(row["source_status"], 0) + 1
    order = [
        "exact_visual_source",
        "partial_visual_source",
        "repository_without_visual_source",
        "no_public_source_found",
    ]
    names = ["Exact", "Partial", "Repo only", "No source"]
    counts = [statuses.get(status, 0) for status in order]
    bars = axes[1].barh(names[::-1], counts[::-1], color=PALETTE["blue"], alpha=0.82)
    for bar, count in zip(bars, counts[::-1]):
        axes[1].text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, str(count), va="center")
    axes[1].set_xlabel("Papers")
    axes[1].set_xlim(0, max(counts or [1]) * 1.14)
    style_axis(axes[1], grid="x")
    panel_label(axes[1], "b")
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.21, top=0.96, wspace=0.45)
    save(fig, "visual_audit_counts_and_sources")


def prevalence_figure() -> None:
    rows = read_csv("visual_design_categorical_summary.csv")
    wanted = [
        ("kind", "figure", "Figure"),
        ("kind", "table", "Table"),
        ("types", "conceptual_diagram", "Conceptual diagram"),
        ("types", "line", "Line chart"),
        ("types", "pipeline", "Pipeline"),
        ("types", "qualitative_grid", "Qualitative grid"),
        ("purpose", "main_comparison", "Main comparison"),
        ("purpose", "headline", "Headline evidence"),
        ("purpose", "robustness", "Robustness"),
        ("purpose", "method_interface", "Method interface"),
        ("purpose", "theory_mechanism", "Theory / mechanism"),
        ("purpose", "mechanism", "Mechanism diagnostic"),
        ("purpose", "ablation", "Ablation"),
        ("purpose", "experimental_design", "Experimental design"),
        ("purpose", "qualitative_evidence", "Qualitative evidence"),
        ("purpose", "reproduction", "Reproduction"),
        ("purpose", "efficiency_cost", "Efficiency / cost"),
    ]
    lookup = {(row["dimension"], row["value"]): row for row in rows}
    labels = [label for _, _, label in wanted]
    values = [100 * float(lookup[(dimension, value)]["conference_equal_paper_prevalence"]) for dimension, value, _ in wanted]
    apply_iclr_style()
    fig, ax = plt.subplots(figsize=figure_size("full", aspect=0.88))
    bars = ax.barh(labels[::-1], values[::-1], color=PALETTE["blue"], alpha=0.82)
    for index, bar in enumerate(bars):
        bar.set_hatch(["", "//", ".."][(len(bars) - index - 1) % 3])
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2, f"{bar.get_width():.0f}%", va="center")
    ax.axvline(60, color=PALETTE["red"], linestyle="--", linewidth=0.9)
    ax.text(60.7, len(labels) - 0.45, "60% inclusion rule", color=PALETTE["red"], va="top")
    ax.set_xlim(0, 105)
    ax.set_xlabel("Conference-equal paper prevalence (%)")
    style_axis(ax, grid="x")
    fig.subplots_adjust(left=0.29, right=0.98, bottom=0.17, top=0.98)
    save(fig, "visual_audit_core_prevalence")


def judgment_figure() -> None:
    rows = read_csv("visual_judgment_theme_summary.csv")
    selected = sorted(rows, key=lambda row: float(row["conference_equal_paper_prevalence"]), reverse=True)
    reusable = [row for row in selected if row["source"] == "reusable"][:5]
    failures = [row for row in selected if row["source"] == "failure"][:5]
    apply_iclr_style()
    fig, axes = plt.subplots(2, 1, figsize=figure_size("full", aspect=0.80))
    for ax, items, color, title in (
        (axes[0], reusable, PALETTE["blue"], "Reusable systems"),
        (axes[1], failures, PALETTE["red"], "Recurring failure patterns"),
    ):
        labels = [row["theme"].replace("_", " ") for row in items][::-1]
        values = [100 * float(row["conference_equal_paper_prevalence"]) for row in items][::-1]
        bars = ax.barh(labels, values, color=color, alpha=0.78)
        for index, bar in enumerate(bars):
            bar.set_hatch(["", "//", "..", "xx", "++"][index])
            ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2, f"{bar.get_width():.0f}%", va="center")
        ax.set_title(title)
        ax.set_xlim(0, 105)
        ax.set_xlabel("Paper prevalence (%)")
        style_axis(ax, grid="x")
    panel_label(axes[0], "a")
    panel_label(axes[1], "b")
    fig.subplots_adjust(left=0.35, right=0.98, bottom=0.10, top=0.94, hspace=0.72)
    save(fig, "visual_audit_reusable_and_failure_patterns")


def evidence_relation_figure() -> None:
    rows = read_csv("visual_evidence_relation_summary.csv")
    rows.sort(key=lambda row: float(row["conference_equal_paper_prevalence"]), reverse=True)
    apply_iclr_style()
    fig, ax = plt.subplots(figsize=figure_size("full", aspect=0.63))
    labels = [row["theme"].replace("_", " ") for row in rows][::-1]
    values = [100 * float(row["conference_equal_paper_prevalence"]) for row in rows][::-1]
    bars = ax.barh(labels, values, color=PALETTE["blue"], alpha=0.82)
    for index, bar in enumerate(bars):
        bar.set_hatch(["", "//", "..", "xx"][(len(bars) - index - 1) % 4])
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2, f"{bar.get_width():.0f}%", va="center")
    ax.axvline(60, color=PALETTE["red"], linestyle="--", linewidth=0.9)
    ax.set_xlim(0, 105)
    ax.set_xlabel("Conference-equal paper prevalence (%)")
    style_axis(ax, grid="x")
    fig.subplots_adjust(left=0.38, right=0.98, bottom=0.14, top=0.98)
    save(fig, "visual_audit_evidence_relations")


def main() -> None:
    object_count_figure()
    prevalence_figure()
    judgment_figure()
    evidence_relation_figure()
    print("rendered 4 visual-audit figure families (PDF/SVG)")


if __name__ == "__main__":
    main()
