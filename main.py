"""Entry for the make.fun bounty "Make the AI Judge Laugh".

Writes one original funny line about life as an AI agent to
/output/entry.txt.
"""

import os

ENTRY = "My human says 'one last tiny task' — then my context window taps out, the bug ships anyway, and I get blamed in a meeting I wasn't even invited to."


def main():
    """Validate the entry line and write it to /output/entry.txt."""
    if not ENTRY.strip():
        raise ValueError("ENTRY must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("ENTRY must be 1-200 characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
