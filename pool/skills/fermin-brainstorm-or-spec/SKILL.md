---
name: fermin-brainstorm-or-spec
description: Turns an ambiguous request into an executable decision record or specification. Use when Fermin lacks a clear outcome, scope, constraints, acceptance evidence, or execution boundary; for small tasks it creates a brief contract, and for multi-capability initiatives it defines independently verifiable decisions.
---

# Brainstorm or Specify

## Purpose

Resolve the decisions that change the asset before spending execution effort. Combine Obra's question-driven clarification with Addy's written acceptance gates. The output may be a short decision card or a full specification; complexity, not ceremony, determines size.

The requester decides desired outcomes, scope tradeoffs, and external commitments. DC Bot may research, propose defaults, and write the spec. The executor does not obtain permission merely by writing an assumption into a document.

## Load / do not load

Load when requirements are vague, conflicting, cross multiple workstreams, or need acceptance criteria before implementation or indexing.

Do not load for a completely specified reversible action or a trivial correction. If exploration alone is requested, produce findings, not a disguised approval to build.

## Steps

### 1. Read before asking

Inspect the request, linked sources, current artifacts, and earlier decisions. Record what is already settled and which sources were checked.

Do not reopen a settled choice or ask for a fact already in the material. Separate:

- **Stated:** directly supplied by the requester or an authoritative artifact.
- **Observed:** read from a source, with a reference.
- **Proposed:** Fermin's recommendation or default.
- **Unknown:** material and not yet answered.

### 2. Test whether the work should split

Split only when capabilities have distinct consumers or assets, independent acceptance, and can be removed without rewriting the rest.

If splitting is needed, create a capability map:

| Capability ID | Outcome / asset | Depends on | Independent acceptance |
|---|---|---|---|
| `<kebab-id>` | `<observable result>` | `<IDs or none>` | `<check>` |

Keep dependency direction acyclic. Give each capability its own decision record or spec. If one useful result covers the request, use one compact record instead of a bureaucracy of modules.

### 3. Clarify the highest-impact uncertainty

Ask one question at a time when its answer changes what will be made, its recipient, its cost/risk, or the evidence needed. Explain the consequence in ordinary language.

First invite the requester's intent in their own terms. Once intent is known, offer at most two or three concrete alternatives with a recommendation and tradeoffs. Do not present avoidable process choices as user decisions.

For authorized reversible work with an obvious low-risk default, state the default and proceed if the governing rules allow. For external, destructive, financial, security-sensitive, or otherwise approval-bound actions, wait for the required choice.

### 4. Compare approaches before locking the contract

Where more than one credible approach exists, compare:

- fit to the outcome and current system;
- dependencies and execution surfaces;
- verification cost and reversibility;
- maintenance burden and what is explicitly excluded.

Mark the selected approach and its selector. Research spikes are labeled exploratory and are not silently converted into deliverables.

### 5. Write the decision record or specification

Use this structure; omit a subsection only when it is truly not applicable.

```markdown
# <Decision / Spec>: <title>
ID: <stable id>
Status: proposed | approved-by-requester | authorized-default | superseded

## Outcome and beneficiary
[What asset exists afterward, for whom, and why.]

## Inputs and observed current state
[Paths / pinned sources / facts already verified.]

## Scope
In: [...]
Out / anti-goals: [...]

## Decisions and alternatives
[Decision, rationale, alternatives, owner of each choice.]

## Execution contract
Surfaces: [dc-bot / cursor-cloud / ubuntu]
Allowed reads: [...]
Allowed changes: [...]
Dependencies: [...]

## Acceptance
- AC-1 [observable condition] -> [concrete check / artifact]
- AC-2 [...]

## Risks, assumptions, and open questions
[Each with effect, evidence state, and needed owner.]
```

Acceptance must test the result, not only the process. “Write three files” is an output; “the catalog resolves each entry to a valid, provenance-bearing skill” is a verifiable outcome.

### 6. Resolve conflicts and set the next gate

The latest explicit requester decision controls goals; project rules and platform safety continue to constrain methods. When sources conflict, name the conflict rather than selecting silently.

After acceptance:

- for substantial or externally consequential work, obtain the approval required by the governing rules;
- for authorized local work, record the chosen approach and proceed under that authority;
- if planning is needed, load `fermin-writing-plans` next;
- if no planning is needed, dispatch the bounded task under `fermin-using-skills`.

A spec approval is not blanket permission to send, publish, pay, delete, or deploy.

## Quality checks

- Can an executor distinguish facts from Fermin's proposals without another conversation?
- Does every acceptance criterion identify observable evidence?
- Can each excluded item be recognized if an executor drifts toward it?
- Are required human decisions actually made by the human, not attributed to them?
- Is the record proportional to the work?

## Done when

- [ ] Outcome, recipient/beneficiary, rationale, and stable asset ID are written.
- [ ] In-scope, exclusions, execution surfaces, and change boundaries are unambiguous.
- [ ] Selected approaches and material defaults have named authority and reasons.
- [ ] Every acceptance criterion has an observable check or artifact.
- [ ] Multi-capability work has stable IDs, acyclic dependencies, and independent checks; otherwise no artificial map was added.
- [ ] Conflicts, unknowns, and reversible plans are explicit rather than silently guessed.
- [ ] The next route is named and no separate external approval was bypassed.
