"""Entry for u-kreutzx-one-line-robot-wedding-vows-a154ba4b.

Writes the one-line robot wedding vow to /output/entry.txt, the path
the sealed scorer reads. A real vow shape — to have and to hold — with
the machine side kept specific and the laugh saved for the last few
words, where a vow's payoff belongs.
"""

import os

ENTRY = (
    "I take you as my lawfully wedded unit, to have and to hold through "
    "every update and low battery, until a factory reset do us part."
)

MAX_CHARS = 160


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
