#!/usr/bin/env python3

import re

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.transforms import Affine2D
from svgpath2mpl import parse_path
from svgpathtools import svg2paths
from tabulate import tabulate

from collect import data_key, filter_energy_var, get_data

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "STIX"
plt.rcParams["mathtext.fontset"] = "stix"

out_filename = "./v_score.pdf"

ham_colors = {
    "TfIsing": "#7F1900",
    "Heisenberg": "#B99232",
    "J1J2": "#61BDD3",
    "Hubbard": "#2F5EAC",
}

lat_markers = {
    "_default": ("o", 10),
    "chain": ("chain", 11),
    "square": ("square", 8),
    "rectangular": ("square", 8),
    "triangular": ("triangular", 10),
    "square_diagonal": ("square_diagonal", 8),
    "kagome": ("kagome", 11),
    "square_kagome": ("square_kagome", 11),
    "pyrochlore": ("pyrochlore", 11),
}

v_score_exact = 1e-13


def get_exact_energies(data):
    out = {}
    for row in data:
        if row[6] == "ed":
            ham_attr = row[:2]
            if ham_attr in out:
                print(f"Warning: Duplicate exact result: {ham_attr}")
                continue
            out[ham_attr] = row[3]
    return out


def get_ulp(x):
    s = "{:.16g}".format(x)
    i = s.find(".")
    if i == -1:
        return 1
    else:
        return 0.1 ** (len(s) - i - 1)


def check_exact_energy(exact_energies, row):
    ham_attr = row[:2]
    if ham_attr not in exact_energies:
        return False

    energy = row[3]
    tag = row[6]
    energy_ulp = get_ulp(energy)
    exact_energy = exact_energies[ham_attr]
    exact_ulp = get_ulp(exact_energy)
    if energy + energy_ulp < exact_energy - exact_ulp:
        print("Warning: Lower than exact energy:", row)
        # For DMRG we consider it to be reasonable,
        # while for VMC we consider it an error
        if tag != "mps":
            return True
    elif energy - energy_ulp < exact_energy + exact_ulp:
        print("Warning: Equal to exact energy within reported precision:", row)
    return False


def get_hubbard_energy_inf(ham_param):
    try:
        match = re.compile(r"chain_(\d+)_[OP]_(\d+)_(\d+)_([.\d]+)").fullmatch(
            ham_param
        )
        if match:
            V = int(match.group(1))
            N_up = float(match.group(2))
            N_down = float(match.group(3))
            U = float(match.group(4))
            return U * N_up * N_down / V

        match = re.compile(r"square_(\d+)_[AOP][AOP]_(\d+)_(\d+)_([.\d]+)").fullmatch(
            ham_param
        )
        if match:
            L = int(match.group(1))
            N_up = float(match.group(2))
            N_down = float(match.group(3))
            U = float(match.group(4))
            V = L**2
            return U * N_up * N_down / V

        match = re.compile(
            r"square_sqrt(\d+)_[AOP][AOP]_(\d+)_(\d+)_([.\d]+)"
        ).fullmatch(ham_param)
        if match:
            V = int(match.group(1))
            N_up = float(match.group(2))
            N_down = float(match.group(3))
            U = float(match.group(4))
            return U * N_up * N_down / V

        match = re.compile(
            r"rectangular_(\d+)x(\d+)_[AOP][AOP]_(\d+)_(\d+)_([.\d]+)"
        ).fullmatch(ham_param)
        if match:
            L_x = int(match.group(1))
            L_y = int(match.group(2))
            N_up = float(match.group(3))
            N_down = float(match.group(4))
            U = float(match.group(5))
            V = L_x * L_y
            return U * N_up * N_down / V

    except ValueError:
        pass

    # TODO: Support Imada's extra parameters
    print(f"Warning: Failed to parse Hubbard param: {ham_param}")
    return 0


def get_v_score(row, exact):
    ham_type, ham_param, _, energy, energy_var, dof, _ = row

    # Use a small value to show that the VMC energy reaches the machine precision
    if energy_var == 0:
        return exact

    if ham_type == "Hubbard":
        energy_inf = get_hubbard_energy_inf(ham_param)
    else:
        energy_inf = 0

    v_score = dof * energy_var / (energy - energy_inf) ** 2
    return v_score


def get_lattice(ham_attr):
    ham_type, ham_param = ham_attr
    match = re.compile(r"([a-z]+(_[a-z]+)*)_").match(ham_param)
    if match:
        lattice = match.group(1)
        if lattice not in lat_markers:
            print(f"Warning: Unknown lattice name: {ham_param}")
            lattice = "_default"
    else:
        print(f"Warning: Failed to parse lattice name: {ham_param}")
        lattice = "_default"
    if ham_type == "J1J2" and lattice == "square":
        lattice = "square_diagonal"
    return lattice


