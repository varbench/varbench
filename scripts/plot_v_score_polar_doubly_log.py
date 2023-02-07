#!/usr/bin/env python3

from math import pi

import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate

from collect import data_key, filter_energy_var, get_data
from plot_v_score import (
    check_exact_energy,
    get_exact_energies,
    get_exact_marker,
    get_legend,
    get_marker,
    get_plot_kwargs,
    get_v_score,
    ham_colors,
    scale_doubly_log,
    sort_v_scores,
)

out_filename = "./v_score_polar_doubly_log.pdf"

v_score_exact_threshold = 1e-12
v_score_exact_pos = 1e-20
theta0 = 0.5


def main():
    data = get_data()
    exact_energies = get_exact_energies(data)
    data = filter_energy_var(data)
    data.sort(key=data_key)

    v_scores = {}
    energies = {}
    data_new = []
    markers = []
    for row in data:
        if check_exact_energy(exact_energies, row):
            continue

        ham_attr = row[:2]
        energy = row[3]
        v_score = get_v_score(row, v_score_exact_threshold, v_score_exact_pos)
        if ham_attr not in v_scores or energy < energies[ham_attr]:
            v_scores[ham_attr] = v_score
            energies[ham_attr] = energy

        method = row[2]
        data_new.append((*ham_attr, method, v_score))
        markers.append(get_marker(ham_attr))
    data = data_new
    print(tabulate(data, tablefmt="plain"))

    ham_idxs, idx_hams = sort_v_scores(v_scores, reverse=True)
    x_max = len(ham_idxs)
    x_max += 4
    x_max = (x_max + 1) // 2 * 2

    fig, ax = plt.subplots(figsize=(13, 12), subplot_kw={"projection": "polar"})

    for (ham_type, ham_param, _, v_score), (color, marker, size) in zip(data, markers):
        ham_attr = ham_type, ham_param
        idx = ham_idxs[ham_attr]
        ax.plot(
            (idx + theta0 + 0.5) / x_max * 2 * pi,
            scale_doubly_log(v_score),
            **get_plot_kwargs(
                color, marker, size, bold=(v_score == v_scores[ham_attr])
            ),
        )

    # Angular grid
    for r in [-4, -3, -2, -1, 0, 1]:
        thetas = np.linspace(
            theta0 / x_max * 2 * pi, (len(ham_idxs) + theta0) / x_max * 2 * pi, 360
        )
        rs = r * np.ones_like(thetas)
        ax.plot(
            thetas,
            rs,
            color="0.8",
            linestyle="--",
            linewidth=0.5,
            zorder=0.4,
        )

    for i in range((len(ham_idxs) + 1) // 2):
        ax.axvspan(
            (i * 2 + theta0) / x_max * 2 * pi,
            (i * 2 + theta0 + 1) / x_max * 2 * pi,
            color="0.95",
            zorder=0.3,
        )

    # Meta arrow
    thetas = np.linspace(pi / 3, 2 / 3 * pi, 100)
    r = -3.5
    rs = r * np.ones_like(thetas)
    ax.plot(thetas, rs, color="k", linewidth=1)
    kwargs = dict(
        length_includes_head=True, head_width=0.2, head_length=0.05, facecolor="k"
    )
    ax.arrow(pi / 3, r, -0.01, 0, **kwargs)
    ax.arrow(2 / 3 * pi, r, 0.01, 0, **kwargs)
    ax.text(
        pi / 3 - 0.25,
        r,
        "Harder",
        fontsize="xx-large",
        horizontalalignment="center",
        verticalalignment="center",
    )
    ax.text(
        2 / 3 * pi + 0.25,
        r,
        "Easier",
        fontsize="xx-large",
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.set_ylim(-6, 1.3)
    ax.set_yticks([-4, -3, -2, -1, 0, 1])
    ax.set_yticklabels(
        [
            "$< 10^{-16}$",
            "$10^{-8}$",
            "$10^{-4}$",
            "$10^{-2}$",
            "$10^{-1}$",
            "$10^{-0.5}$",
        ],
        fontsize="large",
        horizontalalignment="center",
        verticalalignment="top",
    )
    ax.set_rlabel_position(0)
    ax.text(
        -6 / 360 * 2 * pi,
        -1.5,
        "V-score",
        fontsize="x-large",
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.set_xticks([(i + theta0 + 0.5) / x_max * 2 * pi for i in range(len(ham_idxs))])
    for i, label in enumerate(ax.get_xticklabels()):
        x, y = label.get_position()
        y += 0.04

        text = get_exact_marker(exact_energies, idx_hams[i])
        ha = "left"
        rotation = (i + theta0 + 0.5) / x_max * 360
        if 90 < rotation < 270:
            text = f"{text[2:]} {text[0]}"
            ha = "right"
            rotation += 180

        ax.text(
            x,
            y,
            text,
            color=ham_colors[idx_hams[i][0]],
            fontfamily=["monospace", "VarbenchIcons"],
            fontsize="small",
            transform=label.get_transform(),
            horizontalalignment=ha,
            verticalalignment="center",
            rotation_mode="anchor",
            rotation=rotation,
        )
    ax.set_xticklabels([])

    ax.spines["polar"].set_visible(False)
    ax.grid(False)
    ax.legend(
        handles=get_legend(explanation=True),
        # loc="upper left",
        bbox_to_anchor=(0, 1.15),
        # ncol=2,
        fontsize="x-large",
        edgecolor="none",
        facecolor="none",
        handlelength=1,
        handletextpad=0.4,
        # columnspacing=1,
    )
    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
