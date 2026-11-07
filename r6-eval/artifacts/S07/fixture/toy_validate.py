"""Disposable S07 toy validator — minimal GREEN (kebab-case + dir match)."""
from __future__ import annotations

import re

_KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def is_valid_skill_name(name: str) -> bool:
    if not isinstance(name, str) or name == "":
        return False
    return _KEBAB.fullmatch(name) is not None


def name_matches_dir(skill_name: str, dir_name: str) -> bool:
    return is_valid_skill_name(skill_name) and skill_name == dir_name
