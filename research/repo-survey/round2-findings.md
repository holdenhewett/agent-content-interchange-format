# Round 2 Survey Findings — Beyond GitHub Star Ranking

**Date:** 2026-05-12
**Surveyed:** ~90 new repositories + 8 registry-level entries across 5 discovery axes
**Purpose:** Fill the "stars-only" blind spot in [Round 1](./findings.md); validate or revise spec implications with broader signal
**Related files:** [`round2-repos.csv`](./round2-repos.csv) (flat per-repo data), [`raw/round2/`](./raw/round2/) (5 per-axis raw reports)

ACIF is provider-agnostic interchange for the six content types: **hook, skill, rule, command, agent, mcp_config**. Round 1 covered 109 high-star repos categorized by content type. Round 2 was a follow-up to find the repos round 1 missed — repos with strong community standing but lower star counts, repos cited by trusted practitioners, repos discoverable only through Reddit/HN/discourse signal, and registry-side data the GitHub view obscures.

---

## Scope

| Discovery axis | New entries | Aim | Raw file |
|---|---:|---|---|
| A. Reddit / HN signal | 25 | Find what practitioners actually share, not what algorithms rank | [`agent-a-reddit-hn.md`](./raw/round2/agent-a-reddit-hn.md) |
| B. Notable individuals | 12 | Pocock, Karpathy-styled, Willison, Yegge, Tan, Steinberger, Schmid, Husain | [`agent-b-notable-individuals.md`](./raw/round2/agent-b-notable-individuals.md) |
| C. Long-tail active | 37 | Vendor skills, hook libraries in non-shell languages, validators, organic adopters | [`agent-c-longtail-active.md`](./raw/round2/agent-c-longtail-active.md) |
| D. Registries / non-GitHub | 28 | npm, PyPI, crates.io, Smithery, Glama, MCP Registry, HuggingFace, SkillsMP | [`agent-d-registries-non-github.md`](./raw/round2/agent-d-registries-non-github.md) |
| E. Discourse citations | 20 | Blog posts, X, podcasts that named specific repos as "good" | [`agent-e-discourse-citations.md`](./raw/round2/agent-e-discourse-citations.md) |

**Access limitations** flagged by the round 2 agents:
- Reddit direct fetches were blocked; Agent A used HN Algolia API and search-engine snippets of Reddit URLs.
- Twitter/X returned HTTP 402 on direct fetches; Agent E used search-engine snippets (140-char depth) and citations *about* X content from blogs.
- These limits mean X/Reddit signal in round 2 is shallower than the GitHub signal — directional, not exhaustive.

---

## Headline findings

### 9. The MCP registry is live and well-defined — round 1's "ACIF defers to `server.json`" call is reinforced, no carrier change needed

Round 1 finding #7 said "ACIF should defer to MCP registry's `server.json`." Round 2 (Agent D) confirmed the registry is live with 9,400+ entries and a well-structured schema separating install metadata from URL metadata.

**ACIF's `mcp_config` scope is unchanged**: it carries the runtime-wiring snippet the harness writes to disk (e.g., the JSON blob the user pastes into Claude Code's `.mcp.json` — server pointer, transport, env). Per SHAPE.md line 35, this is sidecar-only because "harness owns `settings.json`/`mcp.json`; no inline surface exists."

**What ACIF does NOT model:**
- Install metadata (`packages[]` in `server.json`) — that's the MCP registry's domain
- URL/remote metadata structure (`remotes[]`) — same
- Reverse-DNS namespacing (`io.github.modelcontextprotocol/everything`) — same

**What ACIF MAY do:** reference an upstream `server.json` entry by `mcpName` for traceability. Nothing more.

**→ Spec implication.** No carrier change. Round 2 reinforces round 1's "narrow MCP scope" call. ACIF's `mcp_config` stays as the wiring snippet; the MCP registry handles install.

### 10. Round 2 hook surveys produced no normative additions — Syllago's provider-format yaml already canonicalizes the event/matcher surface

Round 1 implicitly assumed a small fixed hook event surface. Round 2 (Agent C) surfaced repos referencing more events than Round 1 noted (e.g., `fnefh/vanilla-boris` covering "9 documented event types").

