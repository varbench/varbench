#!/usr/bin/env python3

from tabulate import tabulate

from collect import data_key, get_data


def main():
    data = get_data()
    data.sort(key=data_key)

    out = []
    for row in data:
        energy_per_dof = row[3] / row[5]
        out.append((*row[:2], energy_per_dof, row[2]))

    print(tabulate(out, tablefmt="plain"))


if __name__ == "__main__":
    main()
