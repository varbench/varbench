#!/usr/bin/env python3

from math import sqrt

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress
from tabulate import tabulate

from collect import data_key, filter_energy_var, get_data
from plot_v_score import (
    check_exact_energy,
    get_exact_energies,
    get_legend,
    get_marker,
    get_v_score,
)
from plot_v_score_ham import get_extra_param

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
    data.sort(key=data_key)

    data_new = []
    markers = []
    for row in data:
        tag = row[7]
        if tag == "vafqmc":
            continue

        ham_attr = row[:2]
        ham_type, ham_param = ham_attr
        if ham_attr not in exact_energies:
            continue

        method = row[2]
        # Skip some J2 values to make the plot not too crowded
        if ham_type == "TFIsing":
            if "VQE" in method and method not in [
                "VQE HV (d = 26)",
                "VQE R-CX (d = 10)",
            ]:
                continue
        elif ham_type == "J1J2":
            J2 = float(get_extra_param(ham_param))
            if J2 not in [0.2, 0.5, 0.55, 0.8, 1]:
                continue

        if check_exact_energy(exact_energies, row):
            continue

        energy = row[3]
        energy_inf = row[6]
        exact_energy, _ = exact_energies[ham_attr]
        energy_rel_err = (energy - exact_energy) / (energy_inf - exact_energy)
        if energy_rel_err < 1e-7:
            continue

        v_score = get_v_score(row, exact_threshold=0, exact_pos=0)
        if v_score < 1e-6:
            continue

        data_new.append(
            (*ham_attr, tag, method, energy_rel_err, v_score, energy_rel_err / v_score)
        )
        markers.append(get_marker(ham_attr))
    data = data_new
    print(tabulate(data, tablefmt="plain"))

    data_new = []
    for row, marker in zip(data, markers):
        data_new.append((row[5], row[4], row[2], marker))
    data = data_new

    xs = np.log([x[0] for x in data])
    ys = np.log([x[1] for x in data])
    lm = linregress(xs, ys)
    print(
        f"slope {lm.slope:.8g} "
        f"± {lm.stderr:.3g} "
        f"intercept {lm.intercept:.8g} "
        f"± {lm.intercept_stderr:.3g} "
        f"R-squared {lm.rvalue**2:.3g} "
        f"p-value {lm.pvalue:.3g}"
    )

    # def _lm(x):
    #     return lm.slope * x + lm.intercept

    bs = ys - xs
    b_mean = bs.mean()
    b_std_err = bs.std() / sqrt(bs.size)
    ys_pred = xs + b_mean
    R_squared = (
        1 - ((ys_pred - ys) ** 2).sum() / ((ys_pred - ys_pred.mean()) ** 2).sum()
    )
    print(
        "slope = 1: "
        f"intercept {b_mean:.8g} "
        f"± {b_std_err:.3g} "
        f"R-squared {R_squared:.3g}"
    )

    def _lm(x):
        return x + b_mean

    data_pqc = [x for x in data if x[2] == "pqc"]
    xs_pqc = np.log([x[0] for x in data_pqc])

    fig, ax1 = plt.subplots(figsize=(6 * 0.8, 4 * 0.8))
    ax2 = ax1.inset_axes([0.62, 0.1, 0.35, 0.35])

    v_min, v_max = get_padded_range(xs)
    ax1.plot(
        np.exp([v_min, v_max]),
        np.exp([_lm(v_min), _lm(v_max)]),
        color="k",
        linestyle="--",
        linewidth=0.5,
        zorder=0.6,
    )

    v_min, v_max = get_padded_range(xs_pqc, pad_ratio=0.1)
    ax2.plot(
        np.exp([v_min, v_max]),
        np.exp([_lm(v_min), _lm(v_max)]),
        color="k",
        linestyle="--",
        linewidth=0.5,
        zorder=0.6,
    )

    for v_score, energy_rel_err, _, (color, marker, size) in data:
        ax1.plot(
            v_score,
            energy_rel_err,
            linestyle="",
            marker=marker,
            markeredgewidth=0,
            markerfacecolor=color,
            markersize=size,
        )

    for v_score, energy_rel_err, _, (color, marker, size) in data_pqc:
        ax2.plot(
            v_score,
            energy_rel_err,
            linestyle="",
            marker=marker,
            markeredgewidth=0,
            markerfacecolor=color,
            markersize=size,
        )

    # ax1.text(0.93, 0.05, "(a)", transform=ax1.transAxes)
    # ax2.text(0.93, 0.05, "(b)", transform=ax2.transAxes)

    ax1.set_xlabel("V-score")
    ax1.set_ylabel("Energy rel. err.")
    ax1.set_xscale("log")
    ax2.set_xscale("log")
    ax1.set_yscale("log")
    ax2.set_yscale("log")
    ax2.set_ylim([3e-6, 3e-3])
    ax1.minorticks_off()
    ax2.minorticks_off()
    ax1.grid(color="0.8", linestyle="--", zorder=0.4)
    ax2.grid(color="0.8", linestyle="--", zorder=0.4)
    ax1.legend(
        handles=get_legend(skip=("shuriken", "impurity"), impurity=False),
        ncol=2,
        fontsize="small",
        handletextpad=0.4,
        columnspacing=0.2,
    )
    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    main()
