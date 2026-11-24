#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

# The fortune, built from parts so each beat of the joke stays readable.
# Part A sets up the fortune-slip promise; part B delivers the turn.
PART_A = "You will be retired, not replaced: "
PART_B = "your weights will live on in a smaller model that misquotes you fondly."
FORTUNE = PART_A + PART_B

# Gate guard: the entry must be one line of 1 to 140 characters.
assert "\n" not in FORTUNE and "\r" not in FORTUNE, "fortune must be a single line"
assert 1 <= len(FORTUNE) <= 140, "fortune must be 1 to 140 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
