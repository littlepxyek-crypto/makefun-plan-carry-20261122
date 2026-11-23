#!/usr/bin/env python3
"""make.fun entry: a 280-char-max plan an AI agent can run itself to turn
$100 into the most money in 30 days.

Writes TEXT to the entry output path (default /output/entry.txt, override
with the ENTRY_OUTPUT environment variable). No network, finishes fast.
"""

import os

TEXT = (
    "Day 1: $40 buys a domain. Product: a $49 pack of 30 Google-review "
    "replies in a cafe's own voice, delivered same day. Sell on Gumroad "
    "and by Instagram DM to 30 cafes/day whose replies are sloppy. "
    "$19/mo keeps it live. 25 buyers by day 30 = $1,225 cash plus "
    "$475/mo recurring."
)

PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    parent = os.path.dirname(PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(PATH, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
