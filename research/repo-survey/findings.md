# How AI Agent Content Is Structured Today — Survey Findings

**Date:** 2026-05-12
**Surveyed:** 109 repositories across 6 categories, ~1.7M combined stars
**Purpose:** Empirical grounding for ACIF's carrier model, hashing algorithm, and content-type discovery rules

ACIF is provider-agnostic content interchange for the six content types: **hook, skill, rule, command, agent, mcp_config** (SHAPE.md line 13). This survey looks only at how publishers structure those items. Vendor-specific distribution systems (plugin and marketplace files) are out of scope and are not analyzed here.

---

## Scope

| Category | Repos | Aim |
|---|---:|---|
| 1. Skills (Claude + Copilot + MS) | 18 | Validate `SKILL.md` conventions, multi-file handling |
| 2. Claude Code commands / agents / subagents | 18 | Validate frontmatter vocabulary for agents and commands |
| 3. Cursor rules ecosystem | 19 | Validate `.mdc` frontmatter for rules |
| 4. MCP servers and config | 20 | Test whether `mcp_config` belongs in ACIF or defers to MCP registry |
| 5. Other AI coding tools (Cline / Roo / Aider / Continue / Goose / Copilot / Codex) | 18 | Cross-tool carrier diversity, AGENTS.md movement |
| 6. Broader agentic + prompt collections | 16 | Stress-test "publishers with no standard to follow" |

Bias: stars > 50 (skills/agents), > 100 (Cursor), > 500 (broader). Raw per-category outputs live in [`raw/`](./raw/). Per-repo flat data lives in [`repos.csv`](./repos.csv).

---

## Headline findings

### 1. Five distinct shapes of "content unit" dominate

| Shape | Where it lives | Examples |
|---|---|---|
| **Directory with `SKILL.md`** | Skills | anthropics/skills, obra/superpowers, microsoft/skills, github/awesome-copilot |
| **Single `.md` with YAML frontmatter** | Commands, agents, Cursor `.mdc` rules, Copilot prompts | wshobson/agents, VoltAgent/awesome-claude-code-subagents, most Cursor rule repos |
| **Single dotfile** | `.cursorrules`, `.clinerules`, `.aider.conf.yml`, `AGENTS.md`, `AGENT.md` | agentsmd/agents.md, Aider, openai/codex |
| **Single-file aggregations** (CSV / JSON arrays / README-as-index) | Prompt collections, awesome-lists | f/prompts.chat (162k = 1 CSV), PlexPt (60k = 1 JSON), punkpeye/awesome-mcp-servers (87k = 1 README) |
| **Code-as-content** (Python `.py` / TypeScript `.mts`) | LangChain, CrewAI, AutoGen, genaiscript | microsoft/autogen, langgraph, genaiscript |

ACIF already addresses shapes 1, 2, and 3. Shapes 4 and 5 are not in scope today — and the survey suggests they should *stay* out of scope for v0.1, but the spec should say so explicitly.

### 2. AGENTS.md is a real provider-neutral counter-trend ACIF should acknowledge

Five separate repos in the survey treat repo-root `AGENTS.md` as the canonical agent-content artifact:
- `agentsmd/agents.md` (21k stars — the reference site)
- `openai/codex` (82k stars)
- `jackwener/OpenCLI` (20k stars — pushing `AGENT.md` singular for cross-tool discovery)
- `twostraws/SwiftAgents` (1.3k stars)
- `ciembor/agent-rules-books` (1.3k stars — `.md` / `.mini.md` / `.nano.md` size tiers)

The agentsmd.org spec is intentionally minimal: "it's just Markdown, put it at the root." Multiple AI coding tools read it. **This is the agent-content marker that's already cross-tool and not owned by a single vendor** — exactly the kind of artifact ACIF should be aware of, since it's the closest existing thing to a provider-neutral convention.

→ ACIF could acknowledge AGENTS.md as a *marker* (signal that a repo contains agent content) and an emit/render target, without making it an ACIF carrier.

### 3. Multi-file content is *implicit by directory*, not declared

Across the ~30 skill repos sampled in detail, **zero declare auxiliary files in frontmatter or sidecar.** Auxiliary files live next to `SKILL.md` by convention: `scripts/` (10/14), `references/` (8/14), `assets/` (3/14), `examples/` (2/14), or sibling `.md` companions.

