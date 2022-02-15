#!/usr/bin/env python3

import os
from math import sqrt

from natsort import natsort_key
from tabulate import tabulate

root = "../"
ham_types = ["TfIsing", "Heisenberg", "J1J2", "Hubbard"]


def parse_float(s):
    s = s.replace("(", "").replace(")", "")
    return float(s)


def parse_file(data, file_path, file_values):
    fields = ["method", "energy", "energy variance"]

    state = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if state == 0:
                line_lower = line.lower()
                if not all(x in line_lower for x in fields):
                    continue

                cols = [x.strip() for x in line_lower.split("|")]
                field_indices = [cols.index(x) for x in fields]
                state = 1

            elif state == 1:
                if "---" in line:
                    continue

                cols = [x.strip() for x in line.split("|")]
                values = [cols[i] for i in field_indices]
                if (
                    not values[1]
                    or not values[2]
                    or values[2] == "0"
                    or "?" in values[2]
                ):
                    continue

                values[1] = parse_float(values[1])
                if values[1] > 0:
                    values[1] *= -1

                values[2] = parse_float(values[2])
                assert values[2] > 0

                values.append(sqrt(values[2]) / abs(values[1]))

                data.append(file_values + tuple(values))

            else:
                raise ValueError(f"Unknown state: {state}")


def get_data():
    data = []
    for _dir in os.scandir(root):
        if _dir.name not in ham_types:
            continue
        ham_type = _dir.name

        for file in os.scandir(_dir):
            if not file.is_file() or file.name == "README.md":
                continue
            ham_param = file.name.replace(".md", "")

            file_path = os.path.join(root, _dir.name, file.name)
            # print(file_path)
            parse_file(data, file_path, (ham_type, ham_param))

    return data


def get_ham_idx(s):
    return ham_types.index(s)


def data_key(a):
    return (get_ham_idx(a[0]), natsort_key(a[1])) + a[2:]


def main():
    data = get_data()
    data.sort(key=data_key)
    # data.sort(key=lambda x: x[-1])
    print(tabulate(data, tablefmt="plain"))


if __name__ == "__main__":
    main()
