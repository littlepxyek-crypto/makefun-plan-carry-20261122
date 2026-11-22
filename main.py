#!/usr/bin/env python3
"""make.fun entry: a 280-char-max plan an AI agent can run itself to turn
$100 into the most money in 30 days.

Writes TEXT to the entry output path (default /output/entry.txt, override
with the ENTRY_OUTPUT environment variable). No network, finishes fast.
"""

import os

TEXT = (
    "Day 1: put $60 of the $100 into a domain and tools; list on Contra: "
    "'Shopify landing page + copy in 24h', $75. DM 40 stores/day on "
    "Instagram with a free mockup of their page, coded in minutes - "
    "they buy what they already see. Upsell $39/mo updates. "
    "30 sales by day 30 = $2,250."
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
