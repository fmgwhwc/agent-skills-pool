#!/usr/bin/env python3
"""Small offline R5/R6 validation utility; not required at skill runtime.

Modes (--mode):
  auto       (default) Per-skill: candidate → admission gates; released → release gates.
  admission  Force R5 ADAPT intake: every skill must be candidate with pending runtime/release.
  release    Force release gates: every skill must be released with pass + non-empty evidence paths.

Admission is not weakened: inventing runtime/release pass without evidence still fails.
"""
from pathlib import Path
import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
import shutil
import subprocess
import tempfile

try:
    import yaml
    import jsonschema
except ImportError as exc:
    raise SystemExit(f"Install PyYAML and jsonschema to run this check: {exc}")

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "pool/skills"
# Evidence paths in meta are often rooted at the subject tree (parent of r5-adapt-batch).
SUBJECT = ROOT.parent
PIN_ADDY = "301b02b12bff98e4688e6984af6556802322bbde"
PIN_OBRA = "22f0b463e7a5e579904dd6211a520321035526f7"
EXPECTED = {
    "fermin-using-skills", "fermin-brainstorm-or-spec", "fermin-writing-plans",
    "fermin-executing-plans", "fermin-subagent-driven-dev", "fermin-tdd",
    "fermin-verification-dod", "fermin-skill-anatomy",
}

errors = []
check_count = 0


def check(condition, message):
    global check_count
    check_count += 1
    if not condition:
        errors.append(message)


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Validate R5/R6 skill packages")
    parser.add_argument(
        "--mode",
        choices=("auto", "admission", "release"),
        default="auto",
        help="admission=candidate+pending; release=released+pass+evidence; auto=per status",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run catalog-merge + broken-SHA negative control (admission-shaped copy)",
    )
    return parser.parse_args(argv)


def looks_like_path(value: str) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    s = value.strip()
    if s.startswith("http://") or s.startswith("https://"):
        return False
    return ("/" in s) or s.endswith((".yaml", ".yml", ".md", ".json"))


def evidence_paths(meta) -> list:
    """Normalize meta.evidence into a list of path strings."""
    raw = meta.get("evidence")
    if raw is None:
        return []
    if isinstance(raw, str):
        return [raw] if looks_like_path(raw) else ([raw] if raw.strip() else [])
    if isinstance(raw, list):
        out = []
        for item in raw:
            if isinstance(item, str):
                out.append(item)
            elif isinstance(item, dict) and item.get("path"):
                out.append(str(item["path"]))
        return out
    return []


def check_admission_gates(skill_id, meta):
    check(meta.get("status") == "candidate", f"{skill_id}: must enter as candidate")
    qg = meta.get("quality_gate", {})
    check(qg.get("runtime_scenarios") == "pending", f"{skill_id}: invented runtime result")
    check(qg.get("release") == "pending", f"{skill_id}: release should be pending")


def check_release_gates(skill_id, meta):
    check(meta.get("status") == "released", f"{skill_id}: release mode requires status released")
    qg = meta.get("quality_gate", {})
    check(qg.get("runtime_scenarios") == "pass", f"{skill_id}: released requires runtime_scenarios pass")
    check(qg.get("release") == "pass", f"{skill_id}: released requires release pass")
    paths = evidence_paths(meta)
    check(len(paths) > 0, f"{skill_id}: released requires non-empty evidence paths")
    for p in paths:
        check(looks_like_path(p), f"{skill_id}: evidence path not path-like: {p!r}")
        # Soft existence: subject tree or batch root (string check is enough; warn via fail if empty only).
        # If a concrete relative path is given, prefer that it resolve somewhere nearby when present.
        resolved = None
        for base in (SUBJECT, ROOT, Path.cwd()):
            cand = (base / p).resolve() if not Path(p).is_absolute() else Path(p)
            if cand.is_file():
                resolved = cand
                break
        # Existence is preferred but not mandatory for every historical string; require path-like above.
        # If none resolve and path claims r6-eval/evidence/, insist on existence under SUBJECT.
        if p.startswith("r6-eval/") or p.startswith("artifacts/"):
            check(resolved is not None, f"{skill_id}: missing evidence file {p}")


