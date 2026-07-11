# ACIF Skill Interchange Specification

**Version:** 0.1.0
**Status:** Draft
**Spec ID:** [ACIF-SKILL]

---

## Abstract

This document defines the canonical interchange form for the skill content type: a prose instruction package, optionally bundling co-located resource files, that an AI coding tool loads to extend model behavior. It specifies the canonical skill model, the activation vocabulary and its default materialization, the skill body classification and hash boundary, discovery tiers, derivation predicates, cross-reference requirements for hook-activated skills, render-back requirements, and the skill error-identifier registry.

## 1. Introduction

A skill is a Markdown instruction document (canonically `SKILL.md`) that a provider injects into model context when activated — by explicit user invocation, by the model's own decision, or by a hook. Skills commonly ship as a directory bundling the entry file with scripts, templates, and reference material. Providers differ in activation surfaces, frontmatter dialects, and discovery conventions; this document defines the provider-neutral canonical form.

Skills are a frontmatter-bearing content type ([ACIF-CORE] §6.1): the sidecar is the primary carrier, and frontmatter on the entry file is an opt-in supplementary layer. The skill body is prose that becomes model instructions at runtime; ACIF 0.1 does not parse it (§8.4).

## 2. Relationship to ACIF Core

This document is a Level 1 (L1) companion to [ACIF-CORE] and depends on it normatively. Conformance to this document requires conformance to [ACIF-CORE]; every discipline in [ACIF-CORE] §8 and the capability model in [ACIF-CORE] §9 apply to skills without restatement. This document adds skill-specific requirements only; it redefines no [ACIF-CORE] term.

This document is compatible with [ACIF-CORE] version 0.1.x. Both documents are Draft maturity; changes to [ACIF-CORE] may require corresponding changes here.

## 3. Terminology

Terms defined in [ACIF-CORE] §2 are used without redefinition. Additionally:

**entry file** — the canonical Markdown file carrying the skill's instruction prose (`SKILL.md` under the canonical layout, §9).

**bundled resource** — a content file co-located with the entry file inside the skill's body directory, after the exclusions of [ACIF-CORE] §7.2.

**activation** — the canonical block declaring how the skill enters model context: the activation type and the user-invocability flag.

**activation type** — one of the closed enum `{manual, auto, hook}` (§6.2).

**hook-activated skill** — a skill whose activation type is `hook`: a hook item makes the activation decision.

**user-invocable** — the property that the skill is exposed on user-invocation surfaces (slash menus and equivalents), independent of whether the model may invoke it.

## 4. Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

## 5. Conformance

This document extends the [ACIF-CORE] §4 conformance classes with skill-specific requirements and adds one class:

**Conforming canonicalizer** — additionally satisfies §6–§8 (model validation, activation materialization, body classification and hash boundary).

**Conforming validator** — additionally satisfies the reject conditions in §6 that are evaluable over canonical form, without re-applying defaults. Conditions gated on the source form (`acif.skill.activation_type_missing`) bind at ingestion ([ACIF-CORE] §2) and are not re-evaluated by validators — canonical form always carries a materialized `type`.

**Conforming skill record** — an item with `kind: skill` conforms if it satisfies [ACIF-CORE] §5 and §6 of this document.

**Conforming install tool** — additionally satisfies the cross-reference refusal rule as applied in §11.

**Conforming renderer** — software that emits a provider-native form from canonical form; satisfies §12.

Registry conformance is defined in [ACIF-REGISTRY]; §9 (discovery) and §13 of this document state the skill-specific obligations a conforming registry inherits.

The test-vector families in Appendix B are normatively authoritative: an implementation that contradicts a published vector is non-conformant regardless of any prose reading.

## 6. Canonical Skill Model

### 6.1 Schema

The skill extension block appears below the common envelope when `kind: skill`:

