# Round 2 — Package Registries & Non-GitHub Sources

## Methodology

Discovery ran across npm, PyPI, crates.io, the official MCP registry API, Glama, Smithery, HuggingFace, SkillsMP marketplace, and alternative code hosts. Adoption signal is weekly downloads (npm, PyPI via pypistats.org) or total downloads (crates.io). Stars deliberately excluded per brief. npm queries used `npm search` + npmjs downloads API; crates.io used its REST API with `User-Agent` set; PyPI used pypistats.org; registries were fetched via their public APIs or WebFetch. Codeberg and Bitbucket returned no significant signal — those findings are noted under Non-GitHub Hosts.

---

## By Registry

### npm

#### 1. `skills` — Vercel Labs open agent-skills ecosystem

- **URL:** https://www.npmjs.com/package/skills
- **Adoption:** 1,015,180/week; 3,390,405/month (as of 2026-05-05–11)
- **GitHub repo:** https://github.com/vercel-labs/skills
- **Content type:** skill (multi-tool SKILL.md distribution hub)
- **Layout:** Keywords list every major agent runtime as a tag (claude-code, cursor, gemini-cli, codex, windsurf, opencode, goose, amp, kiro-cli, 25+ more). Package acts as the canonical npm entry point for the open agent-skills ecosystem.
- **Distinctive convention:** The `skills` package is essentially the npm-side anchor for the cross-vendor SKILL.md standard. Consumers run `npx skills install <id>` to pull individual skill dirs.

#### 2. `@anthropic-ai/claude-agent-sdk` — Official Claude Agent SDK (TypeScript)

- **URL:** https://www.npmjs.com/package/@anthropic-ai/claude-agent-sdk
- **Adoption:** 5,213,779/week; 20,156,943/month
- **GitHub repo:** https://github.com/anthropics/claude-agent-sdk-typescript
- **Content type:** agent (SDK for building subagents/autonomous agents)
- **Layout:** Standard TypeScript SDK package; exposes programmatic API for spawning Claude as an autonomous coding agent. Not itself a content bundle.
- **Distinctive convention:** The highest-volume claude-specific package on npm by far. Everything in the agent-SDK ecosystem (Composio, Raindrop, Conclave, PostHog wrappers) imports this.

#### 3. `@modelcontextprotocol/sdk` — Official MCP TypeScript SDK

- **URL:** https://www.npmjs.com/package/@modelcontextprotocol/sdk
- **Adoption:** 36,007,542/week
- **GitHub repo:** https://github.com/modelcontextprotocol/typescript-sdk
- **Content type:** mcp_config (foundational SDK; basis for all npm-distributed MCP servers)
- **Layout:** Standard TypeScript library. Not a content bundle; used by virtually every npm-published MCP server.
- **Distinctive convention:** Highest-volume MCP package; more than 35x the volume of the next-highest MCP server package. The `@modelcontextprotocol/ext-apps` companion (1,356,087/week) adds interactive MCP UI surface.

#### 4. `@upstash/context7-mcp` — Context7 MCP server

- **URL:** https://www.npmjs.com/package/@upstash/context7-mcp
- **Adoption:** 1,059,303/week; 4,870,819/month
- **GitHub repo:** https://github.com/upstash/context7
- **Content type:** mcp_config (live documentation MCP server)
- **Layout:** Runnable via `npx @upstash/context7-mcp`. Exposes live library documentation as MCP resources/tools. Config snippet for Claude/Cursor/Windsurf in README.
- **Distinctive convention:** The dominant documentation-as-MCP pattern. Users add it via a single JSON stanza in their mcp config.

#### 5. `@modelcontextprotocol/server-filesystem` — Official filesystem MCP server

- **URL:** https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem
- **Adoption:** 280,404/week
- **GitHub repo:** https://github.com/modelcontextprotocol/servers
- **Content type:** mcp_config
- **Layout:** Single runnable binary; distributed as `npx @modelcontextprotocol/server-filesystem <allowed-paths>`. No content files — exposes filesystem as MCP resource surface.
- **Distinctive convention:** Reference implementation of the stdio-transport MCP server pattern.

