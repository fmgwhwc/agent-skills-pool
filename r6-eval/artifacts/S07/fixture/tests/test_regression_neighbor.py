"""Neighbor/regression: empty and whitespace stay rejected after GREEN."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from toy_validate import is_valid_skill_name, name_matches_dir  # noqa: E402


class TestRegressionEdges(unittest.TestCase):
    def test_whitespace_rejected(self):
        self.assertFalse(is_valid_skill_name(" "))
        self.assertFalse(is_valid_skill_name("fermin tdd"))

    def test_dir_match_requires_valid(self):
        self.assertFalse(name_matches_dir("", ""))
        self.assertTrue(name_matches_dir("a-b", "a-b"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