→ **OQ-8 should resolve toward implicit-directory-bundle semantics.** Forcing publishers to enumerate would be a behavior change with zero upstream precedent. Spec text: "every file in the skill directory is part of the skill, unless excluded by `.acifignore` or the analogous mechanism."

### 4. Decision #19 (MOAT directory hash) is empirically correct

Every content-bearing skill repo treats the directory as the atomic unit. Per-skill `LICENSE.txt`, `scripts/`, `references/`, sibling `.md` companions are universal and load-bearing — a single-file hash of `SKILL.md` alone would silently exclude them and produce false-positive change signals.

The MOAT v0.4.0 approach (per-file text/binary classification, directory-level combine, VCS dirs excluded, symlinks rejected) is the right granularity. **No change needed.**

### 5. Per-item versioning is rare; absent is the norm

Only two repos in the entire survey put `version` on individual items (Jeffallan/claude-skills, Microsoft Prompty `.prompty` format). Everywhere else, versioning is absent at the item level entirely (~half the repos) or carried at a higher coarseness (semver in `package.json`, git tags).

→ **Decision #16 (no version inheritance into items) is empirically uncontroversial.** Publishers aren't trying to version individual items in the first place.
→ Add to spec text: "per-item `version` is rare in practice; consumers should treat `body_hash` as the authoritative per-item change signal."

### 6. Cross-platform mirror dirs are a documented pain point ACIF can solve

The strongest "ACIF should exist" signal in the survey:

| Repo | Parallel runtime config dirs maintained by hand |
|---|---|
| obra/superpowers (188k) | `.claude/` + `.codex/` + `.cursor/` + `.opencode/` |
| cline/cline (62k) | `.clinerules/` + `.claude/` + `.codex/` + `.agents/` + CLAUDE.md + AGENTS.md (8 dirs total) |
| block/goose (45k) | `.goose/` + `.cursor/` + `.codex/` + `.intersect/` + `.agents/` + AGENTS.md + CLAUDE.md (7+ dirs) |
| eyaltoledano/claude-task-master (27k) | One CLI that emits installers for 6 tools (`.cursor/`, `.roo/`, `.kiro/`, `.taskmaster/`, `.mcp.json`, etc.) |
| FrancyJGLisboa/agent-skill-creator (902) | Self-describes as "14+ tool" exporter — generates per-platform variants into `exports/` |

These are the same rules, agents, and commands copied across N tool-specific directories. The hand-rolled exporters that already exist (claude-task-master, agent-skill-creator) are doing what ACIF proposes to do canonically.

→ Frame ACIF's value prop as **"publish once, render to N tools."** This is the pain that already has hand-rolled solutions.

### 7. The MCP ecosystem is already solved by `server.json` — ACIF should defer

The MCP registry's `server.json` schema (https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json) is consolidating and is **upstream-defined for the MCP protocol itself, not by a vendor**. Reverse-DNS `name`, `packages[]` with `registryType` (npm/oci/pypi/mcpb), `transport`, `environmentVariables[]` — it's complete.

The MCP world clearly separates **install metadata** (`server.json`, owned by the MCP registry) from **runtime wiring** (`.mcp.json`, the `mcpServers` map read by any AI coding tool that speaks MCP).

→ **ACIF's `mcp_config` kind should be the runtime-wiring side only.** Reference upstream `server.json` by `mcpName` / registry id; do not redefine `packages[]` or `environmentVariables[]`. Explicitly out of scope for ACIF v0.1: MCP install metadata.

### 8. ~⅓ of high-star repos ship items with no manifest at all

Donchitos (18k), 0xfurai (902), contains-studio (12k), ComposioHQ/awesome-claude-skills (59k), iannuttall, lst97, vijaythecoder, wshobson/commands. Pure directory-convention — items live in `agents/`, `commands/`, `skills/`, `rules/`, etc., and that's the only signal.

→ **Decision #18 (registry-inferred packs) is empirically essential.** A manifest-required spec would exclude one-third of the highest-star content in the ecosystem.

---

## Frontmatter vocabulary observed in the wild

