import re
import sys
from types import SimpleNamespace

import tabulate

tabulate.MIN_PADDING = 0
# Dirty hack to set maximum width of columns
dummy_wcwidth = SimpleNamespace(wcswidth=lambda x: (min(len(x), 60)))

required_fields = ["method", "energy", "energy variance"]


def split_cols(s):
    cols = s.strip().strip("|").split("|")
    cols = tuple(re.compile(r"\s+").sub(" ", x.strip()) for x in cols)
    return cols


def read_file(file_path):
    headers = []
    data = []
    comments = []
    state = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.rstrip()
            line_strip = line.lstrip()
            if state == 0:
                line_lower = line_strip.lower()
                if not all(x in line_lower for x in required_fields):
                    comments.append(line)
                    continue

                headers = split_cols(line_strip)
                state = 1

            else:  # state == 1
                if not line_strip or "---" in line_strip:
                    continue

                cols = split_cols(line_strip)
                if all(not x for x in cols):
                    continue

                if len(headers) < len(cols):
                    print(f"Warning: Too many columns: {line_strip}")
                if len(headers) > len(cols):
                    # print(f"Warning: Not enough columns: {line_strip}")
                    cols += ("",) * (len(headers) - len(cols))

                data.append(cols)

    if state != 1:
        print(f"Warning: Failed to parse {file_path}, wrong state: {state}")

    return headers, data, comments


def write_file(file_path, headers, data, comments):
    tabulate.WIDE_CHARS_MODE = True
    tabulate.wcwidth = dummy_wcwidth

    if file_path:
        f = open(file_path, "w", newline="\n")
    else:
        f = sys.stdout

    for line in comments:
        f.write(line + "\n")
    f.write(
        tabulate.tabulate(data, headers, tablefmt="github", disable_numparse=True)
        + "\n"
    )

    if file_path:
        f.close()

    tabulate.WIDE_CHARS_MODE = False
    tabulate.wcwidth = None