#### 6. `@modelcontextprotocol/server-sequential-thinking` — Sequential thinking MCP server

- **URL:** https://www.npmjs.com/package/@modelcontextprotocol/server-sequential-thinking
- **Adoption:** 103,349/week
- **Content type:** mcp_config (reasoning scaffold exposed as MCP tool)
- **Distinctive convention:** Most-used by install count on Smithery (5,550+ uses per Smithery data). A pure-logic tool with no external API dependency — popular because it works offline.

#### 7. `@sentry/mcp-server` — Official Sentry MCP server

- **URL:** https://www.npmjs.com/package/@sentry/mcp-server
- **Adoption:** 86,688/week
- **GitHub repo:** https://github.com/getsentry/sentry-mcp
- **Content type:** mcp_config
- **Layout:** Versioned `@sentry/mcp-server@0.33.0`. Standard MCP server; exposes Sentry error/issue API as tools.
- **Distinctive convention:** Vendor-official MCP server with high adoption. Shows pattern where SaaS vendors publish their own MCP packages on npm.

#### 8. `skillflag` — Skill bundling CLI convention

- **URL:** https://www.npmjs.com/package/skillflag
- **Adoption:** 248,350/week (CI-driven; most are automated installs in pipelines)
- **GitHub repo:** https://github.com/osolmaz/skillflag
- **Content type:** skill (CLI convention for embedding skills inside any npm package)
- **Layout:** Exposes `skillflag` and `skill-install` binaries. Skills live at `skills/<skill-id>/SKILL.md` inside any npm package. The `--skill list`, `--skill show <id>`, `--skill export <id>` flags work on any package implementing the convention.
- **Distinctive convention:** Treats skill discovery as a stable CLI interface, like `--help`. Packages that implement skillflag become self-describing to agents. High downloads appear to come from CI usage in packages that embed the convention.

#### 9. `vibe-rules` — Multi-tool rules manager

- **URL:** https://www.npmjs.com/package/vibe-rules
- **Adoption:** 16,154/week
- **GitHub repo:** https://github.com/FutureExcited/vibe-rules
- **Content type:** rule (manages Cursor rules, Windsurf rules, and AI prompts across tools)
- **Layout:** CLI that reads/writes `.cursor/rules/*.mdc`, `.windsurf/rules/*.md`, and analogous rule files for multiple AI coding tools from a single source-of-truth.
- **Distinctive convention:** The multi-tool rule sync pattern — one rule definition, N tool-specific serializations. Format divergence across Cursor (.mdc), Windsurf (.md), Claude (CLAUDE.md) is a recurring pain point this addresses.

#### 10. `@rely-ai/caliber` — AI context infrastructure

- **URL:** https://www.npmjs.com/package/@rely-ai/caliber
- **Adoption:** 549/week
- **GitHub repo:** https://github.com/caliber-ai-org/ai-setup
- **Content type:** rule + skill (syncs CLAUDE.md, Cursor rules, and skill files together)
- **Layout:** CLI that introspects the codebase and keeps CLAUDE.md, `.cursor/rules/`, and `~/.claude/skills/` in sync as the codebase evolves. Keywords: `claude-md`, `cursorrules`, `skills`.
- **Distinctive convention:** Treats rule/skill maintenance as a continuous sync problem rather than a one-time bootstrap, using codebase analysis to regenerate context files.

#### 11. `claude-skill-lord` — Curated Claude Code plugin bundle

- **URL:** https://www.npmjs.com/package/claude-skill-lord
- **Adoption:** 14/week (very low; more of a showcase than deployed tool)
- **GitHub repo:** https://github.com/donganhvuphp/Claude-Skills-Lord
- **Content type:** skill + agent + command + rule (bundled collection)
- **Layout:** Claims 43 agents, 165 skills, 114 commands, 11 language rules in a single npm package. Shows the emerging pattern of monorepo-style skill bundles distributed via npm.
- **Distinctive convention:** Most explicit example of all four ACIF content types (agent, skill, command, rule) co-distributed in one package.

