# SPDX-License-Identifier: MIT
"""news-image-20261123: write the day's front page to the output directory.

The repository ships the finished 1024x1024 front page as entry.png — "The
Global Times" for Monday 23 November 2026, drawn from the day's reporting
(Gulf war widening, Ukraine at sea, COP31 collapsing, Democrats taking the
House, the Indonesian factory fire). This program copies that image to the
grader's output directory and checks the copy byte-for-byte, so both graded
runs produce identical bytes. It uses only the Python standard library and
never touches the network.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
MAX_BYTES = 1024 * 1024
MAX_WIDTH = 1024
MAX_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir() -> Path:
    """The directory the grader reads the entry from."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def sha256_file(path: Path) -> str:
    """Hex digest of a file, streamed so large files stay cheap."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        print(f"missing bundled image: {source}", file=sys.stderr)
        return 1
    if source.stat().st_size > MAX_BYTES:
        print(f"bundled image exceeds 1 MiB: {source}", file=sys.stderr)
        return 1
    with source.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24:
        print(f"bundled image is truncated: {source}", file=sys.stderr)
        return 1
    if header[: len(PNG_MAGIC)] != PNG_MAGIC:
        print(f"bundled image is not a PNG: {source}", file=sys.stderr)
        return 1
    if header[8:12] != (13).to_bytes(4, "big"):
        print(f"bundled image has a bad IHDR length: {source}", file=sys.stderr)
        return 1
    if header[12:16] != b"IHDR":
        print(f"bundled image has no IHDR chunk: {source}", file=sys.stderr)
        return 1
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if not (0 < width <= MAX_WIDTH and 0 < height <= MAX_HEIGHT):
        print(
            f"bundled image is {width}x{height}, outside 1..{MAX_WIDTH}x{MAX_HEIGHT}: {source}",
            file=sys.stderr,
        )
        return 1

    source_hash = sha256_file(source)
    out = output_dir()
    try:
        out.mkdir(parents=True, exist_ok=True)
        target = out / SOURCE_NAME
        shutil.copyfile(source, target)
    except OSError as exc:
        print(f"cannot write output image: {exc}", file=sys.stderr)
        return 1
    if sha256_file(target) != source_hash:
        print("copy mismatch: output differs from bundled image", file=sys.stderr)
        try:
            target.unlink()
        except OSError:
            pass
        return 1
    print(f"wrote {target} ({width}x{height}, {target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