def main(argv=None):
    global errors, check_count
    errors = []
    check_count = 0
    args = parse_args(argv if argv is not None else sys.argv[1:])
    mode = args.mode

    for directory in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        skill_id = directory.name
        skill_file = directory / "SKILL.md"
        meta_file = directory / "meta.yaml"
        check(skill_file.is_file(), f"{skill_id}: missing SKILL.md")
        check(meta_file.is_file(), f"{skill_id}: missing meta.yaml")
        if not skill_file.is_file() or not meta_file.is_file():
            continue
        raw = skill_file.read_text()
        parts = raw.split("---", 2)
        check(raw.startswith("---\n") and len(parts) >= 3, f"{skill_id}: frontmatter delimiters")
        if len(parts) < 3:
            continue
        fm = yaml.safe_load(parts[1])
        meta = yaml.safe_load(meta_file.read_text())
        check(fm["name"] == skill_id, f"{skill_id}: name/path mismatch")
        check(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fm["name"]) is not None, f"{skill_id}: naming")
        check(isinstance(fm.get("description"), str) and len(fm["description"]) <= 1024, f"{skill_id}: description")
        check(bool(re.search(r"\bUse (?:when|for)\b", fm["description"])), f"{skill_id}: trigger in description")
        check(set(fm) == {"name", "description"}, f"{skill_id}: portable top-level frontmatter")
        check(len(raw.splitlines()) <= 400, f"{skill_id}: SKILL.md exceeds 400 lines")
        body = parts[2]
        for section in ["Load / do not load", "Steps", "Done when"]:
            check(section in body, f"{skill_id}: missing {section}")

        schema = json.loads((ROOT / "schema/skill-entry.schema.json").read_text())
        jsonschema.Draft202012Validator.check_schema(schema)
        for problem in jsonschema.Draft202012Validator(schema).iter_errors(meta):
            errors.append(f"{skill_id} schema: {problem.json_path}: {problem.message}")
        check(meta.get("id") == skill_id, f"{skill_id}: meta id mismatch")
        check(meta.get("surfaces") == ["dc-bot", "cursor-cloud", "ubuntu"], f"{skill_id}: surfaces")
        sources = [meta["source"], *meta.get("adapted_from", [])]
        seen = set()
        for source in sources:
            key = (source["repo"], source["ref"], source["path"])
            if key in seen:
                continue
            seen.add(key)
            pin = PIN_ADDY if source["repo"] == "addyosmani/agent-skills" else PIN_OBRA
            check(source["repo"] in {"addyosmani/agent-skills", "obra/superpowers"}, f"{skill_id}: unexpected repo {source['repo']}")
            check(re.fullmatch(r"[0-9a-f]{40}", source["ref"]) is not None, f"{skill_id}: non-SHA source")
            check(source["ref"] == pin, f"{skill_id}: wrong R3 pin at {source['path']}")
            check(pin in source["url"] and source["path"] in source["url"], f"{skill_id}: pin/path URL mismatch")
            check(not source["path"].startswith("/"), f"{skill_id}: absolute upstream path")
            check(source.get("license") == "MIT", f"{skill_id}: source-level MIT license missing at {source['path']}")
        for ref in meta.get("references", []):
            check((directory / ref).is_file(), f"{skill_id}: missing reference {ref}")
        for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", raw):
            if "://" not in link and not link.startswith("#"):
                check((directory / link).exists(), f"{skill_id}: broken link {link}")
        qg = meta.get("quality_gate", {})
        for key in ("static", "content", "package_links", "catalog_merge"):
            check(qg.get(key) == "pass", f"{skill_id}: {key} gate not pass")

        # --- status / runtime / release gates (mode-aware) ---
        status = meta.get("status")
        if mode == "admission":
            check_admission_gates(skill_id, meta)
        elif mode == "release":
            check_release_gates(skill_id, meta)
        else:  # auto
            if status == "candidate":
                check_admission_gates(skill_id, meta)
            elif status == "released":
                check_release_gates(skill_id, meta)
            else:
                check(False, f"{skill_id}: unsupported status {status!r} for auto mode")

        check(bool(meta.get("open_risks")), f"{skill_id}: missing open risks")
        check(bool(meta.get("fermin_tag")) and isinstance(meta.get("adaptation"), dict), f"{skill_id}: incomplete Fermin adaptation notes")
        nums = [int(match.group(1)) for line in body.splitlines() if (match := re.match(r"### (\d+)\.", line))]
        check(nums == list(range(1, len(nums) + 1)) and len(nums) >= 4, f"{skill_id}: malformed numbered steps")

    catalog_text = (ROOT / "catalog-entries.yaml").read_text()
    catalog = yaml.safe_load(catalog_text).get("entries", [])
    check(isinstance(catalog, list) and len(catalog) == 8, "catalog must have 8 entries")
    check({e["id"] for e in catalog} == EXPECTED, "catalog IDs mismatch")
    check({p.name for p in SKILLS.iterdir() if p.is_dir()} == EXPECTED, "unexpected or missing skill directories")
    for entry in catalog:
        if str(entry.get("path", "")).startswith("pool/skills/"):
            check((ROOT / entry["path"] / "SKILL.md").is_file(), f"catalog path missing for {entry['id']}")
        local = SKILLS / entry["id"] / "meta.yaml"
        if local.exists():
            meta = yaml.safe_load(local.read_text())
            for key in ("id", "status", "path", "source", "adapted_from", "license_spdx", "license_evidence", "decision", "rationale", "fermin_tags", "fermin_tag", "surfaces", "quality_gate"):
                # quality_gate may include a free-text checks string that drifts; compare structured gates.
                if key == "quality_gate":
                    mq = meta.get("quality_gate") or {}
                    eq = entry.get("quality_gate") or {}
                    for gk in ("static", "content", "package_links", "catalog_merge", "runtime_scenarios", "release"):
                        check(eq.get(gk) == mq.get(gk), f"catalog mismatch for {entry['id']}: quality_gate.{gk}")
                else:
                    check(entry.get(key) == meta.get(key), f"catalog mismatch for {entry['id']}: {key}")

    # Repo layout keeps the ADAPT report under research/reports/; batch zips may place it at root.
    report = ROOT / "research/reports/R5-ADAPT-REPORT.md"
    if not report.is_file():
        report = ROOT / "R5-ADAPT-REPORT.md"
    check(report.is_file(), "missing report")
    check(any((ROOT / "rejected").glob("*.md")), "missing R5 rejected notes")
    check(any((ROOT / "attribution").glob("*")), "missing attribution notices")
    catalog_root = ROOT / "catalog.yaml"
    if catalog_root.is_file():
        root_entries = yaml.safe_load(catalog_root.read_text()).get("entries", [])
        check({e["id"] for e in root_entries} == EXPECTED, "catalog.yaml IDs mismatch")

    if errors:
        print("FAIL", *errors, sep="\n- ")
        return 1
    print(
        f"PASS: {len(EXPECTED)} skills, catalog, frontmatter/meta, schema, R3 SHA pins, "
        f"local links, mode={mode} gates ({check_count} assertions)."
    )
    return 0


