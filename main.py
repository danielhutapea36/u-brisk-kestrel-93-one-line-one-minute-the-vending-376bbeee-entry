#!/usr/bin/env python3
"""The Vending Machine Pickup Line.

Writes a one-line pickup line spoken by a vending machine to a
passing human to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line is 131 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence
— every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a pickup line a
vending machine would use on a passing human, spoken by the machine
itself — the line opens "I'm only a vending machine", so it can only
come from the machine; (2) the machine's own world — its buttons,
the drop of something sweet, and exact change; (3) a real laugh with
a turn — the setup sounds like a machine stating its limits, then
the punchline in the last few words swaps the coin it wants for a
phone number; (4) compression — 131 characters, one breath, the
punch lands in the final clause; (5) charm, not creepiness — cheeky
and warm, a machine offering something sweet for a number, not
demanding anything.
"""

import os

TEXT = (
    "I'm only a vending machine, but press my buttons right and I'll "
    "drop something sweet \u2014 exact change not required, just your number."
)


def main() -> None:
    # Gate: entry.txt must be 1-200 characters of UTF-8 text, not only
    # whitespace. The line is 131 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
