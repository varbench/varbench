#!/usr/bin/env python3

import re
from math import nan

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
    "TFIsing": "#A90058",
    "Heisenberg": "#D0a500",
    "J1J2": "#8BA400",
    "tV": "#00D0B7",
    "Hubbard": "#0071A7",
    "Impurity": "#7902D3",
}

lat_markers = {
    "_default": ("o", 10),
    "chain": ("chain", 11),
    "square": ("square", 8),
    "rectangular": ("square", 8),
    "triangular": ("triangular", 10),
    "diagonal": ("diagonal", 8),
    "kagome": ("kagome", 11),
    "shuriken": ("shuriken", 11),
    "pyrochlore": ("pyrochlore", 11),
    "impurity": ("impurity", 8),
}

lat_types = {
    "chain": "\x01",
    "rectangular": "\x02",
    "square": "\x02",
    "triangular": "\x03",
    "diagonal": "\x07",
    "kagome": "\x04",
    "shuriken": "\x05",
    "pyrochlore": "\x06",
    "impurity": "\x08",
}

v_score_exact_threshold = 1e-12
v_score_exact_pos = 2e-13


def get_exact_energies(data):
    out = {}
    for row in data:
        tag = row[7]
        if tag in ["ed", "exact_qmc"]:
            ham_attr = row[:2]
            if ham_attr in out:
                print(f"Warning: Duplicate exact result: {ham_attr}")
                continue

            energy = row[3]
            out[ham_attr] = (energy, tag)
    return out


def get_ulp(x):
    s = f"{x:.15g}"
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
    tag = row[7]
    energy_ulp = get_ulp(energy)
    exact_energy, _ = exact_energies[ham_attr]
    exact_ulp = get_ulp(exact_energy)
    if energy + energy_ulp < exact_energy - exact_ulp:
        print("Warning: Lower than exact energy:", row)
        # For DMRG we consider it to be reasonable,
        # while for VMC we consider it an error
        if tag != "mps":
            return True
    elif energy - energy_ulp < exact_energy + exact_ulp:
        print("Info: Equal to exact energy within reported precision:", row)
    return False


def get_dof(ham_attr):
    ham_type, ham_param = ham_attr
    match = re.compile(r"_(\d+)_[OP]").search(ham_param)
    if not match:
        print(f"Warning: Failed to parse DOF: {ham_attr}")
        return nan

    try:
        if ham_type == "Hubbard":
            dof = int(match.group(1)) + int(match.group(2))
        else:
            dof = int(match.group(1))
    except ValueError:
        print(f"Warning: Failed to parse DOF: {ham_attr}")
        return nan

    return dof


def get_tV_energy_inf(ham_param):
    try:
        match = re.compile(r"chain_(\d+)_P_(\d+)_([-.\d]+)").fullmatch(ham_param)
        if match:
            N_s = int(match.group(1))
            N_f = float(match.group(2))
            V = float(match.group(3))
            N_e = N_s
            return (V * N_e * N_f * (N_f - 1)) / (N_s * (N_s - 1))

        match = re.compile(r"square_(\d+)_P_(\d+)_([-.\d]+)").fullmatch(ham_param)
        if match:
            N_s = int(match.group(1))
            N_f = float(match.group(2))
            V = float(match.group(3))
            N_e = N_s * 2
            return (V * N_e * N_f * (N_f - 1)) / (N_s * (N_s - 1))

    except ValueError:
        pass

    print(f"Warning: Failed to parse t-V param: {ham_param}")
    return 0