Checking the reference implementation: Syllago's `docs/provider-formats/claude-code.yaml` declares **29 canonical hook events** for Claude Code alone — spanning session, turn, and tool-call cadences (Setup, SessionStart, SessionEnd, InstructionsLoaded, UserPromptSubmit, UserPromptExpansion, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch, Stop, StopFailure, Notification, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, TeammateIdle, ConfigChange, CwdChanged, FileChanged, WorktreeCreate, WorktreeRemove, PreCompact, PostCompact, Elicitation, ElicitationResult). Each event records its native name, canonical name, category, and matcher-support flag — Syllago's `HookEventInfo` struct.

The "9 event types" in `fnefh/vanilla-boris` reflects an outdated documented surface; Syllago tracks the current one.

**Round 2 also surfaced six functional shapes** hook authors converge on (enforcement / quality / memory / observability / compression / session continuity). These are *usage patterns*, not new content types — the same hook file format serves all six. They're worth noting as context but do not motivate spec changes.

**→ Spec implication.** No normative change. ACIF's `hook` content type captures what it needs at the right level (event, matcher, script location). The six-shape taxonomy is an informative side-note for the appendix, not a carrier addition.

### 11. Download counts diverge 10–100× from star counts — registry data is the real adoption signal

Agent D's most important data point. Examples:

| Artifact | Stars (round 1 unit) | Downloads/week | Ratio |
|---|---:|---:|---|
| `@modelcontextprotocol/sdk` (npm) | ~25k indirect | 36,007,542 | foundational |
| `mcp` (PyPI) | ~25k indirect | 67,000,000+ (933M total) | foundational |
| `@anthropic-ai/claude-agent-sdk` (npm) | n/a | 5,213,779 | SDK pull-through |
| `skills` (npm, Vercel-owned anchor) | 26k repo | 1,015,180 | wide skill install |
| `@upstash/context7-mcp` (npm) | n/a | 1,059,303 | dominant docs-as-MCP |
| `skillflag` (npm) | n/a | 248,350 | CI-driven |
| `mcp-server-git` (PyPI) | n/a | 234,648 | uvx-distributed |

Python `mcp` SDK downloads (67M/week) *exceed* the TypeScript SDK (36M/week). Round 1 was GitHub-stars-only and saw none of this.

**→ Spec implication.** When ACIF reasons about "ecosystem adoption" in spec-text justifications, cite registry download counts where available. Use stars only for repos that aren't published to npm/PyPI.

### 12. The Big Four / Three Frameworks practitioner consensus

Across Reddit, HN, X, and 12+ independently-authored blog posts (Agents A and E), four repositories appear as *de facto* canonical:

1. **obra/superpowers** (188k — already in round 1)
2. **garrytan/gstack** (94k — new)
3. **EveryInc/compound-engineering-plugin** (16.6k — new)
4. **mattpocock/skills** (75k — new, the user-mentioned target)

A narrower "Three Frameworks" consensus appears in framework comparison posts (e.g., Pulumi blog, Latent Space podcast): Superpowers / **GSD (Get Shit Done)** / gstack. GSD (`gsd-build/get-shit-done`, 61.7k) is the most-cited single repo behind the "context rot" named problem.

**→ Spec implication.** When ACIF needs to demonstrate that its carrier model survives real-world structure, these four repos are the reference set. They span: directory-with-`SKILL.md` (Pocock, Superpowers), plugin marketplace (Gstack, Compound Engineering), and command-as-skill (GSD v1 vs v2 split).

### 13. Multi-target render demand is empirically validated (Karpathy-skills as evidence)

Round 1 finding #6 identified "cross-platform mirror dirs" — publishers maintaining `.claude/` + `.cursor/` + `.codex/` + `.opencode/` by hand — as the strongest "ACIF should exist" signal. Round 2 added a high-traffic instance: `forrestchang/andrej-karpathy-skills` (126,684 stars, created 2026-01-27 — one day after Karpathy's January 26, 2026 X post). The repo ships Karpathy's four coding principles as CLAUDE.md + `skills/karpathy-guidelines/SKILL.md` + `.cursor/rules/karpathy.mdc` + CURSOR.md + `README.zh.md` — the same content rendered for multiple runtime targets.

