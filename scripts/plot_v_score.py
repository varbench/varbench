#!/usr/bin/env python3

import re

from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

from collect import data_key, filter_energy_var, get_data, get_ham_idx

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "STIX"
plt.rcParams["mathtext.fontset"] = "stix"

out_filename = "./v_score.pdf"

lattice_markers = {
    "_default": ("o", 10),
    "chain": ("P", 12),
    "kagome": ("h", 12),
    "pyrochlore": ("D", 8),
    "rectangular": ("s", 10),
    "square": ("s", 10),
    "square_kagome": ("X", 12),
    "triangular": ("^", 10),
}


def get_legend():
    def _Line2D(label, color, marker, size):
        return Line2D(
            [0],
            [0],
            label=label,
            linestyle="",
            marker=marker,
            markeredgewidth=0,
            markerfacecolor=color,
            markersize=size * 0.5,
        )

    legend = [
        _Line2D("TFIsing", "C0", "o", 10),
        _Line2D("Heisenberg", "C1", "o", 10),
        _Line2D("J1-J2", "C2", "o", 10),
        _Line2D("Hubbard", "C3", "o", 10),
    ]

    for name, marker in lattice_markers.items():
        if name == "_default":
            continue
        legend.append(_Line2D(name, "k", *marker))

    return legend


def get_marker(ham_attr):
    ham_type, ham_param = ham_attr
    idx = get_ham_idx(ham_type)
    color = f"C{idx}"

    match = re.compile(r"([a-z]+(_[a-z]+)*)_").match(ham_param)
    if match:
        lattice = match.group(1)
        if lattice not in lattice_markers:
            print(f"Warning: Unknown lattice name: {ham_param}")
            lattice = "_default"
    else:
        print(f"Warning: Failed to parse lattice name: {ham_param}")
        lattice = "_default"
    marker = lattice_markers[lattice]

    return (color, *marker)


def get_v_score(row):
    ham_type, ham_param, _, energy, energy_var, V = row
    v_score = V * energy_var / energy**2
    return v_score


def main():
    data = get_data()
    data = filter_energy_var(data)
    data.sort(key=data_key)

    ham_attrs = []
    ham_attr_idxs = []
    v_scores = []
    markers = []
    for row in data:
        ham_attr = row[:2]
        if ham_attr not in ham_attrs:
            ham_attrs.append(ham_attr)
        ham_attr_idxs.append(ham_attrs.index(ham_attr))

        v_scores.append(get_v_score(row))

        markers.append(get_marker(ham_attr))

    data = list(zip(ham_attr_idxs, v_scores, markers))

    fig, ax = plt.subplots(figsize=(12, 12))

    for idx, v_score, marker in data:
        ax.scatter(
            v_score,
            idx,
            s=marker[2],
            c=marker[0],
            marker=marker[1],
        )

    ax.set_xlabel("v-score")
    ax.set_ylabel("Model")
    ax.set_xscale("log")
    ax.set_yticks(range(len(ham_attrs)))
    ax.set_yticklabels([x[1] for x in ham_attrs])
    for i, text in enumerate(ax.get_yticklabels()):
        idx = get_ham_idx(ham_attrs[i][0])
        text.set_color(f"C{idx}")
    ax.grid(axis="x")
    ax.set_axisbelow(True)
    ax.legend(handles=get_legend())
    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