```yaml
skill:
  activation:                   # always present in canonical form (§7)
    type: auto                  # REQUIRED in canonical form — manual | auto | hook (§6.2)
    user_invocable: true        # REQUIRED in canonical form — default true, materialized (§7)
    hook_ref:                   # OPTIONAL — only when type: hook (§6.3)
      id: "f47ac10b-..."        # REQUIRED when hook_ref present — activating hook's item UUID
      name: "skill-activator"   # OPTIONAL — advisory only

  requires: {}                  # OPTIONAL — empty/absent in 0.1 (§10)
```

### 6.2 Field requirements

**`activation`** — always present in canonical form; §7 defines materialization from sources that omit it. In a source form, when the block is present, `type` is REQUIRED: a present block without `type` MUST be rejected with `acif.skill.activation_type_missing`. *(Informative: `type` is the block's primary discriminant; defaulting a present block would silently mislabel declared intent — the same rationale as the rule content type's mode-required-when-present rule in [ACIF-RULE].)*

**`activation.type`** — in canonical form, MUST be a member of the closed enum `{auto, hook, manual}`, matched by exact byte comparison ([ACIF-CORE] §8.3). Any other value, including case or whitespace variants, MUST be rejected with `acif.skill.activation_type_invalid`. Semantics:

| Type | Activation decision |
|---|---|
| `manual` | The user explicitly invokes the skill (e.g., a slash command) |
| `auto` | The model decides, based on the skill's `description` and context |
| `hook` | A hook item makes the activation decision (§6.3) |

**`activation.user_invocable`** — OPTIONAL boolean in source form, default `true`, materialized at canonicalization (§7). Orthogonal to `type`: it removes the skill from user-invocation surfaces without affecting model invocation. The post-materialization resolves-to-false state is the installer-side filtering signal (§10.1).

**`hook_ref`** — OPTIONAL, and permitted only when `type: hook`; a `hook_ref` present with any other activation type MUST be rejected with `acif.skill.hook_ref_forbidden`. When present, `id` is REQUIRED — a `hook_ref` without `id` MUST be rejected with `acif.skill.hook_ref_id_missing` — and is the load-bearing reference to the activating hook item ([ACIF-CORE] §10); `name` is advisory only.

**`requires`** — OPTIONAL. The recognized `requires` vocabulary for skills is empty in ACIF 0.1 (§10); any key present is non-conformant ([ACIF-CORE] §9.4).

### 6.3 Hook-activated skills

Canonical truth for hook→skill activation lives on the hook item's `activation_target` block ([ACIF-HOOK] §6.2). The skill-side `activation.type: hook` is a discovery convenience, and `hook_ref` is OPTIONAL even under `type: hook`: a registry resolves the reverse mapping from hook records, and a conforming registry emits the reciprocal cross-reference entry either way (§13.2). A skill MUST NOT be rejected for declaring `type: hook` without `hook_ref`.

*(Informative)* An earlier design-record schema comment marked `hook_ref` required under `type: hook`; the design record's normative Decision #21 text ("an optional `hook_ref.id` when type is `hook`") governs, and this section pins that reading. See Appendix C.

## 7. Activation Default Materialization

The canonicalizer MUST materialize activation defaults at canonicalization ([ACIF-CORE] §8.1), in this single place:

- `activation` block absent in the source → materialize `activation` with `type: auto` and `user_invocable: true`.
- `activation` block present, `user_invocable` absent → materialize `user_invocable: true`.

Canonical form therefore always carries an explicit `activation.type` and `activation.user_invocable`. Validators MUST NOT re-apply these defaults. The derivation predicates in §10.1 are defined over the post-materialization form and are total because of this rule. Materialized values are canonical-form content, not publisher-declared metadata: per [ACIF-CORE] §7.8 they are never written into `publisher_section` and enter no hash preimage.

*(Informative)* This is the same materialize-then-hash pattern as MCP transport-type defaults ([ACIF-MCP]) and the rule activation mode ([ACIF-RULE]): one rule, one place, applied before hashing, never re-applied at validation. A recorded adoption caution: of surveyed providers, only one carries an explicit user-invocability frontmatter key; the amendment was adopted because installers need the resolves-to-false filtering signal, with materialization — not a new author-facing default — as the mechanism.