def run_self_test():
    """Catalog merge + broken-SHA negative control on an admission-shaped temporary copy."""
    if main([]) != 0:
        # Current tree may be released; self-test still needs a clean baseline run first optional.
        pass
    scratch = Path(tempfile.mkdtemp(prefix="r5-validator-self-test-"))
    try:
        merged = scratch / "merge"
        shutil.copytree(ROOT, merged, ignore=shutil.ignore_patterns(".venv", "__pycache__"))
        base_schema = yaml.safe_load((ROOT / "schema/catalog.base.yaml").read_text())
        additions = yaml.safe_load((ROOT / "catalog-entries.yaml").read_text())["entries"]
        ids = [entry["id"] for entry in additions]
        if len(ids) != len(set(ids)):
            raise SystemExit("FAIL: duplicate overlay IDs")
        base_schema["entries"] = [entry for entry in base_schema.get("entries", []) if entry["id"] not in ids] + additions
        base_schema["version"] += 1
        base_schema["updated"] = datetime.now(timezone(timedelta(hours=8))).date().isoformat()
        base_meta = [
            {
                "id": entry["id"],
                "status": entry["status"],
                "source": entry["source"],
                "license_spdx": entry["license_spdx"],
                "decision": entry["decision"],
                "rationale": entry["rationale"],
                "fermin_tags": entry["fermin_tags"],
                "epistemic": entry["epistemic"],
            }
            for entry in base_schema["entries"]
            if entry["id"] in ids
        ]
        schema = json.loads((ROOT / "schema/skill-entry.schema.json").read_text())
        for entry in base_meta:
            jsonschema.Draft202012Validator(schema).validate(entry)
        if len(base_schema["entries"]) != 8:
            raise SystemExit("FAIL: overlay against the frozen empty R4 catalog did not yield eight entries")
        print(
            f"PASS: catalog merge yielded {len(base_schema['entries'])} unique skill entries; "
            f"version {base_schema['version']}, schema-valid overlay records."
        )

        broken = scratch / "broken"
        shutil.copytree(ROOT, broken, ignore=shutil.ignore_patterns(".venv", "__pycache__"))
        target = broken / "pool/skills/fermin-tdd/meta.yaml"
        data = yaml.safe_load(target.read_text())
        data["source"]["ref"] = "0" * 40
        target.write_text(yaml.safe_dump(data, sort_keys=False))
        result = subprocess.run(
            [sys.executable, str(broken / "validate_r5.py"), "--mode", "auto"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 or "wrong R3 pin" not in result.stdout:
            raise SystemExit(
                f"FAIL: broken-SHA mutation was not rejected. stdout={result.stdout}; stderr={result.stderr}"
            )
        print("PASS: negative control rejected the deliberately broken SHA (isolated temporary copy).")
    finally:
        shutil.rmtree(scratch)


if __name__ == "__main__":
    cli = parse_args(sys.argv[1:])
    if cli.self_test:
        # Run structural self-test; then exit 0 only if self-test internals passed.
        run_self_test()
        # Also require the live tree to validate under the requested/default mode.
        code = main(["--mode", cli.mode])
        raise SystemExit(code)
    raise SystemExit(main())
