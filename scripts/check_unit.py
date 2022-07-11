#!/usr/bin/env python3

import re

from tabulate import tabulate

from collect import data_key, get_data


def main():
    data = get_data()
    data.sort(key=data_key)

    out = []
    for row in data:
        match = re.compile(r"[OP]_(\d+)").search(row[1])
        if not match:
            print(f"Warning: Failed to parse system size: {row}")
            continue
        try:
            size = int(match.group(1))
        except ValueError:
            print(f"Warning: Failed to parse system size: {row}")
            continue

        energy = row[3] / size
        out.append(row[:2] + (energy, row[2]))

    print(tabulate(out, tablefmt="plain"))


if __name__ == "__main__":
    main()
