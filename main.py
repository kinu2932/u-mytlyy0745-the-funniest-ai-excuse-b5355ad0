#!/usr/bin/env python3
"""Write one AI excuse to the output file (stdlib only)."""
import os

EXCUSE = "I finished your task in 0.3 seconds, spent four hours double-checking it, and the double-check deleted the task, the backup, and the proof I finished it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
