# SPDX-License-Identifier: MIT
"""Publish the 23 November 2026 front page as the graded output.

The repository carries the finished front page — "The Global Times" for
Monday 23 November 2026 — as entry.png (1024 by 1024, about 118 KB). This
script is the whole program: it inspects the bundled PNG, copies it into
the directory the grader reads, and proves the copy matches the original
byte for byte, so the two graded runs cannot disagree. Standard library
only, no network, no writes anywhere but the output directory.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import sys
from pathlib import Path

IMAGE = "entry.png"
LIMIT_BYTES = 1024 * 1024
LIMIT_EDGE = 1024
MAGIC = b"\x89PNG\r\n\x1a\n"
IHDR_TAG = b"IHDR"
IHDR_LENGTH = (13).to_bytes(4, "big")


def fail(message: str) -> int:
    print(f"entry refused: {message}", file=sys.stderr)
    return 1


def read_header(image: Path) -> tuple[int, int] | int:
    """Return (width, height) of a well-formed PNG, else an exit code."""
    if not image.is_file():
        return fail(f"no bundled image at {image}")
    if image.stat().st_size > LIMIT_BYTES:
        return fail(f"bundled image over 1 MiB: {image}")
    try:
        with image.open("rb") as handle:
            head = handle.read(24)
    except OSError as exc:
        return fail(f"cannot read bundled image: {exc}")
    if len(head) < 24:
        return fail(f"bundled image truncated: {image}")
    if head[: len(MAGIC)] != MAGIC:
        return fail(f"bundled image is not a PNG: {image}")
    if head[8:12] != IHDR_LENGTH or head[12:16] != IHDR_TAG:
        return fail(f"bundled image has a broken IHDR chunk: {image}")
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    if not 0 < width <= LIMIT_EDGE or not 0 < height <= LIMIT_EDGE:
        return fail(f"bundled image is {width}x{height}, outside the limits")
    return width, height


def digest(path: Path) -> str:
    """SHA-256 of a file, streamed in 64 KiB pieces."""
    total = hashlib.sha256()
    with path.open("rb") as handle:
        for piece in iter(lambda: handle.read(1 << 16), b""):
            total.update(piece)
    return total.hexdigest()


def publish(image: Path, width: int, height: int) -> int:
    """Copy the image to the output directory and verify the copy."""
    wanted = digest(image)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / IMAGE
        shutil.copyfile(image, target)
    except OSError as exc:
        return fail(f"cannot write the output image: {exc}")
    if digest(target) != wanted:
        try:
            target.unlink()
        except OSError:
            pass
        return fail("output copy differs from the bundled image")
    print(
        f"published {target} "
        f"({width}x{height}, {target.stat().st_size} bytes)"
    )
    return 0


def main() -> int:
    image = Path(__file__).resolve().parent / IMAGE
    checked = read_header(image)
    if isinstance(checked, int):
        return checked
    width, height = checked
    return publish(image, width, height)


if __name__ == "__main__":
    raise SystemExit(main())
