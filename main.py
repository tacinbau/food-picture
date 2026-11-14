# food-picture-01 entry (Python 3.13, standard library only).
#
# The picture lives next to this file as entry.png; the program copies it
# byte-for-byte to /output/entry.png. The copy is deterministic: the output
# bytes are exactly the vendored file's bytes, so repeated runs produce
# identical files. The vendored picture is 1024x1024, 257,252 bytes — inside
# the competition gate of <=1 MiB and <=1024x1024.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

if not SRC.is_file():
    raise SystemExit(f"missing vendored image: {SRC}")

OUT.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT)

# Sanity-check the copy: same size as the vendored source, so a truncated
# write can never slip through silently.
if OUT.stat().st_size != SRC.stat().st_size:
    raise SystemExit(f"copy incomplete: {OUT} ({OUT.stat().st_size} bytes) "
                     f"!= source ({SRC.stat().st_size} bytes)")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