#### 12. `@neat.is/claude-skill` — Vendor-provided skill + MCP wiring

- **URL:** https://www.npmjs.com/package/@neat.is/claude-skill
- **Adoption:** published 2026-05-12 (today); adoption data not yet available
- **GitHub repo:** https://github.com/NEAT-Technologies/Neat
- **Content type:** skill + mcp_config (drops skill into `~/.claude/skills/` and wires `@neat.is/mcp` into Claude's MCP config)
- **Layout:** Single install wires both the skill and the MCP server config. License: BUSL-1.1.
- **Distinctive convention:** Vendor-managed skill+MCP pair — the skill teaches Claude how to use the vendor's MCP server, and the package installs both atomically. Clean model for ACIF mcp_config + skill co-distribution.

---

### PyPI

#### 13. `mcp` — Official Python MCP SDK (Anthropic)

- **URL:** https://pypi.org/project/mcp/
- **Adoption:** 933M total downloads; 67,242,808/week; 258,035,476/month
- **Content type:** mcp_config (foundational SDK; basis for all Python MCP servers)
- **Layout:** Python SDK package `mcp==1.27.1`. Not a content bundle; the library all Python MCP servers depend on.
- **Distinctive convention:** Dominant Python package in the MCP space. MCP SDK weekly downloads exceed the npm SDK (67M vs 36M), indicating Python MCP server publishing is very active.

#### 14. `mcp-server-git` — Official Git MCP server (Anthropic)

- **URL:** https://pypi.org/project/mcp-server-git/
- **Adoption:** 234,648/week; 1,993,239/month
- **GitHub repo:** https://github.com/modelcontextprotocol/servers
- **Content type:** mcp_config (Git repo access via MCP tools)
- **Layout:** `uvx mcp-server-git` pattern — no installation needed, run directly. Version `2026.1.14`. Exposes 12 Git tools (status, diff, commit, branch, log, etc.) via stdio MCP transport.
- **Distinctive convention:** `uvx`-runnable pattern is the Python analog of `npx`. Date-versioning (`2026.1.14`) rather than semver.

#### 15. `mcp-server` — Standalone Python MCP server SDK

- **URL:** https://pypi.org/project/mcp-server/
- **Adoption:** 16,947/week; 92,227/month
- **Content type:** mcp_config (server SDK with math tools example)
- **Layout:** Simple example server exposing math calculation tools and formula resources. Shows the minimal viable Python MCP server structure.

#### 16. `archon-mcp` — Governance framework deployer

- **URL:** https://pypi.org/project/archon-mcp/
- **Adoption:** rate-limited during query; v0.1.5 on PyPI
- **GitHub repo:** https://github.com/ShanKonduru/ArchonMCP
- **Content type:** rule + skill + command (deploys governance artifacts to project)
- **Layout:** Generates `.github/copilot-instructions.md` (rule), `.github/skills/` (skill files: security.md, migration.md, done.md), `.github/prompts/` (commands: gap-analysis, harden, done), and `docs/` (ADRs, stories). Auto-detects tech stack.
- **Distinctive convention:** MCP server that deploys all four ACIF content types to a project in one command. The only PyPI entry found that explicitly structures output into `skills/` and `prompts/` directories matching ACIF categories.

#### 17. `actionlayer-mcp` — Action catalog MCP server

- **URL:** https://pypi.org/project/actionlayer-mcp/
- **Adoption:** v0.1.0 (very recent, 2026-05-11)
- **Content type:** mcp_config (typed action catalog via MCP)
- **Layout:** Thin shim; exposes `actionlayer_invoke_action` tool plus catalog listing and job management helpers. Auth via bearer key; execution proxied to ActionLayer service.
- **Distinctive convention:** Shows the "shim over hosted service" MCP pattern. The package itself has no logic — it's a config + registration layer.

---

### Smithery

Smithery hosts 7,000+ MCP servers as of April 2026 (grew 407% since Sept 2025 launch of official registry). It uses its own manifest format.

#### 18. Sequential Thinking — Top server by install count

- **Smithery entry:** `@smithery-ai/server-sequential-thinking`
- **Adoption:** 5,550+ uses (Smithery install count, April 2026)
- **Content type:** mcp_config
- **Distinctive convention:** Most-installed server on Smithery is a pure-logic reasoning scaffold with no external API. Confirms that tool-only MCP servers (no resource surface) are extremely popular.

#### 19. GitHub MCP Server — Top by stars and installs

- **Adoption:** 28,300+ GitHub stars; listed as most-installed on Smithery per April 2026 data
- **Content type:** mcp_config
- **Smithery manifest fields:** Smithery uses a `smithery.yaml` file (schema documentation not publicly exposed in parsed form); CLI is at https://github.com/smithery-ai/cli. Server entries expose name, description, and install counts via search results.
- **Distinctive convention:** Smithery's install count is a richer signal than npm downloads — it reflects active agent-side wiring, not just CI pipeline pulls.

---

### MCP Registry (registry.modelcontextprotocol.io)

The official registry reached 9,400+ entries by April 2026. Its REST API is at `https://registry.modelcontextprotocol.io/v0/servers`. The registry is paginated via cursor.

**server.json schema** (observed fields across 50 sampled entries):
```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "<reverse-domain>/<server-id>",
  "title": "...",
  "description": "...",
  "version": "semver",
  "repository": { "url": "...", "source": "github" },
  "websiteUrl": "...",
  "icons": { ... },
  "remotes": [{ "type": "streamable-http", "url": "..." }],
  "packages": [{ "registryType": "pypi|npm", "identifier": "...", "version": "...", "transport": { "type": "stdio" } }]
}
```
`_meta` contains `io.modelcontextprotocol.registry/official` with `status`, `publishedAt`, `updatedAt`, `isLatest`.

#### 20. `ac.inference.sh/mcp` — Sample registry entry (remote MCP)

- **Registry name:** `ac.inference.sh/mcp` v1.0.1
- **Content type:** mcp_config (remote streamable-http MCP)
- **Layout:** No GitHub repo; purely remote. Transport: `streamable-http` at `https://api.inference.sh/mcp`. This is the dominant pattern for vendor-hosted servers in the registry — no local install, just a URL.
- **Distinctive convention:** Reverse-domain namespace (`ac.inference.sh`) enforces publisher identity. The registry distinguishes `packages` (install via npm/pypi) vs `remotes` (connect to URL) — an important structural split ACIF should model.

#### 21. `ai.adeu/adeu` — Sample registry entry (PyPI-backed MCP)

- **Registry name:** `ai.adeu/adeu` v1.5.2
- **GitHub repo:** https://github.com/dealfluence/adeu
- **Content type:** mcp_config (automated DOCX redlining, pypi-delivered)
- **Layout:** `packages[0]` has `registryType: "pypi"`, `identifier: "adeu"`, transport `stdio`. This is the PyPI-as-delivery-channel pattern within the official MCP registry.
- **Distinctive convention:** Demonstrates how the official registry cross-references PyPI packages. An ACIF mcp_config record could carry an analogous `packages[]` array.

---

### Glama

Glama indexes 23,378 MCP servers (as of May 2026) and serves 50,000+ businesses. It provides an API at `https://glama.ai/api/mcp/v1/servers/{owner}/{repo}`. Quality scores (licensing grade, maintenance grade, security grade) and weekly downloads are shown per server.

#### 22. `whodb-cli/clidey` — Top by Glama weekly downloads

- **Glama entry:** https://glama.ai/mcp/servers/clidey
- **Adoption:** 4,816 weekly downloads (Glama metric); A-grade licensing, quality, and maintenance
- **Content type:** mcp_config (database management tool)
- **Distinctive convention:** Glama's weekly download count is their primary ranking signal, different from Smithery's install count and npm's download count. Three independent adoption metrics exist across registries for the same servers.

#### 23. `Financial Datasets MCP Server` — Glama sample entry

- **Adoption:** 2,096 weekly downloads (Glama)
- **Content type:** mcp_config (stock market data)
- **Distinctive convention:** Glama automatically scans for security findings (66% of popular servers had CVEs in Jan–Feb 2026) and surfaces security grade alongside download count.

---

### HuggingFace

#### 24. HuggingFace MCP Server (official)

- **URL:** https://huggingface.co/docs/hub/agents-mcp
- **Content type:** mcp_config
- **Layout:** Config snippet generated at `https://huggingface.co/settings/mcp` per-client. Exposes built-in tools (Model Search, Dataset Search, Spaces Semantic Search, Papers Search, Documentation Semantic Search, Job Management, Hub Repo Details). Users can add any Gradio Space tagged `mcp-server` as an additional tool.
- **Distinctive convention:** HuggingFace Gradio Spaces now auto-expose an `agents.md` endpoint, making any Space a first-class MCP tool. This is a content distribution channel orthogonal to npm/PyPI — no package to install, just a URL. Each Space's `agents.md` acts as a lightweight skill/tool description.

#### 25. Hugging Face Skills (Claude plugin)

- **URL:** https://claude.com/plugins/huggingface-skills
- **Content type:** skill (cross-platform SKILL.md skills for HF workflows)
- **Layout:** Skills distributed via Cursor Marketplace (`cursor.com/marketplace/huggingface`) and Codex Plugins Directory, following the open SKILL.md standard. Includes `/hugging-face-model-trainer`, `/hugging-face-datasets`, `/hugging-face-evaluation` command-style skills.
- **Distinctive convention:** Vendor-owned skills published through multiple marketplaces simultaneously. Confirms that Claude plugins page, Cursor Marketplace, and Codex Plugins Directory are emerging as parallel skill distribution channels.

---

### SkillsMP (independent marketplace)

- **URL:** https://skillsmp.com/
- **Scale:** 1,319,403 skills listed (aggregated from GitHub via web scraping)
- **Content type:** skill (SKILL.md format exclusively)
- **Layout / schema:** All skills use SKILL.md open standard. 12 categories: Tools (315K), Business (232K), Development (191K), Testing & Security (138K), Data & AI (123K), DevOps (107K), Documentation (91K), Content & Media (81K), plus Research, Lifestyle, Databases, Blockchain. Structured JSON-LD metadata (Organization, SoftwareApplication, CollectionPage).
- **Distinctive convention:** Largest aggregator of SKILL.md content. Not a publisher — indexes GitHub. Provides SOC occupation classification across 867 categories — an unusual dimension that no other registry attempts.

---

### Crates.io (Rust)

#### 26. `rust-mcp-sdk` — Async MCP SDK for Rust

- **URL:** https://crates.io/crates/rust-mcp-sdk
- **Adoption:** 124,909 total downloads; 51,971 recent (fastest-growing Rust MCP crate)
- **Content type:** mcp_config (Rust SDK for building MCP servers/clients)
- **Layout:** Full async implementation of MCP spec `2025-11-25`. Uses procedural macros for tool definition (`#[mcp_tool]`). Companion to `rust-mcp-schema` for type-safe schema objects.
- **Distinctive convention:** Rust proc-macro approach to defining MCP tools contrasts with Python's decorator pattern and TypeScript's class-based approach. Same semantic model, three different ergonomics.

#### 27. `mcp-server` (Rust) — Server SDK

- **URL:** https://crates.io/crates/mcp-server
- **Adoption:** 57,831 total; 11,456 recent
- **Content type:** mcp_config (alternative Rust MCP server SDK)

#### 28. `rust-mcp-server` — Rust dev environment MCP server

- **URL:** https://crates.io/crates/rust-mcp-server
- **Adoption:** 4,693 total; 655 recent
- **Content type:** mcp_config (Rust toolchain tools: cargo check, build, test, fmt, clippy, add, machete)
- **Distinctive convention:** Domain-specific MCP server targeting Rust developers. Exposes `cargo` as MCP tools — a pattern where build toolchain commands become agent-callable tools.

---

### Non-GitHub Code Hosts (GitLab / Codeberg / Bitbucket)

**GitLab:** No SKILL.md-style repositories discovered natively on gitlab.com. However, GitLab publishes an official MCP server (`@modelcontextprotocol/server-gitlab`, now deprecated in favor of the native GitLab MCP integration). The `agent-skill-creator` project (GitHub) explicitly supports GitLab as a skill registry backend — teams clone a git repo on GitLab as their private skill registry. GitLab CI integration with Claude Code is documented at code.claude.com/docs/en/gitlab-ci-cd.

**Codeberg / Bitbucket:** No signal found for AI agent skills or MCP servers hosted on Codeberg or Bitbucket. The ecosystem is heavily concentrated on GitHub, npm, and PyPI as the primary distribution layer.

---

## Cross-Cutting Observations

### Adoption divergence from stars

The most striking finding is how poorly GitHub stars predict actual installation. `skills` (1M/week npm downloads) has minimal star count for the package itself. `skillflag` (248K/week) exists primarily as a CI convention, invisible in star counts. `@modelcontextprotocol/sdk` (36M/week) is a foundational dependency that engineers don't star. Meanwhile, the curated collections that dominate star-based discovery (claude-skill-lord, etc.) show 14/week actual downloads. Download counts are 10x–100x more reliable as an adoption signal for infrastructure packages.

### Three distinct delivery models for MCP servers

1. **npm/PyPI + stdio** — Install globally or `npx`/`uvx`, spawn as subprocess, connect via stdin/stdout. Dominant for open-source MCP servers.
2. **Remote streamable-http** — No install; just configure a URL. Dominant in the official registry (many entries have only `remotes`, no `packages`). Enables vendor-managed servers with auth.
3. **HuggingFace Gradio Space `agents.md`** — Zero-config; any Space auto-exposes tools. Emerging pattern; no package management at all.

An ACIF mcp_config record needs to support all three: `packages[]` (registry + install), `remotes[]` (URL + transport type), and potentially a `space_url` or equivalent for the HF pattern.

### server.json namespace convention

The official MCP registry uses reverse-domain names (`ai.adeu/adeu`, `ac.inference.sh/mcp`) enforced by publisher domain ownership proof. This is stricter than npm scopes (`@scope/pkg`) and more like Go module paths. ACIF may want to note this as the emerging canonical namespace for mcp_config entries.

### SKILL.md convergence

The SKILL.md open standard (announced December 2025) has achieved broad cross-vendor adoption (Claude Code, Codex CLI, Gemini CLI, Cursor, Windsurf, GitHub Copilot Agent Mode, Kiro, Goose, Amp, and ~20 more). The npm `skills` package and SkillsMP marketplace both use it. This is now the de facto format for ACIF `skill` content type. Key structural invariants: YAML frontmatter with `name` and `description`, markdown body, optional `scripts/` and `reference/` subdirs, lives at `SKILL.md` in a named directory.

### Rule format fragmentation persists

Unlike skills (converged on SKILL.md), rules remain fragmented: `.cursor/rules/*.mdc` (Cursor), `.windsurf/rules/*.md` (Windsurf), `CLAUDE.md` / `.claude/rules/*.md` (Claude), `.github/copilot-instructions.md` (Copilot), `.cursorrules` (legacy). Packages like `vibe-rules` and `@rely-ai/caliber` exist specifically to paper over this fragmentation. ACIF's `rule` content type is the right abstraction here — a single canonical rule that tooling serializes to each tool's format.

### `packages[]` + `remotes[]` split in official registry

The MCP registry schema's distinction between `packages` (installable, registered in npm/PyPI/etc.) and `remotes` (directly-connectable URLs) directly parallels the ACIF carrier model's need to distinguish "content to install" from "endpoint to configure." This split should inform how ACIF's mcp_config sidecar represents connection vs. installation metadata.