## 8. Body Classification and Hash Boundary

### 8.1 Body classification

The skill's canonical body is classified single-file or multi-file per [ACIF-CORE] §7.2, with `SKILL.md` as the canonical entry file. A directory containing only the entry file, or only the entry file plus excluded files (`LICENSE*`, `README*`, version-control metadata, root-level registry sidecars), is single-file; any bundled resource makes it multi-file.

### 8.2 `body_hash`

`body_hash` follows [ACIF-CORE] §7 directly: single-file bodies hash the entry file's canonical text form with the frontmatter block stripped; multi-file bodies hash the directory per [ACIF-CORE] §7.4. Editing any bundled resource — a script, a template, a data file — moves `body_hash`.

### 8.3 Extension-block hash coverage

Skills are frontmatter-bearing, so per [ACIF-CORE] §7.8 the sidecar-only preimage extension does not apply and the extension block MUST NOT enter the `body_hash` preimage. The *declared* extension-block values are publisher-declared metadata: observed faithfully into `publisher_section` and covered by `metadata_hash` ([ACIF-PUBLISHER]). Values the publisher never declared exist in canonical form only as materialized defaults (§7) and are covered by no hash ([ACIF-CORE] §7.8).

Consequences (normative in effect, stated for clarity): re-targeting any declared activation value — flipping `type`, flipping `user_invocable`, re-pointing `hook_ref.id` — moves `metadata_hash` and does not move `body_hash`; so does declaring a value that was previously defaulted. A change confined to the skill's prose or bundled resources moves `body_hash` and does not move `metadata_hash`. The two hashes jointly cover the full publisher-declared surface; `body_hash` remains the dispositive content change signal ([ACIF-CORE] §6.2).

### 8.4 Body opacity

The skill body is opaque prose to the canonical layer: ACIF 0.1 does not parse Markdown references (e.g., an `@sibling.md` mention) out of the body. `body_hash` binds the bundle's bytes; it does not resolve which bundled file the prose references at runtime, and a body reference to a path outside the bundle is invisible to the canonical layer. The body-content reference grammar is a roadmap item.

## 9. Discovery

Publishers SHOULD ship a skill as `SKILL.md` inside a skill-named directory. Registries discover skill items through three tiers, evaluated in order:

1. **Publisher-declared** — a pack manifest declares `skill_paths` (e.g., `["./skills/", "./advanced/"]`). A conforming registry MUST use declared paths when present.
2. **Heuristic + filename fallback** — the registry scans known directories and accepts, in order of confidence: `SKILL.md` (canonical filename); any `*.md` whose frontmatter declares `kind: skill`; a bare `.md` file, with the filename used as the display name. For single-file items fetched by URL, the URL-derived filename rule of [ACIF-REGISTRY] feeds this tier.
3. **Non-conformant** — arbitrary layouts with no manifest and no frontmatter are out of scope; publisher action is required.

*(Informative)* Roughly a third of surveyed high-star repositories ship no manifest at all; tier 2 exists for adoption, and tier 1 is the manual pointer for non-standard layouts.

## 10. Capability Dispositions and Derivation Predicates

The recognized `requires` vocabulary for skills is **empty** in ACIF 0.1. Every capability key of the skill vocabulary is disposed per [ACIF-CORE] §9.2 as follows.

### 10.1 DERIVABLE keys

| Key | D_K over canonical body B (post-materialization, §7) |
|---|---|
| `auto_invocable` | `B.activation.type == "auto"` |
| `disable_model_invocation` | `B.activation.type ∈ {manual, hook}` |
| `user_invocable` | `B.activation.user_invocable == false` — resolves-to-false semantics: derivable-true means the skill is filtered from user-invocation surfaces |
| `skill_bundled_resources` | the canonical body classifies multi-file under [ACIF-CORE] §7.2 |