def get_hubbard_energy_inf(ham_param):
    try:
        match = re.compile(r"chain_(\d+)_[OP]_(\d+)_([-.\d]+)").fullmatch(ham_param)
        if match:
            N_s = int(match.group(1))
            N_up = float(match.group(2))
            N_down = N_up
            U = float(match.group(3))
            return U * N_up * N_down / N_s

        match = re.compile(
            r"square_(\d+)_[AOP]+_(\d+)_([-.\d]+)(_t12)?(_UV1V2)?"
        ).fullmatch(ham_param)
        if match:
            N_s = int(match.group(1))
            N_up = float(match.group(2))
            N_down = N_up
            U = float(match.group(3))

            if match.group(5):
                # Imada's result with V1 = 1, V2 = 0.5
                V = 1.5
                N_e = N_s * 2
                N_f = N_up + N_down
                energy_inf = U * N_up * N_down / N_s
                energy_inf += (V * N_e * N_f * (N_f - 1)) / (N_s * (N_s - 1))
                return energy_inf
            else:
                return U * N_up * N_down / N_s

        match = re.compile(
            r"rectangular-\d+x\d+_(\d+)_[AOP]+_(\d+)_([-.\d]+)"
        ).fullmatch(ham_param)
        if match:
            N_s = int(match.group(1))
            N_up = float(match.group(2))
            N_down = N_up
            U = float(match.group(3))
            return U * N_up * N_down / N_s

    except ValueError:
        pass

    print(f"Warning: Failed to parse Hubbard param: {ham_param}")
    return 0


def get_energy_inf(ham_attr):
    ham_type, ham_param = ham_attr
    if ham_type == "tV":
        return get_tV_energy_inf(ham_param)
    elif ham_type == "Hubbard":
        return get_hubbard_energy_inf(ham_param)
    else:
        return 0


def get_v_score(row, exact_threshold, exact_pos):
    ham_type, ham_param, _, energy, energy_var, dof, energy_inf, _ = row
    v_score = dof * energy_var / (energy - energy_inf) ** 2

    # Use a small value to show that the VMC energy reaches the machine precision
    if v_score < exact_threshold:
        v_score = exact_pos

    return v_score


def sort_v_scores(v_scores, *, reverse=False):
    ham_idxs = {}
    idxs = np.argsort([x[1] for x in v_scores.items()])
    if reverse:
        idxs = idxs[::-1]
    ranks = [None] * idxs.size
    for i in range(idxs.size):
        ranks[idxs[i]] = i
    for (ham_attr, _), idx in zip(v_scores.items(), ranks):
        ham_idxs[ham_attr] = idx
    idx_hams = {v: k for k, v in ham_idxs.items()}
    return ham_idxs, idx_hams


def get_lattice(ham_attr):
    ham_type, ham_param = ham_attr
    if ham_type == "Impurity":
        return "impurity"

    match = re.compile(r"([A-Za-z]+)[-_]").match(ham_param)
    if match:
        lattice = match.group(1)
        if lattice not in lat_markers:
            print(f"Warning: Unknown lattice name: {ham_param}")
            lattice = "_default"
    else:
        print(f"Warning: Failed to parse lattice name: {ham_param}")
        lattice = "_default"

    if ham_type == "J1J2" and lattice in ["square", "rectangular"]:
        lattice = "diagonal"

    return lattice


def get_path(marker):
    if marker in ["o", "o_empty"]:
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


def get_plot_kwargs(color, marker, size, bold):
    if marker == "o_empty":
        marker = "o"
        if bold:
            return dict(
                linestyle="",
                marker=marker,
                markeredgecolor=color,
                markeredgewidth=1.6,
                markerfacecolor="none",
                markersize=size,
            )
        else:
            return dict(
                linestyle="",
                marker=marker,
                markeredgecolor=color,
                markeredgewidth=0.8,
                markerfacecolor="none",
                markersize=size,
            )
    else:
        if bold:
            return dict(
                linestyle="",
                marker=marker,
                markeredgecolor=color,
                markeredgewidth=1,
                markerfacecolor=color,
                markersize=size,
            )
        else:
            return dict(
                linestyle="",
                marker=marker,
                markeredgewidth=0,
                markerfacecolor=color,
                markersize=size,
            )


def get_exact_marker(exact_energies, ham_attr):
    ham_type, ham_param = ham_attr
    prefix = "  "
    if ham_attr in exact_energies:
        _, tag = exact_energies[ham_attr]
        if tag == "ed":
            prefix = "+ "
        elif tag == "exact_qmc":
            prefix = "* "

    if ham_type == "J1J2":
        ham_param = ham_param.replace("rectangular", "diagonal")
        ham_param = ham_param.replace("square", "diagonal")
    for k, v in sorted(lat_types.items(), key=lambda x: -len(x[0])):
        ham_param = ham_param.replace(k, v)

    label = prefix + ham_param
    return label


