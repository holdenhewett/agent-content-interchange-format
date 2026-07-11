# Punt — capmon session: fill `spec_ref` fields against the published ACIF specs

**Run this from the capmon repo:** `~/.local/src/capmon`. This file lives in the
ACIF repo (`~/.local/src/agent-content-interchange-format`) so it survives across
sessions; delete it (in the ACIF repo, with a small commit) when the work lands.

## Goal

ACIF v0.1 shipped 2026-07-11: ten specs under `specs/` plus a 150-vector
conformance suite under `conformance/` (all committed on `main`). capmon's
publish contract reserves a `spec_ref` field per canonical key, to be filled as
each spec lands — they have all now landed. Fill every `spec_ref` with a
pointer to the owning ACIF section, and fix any capmon data that the published
copies now contradict (**authority direction: capmon conforms to ACIF's copy,
never the reverse**).

## Where things are in capmon (verified only shallowly — explore first)

- `capyaml/types.go` + `capyaml/validate.go` — the capability-YAML schema; find the `spec_ref` field shape there.
- `seederspec.go` / `sourceman.go` / `docs` dirs — likely homes of the canonical-keys and per-provider data. The old syllago layout was `docs/spec/canonical-keys.yaml` + `docs/provider-formats/*.yaml`; capmon may have moved these.
- Per-provider recognizers: `recognize_{provider}.go` — these implement the vocabularies ACIF now owns; divergence from the ACIF copy is a capmon bug.

## The spec_ref map (ACIF side — authoritative sections)

Spec files: `~/.local/src/agent-content-interchange-format/specs/<dir>/spec.md`.
Suggested ref format: `<SPEC-ID> §<section>` (e.g., `ACIF-HOOK Appendix A.1`) —
match whatever convention `spec_ref`'s existing schema/comments imply.

**Owned vocabularies (canonical names + mappings + tiebreakers):**

| Vocabulary | Owning section |
|---|---|
| Canonical tool names (17) + provider mappings + write/edit tiebreaker + matcher translation + MCP tool-name formats | [ACIF-CORE] Appendix A (A.1–A.4) |
| Hook event names (39) + provider mappings + errorOccurred tiebreaker | [ACIF-HOOK] Appendix A (A.1–A.3) |
| Handler-type enum {command, http, prompt, agent} + per-type fields + absent-type residual | [ACIF-HOOK] Appendix B (+ §8.2) |
| OS enum {windows, linux, darwin}, per-OS selection, provider-mechanism mapping (shell collapse, filename convention, interpreter-flag exclusion) | [ACIF-HOOK] §7 (esp. §7.1, §7.4) |
| Rule activation modes {always, glob, model_decision, manual} + total sub-mode mapping + legacy residual | [ACIF-RULE] Appendix A (A.1–A.2), §10 |
| Argument placeholder `$ARGUMENTS` + mapping + boundary rule + positional documented-unrecognized + `!{}`/`@{}` exclusion | [ACIF-COMMAND] Appendix A (A.1–A.4), §7 |
| Skill activation types {auto, hook, manual} | [ACIF-SKILL] §6.2, Appendix A |
| MCP transport enum {stdio, sse, streamable-http} + default materialization | [ACIF-MCP] §6.2, §7 |

**Canonical capability keys (canonical-keys.yaml → dispositions/predicates):**

| Content type | Keys → owning section |
|---|---|
| mcp (8 keys) | [ACIF-MCP] §9.1 (5 DERIVABLE, incl. env_var_expansion's pinned field set), §9.2 (3 OOS-L1) |
| agents (7) | [ACIF-AGENT] §9.1 (4 DERIVABLE incl. subagent_spawning), §9.2 (3 OOS-L1) |
| hooks (9) | [ACIF-HOOK] §10.1 (3 DERIVABLE), §10.2 (6 OOS-L1) |
| skills (15) | [ACIF-SKILL] §10.1 (4 DERIVABLE), §10.2 (11 OOS-L1) |
| rules (5) | [ACIF-RULE] §9.1 (activation_mode), §9.2 (4 OOS-L1 incl. file_imports) |
| commands (2) | [ACIF-COMMAND] §9.1–§9.2 (both OOS-L1) |

**Registry/coverage surfaces capmon feeds:** `provider_capability_coverage`
([ACIF-REGISTRY] §8.4 — rows for file_imports, hierarchical_loading,
cross_provider_recognition, auto_memory, argument_substitution,
builtin_commands, event_provider_coverage); render-back consumption of the
matrix is [ACIF-RENDER] §11 (informative). Body-hash/conformance context:
[ACIF-CORE] §7, `conformance/README.md`.

## Known divergence hazards (check these first)

1. **Anything transcribed from syllago @ `cf047f52`** should be byte-identical to the ACIF copies (they were mechanically verified at repatriation) — but capmon code paths that *compute* mappings (e.g., Go map iteration for reverse translation) must now implement the pinned tiebreakers: write/edit → `file_edit`; copilot-cli `errorOccurred` → `error_occurred`; otherwise lexicographically-smaller canonical name ([ACIF-CORE] §8.4).
2. **Rule activation**: capmon's `RuleMeta`-era representation can't express `manual` vs `model_decision`; the ACIF enum + deterministic legacy residual ([ACIF-RULE] Appendix A.2) is the conformance target. Enrichment was already flagged as repatriation work.
3. **Placeholder boundary rule** ([ACIF-COMMAND] Appendix A.2) is stricter than syllago's old `strings.Contains` behavior.
4. **Coverage rows are observational**: proxy mechanisms MUST NOT be recorded as support ([ACIF-REGISTRY] §8.4); the per-provider files are authoritative over any by-content-type aggregate (a stale aggregate was caught during the commands walk).

## Norms

- capmon is Go: run the build + tests before declaring done (CLAUDE.md compiled-projects rule; use the log-redirect pattern for output hygiene).
- Judgment-light mechanical fill → cheap models fine; anything that requires *interpreting* a spec section stays with a capable model.
- If a capmon key or mapping exists that ACIF doesn't own a section for, do NOT invent an ACIF ref — surface it as a finding (it's either capmon-internal or a missing ACIF roadmap item).

## Resume instruction

Start a fresh session in `~/.local/src/capmon`, then say:
**read ~/.local/src/agent-content-interchange-format/punt-capmon-spec-refs.md and continue.**
