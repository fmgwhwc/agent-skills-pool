# Follow-up (W5.3): validate_r5.py release awareness

Timestamp: 2026-11-07 08:47:00 CST (Asia/Shanghai)

`validate_r5.py` currently hard-asserts for every skill:
- `status == candidate`
- `quality_gate.runtime_scenarios == pending`
- `quality_gate.release == pending`

That was correct for **R5 candidate admission**. After S12, eight `meta.yaml` files are locally `status: released` with runtime/release `pass`.

**Do not** weaken admission silently. Recommended W5.3 change:
1. Split checks: admission mode (candidate) vs release mode (released + cited evidence paths).
2. When `status == released`, require `quality_gate.runtime_scenarios == pass`, `quality_gate.release == pass`, and non-empty `evidence` list pointing at r6-eval YAML paths.
3. Keep rejecting invented runtime passes without evidence paths.

No skill-body SKILL.md edits in S12.
