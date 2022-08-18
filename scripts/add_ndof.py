#!/usr/bin/env python3

import os
import re
from math import nan

from collect import ham_types
from reader import read_file, write_file

root = "../"


def fix_headers(headers):
    fields = ["Energy", "Sigma", "Energy Variance", "Method", "Data Repository"]
    fields_lower = [x.lower() for x in fields]
    out = []
    for col in headers:
        try:
            out.append(fields[fields_lower.index(col.lower())])
        except ValueError:
            out.append(col)
    return out


def get_ndof(ham_attr):
    ham_type, ham_param = ham_attr
    if ham_type == "Hubbard":
        pattern = r"[OP]_(\d+)_(\d+)"
    else:
        pattern = r"[OP]_(\d+)"
    match = re.compile(pattern).search(ham_param)
    if not match:
        print(f"Warning: Failed to parse DOF: {ham_attr}")
        return nan

    try:
        if ham_type == "Hubbard":
            ndof = int(match.group(1)) + int(match.group(2))
        else:
            ndof = int(match.group(1))
    except ValueError:
        print(f"Warning: Failed to parse DOF: {ham_attr}")
        return nan

    return ndof


def main():
    for _dir in os.scandir(root):
        if _dir.name not in ham_types:
            continue
        ham_type = _dir.name

        for file in os.scandir(_dir):
            if not file.is_file() or file.name == "README.md":
                continue
            ham_param = file.name.replace(".md", "")

            file_path = os.path.join(root, _dir.name, file.name)
            print(file_path)
            headers, data, comments = read_file(file_path)
            headers = fix_headers(headers)
            while comments and not comments[0]:
                del comments[0]

            i = headers.index("Energy Variance") + 1
            ndof = get_ndof((ham_type, ham_param))
            headers = (*headers[:i], "DOF", *headers[i:])
            data = [(*x[:i], ndof, *x[i:]) for x in data]

            write_file(file_path, headers, data, comments)


if __name__ == "__main__":
    main()
