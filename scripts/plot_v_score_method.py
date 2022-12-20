#!/usr/bin/env python3

from math import log10
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec

from collect import data_key, filter_energy_var, get_data, known_tags
from plot_v_score import check_exact_energy, get_exact_energies, get_v_score, ham_colors
from plot_v_score_ham import get_lattice, lat_types

out_filename = "./v_score_method.pdf"

v_score_exact_threshold = 1e-12
v_score_exact_pos = 1e-15


def show_tag(tag_lat):
    tag, _ = tag_lat
    tag = tag.upper()
    tag += "      "
    return tag


def main():
    data = get_data()
    exact_energies = get_exact_energies(data)
    data = filter_energy_var(data)
    data.sort(key=data_key)

    data_new = []
    for row in data:
        if check_exact_energy(exact_energies, row):
            continue

        tag = row[6]
        if tag == "exact_qmc":
            continue
        if tag in ["rbm", "rnn"]:
            tag = "nqs"

        ham_attr = row[:2]
        lattice = get_lattice(ham_attr)
        if lattice == "rectangular":
            lattice = "square"
        v_score = get_v_score(row, v_score_exact_threshold, v_score_exact_pos)
        data_new.append((row[0], (tag, lattice), v_score))
    data = data_new

    tag_lats = sorted(
        {x[1] for x in data},
        key=lambda x: (list(lat_types).index(x[1]), known_tags.index(x[0])),
    )

    xs = []
    ys = []
    cs = []
    for ham_type, tag_lat, v_score in data:
        xs.append(v_score)
        ys.append(tag_lats.index(tag_lat))
        cs.append(ham_colors[ham_type])

    fig = plt.figure(figsize=(6, 4))
    xlim1 = (1.5e-16, 6.5e-4)
    xlim2 = (1.5e-4, 4.5e-1)
    gs = GridSpec(
        1,
        2,
        wspace=0.02,
        width_ratios=[log10(xlim1[1] / xlim1[0]), log10(xlim2[1] / xlim2[0]) * 12],
    )
    ax = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    for x, y, c in zip(xs, ys, cs):
        if x < xlim2[0]:
            ax.scatter(x, y, edgecolor=c, facecolor="none", linewidth=0.5)
        else:
            ax2.scatter(x, y, edgecolor=c, facecolor="none", linewidth=0.5)

    y_max = len(tag_lats)
    for i in range(y_max // 2 + 1):
        ax.axhspan(i * 2 - 0.5, i * 2 + 0.5, color="0.95", zorder=0.3)
        ax2.axhspan(i * 2 - 0.5, i * 2 + 0.5, color="0.95", zorder=0.3)

    fig.supxlabel("V-score")
    ax.set_xscale("log")
    ax2.set_xscale("log")
    ax.set_xlim(*xlim1)
    ax2.set_xlim(*xlim2)
    ax.set_ylim(-1, y_max)
    ax2.set_ylim(-1, y_max)
    ax.set_xticks([1e-12, 1e-8, 1e-4])
    ax.set_xticks([v_score_exact_pos], minor=True)
    ax.set_xticklabels(["..."], minor=True)
    ax.xaxis.set_tick_params(which="minor", pad=2)
    ax.spines.right.set_visible(False)
    ax2.spines.left.set_visible(False)

    ax.set_yticks(range(y_max))
    ax.set_yticklabels([show_tag(x) for x in tag_lats], fontsize="small")
    ax.yaxis.set_tick_params(length=0)

    ax2.yaxis.set_tick_params(which="both", length=0)
    ax2.set_yticklabels([])

    d = 2
    kwargs = dict(
        clip_on=False,
        linestyle="",
        marker=[(-1, -d), (1, d)],
        markeredgecolor="k",
        markeredgewidth=0.8,
        markersize=6,
    )
    ax.plot([1, 1], [0, 1], transform=ax.transAxes, **kwargs)
    ax2.plot([0, 0], [0, 1], transform=ax2.transAxes, **kwargs)

    ax.grid(axis="x", color="0.8", linestyle="--")
    ax2.grid(axis="x", color="0.8", linestyle="--")
    ax.set_axisbelow(True)
    ax2.set_axisbelow(True)

    ax_symb = ax.twinx()
    ax_symb.spines.left.set_position(("outward", 10))
    ax_symb.spines.left.set_visible(False)
    ax_symb.spines.right.set_visible(False)
    ax_symb.spines.top.set_visible(False)
    ax_symb.spines.bottom.set_visible(False)
    ax_symb.yaxis.set_ticks_position("left")
    ax_symb.yaxis.set_tick_params(length=0)
    ax_symb.set_ylim(-1, y_max)
    ax_symb.set_yticks(range(y_max))
    ax_symb.set_yticklabels(
        [lat_types[x[1]] for x in tag_lats],
        font=Path("icons/varbench_icons.ttf"),
        fontsize="small",
    )

    # fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
