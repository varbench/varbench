#!/usr/bin/env python3

import os
import re
from math import isnan, nan

from natsort import natsort_key
from tabulate import tabulate
from unidecode import unidecode

from reader import read_file

root = "../"
ham_types = ["TfIsing", "Heisenberg", "J1J2", "Hubbard"]
known_tags = [
    "ed",
    "mps",
    "tn",
    "rbm",
    "rnn",
    "nqs",
    "vmc",
    "fn",
    "vafqmc",
    "afqmc",
    "vqe",
]
required_fields = ["method", "energy", "energy variance", "dof"]


# Sometimes there are special Unicode characters, so we normalize them
def _unidecode(s):
    out = unidecode(s)
    if out != s:
        print(f"Special character detected in {s}")
    return out


def parse_float(s):
    s = _unidecode(s)
    s = s.replace("(", "").replace(")", "")
    if not s:
        return nan

    try:
        return float(s)
    except ValueError:
        print(f"Failed to parse float {s}")
        return nan


def find_tag(s, max_width=60):
    s = _unidecode(s)

    if len(s) > max_width:
        s_short = s[: max_width - 3] + "..."
    else:
        s_short = s

    s = s.lower()
    if any(
        x in s for x in ["exact diag", "exact solution", "numerically exact", "quspin"]
    ):
        tag = "ed"
    elif "dmrg" in s:
        tag = "mps"
    elif "peps" in s:
        tag = "tn"
    elif "rbm" in s:
        tag = "rbm"
    elif "rnn" in s:
        tag = "rnn"
    elif any(x in s for x in ["ffn", "cnn"]):
        tag = "nqs"
    elif any(x in s for x in ["determinant", "jastrow", "bcs"]):
        tag = "vmc"
    elif "mvmc" in s:
        print("Info: Classify as VMC:", s)
        # TODO: Currently this only matches Nikita's results with Jastrow-based methods
        tag = "vmc"
    elif "fn on the" in s:
        tag = "fn"
    elif "vafqmc" in s:
        tag = "vafqmc"
    elif "afqmc" in s:
        tag = "afqmc"
    elif "qmc" in s:
        print("Info: Classify as ED:", s)
        # TODO: Currently this only matches QMC for Heisenberg square_10_OO_100,
        # which is accurate enough to be considered ED
        tag = "ed"
    elif "vqe" in s:
        tag = "vqe"
    else:
        print("Warning: Unknown method:", s)
        tag = ""

    if tag:
        assert tag in known_tags

    return tag, s_short


def parse_data(data, file_path, ham_attr):
    headers, rows, _ = read_file(file_path)
    if not rows:
        return

    headers = tuple(x.lower() for x in headers)
    field_indices = {x: headers.index(x) for x in required_fields}
    for cols in rows:

        def warn(msg):
            print(f"Warning: {msg}: {ham_attr + cols}")

        tag, method = find_tag(cols[field_indices["method"]])

        energy = cols[field_indices["energy"]]
        energy = parse_float(energy)
        if isnan(energy):
            warn("Failed to parse energy")
            continue
        if energy == 0:
            warn("Zero energy")
            continue
        if energy > 0:
            warn("Positive energy")

        energy_var = cols[field_indices["energy variance"]]
        energy_var = parse_float(energy_var)
        # if isnan(energy_var):
        #     warn("Missing variance")
        # if energy_var == 0:
        #     warn("Zero variance")
        # if energy_var < 0:
        #     warn("Negative variance")

        dof = int(cols[field_indices["dof"]])

        data.append((*ham_attr, method, energy, energy_var, dof, tag))


# (ham_type, ham_param, method, energy, energy_var, dof, tag)
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

            # Filter out Hubbard data with strange U values
            if re.compile(r"[^.]+\.\d{4,}").fullmatch(ham_param):
                print(f"Info: Skip strange U value: {(ham_type, ham_param)}")
                continue

            file_path = os.path.join(root, _dir.name, file.name)
            parse_data(data, file_path, (ham_type, ham_param))

    return data


def data_key(row):
    return ham_types.index(row[0]), natsort_key(row[1:])


def filter_energy_var(data):
    out = []
    for row in data:
        energy_var = row[4]
        tag = row[6]
        if isnan(energy_var):
            # if tag != "ed":
            #     print("Warning: Missing variance:", row)
            continue
        if energy_var == 0:
            if tag == "ed":
                continue
            else:
                print("Warning: Zero variance:", row)
        if energy_var < 0:
            print("Warning: Negative variance:", row)
            continue
        out.append(row)
    return out


def main():
    data = get_data()
    data.sort(key=data_key)
    print(tabulate(data, tablefmt="plain"))


if __name__ == "__main__":
    main()
