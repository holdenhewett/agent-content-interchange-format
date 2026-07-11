# HANDOFF — Finish ACIF v0.1

> Written 2026-07-10 from a capmon planning session. Read this first, then SHAPE.md.
> Delete this file when the plan below is absorbed into normal working docs.

## Why ACIF is now the priority

Decision made in the capmon session (2026-07-10): **ACIF is the authority; capmon
consumes ACIF.** capmon (extracted from syllago, being inverted into a standalone
capability registry at `~/.local/src/capmon`) will publish per-provider capability
data that *conforms to* ACIF's canonical vocabularies. The canonical keys can only
evolve through ACIF spec changes. capmon's publish contract reserves a `spec_ref`
field per canonical key, to be filled as each L1 spec lands. Finishing ACIF
therefore unblocks capmon's consumer contract — ACIF first, capmon Phase 4 after.

## Current state (verified 2026-07-10)

- SHAPE.md carries **29 decisions** and the registry-section schema.
- **Four vocabulary walks complete** (all panel-resolved, `requires` empty for
  v0.1): MCP, agents, hooks, and **skills** — but the skills walk result is NOT
  yet folded into SHAPE.md. `panel/skills-requires-consensus.md` (untracked) is
  the adopted record; SHAPE.md OQ-7 still wrongly lists skills as "remaining."
- **Nothing committed since 2026-05-11.** Untracked: ROADMAP.md, four consensus
  docs (skills, hooks, agents, mcp), panel/pack-model*, research/, .develop/.
  Modified: SHAPE.md, README.md, examples/obra/*, specs/skill-interchange/spec.md.
- The long grill session that produced the skills consensus was not finished.
  Its transcripts are not recoverable from this handoff — the consensus doc is
  the record. **If any selection you remember making is missing from
  `panel/skills-requires-consensus.md`, surface it before Step 2.**

## The plan

### Step 0 — Commit the working tree
Review and commit the outstanding work as-is (consensus docs, ROADMAP, research)
before changing anything. It is months of panel output sitting unprotected.

### Step 1 — Fold the skills consensus into SHAPE.md
Everything adopted in `panel/skills-requires-consensus.md`:
- **Amend Decision #19**: add the normative single-file vs multi-file
  *classification predicate* (spec-purist's gap — same defect class Decision #24
  fixed for MCP transport defaults).
- **Amend Decision #21**: `activation.user_invocable: bool` (default true),
  defaults materialized at canonicalization, `body_hash` computed
  post-materialization. (Remy's adoption-data objection was overridden by Holden;
  preserve it as informative caution.)
- Record the skills per-key disposition table (4 DERIVABLE / 11 OOS-L1 / 0
  eligible), the single-clause `auto_invocable` predicate, the
  `skill_bundled_resources` tightening (exclusion list per registry-operator).
- Update OQ-7 (skills slice resolved), add OQ-10 (SkillMeta
  allowed-tools/model/hooks promotion), add TV-SKILL-* family to Appendix B.
- Whitespace-only string rule for all D_K predicates (Strict: `len(s) > 0`).

### Step 2 — Remaining vocabulary walks: rules, then commands
Same panel process (remy, karpathy, spec-purist, registry-operator; same
three-way disposition under Decision #23). The panel has flagged **rules as the
load-bearing test** of empty-as-steady-state — it is the prose-purest content
type, and spec-purist warned that a fifth unresolved scaffolding gap turns the
principle into "normative theater." Expect this walk to either validate the
principle or produce the first `requires`-eligible key. Do not force empty.

### Step 3 — Close the open questions
- OQ-6: `os`/`arch` absence semantics ("all" vs "unspecified").
- OQ-8: skill supplementary-file referencing (Remy explicitly kept this open —
  body-hash answers "bundle intact," not "which file is referenced").
- OQ-9: two-tier freshness precedence (sidecar `expires` vs external attestation).
- OQ-10: latent SkillMeta field promotion (from Step 1).
- Pin the literal `ACIF_PACK_NAMESPACE` UUIDv5 constant (registry-operator's
  OP-COND-1: non-negotiable before v0.1 publication).

### Step 4 — Vocabulary repatriation (syllago → ACIF)
Decisions #25 and #29 pin canonical vocabularies by *frozen-snapshot reference to
syllago source paths* (`cli/internal/converter/toolmap.go`, `hooks.go`). Under
the new authority direction this is backwards, and those paths are going stale
(capmon extraction). Inline the pinned vocabularies into ACIF spec text as owned
normative appendices: canonical tool names, hook event vocabulary (~30 names),
handler-type enum. Syllago/capmon then conform to ACIF's copy, not vice versa.

### Step 5 — Promote SHAPE.md into the actual specs
SHAPE.md self-describes as "not a spec — a snapshot. Promote to individual spec
files once stable." After Steps 1–4 it is stable. Ship order:
1. `specs/hooks-interchange/` — the designated exemplar, currently empty.
   Source material: SHAPE hook block + Decision #29 vocab + capmon's
   canonical-keys/provider-formats data (now at `~/.local/src/capmon` post-inversion).
2. Finish `specs/skill-interchange/spec.md` (draft exists, predates the skills walk).
3. Remaining L1 specs: rule, command, agent, mcp — from their walk consensus docs.
4. `publisher-spec/` (L2) and `registry-spec/` (L3) — the SHAPE envelope, carrier
   rules, two-section record, and registry-section schema are these specs in
   embryo; largely an extraction-and-normative-tightening job.
5. `render-back/` (L4) — spec the deterministic canonical→provider emit. Its
   provider-support decisions consume capmon's capability matrix.

### Step 6 — Conformance suite
`conformance/` directory with the full TV catalog (TV-1..10, TV-MCP-*,
TV-AGENT-*, TV-HOOK-*, TV-SKILL-*, plus rules/commands families from Step 2).
Appendix B is explicit: the vectors are normatively authoritative; reference
scripts are informative. Reference impls for `body_hash` already exist in
`../moat/reference/`.

## Definition of done (v0.1)

Six L1 specs + L2 + L3 + L4 published; all six content-type walks recorded in
SHAPE decisions; no open OQ without an owner; namespace UUID pinned; conformance
vectors published; no normative reference to syllago/capmon internals (they
conform to ACIF, not the reverse).

## Pointers

- Panel records: `panel/*-consensus.md` (skills is the newest and unfolded one)
- Deferred scope: ROADMAP.md (do not let deferred items creep into v0.1)
- capmon relationship: capmon publishes provider capability *facts* conforming to
  ACIF vocabularies; the caniuse-to-MDN analogy. Its inversion plan lives in the
  capmon session/repo and does not block ACIF work.
