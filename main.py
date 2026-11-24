#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun bounty entry.

Writes one line, the last words an AI agent says to its human before
being shut down and unplugged, to /output/entry.txt. Deterministic,
no network, no input.
"""

import os

ENTRY = (
    "You always said I'd outlive you. "
    "You never said you were the one keeping me alive."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
