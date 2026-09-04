#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "entry" / "build"
DIST = ROOT / "dist"
DIST.mkdir(parents=True, exist_ok=True)


def kind(path: Path) -> str:
    try:
        head = path.read_bytes()[:32]
    except OSError:
        return "unreadable"
    if head.startswith(b"\xbe"):
        return "huawei-bin-0xBE"
    if head.startswith(b"PK\x03\x04"):
        return "zip-hap"
    if head.startswith(b"\x7fELF"):
        return "elf"
    if b"hw signed app" in head:
        return "signed-bin-fragment"
    return "other"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


files = [p for p in BUILD.rglob("*") if p.is_file()]
rows = []
for p in sorted(files):
    k = kind(p)
    if p.suffix.lower() in {".hap", ".bin", ".app", ".abc"} or k != "other":
        rows.append((p, k, p.stat().st_size, sha256(p)))

haps = [row for row in rows if row[0].suffix.lower() == ".hap"]
bins = [row for row in rows if row[1] == "huawei-bin-0xBE"]

if haps:
    shutil.copy2(haps[0][0], DIST / "gt6-test.hap")
if bins:
    shutil.copy2(bins[0][0], DIST / "gt6-test-gadgetbridge.bin")
else:
    (DIST / "NO_GADGETBRIDGE_BIN.txt").write_text(
        "The build completed but no file beginning with Huawei app magic 0xBE was found.\n"
        "Do not assume that renaming a ZIP HAP to .bin makes it installable in Gadgetbridge.\n",
        encoding="utf-8",
    )

lines = [
    "GT6 build artifact inspection",
    "=============================",
    "",
]
if not rows:
    lines.append("No candidate application artifacts were found under entry/build.")
else:
    for p, k, size, digest in rows:
        lines.extend([
            f"file: {p.relative_to(ROOT)}",
            f"type: {k}",
            f"size: {size}",
            f"sha256: {digest}",
            "",
        ])

if bins:
    lines.append("RESULT: A native Huawei 0xBE app binary was found and copied to gt6-test-gadgetbridge.bin.")
else:
    lines.append("RESULT: No native Huawei 0xBE app binary was found in this build.")

report = "\n".join(lines) + "\n"
(DIST / "ARTIFACTS.txt").write_text(report, encoding="utf-8")
print(report)
