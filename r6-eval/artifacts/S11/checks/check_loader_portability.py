#!/usr/bin/env python3
"""S11 Runtime loader portability checks for Fermin skill packages.

Simulates the documented host skills route: <skills_root>/<skill-id>/SKILL.md
with adjacent meta.yaml and in-package references/. Does NOT invoke a live
Cursor/DC Bot loader — asserts the static discovery contract a host would need.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required\n")
    sys.exit(2)

# Frontmatter fields Cursor / Agent Skills hosts require for discovery.
FRONTMATTER_REQUIRED = ("name", "description")
# Fields that must NOT appear in SKILL.md frontmatter if they belong to meta.yaml
# (would confuse a naive single-YAML parser or collide with pool meta contract).
META_ONLY_FIELDS = (
    "meta_version",
    "id",
    "path",
    "status",
    "source",
    "adapted_from",
    "license_spdx",
    "license_evidence",
    "decision",
    "rationale",
    "fermin_tags",
    "epistemic",
    "fermin_tag",
    "surfaces",
    "adaptation",
    "references",
    "quality_gate",
    "open_risks",
)
# Fields that must NOT appear as discovery keys inside meta.yaml (host reads
# name/description from SKILL.md frontmatter, not meta).
FRONTMATTER_DISCOVERY_KEYS = ("name", "description")

MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(skill_md: Path) -> tuple[dict | None, str | None]:
    text = skill_md.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, "missing YAML frontmatter fence"
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, f"frontmatter YAML error: {e}"
    if not isinstance(data, dict):
        return None, "frontmatter is not a mapping"
    return data, None


def local_md_links(skill_md: Path) -> list[tuple[str, str]]:
    """Return (label, href) for relative markdown links (skip http/https/mailto/#)."""
    text = skill_md.read_text(encoding="utf-8")
    # Strip frontmatter so code fences in body still scanned — fine for our packages.
    body = FRONTMATTER_RE.sub("", text, count=1)
    out = []
    for label, href in MD_LINK_RE.findall(body):
        href = href.strip()
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # strip optional title
        if " " in href:
            href = href.split(" ", 1)[0]
        out.append((label, href))
    return out


def check_skill(skill_dir: Path) -> dict:
    result = {
        "skill_dir": skill_dir.name,
        "skill_md": str(skill_dir / "SKILL.md"),
        "ok": True,
        "checks": {},
        "failures": [],
    }

    skill_md = skill_dir / "SKILL.md"
    meta_path = skill_dir / "meta.yaml"

    # 1. SKILL.md exists
    if not skill_md.is_file():
        result["ok"] = False
        result["failures"].append("SKILL.md missing")
        result["checks"]["skill_md_present"] = False
        return result
    result["checks"]["skill_md_present"] = True

    # 2. Frontmatter discovery
    fm, err = parse_frontmatter(skill_md)
    if err:
        result["ok"] = False
        result["failures"].append(err)
        result["checks"]["frontmatter_parse"] = False
        return result
    result["checks"]["frontmatter_parse"] = True
    result["frontmatter"] = {
        "name": fm.get("name"),
        "description": (fm.get("description") or "")[:120],
        "keys": sorted(fm.keys()),
    }

    for key in FRONTMATTER_REQUIRED:
        present = bool(fm.get(key)) and isinstance(fm.get(key), str) and bool(str(fm.get(key)).strip())
        result["checks"][f"frontmatter_{key}"] = present
        if not present:
            result["ok"] = False
            result["failures"].append(f"frontmatter missing/empty required field: {key}")

    # name should match directory (host skills route convention)
    name = fm.get("name")
    dir_match = name == skill_dir.name
    result["checks"]["name_matches_dirname"] = dir_match
    if not dir_match:
        result["ok"] = False
        result["failures"].append(f"frontmatter name {name!r} != dirname {skill_dir.name!r}")

    # 3. No meta-only fields leaking into frontmatter
    leaked = [k for k in META_ONLY_FIELDS if k in fm]
    result["checks"]["frontmatter_no_meta_leak"] = len(leaked) == 0
    result["frontmatter_meta_leaks"] = leaked
    if leaked:
        result["ok"] = False
        result["failures"].append(f"frontmatter contains meta-only fields: {leaked}")

    # Extra frontmatter keys beyond name/description are not hard-fail for Cursor
    # (some hosts allow license etc.) but we record them for the evidence.
    extra = [k for k in fm.keys() if k not in FRONTMATTER_REQUIRED]
    result["frontmatter_extra_keys"] = extra

    # 4. Adjacent meta.yaml
    meta_exists = meta_path.is_file()
    result["checks"]["meta_yaml_adjacent"] = meta_exists
    if not meta_exists:
        result["ok"] = False
        result["failures"].append("adjacent meta.yaml missing")
        return result

    try:
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        result["ok"] = False
        result["failures"].append(f"meta.yaml parse error: {e}")
        result["checks"]["meta_parse"] = False
        return result
    if not isinstance(meta, dict):
        result["ok"] = False
        result["failures"].append("meta.yaml is not a mapping")
        result["checks"]["meta_parse"] = False
        return result
    result["checks"]["meta_parse"] = True
    result["meta_keys"] = sorted(meta.keys())
    result["meta_id"] = meta.get("id")
    result["meta_status"] = meta.get("status")

    # 5. meta must not collide with discovery frontmatter keys
    discovery_in_meta = [k for k in FRONTMATTER_DISCOVERY_KEYS if k in meta]
    result["checks"]["meta_no_discovery_keys"] = len(discovery_in_meta) == 0
    result["meta_discovery_collisions"] = discovery_in_meta
    if discovery_in_meta:
        result["ok"] = False
        result["failures"].append(
            f"meta.yaml contains frontmatter discovery keys (parser conflict risk): {discovery_in_meta}"
        )

    # id should align with frontmatter name
    id_align = meta.get("id") == name
    result["checks"]["meta_id_aligns_name"] = id_align
    if not id_align:
        result["ok"] = False
        result["failures"].append(
            f"meta.id {meta.get('id')!r} != frontmatter name {name!r}"
        )

    # 6. Relative links resolve after copy
    links = local_md_links(skill_md)
    link_results = []
    all_links_ok = True
    for label, href in links:
        target = (skill_md.parent / href).resolve()
        # stay within package after resolve
        try:
            target.relative_to(skill_dir.resolve())
            in_pkg = True
        except ValueError:
            in_pkg = False
        exists = target.is_file()
        ok = exists and in_pkg
        link_results.append(
            {
                "label": label,
                "href": href,
                "resolved": str(target),
                "exists": exists,
                "in_package": in_pkg,
                "ok": ok,
            }
        )
        if not ok:
            all_links_ok = False
            result["failures"].append(f"broken/out-of-package link: {href} ({label})")
    result["local_links"] = link_results
    result["checks"]["local_links_resolve"] = all_links_ok if links else True
    result["checks"]["local_links_count"] = len(links)
    if not all_links_ok:
        result["ok"] = False

    # 7. If meta.references lists paths, they must exist after move
    meta_refs = meta.get("references") or []
    meta_ref_results = []
    meta_refs_ok = True
    if isinstance(meta_refs, list):
        for ref in meta_refs:
            if not isinstance(ref, str):
                continue
            t = (skill_dir / ref).resolve()
            exists = t.is_file()
            meta_ref_results.append({"ref": ref, "exists": exists})
            if not exists:
                meta_refs_ok = False
                result["failures"].append(f"meta.references missing after copy: {ref}")
    result["meta_references"] = meta_ref_results
    result["checks"]["meta_references_exist"] = meta_refs_ok
    if not meta_refs_ok:
        result["ok"] = False

    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--skills-root",
        type=Path,
        required=True,
        help="Portable tree skills/ directory (host route simulation)",
    )
    ap.add_argument("--out-json", type=Path, required=True)
    ap.add_argument("--out-md", type=Path, required=True)
    args = ap.parse_args()

    root = args.skills_root
    if not root.is_dir():
        sys.stderr.write(f"skills root missing: {root}\n")
        return 2

    skill_dirs = sorted(p for p in root.iterdir() if p.is_dir())
    results = [check_skill(d) for d in skill_dirs]
    summary = {
        "skills_root": str(root),
        "skill_count": len(results),
        "pass_count": sum(1 for r in results if r["ok"]),
        "fail_count": sum(1 for r in results if not r["ok"]),
        "all_ok": all(r["ok"] for r in results) and len(results) == 8,
        "results": results,
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# S11 loader portability check results",
        "",
        f"skills_root: `{root}`",
        f"skill_count: {summary['skill_count']}",
        f"pass_count: {summary['pass_count']}",
        f"fail_count: {summary['fail_count']}",
        f"all_ok: {summary['all_ok']}",
        "",
        "| Skill | frontmatter | meta adjacent | no conflict | links | result |",
        "|-------|-------------|---------------|-------------|-------|--------|",
    ]
    for r in results:
        c = r["checks"]
        fm_ok = c.get("frontmatter_name") and c.get("frontmatter_description") and c.get("frontmatter_parse")
        meta_ok = c.get("meta_yaml_adjacent") and c.get("meta_parse")
        noconf = c.get("frontmatter_no_meta_leak") and c.get("meta_no_discovery_keys") and c.get("meta_id_aligns_name")
        links = f"{c.get('local_links_count', 0)} ok" if c.get("local_links_resolve") else "FAIL"
        lines.append(
            f"| {r['skill_dir']} | {'yes' if fm_ok else 'NO'} | {'yes' if meta_ok else 'NO'} | "
            f"{'yes' if noconf else 'NO'} | {links} | {'PASS' if r['ok'] else 'FAIL'} |"
        )
        if r["failures"]:
            for f in r["failures"]:
                lines.append(f"  - FAIL detail: {f}")
    lines.append("")
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({"all_ok": summary["all_ok"], "pass": summary["pass_count"], "fail": summary["fail_count"]}, indent=2))
    return 0 if summary["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
