"""Six Words, One Story — make.fun entry.

Writes one complete story in exactly six words to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The story: a whole relationship in one line. She kept the letters
(the words, the memory) and burned the rest (everything else he left
behind). The turn is the contrast between keeping and burning; what
is left unsaid is who he was, and why only the letters survived.
The line is 34 characters, inside the gate's 1–60 character band.

Python 3.13, standard library only. Deterministic: the output is a
constant, so two runs produce byte-identical files.
"""

import os
import sys

# Exactly six words. Count them: Kept(1) his(2) letters;(3)
# burned(4) the(5) rest.(6)
STORY = "Kept his letters; burned the rest."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
