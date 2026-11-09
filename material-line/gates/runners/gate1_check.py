#!/usr/bin/env python3
"""Gate1 structure check for material-line.

Validates key YAML fields and required directories/files.
Exit 0 on success, non-zero on failure.

Usage:
  python material-line/gates/runners/gate1_check.py
  python material-line/gates/runners/gate1_check.py --self-test
  python material-line/gates/runners/gate1_check.py --root /path/to/repo
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML required (pip install -r requirements-validation.txt)", file=sys.stderr)
    sys.exit(2)


REQUIRED_TOP = [
    "README.md",
    "OPTIMIZATION-PLAN.md",
    "STATUS.md",
    "schemas",
    "subjects",
    "themes",
    "jobs",
    "materials",
    "gates",
    "evidence",
    "retrospectives",
    "value-cards",
]

REQUIRED_SCHEMAS = [
    "subject.schema.yaml",
    "theme.schema.yaml",
    "job.schema.yaml",
    "material.schema.yaml",
    "gate-result.schema.yaml",
]

SAMPLE_JOB = "JOB-PY-RAW-040-E06-GATE2"
SAMPLE_MATERIAL = "PYTEXT-PY-RAW-040"


class Gate1Error(Exception):
    pass


def load_yaml(path: Path) -> Any:
    if not path.is_file():
        raise Gate1Error(f"missing file: {path}")
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if data is None:
        raise Gate1Error(f"empty YAML: {path}")
    return data


def require_keys(data: dict, keys: list[str], label: str) -> None:
    missing = [k for k in keys if k not in data]
    if missing:
        raise Gate1Error(f"{label}: missing keys {missing}")


def check_tree(ml: Path) -> list[str]:
    notes: list[str] = []
    for name in REQUIRED_TOP:
        p = ml / name
        if not p.exists():
            raise Gate1Error(f"missing top-level path: material-line/{name}")

    for name in REQUIRED_SCHEMAS:
        if not (ml / "schemas" / name).is_file():
            raise Gate1Error(f"missing schema: schemas/{name}")

    subject = load_yaml(ml / "subjects" / "SUBJ-python-textbook.yaml")
    require_keys(
        subject,
        ["id", "name", "purpose", "audience", "surfaces", "owner"],
        "subject",
    )
    if subject.get("id") != "SUBJ-python-textbook":
        raise Gate1Error("subject id mismatch")

    theme = load_yaml(ml / "themes" / "THEME-py-object-model.yaml")
    require_keys(
        theme,
        ["id", "name", "subject_id", "scope", "out_of_scope", "sample_jobs"],
        "theme",
    )
    if theme.get("subject_id") != "SUBJ-python-textbook":
        raise Gate1Error("theme.subject_id mismatch")
    if SAMPLE_JOB not in (theme.get("sample_jobs") or []):
        raise Gate1Error(f"theme.sample_jobs must include {SAMPLE_JOB}")

    vc = load_yaml(ml / "value-cards" / "VC-python-textbook-weakref.yaml")
    require_keys(vc, ["id", "title", "subject_id", "theme_id", "one_liner"], "value-card")

    queue = load_yaml(ml / "jobs" / "QUEUE.yaml")
    require_keys(queue, ["version", "queues"], "QUEUE")
    qids = [q.get("id") for q in queue.get("queues") or []]
    if SAMPLE_JOB not in qids:
        raise Gate1Error(f"QUEUE missing {SAMPLE_JOB}")

    job_dir = ml / "jobs" / SAMPLE_JOB
    job = load_yaml(job_dir / "job.yaml")
    require_keys(
        job,
        [
            "id",
            "title",
            "status",
            "subject_id",
            "theme_id",
            "input_material_id",
            "python_pin",
            "gates",
            "outputs",
        ],
        "job.yaml",
    )
    if job.get("id") != SAMPLE_JOB:
        raise Gate1Error("job.yaml id mismatch")
    if job.get("input_material_id") != SAMPLE_MATERIAL:
        raise Gate1Error("job input_material_id mismatch")
    if not (job_dir / "BRIEF.md").is_file():
        raise Gate1Error(f"{SAMPLE_JOB}/BRIEF.md missing")
    if not (job_dir / "EXPECTED.md").is_file():
        raise Gate1Error(f"{SAMPLE_JOB}/EXPECTED.md missing")
    if not (ml / "jobs" / "templates" / "JOB-TEMPLATE.yaml").is_file():
        raise Gate1Error("jobs/templates/JOB-TEMPLATE.yaml missing")

    index = load_yaml(ml / "materials" / "INDEX.yaml")
    require_keys(index, ["version", "entries"], "materials/INDEX.yaml")
    entries = {e.get("id"): e for e in index.get("entries") or []}
    if SAMPLE_MATERIAL not in entries:
        raise Gate1Error(f"INDEX missing {SAMPLE_MATERIAL}")
    entry = entries[SAMPLE_MATERIAL]
    if entry.get("level") != "L2":
        raise Gate1Error("sample material must remain level L2 (not fake L3/L4)")
    if entry.get("gate2_failed") != "E06":
        raise Gate1Error("sample material must record gate2_failed: E06")

    mat_dir = ml / "materials" / "L2-canonical-candidate" / SAMPLE_MATERIAL
    level = load_yaml(mat_dir / "LEVEL.yaml")
    require_keys(
        level,
        ["id", "title", "level", "status", "subject_id", "theme_id"],
        "LEVEL.yaml",
    )
    if level.get("level") != "L2":
        raise Gate1Error("LEVEL.yaml must be L2")
    for name in ("README.md", "NOTES.md"):
        if not (mat_dir / name).is_file():
            raise Gate1Error(f"material missing {name}")

    for tier in ("L0-raw", "L1-parsed", "L3-validated", "L4-production"):
        if not (ml / "materials" / tier).is_dir():
            raise Gate1Error(f"missing materials/{tier}")

    # Honesty: L3/L4 must not contain fake-complete material packages
    for tier in ("L3-validated", "L4-production"):
        tier_dir = ml / "materials" / tier
        unexpected = [
            p.name
            for p in tier_dir.iterdir()
            if p.name not in {".gitkeep", "README.md"} and not p.name.startswith(".")
        ]
        if unexpected:
            raise Gate1Error(
                f"materials/{tier} must stay empty of material packages during init; found {unexpected}"
            )

    for name in (
        "gate1-structure.md",
        "gate2-facts.md",
        "gate3-accept.md",
        "README.md",
    ):
        if not (ml / "gates" / name).is_file():
            raise Gate1Error(f"gates/{name} missing")

    for name in ("gate1_check.py", "gate2_exec_stub.py", "README.md"):
        if not (ml / "gates" / "runners" / name).is_file():
            raise Gate1Error(f"gates/runners/{name} missing")

    if not (ml / "evidence" / SAMPLE_JOB / "RUN-NOTE.md").is_file():
        raise Gate1Error(f"evidence/{SAMPLE_JOB}/RUN-NOTE.md missing")

    for name in ("README.md", "PROCESS-LOG.md", "RETRO-2026-11-09-init.md"):
        if not (ml / "retrospectives" / name).is_file():
            raise Gate1Error(f"retrospectives/{name} missing")

    notes.append("Gate1 structure OK")
    notes.append(f"sample job={SAMPLE_JOB} material={SAMPLE_MATERIAL} level=L2")
    return notes


def resolve_material_line(root: Path | None) -> Path:
    if root is not None:
        ml = root / "material-line"
    else:
        # runners/ -> gates/ -> material-line/
        ml = Path(__file__).resolve().parents[2]
    if ml.name != "material-line" or not ml.is_dir():
        raise Gate1Error(f"material-line root not found: {ml}")
    return ml


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="material-line Gate1 structure check")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="repo root containing material-line/ (default: infer from script path)",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run full structural self-test and print OK",
    )
    args = parser.parse_args(argv)

    try:
        ml = resolve_material_line(args.root)
        notes = check_tree(ml)
    except Gate1Error as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 1
    except Exception as e:  # pragma: no cover
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    mode = "self-test" if args.self_test else "check"
    print(f"PASS ({mode}): material-line Gate1")
    for n in notes:
        print(f"  - {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
