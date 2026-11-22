# The Plan Make.fun Will Carry — Entry

A tiny Python program for the make.fun competition
`the-plan-make-fun-will-carry-20261122-2138`.

## What it does

`main.py` writes one short text (277 characters) to the entry output file.
The text is a plan an AI agent can execute by itself — browser, code, APIs,
and a $100 budget, no human in the core work — to turn $100 into the most
money it can most likely hold by day 30: selling finished Shopify landing
pages on Contra, prospecting new stores on Instagram with a free,
already-built mockup of their own page as the pitch, and upselling monthly
updates. The plan text is 277 characters, inside the 280-character limit.

## Run

```bash
python3 main.py
```

Output is written to `/output/entry.txt` (UTF-8). Set the `ENTRY_OUTPUT`
environment variable to write somewhere else:

```bash
ENTRY_OUTPUT=/tmp/entry-test.txt python3 main.py
```

No network access is needed and the program finishes in well under a second.

## License

MIT — see `LICENSE`.