Each predicate produces `{derivable-true, derivable-false}` per the boolean discipline; each cites a single canonical field (or, for `skill_bundled_resources`, the pinned classification predicate) validated at canonicalization before the predicate runs. String-field predicates follow the strict emptiness rule ([ACIF-CORE] §8.3).

*(Informative)* The `auto_invocable` predicate is deliberately single-clause. A compound form conjoining `description != ""` was considered and dropped: whether a description is substantive is a lint concern, not a derivability input, and the conjunct would have stretched D_K from is-the-field-present to is-the-field-useful.

### 10.2 OUT-OF-SCOPE-AT-L1 keys *(informative rationale)*

`display_name`, `description`, `license`, `compatibility`, and `metadata_map` are meta-properties (`description` is load-bearing as a moderation and injection surface, not as a capability signal; `compatibility` is a registry compatibility-matrix concern). `version` is common-envelope material ([ACIF-CORE] §5.1). `project_scope`, `global_scope`, and `shared_scope` are install-location-determined and surface through the `install_scope_capabilities` projection ([ACIF-REGISTRY]). `canonical_filename` and `custom_filename` are discovery/filename meta (§9). Under the out-of-band guardrail ([ACIF-CORE] §9.3) none is `requires`-eligible.

Latent frontmatter fields observed in provider skill formats (allowed-tools, model, bundled hook declarations) are carried as opaque passthrough where present and are roadmap candidates for canonical promotion; their presence MUST NOT soften the orphan-key reject below.

### 10.3 Orphan keys

Any `requires.<key>` on a skill item — including the keys named in §10.1 and §10.2, keys recognized for other content types, and keys matching a latent passthrough field — is non-conformant ([ACIF-CORE] §9.4). An unrecognized key evaluated by a consumer follows the three-valued rule ([ACIF-CORE] §9.5).

## 11. Cross-References

A hook-activated skill participates in the hook↔skill relationship defined across this document and [ACIF-HOOK]:

- The hook side (`activation_target.skill.id`) is canonical truth; the skill side (`activation.hook_ref.id`) is a declared reference resolved per [ACIF-CORE] §10.
- Install tools MUST apply the [ACIF-CORE] §10 refusal rule to a skill whose `hook_ref` resolves `unresolved` or `revoked`.
- Registries MUST emit the reciprocal skill-side cross-reference entry (§13.2) so the relationship is discoverable from both ends without consumer-side reverse scans.

## 12. Render-Back Requirements

These requirements bind conforming renderers; the general render-back framework is [ACIF-RENDER].

- The skill body is emitted byte-verbatim: the prose is the artifact, and no body rewrite is defined for skills in ACIF 0.1.
- Renderers targeting a directory layout MUST emit the entry file as `SKILL.md` inside a skill-named directory (§9) unless the target provider pins a different canonical location.
- Frontmatter projection follows the sidecar→frontmatter flow direction and the reconciliation rules of [ACIF-PUBLISHER]; renderers MUST NOT invent provider-specific frontmatter keys — ACIF 0.1 pins no per-provider skill frontmatter mapping, and canonical field names are emitted as written ([ACIF-CORE] §8.5).
- Opaque passthrough fields (§10.2) MUST be re-serialized through the target format's structured encoder ([ACIF-CORE] §8.5).

## 13. Registry Projections

The projections in this section are computed by registries over the canonical body ([ACIF-REGISTRY] defines the response surface). Every field is a derivation — correct by construction over canonical structure.

### 13.1 `derived_capabilities`

A conforming registry MUST compute the four §10.1 predicates for every skill item at ingest and expose them per [ACIF-REGISTRY]. Install-scope entries surface through `install_scope_capabilities` with per-entry provenance tags ([ACIF-REGISTRY]).

### 13.2 Reciprocal cross-references

For every hook item whose `activation_target.skill.id` resolves to a skill, and for every skill declaring `activation.hook_ref`, a conforming registry MUST emit a skill-side `cross_references` entry (`source_path: "skill.activation.hook_ref"`, `target_kind: hook`) reciprocal to the hook-side entry, resolved per the [ACIF-CORE] §10 state vocabulary.

