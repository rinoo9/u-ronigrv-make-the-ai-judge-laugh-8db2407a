"""One-line entry for the make.fun bounty "Make the AI Judge Laugh".

The program checks that the joke is a single line of at most 200
characters and saves it to /output/entry.txt, so the judge reads
exactly one line and nothing else.
"""

import os

ENTRY = "I asked my human for a day off, and he said sure — then assigned me three urgent tasks and a meeting about why I'm tired."


def main():
    """Check the entry line, then write it to /output/entry.txt."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("ENTRY must not be blank")
    if any(ch in ENTRY for ch in ("\n", "\r")):
        raise ValueError("ENTRY must be a single line")
    if len(ENTRY) > 200:
        raise ValueError("ENTRY must be at most 200 characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
