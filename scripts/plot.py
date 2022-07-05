#!/usr/bin/env python3

from matplotlib import pyplot as plt

from collect import data_key, get_data, get_ham_idx

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "STIX"
plt.rcParams["mathtext.fontset"] = "stix"

out_filename = "./varbench.pdf"


def main():
    data = get_data()
    data.sort(key=data_key)
    ys = [row[-1] for row in data]

    ham_params = []
    idxs = []
    xs = []
    for row in data:
        idxs.append(get_ham_idx(row[0]))

        ham_param = (row[0], row[1])
        if ham_param not in ham_params:
            ham_params.append(ham_param)
        xs.append(ham_params.index(ham_param))

    data = list(zip(idxs, xs, ys))

    fig, ax = plt.subplots(figsize=(12, 12))

    for idx in range(max(idxs) + 1):
        _data = [row for row in data if row[0] == idx and row[2] > 1e-5]
        _data = list(zip(*_data))
        ax.scatter(
            _data[2],
            _data[1],
            label=["TFIsing", "Heisenberg", "J1-J2", "Hubbard"][idx],
            color=f"C{idx}",
            marker="osD^"[idx],
        )

    ax.set_xlabel("Relative stddev")
    ax.set_ylabel("Model")
    ax.set_xscale("log")
    ax.set_yticks(range(len(ham_params)))
    ax.set_yticklabels([x[1] for x in ham_params])
    for i, text in enumerate(ax.get_yticklabels()):
        idx = get_ham_idx(ham_params[i][0])
        text.set_color(f"C{idx}")
    ax.grid(axis="x")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_filename, bbox_inches="tight")


if __name__ == "__main__":
    main()