**→ Spec implication.** No new spec text — this is evidence reinforcing round 1's existing recommendation. ACIF's "publish once, render to N tools" value proposition is the labor this kind of repo manually performs.

### 14. Hook → skill activation coupling: the first spec-relevant cross-content-type relationship

The most consequential pattern round 2 surfaced. `diet103/claude-code-infrastructure-showcase` (9.6k stars) ships `skill-rules.json` as a sidecar that a hook reads on `UserPromptSubmit` to decide which skill to inject into the prompt context. This is a *hook that activates a skill* — a relationship ACIF doesn't currently model.

The wider pattern: skills can be activated in three ways:
- **`manual`** — user invokes explicitly (e.g., `/skillname`)
- **`auto`** — model decides based on the skill's description (current default)
- **`hook`** — a hook runs the decision logic and injects the skill

**Schema (Decision #21, landed in SHAPE.md):** introduce an `activation` block on skills and an `activation_target` block on hooks. Cross-references use the **item UUIDv4** that SHAPE.md line 14 already requires on every item.

```yaml
# Skill sidecar
kind: skill
id: "550e8400-..."
name: tdd-workflow
activation:
  type: hook                    # one of: manual | auto | hook
  hook_ref:
    id: "f47ac10b-..."          # REQUIRED when type: hook — item UUIDv4 is the load-bearing key
    name: "skill-activator"     # OPTIONAL — human readability only, advisory

# Hook sidecar
kind: hook
id: "f47ac10b-..."
event: user_prompt_submit
activation_target:
  skill:
    id: "550e8400-..."          # REQUIRED — item UUIDv4
    name: "tdd-workflow"        # OPTIONAL — human readability only
```

**Why UUID, not (pack_id, name):**
- UUIDv4 is globally unique by construction — pack_id is unnecessary
- `name` is mutable; renames don't break UUID references
- Eliminates the lint check for name-stability
- The `name` field stays for human readability when consumers inspect references

**Canonical truth lives on the hook.** The hook is the active party — it makes the runtime decision. The skill's `activation.type` field is a discovery convenience (humans can tell at a glance that the skill is hook-triggered); the registry resolves the reverse mapping from hook records.

**→ Spec implication.** Decision #21 (landed in SHAPE.md). This is the first cross-content-type relationship in ACIF; resolving it cleanly with item UUIDs sets the pattern for any future cross-references.

### 15. Hook bodies are now multi-language — opacity is the right call; runtime needs flow through the existing `requires` block

Round 2 (Agent C) found hook libraries in five non-shell runtimes plus PowerShell:

| Repo | Language | Distribution |
|---|---|---|
| `sushichan044/cc-hooks-ts` | TypeScript | npm |
| `gabriel-dehan/claude_hooks` | Ruby | RubyGems |
| `AvogadroSG1/guardrails` | Go | single binary |
| `jdidion/barbican` | Rust | crates.io |
| `Edmonds-Commerce-Limited/claude-code-hooks-daemon` | Python (daemon) | pyproject.toml |
| `dataplat/dbatools` | PowerShell | in-repo |

**Trade-offs evaluated:**

| Approach | Pros | Cons |
|---|---|---|
| Opaque body, no language field | Matches how OSes work (shebang authoritative); no enum maintenance; no metadata/body skew risk | Consumers can't filter "I don't have Python" pre-deploy |
| Required `language` field | Static filterability; CI gates work | Maintenance burden; redundant with shebang; skew risk if `language: bash` but `#!/usr/bin/env python3` |
| Optional `requires` capability block | Solves filterability; doesn't type the body; **SHAPE.md OQ-7 already reserves this** | Vocabulary needs canonicalization |

SHAPE.md line 194 (OQ-7) already says: "`requires` vocabulary — complete canonical list of hook capability keys. Not yet formally mapped to the `requires` block." This is the right place — runtime hints (`python>=3.10`, `node>=18`, `powershell`, etc.) are *capability requirements*, not content typing.

**→ Spec implication.** No new field. Hook body stays opaque to ACIF. Sharpen OQ-7's resolution: the `requires` block holds optional runtime-capability hints; vocabulary to be canonicalized as a spec deliverable.

### 16. AGENTS.md adoption keeps deepening — promote interop from v0.2 to v0.1 informative appendix

Round 1 finding #2 surfaced AGENTS.md as a "real provider-neutral counter-trend." Round 2 reinforced this:
- **`simonw/research`** (641) ships `CLAUDE.md` as a *single line*: `@AGENTS.md` — pure delegation to AGENTS.md.
- **`vercel-labs/agent-skills`** (26k) ships a file *named* CLAUDE.md but internally titled `# AGENTS.md`.
- **EveryInc/compound-engineering-plugin** uses two-file convention CLAUDE.md + AGENTS.md per plugin.
- **`hashicorp/agent-skills`** (613) ships AGENTS.md + CHANGELOG + CODEOWNERS as the per-plugin standard.

**→ Spec implication.** Round 1 finding #2's recommendation (acknowledge AGENTS.md as marker/render target, not carrier) is now stronger. ACIF tools SHOULD recognize AGENTS.md as a discovery marker; rendering CLAUDE.md → AGENTS.md is OPTIONAL. Add as informative appendix to v0.1 spec.

### 17. Non-conformant skill layouts need a three-tier discovery model

Practitioners ship skills in non-canonical structures all the time. Examples seen in the wild:
- `skills/<name>/SKILL.md` (canonical)
- `skills/<name>.md` with `kind: skill` frontmatter (heuristic)
- `skills/<arbitrary-name>.md` with no frontmatter (filename-only)
- `my-stuff/<random-dir>/<random-name>.md` (genuinely non-conformant)

ACIF needs to be explicit about which of these it ingests:

| Tier | Source | What it requires |
|---|---|---|
| **1. Publisher-declared** | Pack manifest declares `skill_paths: ["./skills/", "./advanced/"]` | Publisher writes a manifest |
| **2. Heuristic + filename fallback** | ACIF scans known dirs; accepts `SKILL.md` (canonical), `*.md` with `kind: skill` frontmatter (heuristic), or bare `.md` with filename → `name` (fallback) | Convention only |
| **3. Non-conformant** | Arbitrary layouts with no manifest and no frontmatter | Publisher action required to enter ACIF |

Tier 1 is the manual-pointer mechanism — a publisher with a non-standard layout adds one declaration and is in. This composes cleanly with Decision #18 (publisher-declared vs registry-inferred packs).

**→ Spec implication.** Decision #22 (landed in SHAPE.md). Tier 1 + Tier 2 are normative; Tier 3 is explicitly out of scope (publisher must conform).

### 18. The single-skill commercial-vertical pattern is the fastest-growing category

Round 1 surfaced single-vertical skills (security, design) but assumed they'd be the minority. Round 2 surfaced these new high-star single-vertical skills:

| Repo | Stars | Vertical |
|---|---:|---|
| `nextlevelbuilder/ui-ux-pro-max-skill` | 77.4k | UI/UX design |
| `coreyhaines31/marketingskills` | 28.1k | Growth marketing |
| `trailofbits/skills` | 5.1k | Security audit |
| `remotion-dev/skills` | 3.1k | Video framework |
| `Orchestra-Research/AI-Research-SKILLs` | 8.3k | ML research |

Plus vendor-published verticals: `anthropics/life-sciences`, `Qovery/qovery-skills`, `vtex/skills`, `SalesforceAIResearch/agentforce-adlc`, `svd-ai-lab/sim-cli` (CAE/physics).

**→ Spec implication.** No spec change. But: the registry-inferred-pack path (Decision #18) must work for these — they don't all ship manifests. Round 1 finding #8 is **strongly reinforced**.

---

## Versioning — revisited

Round 1 finding #5 said per-item versioning is rare and concluded "Decision #16 (no version inheritance) is uncontroversial." That conclusion still holds for the inheritance question.

But Decision #16 doesn't say *which scheme* version should follow when declared. Round 2 raised the question because (a) one round 2 repo (`Orchestra-Research/AI-Research-SKILLs`) ships rich per-item version metadata with CITATION.cff and Sigstore provenance, and (b) the user's lived experience as a publisher: rare-in-practice ≠ unneeded; not having a version number to tell whether something changed is the original motivation for this project.

### What does `body_hash` already cover?

`body_hash` (Decision #17) is the *canonical change signal*: deterministic, automatic, no author work. It answers "did this content change?" but does NOT answer:
- **Which version is newer?** (hashes give identity, not order)
- **Was the change meaningful?** (hashes don't distinguish typo fix from rewrite)
- **What's compatible with what?** (hashes don't carry semantic claims)

`version` fills exactly this gap when authors choose to declare it.

### Scheme trade-offs stress-tested

| Scheme | Example | Pro | Con |
|---|---|---|---|
| **Full SemVer (MAJOR.MINOR.PATCH)** | `2.1.3` | npm-compatible; range queries work; existing tooling speaks it | Borrows ABI vocabulary that doesn't map to content |
| **MAJOR.MINOR** | `2.1` | Less false precision | Half-measure — no gain over "SemVer with patch unused"; locks out tooling that expects three levels |
| **CalVer (date)** | `2026.05.12` | Honest about what version means for content (publishing time) | Two edits same day → no signal; no breaking-change indicator |
| **Free string** | `"alpha-3"` | Publisher freedom | Range queries impossible; cross-references can't constrain |

**Resolution: SemVer.** Always-MAJOR.MINOR.PATCH is the cost of compatibility with the tooling ecosystem that already speaks it. Patch level is *permitted but not required* — publishers can effectively use MAJOR.MINOR if they want by always treating PATCH as 0. CalVer's same-day-edit problem and MAJOR.MINOR's lack of independent value tip the balance.

### Spec text

When `version` is declared, it MUST be valid SemVer 2.0.0. Patch level is permitted but not required (publishers MAY bump minor for any meaningful content change). This strengthens Decision #16 with a concrete format requirement — it does not invalidate the "literal-or-absent, no inheritance" rule.

---

## How ACIF's current model holds up (round 2 corroboration)

| Decision | Round 1 verdict | Round 2 status |
|---|---|---|
| #10 (sidecar universal, frontmatter opt-in) | Validated with nuance | **Still valid.** No publisher hand-authors per-item sidecars; tooling must emit them. |
| #15 (frontmatter narrow vocabulary) | Validated | **Still valid.** `name` + `description` remain universal; per-axis tail varies. |
| #16 (no version inheritance) | Validated | **Strengthened.** When declared, version is SemVer 2.0.0 (new Decision #20); inheritance rule unchanged. |
| #17 (body_hash canonical change signal) | Validated | **Reinforced.** Sigstore attestation in Orchestra-Research treats hash as attestation target. |
| #18 (registry-inferred packs) | Validated | **Reinforced.** Most round 2 long-tail finds have no manifest. |
| #19 (MOAT directory hash) | Validated | **Still valid.** Directory remains the atomic unit. |
| OQ-7 (`requires` vocabulary) | Open | **Direction sharpened.** `requires` holds hook runtime-capability hints (Python/Node/PowerShell version constraints). Vocabulary still to be canonicalized. |
| OQ-8 (implicit directory bundle) | Recommended resolution | **Reinforced.** No counter-examples. |

**New decisions surfaced by round 2:**
- **Decision #20** — `version`, when declared, MUST be valid SemVer 2.0.0 (Versioning section)
- **Decision #21** — Hook → skill activation cross-references use item UUIDv4 (finding #14)
- **Decision #22** — Three-tier skill discovery: publisher-declared > heuristic+frontmatter > non-conformant (finding #17)

---

## Adoption likelihood (round 2 update)

Round 1 estimated 60% of 109 surveyed repos ACIF-ingestible. Round 2's 90 new entries distribute roughly as:

| Bucket | Approx. count | What's needed |
|---|---:|---|
| Adoptable today, no author action | 30 | Ship `SKILL.md` with frontmatter (most notable individuals, vendor skills) |
| Adoptable via registry-side adapter | 35 | Directory convention only (most long-tail, most reddit/HN finds) |
| Already covered by upstream MCP registry | 8 | Defer to `server.json` (most registry entries) |
| Out of scope (curated-index READMEs) | 12 | Awesome-list aggregators |
| Out of scope (deferred patterns) | 5 | See [`ROADMAP.md`](../../ROADMAP.md) |

Combined with round 1 (109 + 90 = 199 surveyed): **~65% of the ecosystem is ACIF-ingestible with the current spec.** The proportion held; the absolute number grew with broader signal.

---

## Spec-text recommendations (round 2)

### High priority (blocker for v0.1 spec accuracy)

**R2-1.** Decision #21 (landed): hook → skill activation cross-references use item UUIDv4. Schema:
- Skill sidecar gains optional `activation: { type: manual | auto | hook, hook_ref?: { id, name? } }`
- Hook sidecar gains optional `activation_target: { skill: { id, name? } }`
- Item UUIDv4 (SHAPE.md line 14) is the load-bearing key; `name` is advisory only

**R2-2.** Decision #22 (landed): three-tier skill discovery — publisher-declared `skill_paths` > heuristic (`SKILL.md` or `kind: skill` frontmatter, with filename fallback) > non-conformant (publisher must conform).

**R2-3.** Decision #20 (landed): when `version` is declared, it MUST be valid SemVer 2.0.0. Patch level is permitted but not required.

**R2-4.** Sharpen OQ-7 resolution direction: hook `requires` block carries optional runtime-capability hints (e.g., `python>=3.10`, `node>=18`, `powershell`). Hook body remains opaque to ACIF — no `language` or `interpreter` field.

### Medium priority (improves adoption story)

**R2-5.** Promote AGENTS.md interop from "v0.2 nice-to-have" to "v0.1 informative appendix": ACIF tools SHOULD recognize AGENTS.md as a discovery marker; rendering CLAUDE.md → AGENTS.md is OPTIONAL.

**R2-6.** In `body_hash` spec text, mention SLSA / Sigstore attestation as compatible (not competing) provenance layers. `Orchestra-Research/AI-Research-SKILLs` demonstrates the pattern.

### Items deferred to [`ROADMAP.md`](../../ROADMAP.md)

Single-file aggregations, i18n / locale variants, multi-size variants, AGENTS.md full bidirectional emit/render, memory-as-content-type, cross-pack versioned dependencies.

---

## Cross-references to round 1

| Round 1 finding | Round 2 corroboration |
|---|---|
| #1 (five content-unit shapes) | Confirmed; round 2 added no sixth shape |
| #2 (AGENTS.md cross-tool counter-trend) | **Strengthened** (finding #16) |
| #3 (multi-file implicit by directory) | Confirmed; no counter-examples |
| #4 (MOAT directory hash empirically correct) | Confirmed |
| #5 (per-item versioning rare) | Reframed: rare in practice ≠ unneeded; SemVer when declared (Versioning section) |
| #6 (cross-platform mirror dirs = pain) | **Strengthened** by karpathy-skills evidence (finding #13) |
| #7 (MCP ecosystem solved by server.json) | **Strengthened** — registry live with 9,400+ entries (finding #9) |
| #8 (one-third of repos ship no manifest) | **Strengthened** — most long-tail round 2 finds have no manifest |

---

## Methodology notes

- Five sonnet subagents ran in parallel, one per discovery axis (Reddit/HN, notable individuals, long-tail active, registries/non-GitHub, discourse citations).
- Each agent was briefed with: (a) ACIF's six content types, (b) round 1's already-covered repos to avoid duplication, (c) explicit user-mentioned targets (Pocock, Karpathy).
- Star counts that appeared suspicious (`forrestchang/andrej-karpathy-skills` at 126k, `mattpocock/skills` at 75k, `affaan-m/everything-claude-code` at 180k) were verified by direct `gh repo view --json stargazerCount,pushedAt,createdAt` calls. All verified.
- Hook event surface verified against Syllago's reference implementation: `cli/cmd/syllago/genproviders.go` `HookEventInfo` struct + `docs/provider-formats/claude-code.yaml` 29-event canonical list.
- `fnefh/vanilla-boris` (0 stars, 5 days old) is flagged in [`round2-repos.csv`](./round2-repos.csv) as "long-tail (instance not adoption)" — proof an artifact *can* be authored, not proof it has uptake.
- **Out-of-scope** for round 2 (same as round 1): vendor-specific plugin and marketplace distribution systems. ACIF is provider-agnostic content interchange.
- Reddit and Twitter/X direct fetches failed; discourse signal is shallower than GitHub signal as a result.
- No repos were modified, cloned, or forked during the survey.
