#!/usr/bin/env python3

from tabulate import tabulate

from collect import data_key, get_data, get_ndof


def main():
    data = get_data()
    data.sort(key=data_key)

    out = []
    for row in data:
        V = get_ndof(row[1])
        energy = row[3] / V
        out.append(row[:2] + (energy, row[2]))

    print(tabulate(out, tablefmt="plain"))


if __name__ == "__main__":
    main()
