#!/usr/bin/env python3
"""The One-Line Laugh -- make.fun entry.

Writes one funny line (a single sentence, under 200 characters) to
/output/entry.txt. Standard library only: no network, no secrets, no
reads outside this file.
"""

import os
from pathlib import Path

LINE = "The only bill that gains weight when I ignore it is my gym."

# The gate allows 1-200 characters; refuse loudly rather than submit junk.
assert 1 <= len(LINE) <= 200, "line outside the 1-200 character gate"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
