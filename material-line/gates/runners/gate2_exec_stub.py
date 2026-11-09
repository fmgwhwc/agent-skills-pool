#!/usr/bin/env python3
"""Gate2 stub: extract / list fenced python blocks from Markdown.

This is a STUB toward a full Gate2 facts runner (isolated exec + prediction
diff + evidence sidecar). It does NOT claim Gate2 pass.

Usage:
  python material-line/gates/runners/gate2_exec_stub.py path/to/file.md
  python material-line/gates/runners/gate2_exec_stub.py --dry-run path/to/file.md
  python material-line/gates/runners/gate2_exec_stub.py --list path/to/file.md
  python material-line/gates/runners/gate2_exec_stub.py --extract path/to/file.md

Future (not in this PR): pin interpreter, run blocks, compare expected vs actual,
write evidence under material-line/evidence/<JOB-ID>/.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FENCE_RE = re.compile(
    r"```(?:python|py)\s*\n(.*?)```",
    re.IGNORECASE | re.DOTALL,
)


def extract_python_fences(text: str) -> list[str]:
    return [m.group(1).strip("\n") for m in FENCE_RE.finditer(text)]


def cmd_list(blocks: list[str]) -> None:
    print(f"found {len(blocks)} python fence(s)")
    for i, block in enumerate(blocks, 1):
        lines = block.splitlines() or [""]
        preview = lines[0][:72]
        print(f"  [{i}] lines={len(lines)} preview={preview!r}")


def cmd_extract(blocks: list[str], out_dir: Path | None) -> None:
    if out_dir is None:
        for i, block in enumerate(blocks, 1):
            print(f"----- block {i} -----")
            print(block)
            if not block.endswith("\n"):
                print()
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, block in enumerate(blocks, 1):
        path = out_dir / f"block_{i:02d}.py"
        path.write_text(block + ("\n" if not block.endswith("\n") else ""), encoding="utf-8")
        print(f"wrote {path}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Gate2 stub: list/extract python fences (not a full comparator)",
    )
    parser.add_argument("markdown", type=Path, help="Markdown file to scan")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="discover fences only; do not execute (default behavior is also non-executing)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="print fence inventory (default if no --extract)",
    )
    parser.add_argument(
        "--extract",
        action="store_true",
        help="print or write extracted blocks",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="with --extract, write block_XX.py files here",
    )
    args = parser.parse_args(argv)

    path: Path = args.markdown
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    blocks = extract_python_fences(text)

    print("gate2_exec_stub: STUB toward full Gate2 (exec + prediction diff)")
    print(f"input: {path}")
    print(f"dry_run: {True if args.dry_run or not args.extract else args.dry_run}")

    # Default: list inventory. Never execute in this stub.
    if args.extract and not args.dry_run:
        # Still no execution — extract only. Documented stub path.
        cmd_extract(blocks, args.out_dir)
    else:
        cmd_list(blocks)
        if args.dry_run:
            print("dry-run: skipped execution and prediction compare (not implemented)")

    print(
        "NOTE: full comparator (pinned interpreter, stdout diff, evidence write) "
        "is a later iteration — this stub must not be treated as Gate2 pass."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