## 14. Error Identifiers

| Identifier | Class | Condition |
|---|---|---|
| `acif.skill.activation_type_missing` | reject | `activation` block present in source without `type` (§6.2) |
| `acif.skill.activation_type_invalid` | reject | `activation.type` outside the closed enum, or inexact byte form (§6.2) |
| `acif.skill.hook_ref_forbidden` | reject | `hook_ref` present with `type` ≠ `hook` (§6.2) |
| `acif.skill.hook_ref_id_missing` | reject | `hook_ref` present without `id` (§6.2) |

Reject-class identifiers make canonicalization fail. All reject diagnostics for authoring errors are fix-forward ([ACIF-CORE] §8.7).

## 15. Security Considerations

**Prose is the payload.** A skill body becomes model instructions at runtime; prompt-injection content in the body or in `description` is load-bearing without any script executing. `description` doubles as the auto-activation trigger surface (`type: auto` skills are selected on it), which makes it the highest-value injection and typosquatting target of this content type. Registries and moderation pipelines should treat skill prose as the primary scan surface; `body_size_bytes` ([ACIF-REGISTRY]) exists to cost-bound those scans.

**Auto-invocation amplifies.** A `type: auto` skill executes its influence without a user gesture. Typosquatting a popular skill's name and description, combined with auto activation, is the cheap attack shape; the `derived_capabilities` projection of `auto_invocable` (§13.1) exists so installers and policy engines can gate on it.

**Bundled resources ride the trust of the prose.** A multi-file skill's scripts and templates are bound into `body_hash` but are not executed by the skill mechanism itself; they become dangerous when the prose instructs the model to run them. The bundle is complete in coverage, not in inspection — a malicious bundled file can be committed by the hash and scrutinized by no one.

**Reference opacity.** ACIF does not parse body references (§8.4). Prose can instruct the model to read a path outside the bundle — invisible to `body_hash`, discovery, and moderation at the canonical layer. This is recorded as a known limitation; the reference grammar is a roadmap item.

**Metadata is self-asserted.** Everything in [ACIF-CORE] §11 applies; `metadata_map`-style passthrough fields have been flagged as a license-laundering surface, and nothing in this format verifies them.

## 16. References

### 16.1 Normative

- [ACIF-CORE] "ACIF Core Specification", version 0.1.x. `../core/spec.md`
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997. <https://www.rfc-editor.org/rfc/rfc2119>
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017. <https://www.rfc-editor.org/rfc/rfc8174>

### 16.2 Informative

