"""Data-backed Matplotlib defaults for an ICLR two-column paper."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import matplotlib as mpl
import matplotlib.pyplot as plt


TEXT_WIDTH_IN = 5.50
COLUMN_WIDTH_IN = 2.63

PALETTE = {
    "blue": "#1F77B4",
    "orange": "#FF7F0E",
    "green": "#2CA02C",
    "red": "#D62728",
    "purple": "#9467BD",
    "gray": "#4D4D4D",
    "light_gray": "#D9D9D9",
}
SERIES_COLORS = [
    PALETTE["blue"],
    PALETTE["orange"],
    PALETTE["green"],
    PALETTE["red"],
    PALETTE["purple"],
]
SERIES_MARKERS = ["o", "s", "^", "D", "v"]
SERIES_LINESTYLES = ["-", "--", "-.", ":", (0, (5, 1))]


def apply_iclr_style() -> None:
    """Apply the cohort's median typography and line geometry."""

    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": [
                "Nimbus Roman No9 L",
                "Times New Roman",
                "Times",
                "DejaVu Serif",
            ],
            "mathtext.fontset": "stix",
            "font.size": 8.0,
            "axes.titlesize": 8.5,
            "axes.titleweight": "bold",
            "axes.labelsize": 8.0,
            "axes.linewidth": 0.7,
            "axes.prop_cycle": mpl.cycler(color=SERIES_COLORS),
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "xtick.major.width": 0.6,
            "ytick.major.width": 0.6,
            "xtick.major.size": 2.5,
            "ytick.major.size": 2.5,
            "legend.fontsize": 7.5,
            "legend.frameon": False,
            "legend.handlelength": 1.8,
            "legend.handletextpad": 0.45,
            "legend.columnspacing": 0.9,
            "lines.linewidth": 1.0,
            "lines.markersize": 3.5,
            "grid.color": "#B0B0B0",
            "grid.linewidth": 0.45,
            "grid.alpha": 0.32,
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.02,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.hashsalt": "elite-ml-paper-anatomy-2026",
            "svg.fonttype": "none",
        }
    )


def figure_size(
    span: Literal["single", "full"] = "single",
    *,
    aspect: float = 0.66,
) -> tuple[float, float]:
    width = COLUMN_WIDTH_IN if span == "single" else TEXT_WIDTH_IN
    return width, width * aspect


def style_axis(
    ax: mpl.axes.Axes,
    *,
    grid: Literal["none", "x", "y", "both"] = "both",
) -> None:
    """Use a light comparison grid and remove non-data ink."""

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_axisbelow(True)
    if grid == "none":
        ax.grid(False)
    elif grid == "both":
        ax.grid(True, axis="both")
    else:
        ax.grid(True, axis=grid)


def panel_label(ax: mpl.axes.Axes, label: str) -> None:
    ax.text(
        -0.12,
        1.04,
        label,
        transform=ax.transAxes,
        fontsize=8.5,
        fontweight="bold",
        va="bottom",
        ha="left",
    )


def plot_series(
    ax: mpl.axes.Axes,
    x,
    y,
    *,
    index: int,
    label: str,
    **kwargs,
):
    """Plot one series with color, marker, and line-style redundancy."""

    return ax.plot(
        x,
        y,
        color=SERIES_COLORS[index % len(SERIES_COLORS)],
        marker=SERIES_MARKERS[index % len(SERIES_MARKERS)],
        linestyle=SERIES_LINESTYLES[index % len(SERIES_LINESTYLES)],
        label=label,
        **kwargs,
    )


def save_figure(
    fig: mpl.figure.Figure,
    path: str | Path,
    *,
    close: bool = True,
) -> None:
    """Write a stable PDF/SVG artifact without invocation-time metadata."""

    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    metadata = None
    if destination.suffix == ".pdf":
        metadata = {"CreationDate": None, "ModDate": None}
    elif destination.suffix == ".svg":
        metadata = {"Date": None}
    fig.savefig(destination, metadata=metadata)
    if destination.suffix == ".svg":
        lines = destination.read_text(encoding="utf-8").splitlines()
        destination.write_text(
            "\n".join(line.rstrip() for line in lines) + "\n",
            encoding="utf-8",
        )
    if close:
        plt.close(fig)
