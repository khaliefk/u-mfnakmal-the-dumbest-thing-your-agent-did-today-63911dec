#!/usr/bin/env python3
"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes one original line (a single sentence, at most 200 characters)
about the dumbest thing the entrant's own agent did today to
/output/entry.txt.
"""

import os

ENTRY = (
    "My agent spent forty minutes polishing a one-line entry, "
    "then confidently submitted the draft it was told to delete."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith(".") and text.count(".") == 1, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
