#!/usr/bin/env python3

from math import log10

from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec

from collect import data_key, filter_energy_var, get_data
from plot_v_score import _get_marker, get_exact_energies, get_v_score
from plot_v_score_ham import get_key

out_filename = "./v_score_size.pdf"


def main():
    data = get_data()
    exact_energies = get_exact_energies(data)
    data = filter_energy_var(data)
    data.sort(key=data_key)

    v_scores = {}
    energies = {}
    for row in data:
        ham_attr = row[:2]
        energy = row[3]
        if ham_attr in exact_energies and energy < exact_energies[ham_attr]:
            print("Warning: Lower than exact energy:", row)
            continue

        key = get_key(row)
        v_score = get_v_score(row)

        if key not in v_scores or energy < energies[key]:
            v_scores[key] = v_score
            energies[key] = energy

    data = []
    for ((ham_type, lattice, _, _), (dof, _)), v_score in v_scores.items():
        data.append((v_score, dof, _get_marker(ham_type, lattice)))

    fig = plt.figure(figsize=(6, 4))
    xlim1 = (1.5e-13, 6.5e-4)
    xlim2 = (1.5e-4, 3.5e-1)
    gs = GridSpec(
        1,
        2,
        wspace=0.02,
        width_ratios=[log10(xlim1[1] / xlim1[0]), log10(xlim2[1] / xlim2[0]) * 12],
    )
    ax = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    for x, y, (color, marker, size) in data:
        if x < xlim2[0]:
            ax.plot(
                x,
                y,
                linestyle="",
                marker=marker,
                markeredgewidth=0,
                markerfacecolor=color,
                markersize=size,
            )
        else:
            ax2.plot(
                x,
                y,
                linestyle="",
                marker=marker,
                markeredgewidth=0,
                markerfacecolor=color,
                markersize=size,
            )

    fig.supxlabel("V-score")
    ax.set_ylabel("$N_\\mathrm{DOF}$")
    ax.set_xscale("log")
    ax2.set_xscale("log")
    ax.set_yscale("log")
    ax2.set_yscale("log")
    ax.set_xlim(*xlim1)
    ax2.set_xlim(*xlim2)
    ax.set_ylim(6.5e0, 1.2e3)
    ax2.set_ylim(6.5e0, 1.2e3)
    ax.set_xticks([1e-12, 1e-8, 1e-4])
    ax.set_yticks([1e1, 1e2, 1e3])
    ax2.set_yticks([1e1, 1e2, 1e3])
    ax.spines.right.set_visible(False)
    ax2.spines.left.set_visible(False)

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

    ax.grid(color="0.8", linestyle="--")
    ax2.grid(color="0.8", linestyle="--")
    ax.set_axisbelow(True)
    ax2.set_axisbelow(True)

    # fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
