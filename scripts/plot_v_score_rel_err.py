#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress
from tabulate import tabulate

from collect import filter_energy_var, get_data
from plot_v_score import (
    check_exact_energy,
    get_exact_energies,
    get_legend,
    get_marker,
    get_v_score,
)

out_filename = "./v_score_rel_err.pdf"


def get_padded_range(xs, pad_ratio=0.02):
    x_min = xs.min()
    x_max = xs.max()
    pad = pad_ratio * (x_max - x_min)
    v_min = x_min - pad
    v_max = x_max + pad
    return v_min, v_max


def main():
    data = get_data()
    exact_energies = get_exact_energies(data)
    data = filter_energy_var(data)

    data_new = []
    markers = []
    for row in data:
        ham_attr = row[:2]
        if ham_attr not in exact_energies:
            continue

        if check_exact_energy(exact_energies, row):
            continue

        method = row[2]
        energy = row[3]
        exact_energy = exact_energies[ham_attr]
        energy_rel_err = (energy - exact_energy) / abs(exact_energy)
        if energy_rel_err < 1e-7:
            continue

        v_score = get_v_score(row, exact=1e-16)
        if v_score < 1e-6:
            continue

        data_new.append(
            (*ham_attr, method, energy_rel_err, v_score, energy_rel_err / v_score)
        )
        markers.append(get_marker(ham_attr))
    data = data_new
    print(tabulate(data, tablefmt="plain"))

    data_new = []
    for row, marker in zip(data, markers):
        data_new.append((row[4], row[3], marker))
    data = data_new

    xs = np.log([x[0] for x in data])
    ys = np.log([x[1] for x in data])
    lm = linregress(xs, ys)
    print(
        f"slope {lm.slope:.8g} "
        f"intercept {lm.intercept:.8g} "
        f"R-squared {lm.rvalue**2:.3g} "
        f"p-value {lm.pvalue:.3g} "
        f"slope_std_err {lm.stderr:.3g} "
        f"intercept_std_err {lm.intercept_stderr:.3g}"
    )

    def _lm(x):
        return lm.intercept + lm.slope * x

    fig, ax = plt.subplots(figsize=(6, 4))

    v_min, v_max = get_padded_range(xs)
    ax.plot(
        np.exp([v_min, v_max]),
        np.exp([_lm(v_min), _lm(v_max)]),
        color="k",
        linestyle="--",
        linewidth=0.5,
        zorder=0.6,
    )

    for v_score, energy_rel_err, (color, marker, size) in data:
        ax.plot(
            v_score,
            energy_rel_err,
            linestyle="",
            marker=marker,
            markeredgewidth=0,
            markerfacecolor=color,
            markersize=size,
        )

    ax.set_xlabel("V-score")
    ax.set_ylabel("Energy rel. err.")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid(color="0.8", linestyle="--", zorder=0.4)
    ax.legend(handles=get_legend(skip=("square_kagome",)), ncol=2, columnspacing=1)
    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
