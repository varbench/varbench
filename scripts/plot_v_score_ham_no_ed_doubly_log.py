#!/usr/bin/env python3

from matplotlib import pyplot as plt

from collect import data_key, filter_energy_var, get_data, ham_types
from plot_v_score import get_exact_energies, get_v_score, ham_colors, scale_doubly_log
from plot_v_score_ham import (
    get_ax_left_yticks,
    get_key,
    ham_attr_key,
    lat_types,
    show_ham_attr,
)

out_filename = "./v_score_ham_no_ed_doubly_log.pdf"

v_score_exact_threshold = 1e-12
v_score_exact_pos = 1e-16


def main():
    data = get_data()
    exact_energies = get_exact_energies(data)
    data = filter_energy_var(data)
    data.sort(key=data_key)

    v_scores = {}
    energies = {}
    for row in data:
        ham_attr = row[:2]
        if ham_attr in exact_energies and exact_energies[ham_attr][1] == "ed":
            continue

        energy = row[3]
        key = get_key(row)
        v_score = get_v_score(row, v_score_exact_threshold, v_score_exact_pos)

        if key not in v_scores or energy < energies[key]:
            v_scores[key] = v_score
            energies[key] = energy

    ham_attrs = sorted({x[0] for x in v_scores}, key=ham_attr_key)

    xs = []
    ys = []
    cs = []
    for (ham_attr, _), v_score in v_scores.items():
        xs.append(v_score)
        ys.append(ham_attrs.index(ham_attr))
        cs.append(ham_colors[ham_attr[0]])

    fig, ax = plt.subplots(figsize=(6 * 0.8, 4 * 0.8))

    for x, y, c in zip(xs, ys, cs):
        ax.scatter(scale_doubly_log(x), y, edgecolor=c, facecolor="none", linewidth=0.5)

    y_max = len(ham_attrs)
    for i in range(y_max // 2 + 1):
        ax.axhspan(i * 2 - 0.5, i * 2 + 0.5, color="0.95", zorder=0.3)

    ax.set_xlabel("V-score")
    ax.set_xlim(-3.7, 0.3)
    ax.set_ylim(-1, y_max)
    ax.set_xticks([-3, -2, -1, 0])
    ax.set_xticklabels(
        [
            "$10^{-8}$",
            "$10^{-4}$",
            "$10^{-2}$",
            "$10^{-1}$",
        ]
    )

    ax.set_yticks(range(y_max))
    ax.set_yticklabels(
        [show_ham_attr(x) for x in ham_attrs], fontfamily="monospace", fontsize="small"
    )
    ax.yaxis.set_tick_params(length=0)
    for i, text in enumerate(ax.get_yticklabels()):
        text.set_color(ham_colors[ham_attrs[i][0]])

    ax.grid(axis="x", color="0.8", linestyle="--")
    ax.set_axisbelow(True)

    ax_symb = ax.twinx()
    ax_symb.spines.left.set_position(("outward", 11))
    ax_symb.spines.left.set_visible(False)
    ax_symb.spines.right.set_visible(False)
    ax_symb.spines.top.set_visible(False)
    ax_symb.spines.bottom.set_visible(False)
    ax_symb.yaxis.set_ticks_position("left")
    ax_symb.yaxis.set_tick_params(length=0)
    ax_symb.set_ylim(-1, y_max)
    ax_symb.set_yticks(range(y_max))
    ax_symb.set_yticklabels(
        [lat_types[x[1]] for x in ham_attrs],
        font="VarbenchIcons",
        fontsize="small",
    )
    for i, text in enumerate(ax_symb.get_yticklabels()):
        text.set_color(ham_colors[ham_attrs[i][0]])

    ax_left = ax.twinx()
    ax_left.spines.left.set_position(("outward", 42))
    ax_left.spines.left.set_visible(False)
    ax_left.spines.right.set_visible(False)
    ax_left.spines.top.set_visible(False)
    ax_left.spines.bottom.set_visible(False)
    ax_left.yaxis.set_ticks_position("left")
    ax_left.yaxis.set_tick_params(length=0)
    ax_left.set_ylim(-1, y_max)
    yticks = get_ax_left_yticks(ham_attrs)
    yticks[2] -= 0.5
    yticks[3] += 0.7
    yticks[4] -= 1
    yticks[5] -= 1
    ax_left.set_yticks(yticks)
    ax_left.set_yticklabels(
        ["TFIM", "Heisenberg", "$J_1$-$J_2$", "$t$-$V$", "Hubbard", "Impurity"],
        horizontalalignment="center",
        rotation=90,
        rotation_mode="anchor",
    )
    for i, text in enumerate(ax_left.get_yticklabels()):
        text.set_color(ham_colors[ham_types[i]])

    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