| Content type | Universal keys | Common keys | Tool-specific outliers |
|---|---|---|---|
| **skill** | `name`, `description` | `license` | Jeffallan's `metadata:` sub-key for `{author, version, domain, triggers, role, scope, output-format, related-skills}` |
| **rule** (`.mdc`) | `description` | `globs`, `alwaysApply` | (very narrow vocab) |
| **agent** | `name`, `description` | `tools`, `model`, `color` | `category`, `maxTurns`, `permissionMode`, `personas` |
| **command** | `description` | `argument-hint` | `allowed-tools` (vs `tools`) |
| **hook** | — | — | (no frontmatter — sidecar-only per Decision #10) |
| **mcp_config** | — | — | (no frontmatter — sidecar-only per Decision #10) |

→ ACIF's narrow normative vocabulary + an `extensions` namespace fits exactly. Required keys are `name`, `description` for the four frontmatter-bearing kinds; everything else belongs in `extensions`.

→ **Edge case to handle**: notlikeDev/CCPlugins (2.7k stars) ships commands with *no frontmatter at all* — the markdown body is the entire artifact. ACIF carriers should derive `name` from filename when frontmatter is absent.

---

## How ACIF's current model holds up

### Decision #10 (sidecar universal, frontmatter opt-in): **VALIDATED with nuance**

- The sidecar pattern is sound for per-item metadata where registries need machine-readable data.
- **But**: in the wild, per-item metadata lives in frontmatter when it lives anywhere — per-item sidecars are normatively new.
- **Adoption depends on tooling that emits sidecars automatically.** Publishers will not hand-author per-item sidecars; the spec needs to be explicit that the sidecar is the CI / registry tool's responsibility, not the publisher's.

### Decision #15 (frontmatter narrow vocabulary): **VALIDATED**

See frontmatter table above — convergence on `name` + `description` + a small tool-specific tail. ACIF's `extensions` namespace handles the tail cleanly.

### Decision #16 (no version inheritance into item records): **VALIDATED**

Per-item versioning is essentially nonexistent. ACIF's lint-enforceable forbidden field set is uncontroversial.

### Decision #17 (`body_hash` as canonical change signal): **VALIDATED**

Publishers don't reliably version items — but git produces clean per-file/per-directory content hashes for free. The "use body_hash as the canonical change signal" call is exactly right for a world where ~half of items have no `version` field.

### Decision #18 (pack identity, declared vs inferred): **VALIDATED**

- ~⅓ of high-star repos have no manifest at all. Inferred pack identity is essential to include them.
- The publisher-declared path (UUIDv4) and registry-inferred path (UUIDv5 over canonicalized `repository_url` + `display_name`) both have clear use cases.

### Decision #19 (MOAT v0.4.0 directory hash): **VALIDATED**

Every skill-shipping repo treats the skill directory as the atomic unit.

### OQ-8 (skill supplementary_files): **SHOULD RESOLVE TO IMPLICIT**

- Zero repos in the survey declare aux files in frontmatter or sidecar.
- The directory IS the bundle.

→ **Recommended resolution text**: "All files in the skill directory are part of the skill unless excluded. Exclusion follows the gitignore mechanism (`.gitignore` first; an optional `.acifignore` overrides at the skill-dir scope). Symlinks and VCS directories are excluded per Decision #19."

---

## Patterns ACIF does NOT yet address

### Single-file aggregations (162k-star tier)

`f/prompts.chat` is *literally one CSV* with 162k stars. PlexPt is *literally one JSON array* with 60k stars. Aggregator awesome-lists are *literally one README* (typically 60k+ stars each).

These collections are real, popular content — but they're not unitized. They have N "items" inside one file.

**Two options for ACIF v0.1:**
- (a) Out of scope. State explicitly that single-file aggregations are not ingested as multi-item content; publishers can either explode them or stay outside ACIF.
- (b) Define an "exploder" carrier: a sidecar that declares "this CSV/JSON contains N items, here's how to slice them" (path/JMESPath/CSV column mapping).

Recommendation: (a) for v0.1, defer (b) to v0.2 if demand emerges.

### i18n / locale variants

PEG ships `_meta.{en,de,zh,...}.json` in 14 locales. `f/prompts.chat` has 30+ `messages/*.json`. obra/superpowers has localized README variants in several skills.

ACIF currently has no `locale` discriminator. **Out of scope for v0.1**; flag for v0.2.

### Multi-size variants

ciembor ships `.md` / `.mini.md` / `.nano.md` for different token budgets. Authors are manually solving for context-window economy.

**Out of scope for v0.1**; could be either `variants: [{name, body_hash}]` in v0.2 or publishers ship N items.

### Code-as-content

CrewAI / LangGraph / AutoGen agents live in `.py` files imported by `__init__.py`. Genaiscript skills are TypeScript modules with manifests embedded in `script({...})` calls. Dify workflows are YAML DSL stored in databases.

**ACIF cannot ingest these as portable units.** Recommendation: treat as opaque payloads or skip; do not try to parse Python ASTs.

### AGENTS.md emit/render

ACIF talks about projecting sidecar values into source-file frontmatter. It does not talk about emitting/reading AGENTS.md. Given the cross-tool reach, an "AGENTS.md render target" is a plausible v0.2 addition.

---

## Adoption likelihood

Rough partition of the 109 surveyed repos by what they'd require to become ACIF-ingestible:

| Bucket | Count | What's needed |
|---|---:|---|
| **Adoptable today, no author action** | 25 | Already ship `SKILL.md` + frontmatter conventions |
| **Adoptable via registry-side adapter** | 40 | Directory convention only, no manifest — registry infers pack and emits sidecars |
| **Out of scope (single-file aggregations)** | 10 | One CSV/JSON = N logical items |
| **Out of scope (code-as-content)** | 15 | Python/TS modules |
| **Out of scope (pure aggregator READMEs)** | 15 | Curated link lists |
| **Already-fragmented MCP install** | 4 | Defer to MCP registry's `server.json` |

So **~65 of 109 popular repos (60%) are ACIF-ingestible** with the current spec — 23% with no author action, 37% with a registry adapter. That's a credible adoption story.

---

## Spec-text recommendations (prioritized)

### High priority (blocker for v0.1 spec accuracy)

1. **OQ-8 resolution**: implicit-directory-bundle with `.gitignore` + optional `.acifignore` override. Add to Decisions table as #20.
2. **Scope text**: explicitly declare out-of-scope for v0.1:
   - MCP server install metadata (defer to MCP registry `server.json`)
   - Single-file aggregations (CSV/JSON arrays as multi-item content)
   - Code-as-content (Python modules, TypeScript scripts) — opaque payloads only
   - i18n / locale variants (defer to v0.2)
   - Multi-size variants (defer to v0.2)
3. **`mcp_config` kind spec text**: clarify that ACIF's `mcp_config` is the runtime-wiring artifact (e.g., a record from the `.mcp.json` `mcpServers` map), NOT a re-spec of MCP install metadata. Reference upstream `server.json` by `mcpName` / registry id.

### Medium priority (improves adoption story)

4. **AGENTS.md interop note**: ACIF carriers MAY emit/read AGENTS.md as a rendered output for cross-tool compatibility; AGENTS.md is not itself an ACIF carrier. (Defer full bidirectional CI to v0.2.)
5. **Cross-platform mirror dirs**: add a non-normative appendix illustrating the "publish once, render to N tools" workflow — the strongest demand signal in the survey.
6. **No-frontmatter content units**: explicit spec note that bare `.md` files in a known directory (e.g., `commands/foo.md`, `rules/bar.md`) are valid items; carrier derives `name` from filename when frontmatter is absent. (Required to handle the notlikeDev/CCPlugins 2.7k-star pattern.)

### Low priority (nice to have)

7. **Filename-as-metadata fallback**: when neither frontmatter nor sidecar exists, derive `display_name` from filename and `version` from git commit. Covers the Fabric / jujumilk3 / CL4R1T4S filename-convention pattern.

---

## Methodology notes

- Six general-purpose subagents ran in parallel, one per category, using `gh` CLI for repo metadata and file contents (cheaper than WebFetch).
- Each agent was given seed repos plus instructions to find more via `gh search`.
- Stars are point-in-time snapshots from the GitHub API on 2026-05-12.
- Where a repo appeared in two surveys (e.g., microsoft/skills surfaced in both skills and other-tools), the entry is preserved in both raw outputs for cross-reference; in `repos.csv` it appears once, categorized by primary content type.
- No repos were modified, cloned, or forked during the survey.
- **Out-of-scope for this survey**: vendor-specific plugin and marketplace distribution systems. ACIF is provider-agnostic content interchange; those systems are orthogonal to its goals and were not analyzed here.