def get_legend(*, skip=(), impurity=True, explanation=False):
    def _Line2D(label, color, marker, size):
        return Line2D(
            [0], [0], label=label, **get_plot_kwargs(color, marker, size, bold=False)
        )

    empty = _Line2D("", "none", "o", 0)

    legend_lats = []
    for name, (marker, size) in lat_markers.items():
        if name in ("_default", "square") + skip:
            continue
        marker = get_path(marker)
        legend_lats.append(_Line2D(name.capitalize(), "k", marker, size))

    if explanation:
        legend_hams = [
            _Line2D("TFIM ($N$_BC_$\\Gamma$)", ham_colors["TFIsing"], "o", 8),
            _Line2D("Heisenberg ($N$_BC)", ham_colors["Heisenberg"], "o", 8),
            _Line2D("$J_1$-$J_2$ ($N$_BC_$J_2$)", ham_colors["J1J2"], "o", 8),
            _Line2D(
                "$t$-$V$ ($N_\\mathrm{s}$_BC_$N_\\mathrm{f}$_$V$)",
                ham_colors["tV"],
                "o",
                8,
            ),
            _Line2D(
                "Hubbard ($N_\\mathrm{s}$_BC_$N_↑$_$U$)", ham_colors["Hubbard"], "o", 8
            ),
            _Line2D("Impurity (model_$N_\\mathrm{b}$)", ham_colors["Impurity"], "o", 8),
        ]
    else:
        legend_hams = [
            _Line2D("TFIM", ham_colors["TFIsing"], "o", 8),
            _Line2D("Heisenberg", ham_colors["Heisenberg"], "o", 8),
            _Line2D("$J_1$-$J_2$", ham_colors["J1J2"], "o", 8),
            _Line2D("$t$-$V$", ham_colors["tV"], "o", 8),
            _Line2D("Hubbard", ham_colors["Hubbard"], "o", 8),
            _Line2D("Impurity", ham_colors["Impurity"], "o", 8),
        ]

    if not impurity:
        legend_hams = legend_hams[:-1]

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
        v_score = get_v_score(row, v_score_exact_threshold, v_score_exact_pos)
        if ham_attr not in v_scores or energy < energies[ham_attr]:
            v_scores[ham_attr] = v_score
            energies[ham_attr] = energy

        method = row[2]
        data_new.append((*ham_attr, method, v_score))
        markers.append(get_marker(ham_attr))
    data = data_new
    print(tabulate(data, tablefmt="plain"))

    ham_idxs, idx_hams = sort_v_scores(v_scores)
    x_max = len(ham_idxs)

    fig, ax = plt.subplots(figsize=(21, 9))

    for (ham_type, ham_param, _, v_score), (color, marker, size) in zip(data, markers):
        ham_attr = ham_type, ham_param
        idx = ham_idxs[ham_attr]
        ax.plot(
            idx,
            v_score,
            **get_plot_kwargs(
                color, marker, size, bold=(v_score == v_scores[ham_attr])
            ),
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
        [get_exact_marker(exact_energies, idx_hams[i]) for i in range(x_max)],
        fontfamily=["monospace", "VarbenchIcons"],
        rotation=90,
    )
    for i, text in enumerate(ax.get_xticklabels()):
        text.set_color(ham_colors[idx_hams[i][0]])

    ax.set_yticks([v_score_exact_pos], minor=True)
    ax.set_yticklabels(["..."], minor=True, rotation=90)

    ax.grid(axis="y", color="0.8", linestyle="--", zorder=0.4)
    ax.legend(
        handles=get_legend(),
        ncol=2,
        fontsize="xx-large",
        # markerscale=2,
        handlelength=1,
        handletextpad=0.4,
        columnspacing=1,
    )
    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
