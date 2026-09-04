#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SIGNED = DIST / "gt6-test-gadgetbridge.bin"
REPORT = DIST / "ARTIFACTS.txt"

if not SIGNED.exists():
    raise SystemExit("signed BIN is missing")

data = SIGNED.read_bytes()
if not data.startswith(b"\xbe"):
    raise SystemExit("signed BIN no longer starts with Huawei app magic 0xBE")
if len(data) < 32:
    raise SystemExit("signed BIN is too short for signing header")

head = data[-32:]
if head[:16] != b"hw signed app   ":
    raise SystemExit("signed BIN has no 'hw signed app' footer")
if head[16:20] != b"1000":
    raise SystemExit("signed BIN has unexpected signing version")

signed_area_size = int.from_bytes(head[20:24], "big")
block_count = int.from_bytes(head[24:28], "big")
reserved = int.from_bytes(head[28:32], "big")
digest = hashlib.sha256(data).hexdigest()

extra = f"""

Account-free development signature
==================================
file: dist/gt6-test-gadgetbridge.bin
type: huawei-bin-0xBE-signed
size: {len(data)}
sha256: {digest}
signature_magic: hw signed app
signature_version: 1000
signed_area_size: {signed_area_size}
block_count: {block_count}
reserved: {reserved}

RESULT: Signed Huawei BIN is structurally ready for the Gadgetbridge installation test.
NOTE: The signature uses the public OpenHarmony development identity. Whether retail GT6 firmware trusts it must be tested on the watch.
"""

with REPORT.open("a", encoding="utf-8") as f:
    f.write(extra)
print(extra)