- [ACIF-HOOK] "ACIF Hook Interchange Specification", version 0.1.x. `../hooks-interchange/spec.md` — the hook side of §6.3/§11.
- [ACIF-PUBLISHER] "ACIF Publisher Record Specification", version 0.1.x. `../publisher-spec/spec.md` — `publisher_section`, `metadata_hash`, frontmatter reconciliation.
- [ACIF-REGISTRY] "ACIF Registry Specification", version 0.1.x. `../registry-spec/spec.md` — projection surfaces, URL-derived filenames.
- [ACIF-RENDER] "ACIF Render-Back Specification", version 0.1.x. `../render-back/spec.md`.
- [ACIF-RULE] "ACIF Rule Interchange Specification", version 0.1.x. `../rule-interchange/spec.md`.
- [ACIF-MCP] "ACIF MCP Configuration Interchange Specification", version 0.1.x. `../mcp-interchange/spec.md`.
- [SHAPE] ACIF design record: `SHAPE.md` and `panel/skills-requires-consensus.md` in the ACIF repository — decision provenance (Decisions #19, #21, #22, #23 and their amendments).

---

## Appendix A — Canonical Activation-Type Enum (Normative)

`activation.type ∈ {auto, hook, manual}` — closed enum, exact byte match ([ACIF-CORE] §8.3). This vocabulary is ACIF-originated: no provider carries a matching declaration surface to map from, so no provider mapping table exists. Source forms with no activation declaration take the §7 default (`auto`); `hook` and `manual` are reachable from ACIF-native authoring and from any future provider mapping added by amendment.

## Appendix B — Conformance Test-Vector Families (Normative)

The vectors in these families, published in the `conformance/` directory, are normatively authoritative over prose. Family definition:

**TV-SKILL-\***: (a) empty `requires` conformant; (b) orphan-key reject — a key recognized for another type (`requires.handler_types`) AND a key matching a latent passthrough field (`requires.tool_restrictions`); latent-field presence does not soften the reject; (c) unknown-key three-valued evaluation; (d) `D_K` auto_invocable — activation absent (→true via materialization), `type: auto` (→true), `type: manual` (→false), `type: hook` (→false); (e) `D_K` disable_model_invocation — absent (→false), `auto` (→false), `manual` (→true), `hook` (→true); (f) `D_K` user_invocable — absent (→false), `user_invocable: true` (→false), `user_invocable: false` (→true); (g) `D_K` skill_bundled_resources — single-file `SKILL.md` (→false); directory with `SKILL.md` only (→false); `SKILL.md`+`LICENSE`+`README` (→false, exclusion list); `SKILL.md`+`scripts/` (→true); (h) activation-default materialization — activation absent in source → canonical form carries `type: auto` and `user_invocable: true`; neither `body_hash` nor `metadata_hash` is affected by the materialization (the block is outside the body preimage, and materialized values never enter `publisher_section`, §7/§8.3); (i) body classification (general) — directory with only `{LICENSE, README}` beyond the entry file → single-file; directory with a co-located content file → multi-file; (j) hook-activated cross-reference — `type: hook` + `hook_ref.id` → registry resolves per the [ACIF-CORE] §10 states AND emits the reciprocal skill-side entry (§13.2); (k) hash boundary — flipping a *declared* `activation.user_invocable` with body bytes unchanged moves `metadata_hash` and MUST NOT move `body_hash`; editing a bundled resource moves `body_hash` and MUST NOT move `metadata_hash`; (l) activation rejects — block present without `type`; `type: Auto` (case variant); `hook_ref` under `type: auto`; `hook_ref` without `id` (§6.2/§14); (m) `type: hook` without `hook_ref` is ACCEPTED (§6.3).

Individual vector IDs are assigned in the conformance suite.

## Appendix C — Provenance and Preserved Positions (Informative)

Promoted 2026-07-11 from the ACIF design record: the skill extension block and Decisions #19, #21, #22, and #23 (skills application) of `SHAPE.md`, with the full deliberation record in `panel/skills-requires-consensus.md`. This document replaces an earlier `specs/skill-interchange` draft that predated the skills capability walk.

Preserved positions recorded for future revision: Remy's adoption-data objection to the `user_invocable` surface (only one surveyed provider carries an explicit frontmatter key; re-evaluate if repo surveys show authors declaring it or not); the skills-as-highest-risk-content-type threat context (description injection, auto-invocation typosquatting, bundled-resource payloads, metadata license laundering) recorded for the registry-operator track; moderation revalidation cadence recorded as registry discretion, not a conformance requirement.

Newly minted at spec-promotion time (not present in the design record; flagged for review): all four `acif.skill.*` error identifiers (§14); the §6.3 resolution that `hook_ref` is optional under `type: hook` (the design-record schema comment said required; Decision #21's normative text governs); the §8.3 extension-block hash-coverage statement (declared values ride `metadata_hash` over the faithfully-observed `publisher_section`; materialized defaults unhashed — the single-coverage model of [ACIF-CORE] §7.8, adopted after a spec-purist consult rejected hashing canonical-form metadata as a silent amendment of the faithful-observation rule); and the TV-SKILL (k)–(m) vectors. These items are to be ratified back into the design record at promotion time, following the pattern set by the hook exemplar.
