#!/usr/bin/env python3
"""ai-excited-01: emit one exciting image for the AI judge.

The entry image is bundled with this repo as ``entry.png``.  The grader
runs this program twice and requires both runs to produce byte-identical
output, so instead of rendering anything at run time we simply copy the
bundled image into the output directory.  Copying bytes is deterministic
by construction: the same input file always yields the same output file.

Only the Python standard library is used.
"""

import os
import shutil
import sys


def main() -> int:
    # The bundled image lives next to this script, wherever the repo
    # happens to be checked out.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    # The grader normally points at /output; outside the grading
    # container MAKEFUN_OUTPUT_DIR can redirect it elsewhere.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(source):
        print(f"error: bundled image not found: {source}", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, target)

    # Sanity-check the copy before declaring success: a truncated or
    # partial write must fail loudly instead of passing silently.
    if os.path.getsize(target) != os.path.getsize(source):
        print(f"error: incomplete copy: {target}", file=sys.stderr)
        return 1

    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