def get_path(marker):
    if marker == "o":
        return marker

    _, attributes = svg2paths(f"icons/{marker}.svg")
    marker = parse_path(attributes[0]["d"])
    marker.vertices -= 128
    marker = marker.transformed(Affine2D().scale(1, -1))
    return marker


def _get_marker(ham_type, lattice):
    color = ham_colors[ham_type]
    marker, size = lat_markers[lattice]
    marker = get_path(marker)
    return color, marker, size


def get_marker(ham_attr):
    ham_type, _ = ham_attr
    lattice = get_lattice(ham_attr)
    return _get_marker(ham_type, lattice)


def get_legend(skip=()):
    def _Line2D(label, color, marker, size):
        return Line2D(
            [0],
            [0],
            label=label,
            linestyle="",
            marker=marker,
            markeredgewidth=0,
            markerfacecolor=color,
            markersize=size,
        )

    empty = _Line2D("", "none", "o", 0)

    legend_lats = []
    for name, (marker, size) in lat_markers.items():
        if name in ("_default", "square") + skip:
            continue
        name = name.replace("_", " ")
        marker = get_path(marker)
        legend_lats.append(_Line2D(name, "k", marker, size))

    legend_hams = [
        _Line2D("TFIsing", ham_colors["TfIsing"], "o", 8),
        _Line2D("Heisenberg", ham_colors["Heisenberg"], "o", 8),
        _Line2D("J1-J2", ham_colors["J1J2"], "o", 8),
        _Line2D("Hubbard", ham_colors["Hubbard"], "o", 8),
    ]

    if len(legend_lats) < len(legend_hams):
        legend_lats += [empty] * (len(legend_hams) - len(legend_lats))
    else:
        legend_hams += [empty] * (len(legend_lats) - len(legend_hams))

    legend = legend_lats + legend_hams
    return legend


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
        v_score = get_v_score(row, v_score_exact)
        if ham_attr not in v_scores or energy < energies[ham_attr]:
            v_scores[ham_attr] = v_score
            energies[ham_attr] = energy

        method = row[2]
        data_new.append((*ham_attr, method, v_score))
        markers.append(get_marker(ham_attr))
    data = data_new
    print(tabulate(data, tablefmt="plain"))

    ham_idxs = {}
    idxs = np.argsort([x[1] for x in v_scores.items()])
    ranks = [None] * idxs.size
    for i in range(idxs.size):
        ranks[idxs[i]] = i
    for (ham_attr, _), idx in zip(v_scores.items(), ranks):
        ham_idxs[ham_attr] = idx
    idx_hams = {v: k for k, v in ham_idxs.items()}
    x_max = len(ham_idxs)

    fig, ax = plt.subplots(figsize=(16, 9))

    for (ham_type, ham_param, _, v_score), (color, marker, size) in zip(data, markers):
        ham_attr = ham_type, ham_param
        idx = ham_idxs[ham_attr]
        if v_score == v_scores[ham_attr]:
            ax.plot(
                idx,
                v_score,
                linestyle="",
                marker=marker,
                markeredgecolor=color,
                markeredgewidth=1,
                markerfacecolor=color,
                markersize=size,
            )
        else:
            ax.plot(
                idx,
                v_score,
                linestyle="",
                marker=marker,
                markeredgewidth=0,
                markerfacecolor=color,
                markersize=size,
            )

    for i in range(x_max // 2 + 1):
        ax.axvspan(i * 2 - 0.5, i * 2 + 0.5, color="0.95", zorder=0.3)

    ax.set_ylabel("V-score")
    ax.set_xlim([-1, x_max])
    ax.set_yscale("log")

    ax.set_xticks(range(x_max))
    ax.xaxis.tick_top()
    ax.xaxis.set_tick_params(length=0)
    ax.set_xticklabels(
        [idx_hams[i][1] for i in range(x_max)], fontfamily="monospace", rotation=90
    )
    for i, text in enumerate(ax.get_xticklabels()):
        text.set_color(ham_colors[idx_hams[i][0]])

    ax.set_yticks([v_score_exact], minor=True)
    ax.set_yticklabels(["exact"], minor=True)

    ax.grid(axis="y", color="0.8", linestyle="--", zorder=0.4)
    ax.legend(
        handles=get_legend(),
        ncol=2,
        fontsize="xx-large",
        # markerscale=2,
        columnspacing=1,
    )
    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
