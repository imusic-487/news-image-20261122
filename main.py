# The World in One Page — news-image-20261122 entry (Python 3.13, standard library only).
#
# The entry image is the entry.png beside this file: a dense 50-story data
# poster summing up Sunday 22 November 2026 — COP31 collapsing in Antalya,
# Iran's strikes on US bases in Bahrain, the 'El Chapo Isidro' capture in
# Sinaloa, Democrats clinching 258 House seats, and 46 more stories, each
# with its source named and one-sided claims labelled CLAIM.
#
# The program copies that image to /output/entry.png, byte for byte, so the
# judge sees exactly the image the repository holds. No network, no
# randomness, no timestamps: every run writes the same bytes. The copy is
# verified by size and by image signature before the program returns.
# PNG files begin with b"\x89PNG\r\n\x1a\n", JPEG files with b"\xff\xd8\xff".
# A truncated or wrong-format copy fails loudly instead of reaching the judge.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DESTINATION = OUTPUT_DIR / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    # Fail loudly rather than hand the grader a truncated copy.
    if DESTINATION.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")
    with open(SOURCE, "rb") as fh:
        source_magic = fh.read(8)
    with open(DESTINATION, "rb") as fh:
        magic = fh.read(8)
    if magic != source_magic:
        raise RuntimeError("entry.png copy does not match the source")
    if not (magic.startswith(PNG_MAGIC) or magic.startswith(JPEG_MAGIC)):
        raise RuntimeError("entry.png is neither a whole PNG nor a whole JPEG")


if __name__ == "__main__":
    main()
