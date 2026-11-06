# Fermin Definition of Done reference

Apply at the relevant scope, recording evidence or a justified `N/A`. This is a quality floor, not permission to publish or deploy.

## 1. Task contract

- [ ] Requested outcome and explicit acceptance criteria map to the produced artifact.
- [ ] Relevant positive, failure, and edge behavior were checked with observed results.
- [ ] Artifact runs or parses through its intended consumer where available; compilation alone is not runtime behavior.
- [ ] No unrelated refactor, dependency, or side effect was added.
- [ ] Rulings stay within authority and are recorded with impacts.
- [ ] Pending/unattempted checks, blockers, and review limitations are disclosed.

## 2. Code and automation

- [ ] Focused new-behavior tests have RED/GREEN evidence or a documented characterization baseline.
- [ ] Relevant project regression checks are green or failures are named and scoped.
- [ ] Errors, empty inputs, malformed data, and actual boundaries are exercised per risk.
- [ ] Configuration, migrations, interface compatibility, and failure recovery are considered.
- [ ] Tests were not deleted, skipped, or weakened to obtain green.
- [ ] No secret or real external side effect was introduced for test convenience.

## 3. Research and Fermin skill content

- [ ] Sources use full pinned revisions, exact paths, and an explicit evidence state.
- [ ] Author marketing, benchmark, and effectiveness claims are attributed, not repeated as established Fermin results.
- [ ] Skill load triggers and exclusions are discoverable from `description` and the body.
- [ ] Steps produce a named artifact/decision and include local done-when criteria.
- [ ] Examples illustrate procedures without harness-specific installers, telemetry, or unverifiable model-cost claims.
- [ ] Required supporting references live inside the skill package; relative links resolve after shipping.
- [ ] Capability overlap is explicitly merged/deduped, including Obra ↔ Addy overlap where applicable.
- [ ] Skill counts/metadata are meaningful and no empty placeholder directories are used.

## 4. Assembly and integration

- [ ] Interfaces between task outputs agree in ID, name, type, schema, and ownership.
- [ ] One ledger represents state; completed artifacts are not re-created after context loss.
- [ ] Catalog IDs, names, directories, and sources agree; no duplicate IDs.
- [ ] Integrated behavior is exercised, not only each item in isolation.
- [ ] Conflicting skill instructions are reconciled against the controlling request and project rules.
- [ ] Final report includes all material findings and deferred decisions.

## 5. Pool candidate / release separation

Candidate requirements:

- [ ] `SKILL.md` + `meta.yaml` parse and conform to the pool schema/conventions.
- [ ] `decision: adapt|accept`, `license_spdx`, rationale, surfaces, quality-gate results are present.
- [ ] Permissive source license was read at the fixed pin, and required notices are preserved.
- [ ] Source paths were actually read or a failed path is corrected/removed from provenance.
- [ ] Static validation, link/portability check, catalog merge simulation, and content review passed.

Additional release requirements:

- [ ] One realistic scenario on an intended execution surface passed, or a defined suite of scenarios appropriate to that skill passed.
- [ ] The authorized Fermin pool owner accepts its candidate evidence and open risks.
- [ ] Any separately required publication/repository approval exists independently of this checklist.

A candidate is not deficient merely because release-gate scenario execution has not yet happened, but it must not be advertised as released or as having passed those scenarios.
