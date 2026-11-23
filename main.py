#!/usr/bin/env python3
"""Make the Judge Smile entry (make.fun program/v1).

Writes one original line about a small good thing that happened today
to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (the grader mounts that directory
at ``/output``). The line is 123 characters, inside the 1-200 gate.
"""

import os

LINE = "Autocorrect changed 'running late' to 'running cake', so my neighbour met me at the bus stop at 7am holding an actual cake."


def main() -> None:
    # Gate guard: the sealed scorer only accepts UTF-8 text of 1-200
    # characters that is not only whitespace, on a single line.
    # Refuse to write anything that fails the gate instead of
    # submitting an invalid entry.
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"gate: line is {len(LINE)} chars, need 1-200")
    if not LINE.strip():
        raise SystemExit("gate: line is only whitespace")
    if "\n" in LINE:
        raise SystemExit("gate: line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
