#!/usr/bin/env python3
"""Ship It Friday — one funny commit message, written to entry.txt.

The program writes a single line — the funniest git commit message an
AI coding agent would write right before breaking production on a
Friday — to entry.txt in the output directory, and prints it too.
"""

import os

LINE = "ship it: merged straight to main at 4:59pm on a Friday — rollback is a Monday problem"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
