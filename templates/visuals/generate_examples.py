#!/usr/bin/env python3
"""Render the reusable full-width result figure in PDF and SVG."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from iclr_style import (
    PALETTE,
    SERIES_COLORS,
    apply_iclr_style,
    figure_size,
    panel_label,
    plot_series,
    save_figure,
    style_axis,
)


def build(output: Path) -> None:
    apply_iclr_style()
    fig, axes = plt.subplots(1, 2, figsize=figure_size("full", aspect=0.42))
    budgets = [1, 2, 4, 8, 16]
    series = {
        "Ours": [61.0, 67.5, 73.2, 77.8, 80.1],
        "Baseline A": [58.2, 62.4, 66.3, 68.5, 69.1],
        "Baseline B": [56.8, 61.7, 68.0, 72.1, 74.0],
    }
    for index, (label, values) in enumerate(series.items()):
        plot_series(axes[0], budgets, values, index=index, label=label)
    spread = [1.4, 1.2, 1.0, 0.9, 0.8]
    ours = series["Ours"]
    axes[0].fill_between(
        budgets,
        [value - delta for value, delta in zip(ours, spread)],
        [value + delta for value, delta in zip(ours, spread)],
        color=PALETTE["blue"],
        alpha=0.18,
        linewidth=0,
    )
    axes[0].set_xscale("log", base=2)
    axes[0].set_xticks(budgets, [str(value) for value in budgets])
    axes[0].set_xlabel("Inference budget")
    axes[0].set_ylabel("Success rate (%)")
    axes[0].legend(loc="lower right")
    style_axis(axes[0], grid="both")
    panel_label(axes[0], "a")

    compute = [0.8, 1.3, 2.0, 3.1, 4.7]
    quality = [67.0, 72.4, 76.1, 78.2, 79.0]
    axes[1].plot(
        compute,
        quality,
        color=SERIES_COLORS[0],
        marker="o",
        linestyle="-",
    )
    axes[1].scatter([1.6, 2.7, 4.2], [68.2, 72.8, 75.0], color=SERIES_COLORS[1], marker="s", label="Baseline")
    axes[1].annotate(
        "Ours",
        xy=(compute[-1], quality[-1]),
        xytext=(-4, 4),
        textcoords="offset points",
        ha="right",
        color=SERIES_COLORS[0],
        fontweight="bold",
    )
    axes[1].set_xlabel("Compute (relative units)")
    axes[1].set_ylabel("Quality (%)")
    axes[1].legend(loc="lower right")
    style_axis(axes[1], grid="both")
    panel_label(axes[1], "b")

    fig.subplots_adjust(left=0.09, right=0.99, bottom=0.20, top=0.95, wspace=0.34)
    for suffix in (".pdf", ".svg"):
        save_path = output.with_suffix(suffix)
        save_figure(fig, save_path, close=False)
    plt.close(fig)


if __name__ == "__main__":
    build(Path(__file__).with_name("examples") / "main_result")
