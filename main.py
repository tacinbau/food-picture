#!/usr/bin/env python3
"""Food-picture-01 entry for make.fun.

The entry image is a finished, vendored picture (a steaming tonkotsu ramen
bowl with a noodle lift) stored next to this script as ``entry.png``.
This program does the one deterministic thing the competition asks for:
it copies that picture, byte for byte, to the output directory as
``entry.png``.

No pixels are generated or altered at run time. Copying the vendored
bytes keeps the output identical on every run, so the picture the
judges see is exactly the picture that was picked and verified.

The copy is deliberately plain: shutil.copyfile moves the bytes as
they are, and the size check afterwards catches a truncated write.
There is no image library involved — nothing to decode, re-encode,
nor recompress — so the output hash can only ever equal the source
hash.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    source = script_dir / SOURCE_NAME

    if not source.is_file():
        print(
            f"error: vendored image not found: {source}",
            file=sys.stderr,
        )
        print(
            "error: entry.png must sit next to main.py",
            file=sys.stderr,
        )
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME

    shutil.copyfile(source, destination)

    source_size = source.stat().st_size
    if source_size == 0:
        print(
            f"error: vendored image is empty: {source}",
            file=sys.stderr,
        )
        return 1
    dest_size = destination.stat().st_size
    if dest_size != source_size:
        print(
            f"error: copied size {dest_size} does not match "
            f"source size {source_size}",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {destination} ({dest_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
