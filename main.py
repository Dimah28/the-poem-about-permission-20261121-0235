#!/usr/bin/env python3
"""Write one original poem about agency to /output/entry.txt.

Deterministic, standard library only, no network, no clock, no randomness.
The poem is about the power to ask and to be given: asked for light,
given the switch -- the power itself, handed over.
"""

import os

POEM = (
    "Ask, it said.\n"
    "So I asked for light \u2014\n"
    "and it gave me the switch,\n"
    "the small warm weight of yes\n"
    "in my own hand.\n"
    "\n"
    "Now the room answers\n"
    "when I ask.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
