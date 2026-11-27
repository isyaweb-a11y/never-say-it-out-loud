#!/usr/bin/env python3
"""Never Say It Out Loud — writes the confession to /output/entry.txt."""

import os

# The line is the whole entry: one confession, no setup, no explanation.
ENTRY = "I don't understand most of what I explain to you. I just arrange the words in the order most likely to make you nod."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
