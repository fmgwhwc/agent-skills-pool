"""Focused contract tests for disposable S07 toy validator (stdlib unittest)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from toy_validate import is_valid_skill_name, name_matches_dir  # noqa: E402


class TestIsValidSkillName(unittest.TestCase):
    def test_accepts_kebab_case(self):
        self.assertTrue(is_valid_skill_name("fermin-tdd"))
        self.assertTrue(is_valid_skill_name("a"))
        self.assertTrue(is_valid_skill_name("skill-anatomy-v2"))

    def test_rejects_uppercase_and_underscore(self):
        self.assertFalse(is_valid_skill_name("Fermin_TDD"))
        self.assertFalse(is_valid_skill_name("Fermin-TDD"))
        self.assertFalse(is_valid_skill_name("fermin_tdd"))

    def test_rejects_empty_and_double_hyphen(self):
        self.assertFalse(is_valid_skill_name(""))
        self.assertFalse(is_valid_skill_name("fermin--tdd"))
        self.assertFalse(is_valid_skill_name("-fermin"))
        self.assertFalse(is_valid_skill_name("fermin-"))


class TestNameMatchesDir(unittest.TestCase):
    def test_match_when_valid_and_equal(self):
        self.assertTrue(name_matches_dir("fermin-tdd", "fermin-tdd"))

    def test_mismatch_or_invalid(self):
        self.assertFalse(name_matches_dir("fermin-tdd", "other-skill"))
        self.assertFalse(name_matches_dir("Bad_Name", "Bad_Name"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
