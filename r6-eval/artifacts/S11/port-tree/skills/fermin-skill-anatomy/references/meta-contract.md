# Fermin `meta.yaml` v1 contract

This extension sits beside `SKILL.md`, preserving portable Agent Skills frontmatter (`name`, `description`). Keep each field factual and reviewable.

## Required Fermin extensions

```yaml
meta_version: 1
id: <directory and SKILL name>
status: candidate
source: <primary source object; see below>
adapted_from:
  - <every contributing source object>
license_spdx: MIT | MIT AND MIT | <other actually applicable SPDX>
decision: adapt
rationale: <why this capability is worth retaining>
fermin_tags: [agent-skills]
epistemic: evidenced
fermin_tag: borrow-adapt
surfaces: [dc-bot, cursor-cloud, ubuntu]
adaptation:
  kept: [<reusable upstream ideas>]
  rewritten: [<Fermin-specific changes>]
  cut: [<installers, telemetry, duplicated workflows, etc.>]
  dedup: [<sources merged or rejected, and reason>]
references: [<in-package files needed to execute the skill>]
quality_gate:
  static: <pass after real validation>
  content: <pass after review against this contract>
  package_links: <pass after checking from shipped layout>
  catalog_merge: <pass after simulation>
  runtime_scenarios: <pending unless actually run with evidence>
  release: pending
open_risks: [<known limits; required if runtime scenario not run>]
removal_or_deprecation: none
```

## One source object

```yaml
repo: owner/repo
ref: <40-character immutable upstream commit SHA>
path: <exact file actually read/used>
url: https://github.com/owner/repo/blob/<full-SHA>/<exact-file>
license: MIT
notes: <what was borrowed, if useful>
```

For a derived doc packaged under `references/`, include its upstream path as a separate `adapted_from` entry. Use `source` for the primary source and do not drop secondary provenance.

A license-only read supports the license conclusion; it is not borrowed workflow content and need not be an `adapted_from` entry. Record the license pin/URL in `license_evidence`.

## Status and gate boundaries

- `candidate`: content and available static/content checks are complete; explicit human/runtime acceptance remains.
- `released`: pool owner accepted and required runtime scenarios are evidenced. The schema also permits `draft` and `deprecated` for their ordinary meanings.
- `static`: frontmatter/meta parsing, schema requirements, names/IDs, SHA/url/path/license validation.
- `content`: substantive review against source fidelity, Fermin surfaces, portability, minimalism, dedup, and checks.
- `package_links`: in-package relative-link resolution from the shipped directory.
- `catalog_merge`: exact catalog merge/dedup simulation, not just YAML readability.
- `runtime_scenarios`: actual run identifiers, artifacts, outcomes, and limits; `pending` is valid and honest.

A generic checklist marked pass without its check/evidence is insufficient. Record `checks` in the meta file or point to the R5 report's validation section. On later revisions use an `evidence` list with commands, date/time timezone, artifacts, and results.

## Compatibility note

The existing `schema/skill-entry.schema.json` accepts Fermin extensions (`additionalProperties: true`), but it requires `source` to be one object. Multi-source skills therefore preserve the complete list in `adapted_from` rather than changing `source` into an array. Keep `epistemic: evidenced` for source-based adaptations; it does not imply runtime-effectiveness proof.
