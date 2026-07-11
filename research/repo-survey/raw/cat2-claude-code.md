# Category 2: Claude Code Commands, Agents, Subagents — Raw Agent Output

> **Edit note (2026-05-12):** Vendor-specific plugin/marketplace distribution systems (`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, etc.) are out of scope for ACIF — it is provider-agnostic content interchange, not a distribution-system spec. Observations about those files have been stripped from this raw file; what remains is content-shape data (frontmatter vocabulary, layout patterns, discovery, versioning).

18 repos analyzed (17 content + anthropics/claude-code).

## Table

| repo | stars | content_types | layout_pattern | content_unit | multi_file_aux | versioning | discovery_pattern | frontmatter_fields | quirks |
|------|------:|---------------|----------------|--------------|----------------|------------|-------------------|--------------------|--------|
| anthropics/claude-code | 122830 | command, agent, skill | hybrid (by-type) | single-md-frontmatter (cmd/agent), dir-with-SKILL.md (skill) | dir-convention (`commands/`, `agents/`, `skills/`) | repo-level | dir-convention | description, argument-hint, name | Canonical layout |
| wshobson/agents | 35261 | agent, skill, command | hybrid (by-section) | single-md-frontmatter (agent), dir-with-SKILL.md (skill) | dir-convention | semver (1.3.1 etc.) | dir-convention | name, description, model, tools | Multi-section repo |
| davila7/claude-code-templates | 27204 | agent, command, skill, hook, mcp | by-type then by-topic | single-md-frontmatter (agent/cmd), dir-with-SKILL.md | dir-convention; CLI installs | git-tags + package.json | mixed (filename + CLI registry) | name, description, tools, model, color, permissionMode | Content is npm-distributed; massive (cli-tool/components/) |
| SuperClaude-Org/SuperClaude_Framework | 22754 | command, agent, skill, hook, mcp, mode | by-type | single-md-frontmatter | dir-convention | semver (4.3.0) | dir-convention | name, description, category, personas | — |
| VoltAgent/awesome-claude-code-subagents | 19629 | agent | by-topic (numbered cats) | single-md-frontmatter | dir-convention | semver (1.0.2) | dir-convention | name, description, tools, model | Numbered category directories |
| Donchitos/Claude-Code-Game-Studios | 18475 | agent, skill, rule, hook | by-type | single-md-frontmatter (agent/rule), dir-with-SKILL.md (skill) | dir-convention | none | dir-convention | name, description, tools, model, maxTurns | Adds `maxTurns`; rich `rules/` dir, no manifest |
| contains-studio/agents | 12376 | agent | by-topic (engineering, design...) | single-md-frontmatter | dir-convention | none | dir-convention + filename | name, description (with inline `<example>` blocks), tools, color | Embeds long XML examples inside YAML description |
| ChrisWiles/claude-code-showcase | 5882 | command, agent, skill, hook | by-type | single-md-frontmatter | dir-convention | none | dir-convention | description, allowed-tools | Uses `allowed-tools` (not `tools`); description-only frontmatter for commands |
| vijaythecoder/awesome-claude-agents | 4248 | agent | by-topic (core, orchestrators, specialized, universal) | single-md-frontmatter | dir-convention | none | dir-convention | name, description, tools, model | Heavy use of MCP tool names in `tools:` field |
| zebbern/claude-code-guide | 4115 | agent, skill | by-type | single-md-frontmatter (agent), dir-with-SKILL.md (skill) | dir-convention | none | dir-convention | name, description, tools | Mix of agents (flat md) and skills (dir+SKILL.md+references/) |
| notlikeDev/CCPlugins (was brennercruvinel) | 2692 | command | flat | single-md-no-frontmatter | install.sh/install.py copy files | none | filename-only | (none) | NO frontmatter at all — content is the entire spec |
| wshobson/commands | 2450 | command | by-type (tools/ + workflows/) | single-md-frontmatter | dir-convention | git-tags | dir-convention | model | Minimal frontmatter (only `model:`); body carries everything |
| iannuttall/claude-agents | 2052 | agent | flat | single-md-frontmatter | dir-convention | none | dir-convention | name, description | Smallest viable: just name + description |
| rohitg00/awesome-claude-code-toolkit | 1628 | agent, command, skill, hook, rule, mcp | hybrid (by-type top-level) | single-md-frontmatter or dir-with-SKILL.md | dir-convention | repo-level | dir-convention | name, description | Mirror-style: many sibling categories under one repo |
| ComposioHQ/awesome-claude-plugins | 1652 | agent (+other) | by-section (one section per top-level dir) | single-md-frontmatter | dir-convention | per-section | dir-convention | name, description | Each top-level dir is self-contained |
| feiskyer/claude-code-settings | 1501 | agent, command, skill, hook, mcp, rule | by-type | single-md-frontmatter | dir-convention + `.mcp.json` at root | semver (2.1.7) | dir-convention | name, description, color | Adds `.mcp.json` and `settings.json` as siblings; whole repo is one bundle |
| lst97/claude-code-sub-agents | 1563 | agent | by-topic | single-md-frontmatter | dir-convention | none | dir-convention | name, description, tools (many MCP tools), model | MCP tool names baked into agent frontmatter |
| 0xfurai/claude-code-subagents | 902 | agent | flat (138 files) | single-md-frontmatter | dir-convention | none | filename-convention | name, description, model | Pure flat; no organization at all |

## Narrative

**Frontmatter dominates; sidecars are absent.** Of 18 repos sampled, 17 ship items as `single-md-frontmatter` (agents/commands) or `dir-with-SKILL.md` (skills). Zero use sidecar JSON/YAML for per-item metadata. The community has effectively converged on frontmatter for items, with discovery by directory convention. This is strong signal for ACIF Decision #10: in this ecosystem, sidecars at item scope are normatively new.

**Frontmatter fields are nearly stable but not identical.** `name` and `description` appear in all repos that use frontmatter. `tools`, `model`, `color`, `category` are common. Outliers: `allowed-tools` (ChrisWiles), `maxTurns` (Donchitos), `permissionMode` (davila7), `personas` (SuperClaude), `argument-hint` (anthropics commands). One repo (notlikeDev/CCPlugins) uses *no frontmatter at all* — the markdown body is the entire artifact. Several put rich XML `<example>` blocks inside the description string. This argues for ACIF's `extensions` namespace and treating frontmatter as the dominant carrier with tolerance for arbitrary keys.

**Discovery is overwhelmingly dir-convention.** Items live in `agents/`, `commands/`, `skills/`, `hooks/`, `mcps/`, `rules/` directories. Explicit-path declarations are rare; most repos rely on dir-convention alone.

**Surprises.** (1) `notlikeDev/CCPlugins` (2.7k stars) ships commands with zero frontmatter — pure markdown. (2) Several repos embed MCP-server-specific tool names (`mcp__context7__resolve-library-id`) in agent frontmatter, coupling content to specific tools. (3) `description` strings contain multi-line XML/HTML examples in YAML (contains-studio), which stresses naive YAML parsers. (4) Versioning is mostly absent at item level; when present it's at repo level only.

## ACIF implications

- **Frontmatter MUST remain the primary item carrier**: 17/18 repos use it; ACIF's "sidecar universal, frontmatter opt-in" design (Decision 15) is correct, but expect frontmatter to be the *de facto* authored surface for almost all imported content of these types.
- **Pack inference is the dominant scenario**: A surprising number of high-star repos (Donchitos 18k, 0xfurai, iannuttall, contains-studio 12k, ComposioHQ-agents-related) ship items with no pack file. ACIF must allow inferring a pack from directory layout alone — pack identity should fall back to repo URL + path. Validates Decision #18's inferred-pack path.
- **Discovery via dir-convention is mandatory**: ACIF carriers should scan `agents/`, `commands/`, `skills/`, `hooks/`, `mcps/`, `rules/` even when no manifest lists them.
- **Schema flexibility for frontmatter**: Required keys are `name`, `description`; everything else (`tools`, `model`, `color`, `category`, `maxTurns`, `allowed-tools`, `permissionMode`, `argument-hint`, `personas`) is tool-specific. ACIF's `extensions` field is the right home for these; do not normalize them away.
- **`SKILL.md` is the de-facto skill marker**: All skill-shipping repos use `dir-with-SKILL.md`; ACIF should treat `SKILL.md` presence as definitive evidence of a skill content unit.
- **Tolerate no-frontmatter content units**: At least one popular repo (CCPlugins, 2.7k stars) ships frontmatter-less commands. ACIF carriers should accept a bare `.md` with no frontmatter as a valid item when discovered in a known dir, deriving `name` from the filename.
- **Versioning is repo-scoped, not item-scoped**: Per-item versions essentially do not exist in this ecosystem. ACIF should not require item-level versions; inherit from pack or git ref.
