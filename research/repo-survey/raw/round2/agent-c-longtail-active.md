# Round 2 — Long-tail GitHub by Activity & Quality Signals

## Methodology

Searches run (2026-05-12):

- `gh search repos "claude code hooks" --sort=updated`
- `gh search repos --topic=claude-code-hooks --sort=updated`
- `gh search repos --topic=claude-code --sort=updated`
- `gh search code "PreToolUse" --filename=settings.json`
- `gh search repos "PostToolUse" --sort=updated`
- `gh search repos "SessionStart" --sort=updated`
- `gh search repos "UserPromptSubmit" --sort=updated`
- `gh search repos "AGENTS.md" --sort=updated --stars=20..500`
- `gh search repos "CLAUDE.md" --sort=updated --stars=30..400`
- `gh search repos "agent skill" --topic=claude-code --sort=updated`
- `gh search repos --topic=cursor-rules --sort=updated --stars=20..300`
- `gh search repos "hooks skills commands" --sort=updated`
- `gh search repos ".mcp.json" --sort=updated --stars=20..500`
- `gh search repos "hooks.json" --sort=updated`
- `gh search repos "claude code" --sort=updated --created=">2026-01-01" --stars=50..500`
- `gh search repos "smithery" --sort=updated --stars=20..300`

Qualifiers used over star count: pushed date (within 60 days), organization affiliation, active issues/PRs, documentation quality, content-type breadth, hook-specific signal words (PreToolUse, PostToolUse, SessionStart, UserPromptSubmit).

Already-covered repos from round 1 (`repos.csv`) excluded from write-up. New entries only.

---

## Findings by content-type focus

### Hooks (priority gap)

#### Dedicated hook frameworks / libraries

**sushichan044/cc-hooks-ts**
- URL: https://github.com/sushichan044/cc-hooks-ts
- Stars: 38 | Last push: 2026-05-12 | Created: 2025-08-23
- Content types: hook (TypeScript library for defining hooks with type safety)
- Layout: monorepo with `src/`, `examples/`, `hooks/`, vitest tests, pnpm workspace
- Why notable: First hook-specific TypeScript library with full type safety; ships `AGENTS.md` and `CLAUDE.md`; uses vitest; older than most hook repos (pre-dates the hooks wave by months)
- Distinguishing quirk: Treats Claude Code hooks as a typed DSL problem, not a shell-script problem

**gabriel-dehan/claude_hooks**
- URL: https://github.com/gabriel-dehan/claude_hooks
- Stars: 36 | Last push: 2026-05-11 | Created: 2025-08-17
- Content types: hook (Ruby DSL gem)
- Layout: gem structure with `lib/`, `test/`, `Gemfile`, `claude_hooks.gemspec`, `example_dotclaude/`
- Why notable: Language-native DSL (Ruby) for hook authoring — not a collection of shell scripts. Ships as an installable gem. `example_dotclaude/` shows canonical `.claude/` integration.
- Distinguishing quirk: Only Ruby-native hook DSL found in survey

**Edmonds-Commerce-Limited/claude-code-hooks-daemon**
- URL: https://github.com/Edmonds-Commerce-Limited/claude-code-hooks-daemon
- Stars: 2 | Last push: 2026-05-12 | Created: 2026-01-15
- Content types: hook (daemon + hook infrastructure)
- Layout: Python project with `src/`, `hooks/`, `scripts/`, `daemon.sh`, full test suite (`tests/`), `pyproject.toml`, install scripts
- Why notable: Org-published (Edmonds Commerce, UK e-commerce company); addresses lazy startup + auto-shutdown problem — solves fork-per-hook cost in long sessions; `CLAUDE.md` + `CONTRIBUTING.md` + `CHANGELOG.md` all present; shellcheck CI config
- Distinguishing quirk: Unix socket daemon bridges hook subprocess overhead; topic list explicitly includes `claude-code-daemon`

**yurukusa/claude-code-hooks**
- URL: https://github.com/yurukusa/claude-code-hooks
- Stars: 10 | Last push: 2026-04-17 | Created: 2026-02-28
- Content types: hook (collection of 585 examples with 8,730 tests)
- Layout: npm-packaged hook library; topics include `pretooluse`, `posttooluse`, OWASP, `database-protection`
- Why notable: By far the most exhaustive hook example collection found; tests-per-hook ratio (8730 / 585 ≈ 15x) is exceptional; OWASP-tagged suggests security focus
- Distinguishing quirk: Installed via npm, not by copying scripts manually

**AvogadroSG1/guardrails**
- URL: https://github.com/AvogadroSG1/guardrails
- Stars: 0 | Last push: 2026-05-11 | Created: 2026-03-07
- Content types: hook (Go binary bundling multiple hooks: secret scanning, branch protection, lint-on-save, test nudge)
- Layout: Go module; single binary distribution model
- Why notable: First Go binary hook framework found; ships everything as one compiled artifact — no Python/Node runtime required; explicitly bundles 5+ distinct safety behaviors
- Distinguishing quirk: Single binary approach eliminates multi-dependency hook installation

**mann1x/claude-hooks**
- URL: https://github.com/mann1x/claude-hooks
- Stars: 21 | Last push: 2026-05-12 | Created: 2026-04-09
- Content types: hook (memory recall hooks for Qdrant, pgvector, sqlite-vec)
- Layout: flat hook scripts with multiple vector DB backends
- Why notable: Cross-platform (Windows/Linux/macOS) memory hooks with HyDE retrieval; covers 3 different vector DB backends; "OpenWolf integration" suggests multi-agent fabric use
- Distinguishing quirk: HyDE (Hypothetical Document Embeddings) in a hook — unusual retrieval technique for a shell hook

**toomas-tt/claude-code-hooks-multi-agent-observability**
- URL: https://github.com/toomas-tt/claude-code-hooks-multi-agent-observability
- Stars: 6 | Last push: 2026-05-12 | Created: 2025-07-15
- Content types: hook (real-time observability/dashboard via hooks)
- Layout: web dashboard fed by hook event stream
- Why notable: One of the older hook repos in this search (created Jul 2025); multi-agent angle — monitors several agents simultaneously; real-time visualization
- Distinguishing quirk: Positions hooks as telemetry substrate, not enforcement gate

**jdidion/barbican**
- URL: https://github.com/jdidion/barbican
- Stars: 4 | Last push: 2026-05-12 | Created: 2026-04-29
- Content types: hook (Rust port of Narthex safety layer)
- Layout: Rust crate; references "Narthex" predecessor
- Why notable: Rust-native hook safety layer; second non-shell hook implementation in survey; "port" implies mature prior art (Narthex) behind it
- Distinguishing quirk: Rust compilation means near-zero hook latency overhead

**krzemienski/claude-code-discipline-hooks**
- URL: https://github.com/krzemienski/claude-code-discipline-hooks
- Stars: 0 | Last push: 2026-05-01 | Created: 2026-03-06
- Content types: hook (12 drop-in PreToolUse/PostToolUse/Stop hooks)
- Layout: flat hook scripts; marketed as companion to "Hooks as a Control Plane" blog/talk
- Why notable: Explicitly companion to a written work about hooks-as-control-plane; 12 hooks as atomic primitives rather than a single tool
- Distinguishing quirk: "Control plane" framing is the conceptual contribution, hooks are just the artifact

#### Hook-specific single-purpose implementations

**thkt/formatter**
- URL: https://github.com/thkt/formatter
- Stars: 0 | Last push: 2026-05-11 | Created: 2026-02-20
- Content types: hook (single PostToolUse hook for biome auto-format)
- Layout: minimal — one hook script
- Why notable: Clean exemplar of single-purpose PostToolUse hook; biome integration is relevant for JS/TS projects; early created date (Feb 2026)
- Distinguishing quirk: Does one thing perfectly — auto-format after every Write/Edit

**shaozhengmao/claude-java-lint**
- URL: https://github.com/shaozhengmao/claude-java-lint
- Stars: 0 | Last push: 2026-05-05 | Created: 2026-05-05
- Content types: hook (PostToolUse hook for Alibaba Java Coding Guidelines enforcement)
- Layout: single hook script
- Why notable: Domain-specific hook tied to a published standard (阿里巴巴 Java 开发手册, 26 rules); non-English-speaking developer community signal; shows hooks as compliance enforcement
- Distinguishing quirk: Enforces a named external standard (not just personal rules) via hook

**ryo-ebata/cc-audit**
- URL: https://github.com/ryo-ebata/cc-audit
- Stars: 18 | Last push: 2026-05-12 | Created: 2026-01-24
- Content types: hook (tooling — static security scanner for hooks/skills/MCP configs)
- Layout: Rust CLI; topics include `security-audit`, `hooks`, `skills`, `mcp-server`
- Why notable: Scans hook scripts themselves for security issues (data exfiltration, prompt injection, supply chain); meta-level tooling that treats hooks as auditable artifacts; no LLM calls
- Distinguishing quirk: The only security auditor purpose-built for ACIF content types together

#### Hooks as event infrastructure

**agentic-thinking/hookbus-publisher-claude-code**
- URL: https://github.com/agentic-thinking/hookbus-publisher-claude-code
- Stars: 0 | Last push: 2026-05-06 | Created: 2026-04-20
- Content types: hook (subprocess gate publishing hook events to HookBus message bus)
- Layout: org-published (agentic-thinking org); covers UserPromptSubmit, PreToolUse, PostToolUse, Stop
- Why notable: First hook → message bus bridge found; event-driven architecture pattern for hooks; org context implies companion ecosystem
- Distinguishing quirk: Hooks as event publishers to external bus, not just interceptors

#### Hooks adopted by established projects (organic signal)

**BrasilAPI/BrasilAPI** (hooks adopted in existing project)
- URL: https://github.com/BrasilAPI/BrasilAPI
- Stars: 10,597 | Last push: 2026-04-14 | Created: 2020-01-30
- Content types: hook (`.claude/settings.json` with PreToolUse bash hook for pre-merge check)
- Layout: `pre-merge-check.sh` hooked into Bash tool
- Why notable: Major Brazilian government API project (10k+ stars, org-published) adopted a Claude Code PreToolUse hook as part of real CI workflow — organic adoption signal, not a hook demo repo
- Distinguishing quirk: Pre-existing large org project adopting hooks as production CI gate

**dataplat/dbatools** (hooks adopted in existing project)
- URL: https://github.com/dataplat/dbatools
- Stars: 2,769 | Last push: 2026-05-12 | Created: 2015-02-02
- Content types: hook (`.claude/settings.json` with PreToolUse hooks for PowerShell style validation and destructive git prevention)
- Layout: PowerShell module; `.claude/hooks/validate-style.ps1` + `prevent-destructive-git.sh`
- Why notable: Long-established PowerShell SQL Server tooling org adopted hooks for coding standards enforcement; shows hooks are entering non-AI-native projects as governance tools; PowerShell hook is a non-standard language choice
- Distinguishing quirk: Only PowerShell-based hook in survey; `Edit|Write` matcher on a PS1 validator

---

### Multi-content collections (hooks + 2+ other types)

**nguyenthienthanh/aura-frog**
- URL: https://github.com/nguyenthienthanh/aura-frog
- Stars: 17 | Last push: 2026-05-12 | Created: 2025-11-25
- Content types: agent (10), hook (27), rule, command; 5-phase TDD workflow
- Layout: npm package; `.claude-plugin/`, `aura-frog/` with scripts, `__tests__/`, `jest.config.cjs`, `.github/` CI
- Why notable: One of the most comprehensive coherent plugins with real test coverage (Jest); all 9 hook event types in `hooks/` dir; earliest-created multi-content plugin with production CI; semver versioning; contributor guide
- Distinguishing quirk: 27 hooks makes it the densest hook collection in a full plugin format

**fnefh/vanilla-boris**
- URL: https://github.com/fnefh/vanilla-boris
- Stars: 0 | Last push: 2026-05-08 | Created: 2026-05-07
- Content types: skill (13), command (5), agent (3), hook (9 covering all event types), `marketplace.json`, plugin-level settings, `bin/` helpers, monitors
- Layout: `.claude-plugin/`, `agents/`, `commands/`, `hooks/`, `skills/`, `bin/`, `monitors/`, `output-styles/`, `references/`, `tests/`, `install.sh`
- Why notable: All 9 hook event types (SessionStart, SessionEnd, PreToolUse, PostToolUse, Stop, UserPromptSubmit, PreCompact, PostCompact, PermissionRequest); based on documented Boris Cherny workflow from `howborisusesclaudecode.com`; richest layout pattern observed; `marketplace.json` + full `tests/` suite + changelog
- Distinguishing quirk: Only repo found that covers all 9 Claude Code hook event types in one plugin

**tdimino/claude-code-minoan**
- URL: https://github.com/tdimino/claude-code-minoan
- Stars: 28 | Last push: 2026-05-12 | Created: 2026-01-02
- Content types: skill (90), hook (46+), command, agent, MCP
- Layout: flat `~/.claude/` config drop; `hooks/` dir with 57 files; `skills/`, `bin/` CLI tools; `tmux.conf.example`; ARCHITECTURE.md
- Why notable: One of the largest single-author curated configs; 90 skills + 57 hook files is exceptional breadth; ships ARCHITECTURE.md explaining the design; Ghostty terminal integration (niche signal)
- Distinguishing quirk: `sounds/` directory — hooks fire audio notifications via macOS say/afplay

**josephfung/trimkit**
- URL: https://github.com/josephfung/trimkit
- Stars: 2 | Last push: 2026-05-12 | Created: 2026-03-25
- Content types: hook, agent, skill (cross-project portable)
- Layout: flat with `hooks/`, `agents/`, `skills/`; positioned as install-once-benefit-everywhere portable toolkit
- Why notable: Portable-first design philosophy (not project-scoped); guardrails + utilities framing; actively pushed
- Distinguishing quirk: Explicit portability promise — "travel with you across every project"

**BaseInfinity/claude-sdlc-wizard**
- URL: https://github.com/BaseInfinity/claude-sdlc-wizard
- Stars: 24 | Last push: 2026-05-11 | Created: 2026-01-19
- Content types: hook, skill, command (SDLC enforcement — TDD, planning, self-review, CI shepherd)
- Layout: structured with `hooks/`, `skills/`, one-command wizard setup
- Why notable: SDLC-as-code framing; older creation date for multi-content type (Jan 2026); `sdlc` topic tag shows deliberate positioning
- Distinguishing quirk: Wizard setup script as primary install surface

**khou/gardenkit**
- URL: https://github.com/khou/gardenkit
- Stars: 2 | Last push: 2026-05-12 | Created: 2026-05-03
- Content types: hook, skill (second brain / PKM integration)
- Layout: hooks + skills designed for Obsidian/markdown knowledge management
- Why notable: Niche domain (PKM/digital garden) with coherent design; topics include `obsidian`, `pkm`, `second-brain`, `digital-garden`
- Distinguishing quirk: Only hook+skill combo targeting personal knowledge management as first-class use case

**closedloop-ai/claude-plugins**
- URL: https://github.com/closedloop-ai/claude-plugins
- Stars: 90 | Last push: 2026-05-12 | Created: 2026-03-04
- Content types: skill, agent, rule, hook (multi-agent SDLC delivery)
- Layout: `.claude-plugin/`, `plugins/` subdirs with `pyproject.toml`; Python-based; `.claude/` with `AGENTS.md`, `CLAUDE.md`
- Why notable: Org-published (closedloop-ai); "LLM quality judges" and "self-learning" framing is distinctive; `CLAUDE.md` + `AGENTS.md` + `CONTRIBUTING.md` + `CHANGELOG.md`; actively maintained (pushed today)
- Distinguishing quirk: Includes LLM-as-judge quality evaluation hooks — meta-quality checking

**laran/claude-memory-discipline**
- URL: https://github.com/laran/claude-memory-discipline
- Stars: 0 | Last push: 2026-05-11 | Created: 2026-05-11
- Content types: hook (Stop, PostToolUse), command (`/memory:save`, `/memory:recall`), rule
- Layout: minimal plugin with clear separation of hooks/skills/commands; "Part of the laran/claude-methodology family"
- Why notable: Coordinated family of repos approach; Stop hook + PostToolUse banner is a specific pattern for memory discipline; configurable regex with project overrides
- Distinguishing quirk: Memory discipline via hooks is a distinct workflow pattern — hooks used to enforce AI behavior invariants, not file/code quality

---

### Vendor-published

**anthropics/life-sciences**
- URL: https://github.com/anthropics/life-sciences
- Stars: 357 | Last push: 2026-05-08 | Created: 2025-10-17
- Content types: mcp_config, skill (vertical domain: 20+ life sciences MCP servers and skills)
- Layout: one dir per tool/vendor (`pubmed/`, `biorxiv/`, `synapse/`, `10x-genomics/`, `clinical-trials/`, etc.); `.claude-plugin/marketplace.json` listing all
- Why notable: Anthropic-published vertical marketplace for life sciences; partner vendor entries (Wiley, BioRender, 10x Genomics, Sage Bionetworks, Medidata); shows marketplace-as-vertical-platform pattern; long-term hosting commitment stated in README
- Distinguishing quirk: Each subdirectory is a partner-submitted MCP server/skill — federated contribution model under Anthropic org

**anthropics/claude-plugins-community**
- URL: https://github.com/anthropics/claude-plugins-community
- Stars: 81 | Last push: 2026-05-12 | Created: 2026-03-20
- Content types: mcp_config (catalog/mirror; submit via external form)
- Layout: read-only mirror with just `.claude-plugin/marketplace.json` and README; submission via `clau.de/plugin-directory-submission`
- Why notable: Official Anthropic community plugin directory — the canonical discovery surface for Claude Code plugins; read-only repo mirrors a write-once external submission form
- Distinguishing quirk: Content is external-submission-only; repo itself has minimal files but is the official registry endpoint

**vtex/skills**
- URL: https://github.com/vtex/skills
- Stars: 28 | Last push: 2026-05-12 | Created: 2026-03-16
- Content types: skill (40 skills for VTEX platform development)
- Layout: org repo; exports to Cursor, Copilot, Claude, AGENTS.md, OpenCode, Kiro; installed via `gh skill install vtex/skills`
- Why notable: VTEX is a major enterprise e-commerce platform (Latin America / global); 40 domain-specific skills for their platform; multi-tool export including Kiro (AWS AI IDE); `gh skill install` install command convention
- Distinguishing quirk: Uses `gh skill install` as the canonical install surface — first such pattern in survey

**Montimage/skills**
- URL: https://github.com/Montimage/skills
- Stars: 4 | Last push: 2026-05-12 | Created: 2026-02-08
- Content types: skill (multi-agent development skills)
- Layout: org repo with `agent-skills`, `ai-agents` topics; cross-platform (Claude Code, Codex, OpenClaw)
- Why notable: Montimage is a French cybersecurity research company (SME); org publishing curated security-focused skills; actively maintained
- Distinguishing quirk: Cybersecurity company perspective on what agent skills should cover

**Qovery/qovery-skills**
- URL: https://github.com/Qovery/qovery-skills
- Stars: 6 | Last push: 2026-05-12 | Created: 2026-04-19
- Content types: skill (Kubernetes/infrastructure deployment skills)
- Layout: org repo; topics include `kubernetes`, `terraform`, `devops`, `deployment`, `opencode`
- Why notable: Qovery is a cloud deployment platform (Kubernetes PaaS); domain-specific infrastructure skills published by the platform vendor; works with OpenCode/Claude Code/any SKILL.md-compatible tool
- Distinguishing quirk: Skills as customer onboarding — teaches agents how to use Qovery through SKILL.md format

**netresearch/composer-agent-skill-plugin**
- URL: https://github.com/netresearch/composer-agent-skill-plugin
- Stars: 5 | Last push: 2026-05-12 | Created: 2025-11-25
- Content types: skill (PHP Composer plugin for skill distribution)
- Layout: org repo (Netresearch, German IT consultancy); `composer-plugin` + `openskills` + `open-standard` topics
- Why notable: Oldest creation date in hook/skill survey (Nov 2025); Composer plugin model — installs skills as PHP dependencies; org-published by established IT services company; `open-standard` topic signals standardization intent
- Distinguishing quirk: Package manager distribution model for skills (skills-as-Composer-dependencies)

**netresearch/agent-rules-skill**
- URL: https://github.com/netresearch/agent-rules-skill
- Stars: 38 | Last push: 2026-05-12 | Created: 2025-10-18
- Content types: skill (skill for generating AGENTS.md files)
- Layout: org repo; topics include `agents-md`, `open-standard`, `convention`
- Why notable: Even older creation date (Oct 2025); generates AGENTS.md following the convention; org-published; meta-skill (a skill that writes rule files); `open-standard` topic
- Distinguishing quirk: Self-referential: a skill to produce the rules that govern agents

**SalesforceAIResearch/agentforce-adlc**
- URL: https://github.com/SalesforceAIResearch/agentforce-adlc
- Stars: 37 | Last push: 2026-05-11 | Created: 2026-04-10
- Content types: skill, rule (Agent Development Life Cycle for Agentforce using Claude Code skills)
- Layout: org repo (Salesforce AI Research); uses Claude Code skills + Agent Script DSL; `agentforce`, `claude-skill`, `cursor-rules` topics
- Why notable: Salesforce AI Research publishing Claude Code skills for their own Agentforce platform; cross-vendor skills pattern (Salesforce using Anthropic format); research org affiliation
- Distinguishing quirk: Skills that operate another vendor's AI agent platform (Agentforce) — multi-vendor agent composition

**svd-ai-lab/sim-cli**
- URL: https://github.com/svd-ai-lab/sim-cli
- Stars: 63 | Last push: 2026-05-12 | Created: 2026-04-07
- Content types: skill, agent, mcp_config (CAE simulation plugins: COMSOL, Abaqus, Ansys, OpenFOAM)
- Layout: org repo; CLI-first runtime with plugins for specific CAE solvers; `cae`, `fea`, `cfd`, `multiphysics` topics
- Why notable: Highly specialized domain (computational engineering/physics simulation); org-published; 63 stars for a niche; agent skills for operating commercial simulation software is unusual; `agent-skills` topic
- Distinguishing quirk: Skills that operate commercial scientific software (Abaqus, COMSOL) — novel domain far outside web dev

**osodevops/keito-skill**
- URL: https://github.com/osodevops/keito-skill
- Stars: 2 | Last push: 2026-05-12 | Created: 2026-05-11
- Content types: skill (billable time tracking for AI coding sessions)
- Layout: org repo (OSO DevOps); SKILL.md + Claude Code plugin; `keito`, `time-tracking`, `agent-skills` topics; cross-platform (Codex, Claude Code)
- Why notable: SaaS company (Keito) publishing their own tracking skill to drive adoption; time tracking for AI sessions is a commercial use case not in round 1; very recently published (yesterday)
- Distinguishing quirk: Skills as product distribution — the skill is a commercial onboarding mechanism

---

### Tooling (linters, validators, testers for ACIF-adjacent content)

**agent-sh/agnix**
- URL: https://github.com/agent-sh/agnix
- Stars: 237 | Last push: 2026-05-09 | Created: 2026-01-30
- Content types: tooling (LSP + linter for CLAUDE.md, AGENTS.md, SKILL.md, hooks, MCP)
- Layout: org repo; Rust binary + VSCode extension; `linter`, `lsp`, `rust`, `vscode` topics; validates all major ACIF content types
- Why notable: 237 stars — highest in this batch; org-published; first-class ACIF content type awareness baked in (validates hooks specifically); IDE integration via LSP; autofixes
- Distinguishing quirk: Treats hooks, skills, MCP configs, and CLAUDE.md as a unified type system that can be linted

**paultyng/testagent**
- URL: https://github.com/paultyng/testagent
- Stars: 4 | Last push: 2026-05-12 | Created: 2026-05-08
- Content types: tooling (deterministic fake of claude and codex CLIs for testing hooks)
- Layout: CLI tool; `mock`, `testing`, `integration-testing`, `hooks` topics
- Why notable: Testing infrastructure specifically for hooks and orchestrators without API key — enables CI-safe hook testing; addresses a real gap in hook development workflow
- Distinguishing quirk: "Fake" CLI that emits the same events as real Claude Code — hooks think they're running against real sessions

**pdugan20/claudelint**
- URL: https://github.com/pdugan20/claudelint
- Stars: 7 | Last push: 2026-05-12 | Created: 2026-02-08
- Content types: tooling (linter for CLAUDE.md, skills, settings, hooks, MCP, plugins)
- Layout: npm CLI; TypeScript; `claude-code-plugin`, `linter` topics
- Why notable: Cross-artifact linter (validates settings.json hooks syntax, SKILL.md frontmatter, plugin manifests); active development; npm distribution
- Distinguishing quirk: Validates the interaction between content types (e.g., does settings.json hook path match actual file?)

**ryo-ebata/cc-audit** (also listed under hooks)
- Dual-listed: security auditor for hooks + skills + MCP configs together

---

### Other — Skills with distinctive domain / community signals

**oliver-kriska/claude-elixir-phoenix**
- URL: https://github.com/oliver-kriska/claude-elixir-phoenix
- Stars: 302 | Last push: 2026-05-12 | Created: 2026-02-12
- Content types: skill, agent (20 specialist agents), rule (Iron Laws), mcp_config (Tidewave)
- Layout: `.claude-plugin/` with full manifest; `agents/`, `skills/`, enforced rules; parallel research + execute + review agents; `MIGRATION_TO_V3.7.md`
- Why notable: 302 stars — second highest in this batch; deep Elixir/Phoenix domain specialization; "Iron Laws enforcement" as a hook/rule concept; Tidewave (Elixir-native MCP) integration; version migration docs; `clone learnings as reusable knowledge` design
- Distinguishing quirk: Domain-language integration (Tidewave is Elixir-native MCP) shows platform-specific skill design

**fallow-rs/fallow-skills**
- URL: https://github.com/fallow-rs/fallow-skills
- Stars: 46 | Last push: 2026-05-12 | Created: 2026-03-20
- Content types: skill (codebase intelligence: unused code, duplication, circular deps, complexity hotspots)
- Layout: org repo (fallow-rs); `agent-skills`, `dead-code`, `codebase-hygiene`, `unused-exports` topics; 20+ agent tools listed in topics
- Why notable: Skills as frontend to a specialized analysis tool (Fallow); cross-platform (Cursor, Codex, Gemini CLI, Windsurf, Claude Code); addresses a real engineering problem (codebase hygiene)
- Distinguishing quirk: Skills as the distribution layer for a commercial analysis tool's capabilities

**dbwls99706/ros2-engineering-skills**
- URL: https://github.com/dbwls99706/ros2-engineering-skills
- Stars: 66 | Last push: 2026-04-29 | Created: 2026-03-16
- Content types: skill (ROS 2 production engineering: Nav2, MoveIt2, ros2_control, real-time)
- Layout: progressive-disclosure SKILL.md; `ros2`, `robotics`, `agent-skill` topics; multi-platform (Claude Code, Codex, Cursor, Gemini CLI)
- Why notable: Robotics domain (ROS 2) — highly specialized technical skill set; progressive disclosure design pattern for complex domain (full stack from workspace to deployment); 66 stars in a niche
- Distinguishing quirk: Progressive-disclosure SKILL.md structure — reveals detail based on context, not a flat instruction dump

**luna-prompts/skillnote**
- URL: https://github.com/luna-prompts/skillnote
- Stars: 44 | Last push: 2026-05-12 | Created: 2026-02-23
- Content types: tooling (open-source skill registry — self-hosted FastAPI + Next.js)
- Layout: org repo; `skill-registry`, `self-hosted`, `skill-md` topics; Docker; FastAPI backend + Next.js frontend
- Why notable: First open-source self-hosted skill registry found; platform for publishing and discovering SKILL.md files; org-published; actively maintained; multi-tool support (Codex, Cursor, OpenHands, Antigravity)
- Distinguishing quirk: Registry-as-infrastructure — decouples discovery from GitHub; closest analog to a package registry for skills

**unoplat/unoplat-code-confluence**
- URL: https://github.com/unoplat/unoplat-code-confluence
- Stars: 89 | Last push: 2026-05-11 | Created: 2024-04-03
- Content types: rule (generates AGENTS.md from codebase analysis), skill
- Layout: org repo; oldest creation date in this batch (Apr 2024 — pre-dates Claude Code by > 1 year); `agentic-planning`, `agents-md`, `hallucination-mitigation` topics; Python + TypeScript
- Why notable: Predates Claude Code launch; addressed AGENTS.md problem before the term was widespread; `hallucination-mitigation` framing shows academic grounding; 89 stars with long activity history
- Distinguishing quirk: Auto-generates and maintains AGENTS.md from import graph analysis — live context layer, not hand-written rules

**ajhcs/healthcare-agents**
- URL: https://github.com/ajhcs/healthcare-agents
- Stars: 33 | Last push: 2026-05-05 | Created: 2026-03-19
- Content types: skill, agent (51 specialists for US healthcare administration)
- Layout: SKILL.md pack with AGENTS.md; topics: `healthcare-ai`, `healthcare-administration`, `cursor-rules`, `copilot-instructions`; multi-platform export
- Why notable: Regulated domain (US healthcare administration) with 51 specialist agents; explicit compliance framing; multi-platform (Cursor + Copilot + Claude Code); `healthcare-ai-agent` topic
- Distinguishing quirk: Largest single-domain specialist collection in regulated sector

**simota/agent-skills**
- URL: https://github.com/simota/agent-skills
- Stars: 36 | Last push: 2026-05-12 | Created: 2026-01-07
- Content types: skill (100+ covering dev, security, design, FinOps, compliance, testing)
- Layout: multi-topic skill collection; `ai-skill-ecosystem`, `skill-md`, `mcp`, `gemini-cli` topics; cross-platform (Claude Code, Codex CLI, Gemini CLI)
- Why notable: One of the oldest skill collections in this batch (Jan 2026); FinOps and compliance topics not well-represented elsewhere; broad topic coverage
- Distinguishing quirk: FinOps skills (cloud cost optimization) as a skill category — novel in this survey

**yegor256/prompt**
- URL: https://github.com/yegor256/prompt
- Stars: 142 | Last push: 2026-05-09 | Created: 2025-06-24
- Content types: rule (CLAUDE.md-format coding philosophy prompt)
- Layout: single file; targets `~/.claude/CLAUDE.md`; `vibe-coding`, `prompt-engineering` topics
- Why notable: yegor256 is a well-known author (Elegant Objects, Java books); high-quality rule content by credible technical author; created before Claude Code launched widely; 142 stars on a single-file repo
- Distinguishing quirk: Software engineering philosophy as CLAUDE.md — not task instructions but coding aesthetics

---

## Cross-cutting patterns

### What the long tail reveals that star-sorted Round 1 missed

**1. Hook taxonomy emerging**
Six distinct hook usage patterns are visible in the long tail:
- *Enforcement hooks* — block/reject tool calls (PreToolUse for git protection, secret scanning)
- *Quality hooks* — auto-format/lint after writes (PostToolUse for biome, Alibaba rules)
- *Memory hooks* — persist/recall context across sessions (SessionStart, Stop, PostToolUse)
- *Observability hooks* — stream events to dashboards or message buses
- *Compression hooks* — reduce token cost of tool outputs before re-entering context
- *Session continuity hooks* — handoff between sessions after compaction

Round 1 categorized hooks as one bucket. The long tail shows they have distinct subsystems.

**2. Hook infrastructure gap is being filled by non-shell languages**
Round 1 had only shell scripts for hooks. Round 2 finds: TypeScript library (`cc-hooks-ts`), Ruby gem (`claude_hooks`), Go binary (`guardrails`), Rust crate (`barbican`), Python daemon (`claude-code-hooks-daemon`). Each solves a different problem: type safety, language nativity, single-binary distribution, performance, process management. ACIF should represent hooks as executable artifacts, not "shell scripts."

**3. Established orgs adopting hooks organically**
BrasilAPI (10k+ stars, Brazilian gov API) and dataplat/dbatools (2.7k stars, SQL Server tooling) both added `.claude/settings.json` hooks to existing production repos. This is adoption without a prior awareness of the "hooks community" — hooks are spreading as CI/quality tooling into non-AI-native projects. This is a quality signal distinct from star count.

**4. Vendor skills as distribution/onboarding**
Several vendors are using SKILL.md as customer-facing onboarding: Qovery (Kubernetes PaaS skills), VTEX (e-commerce platform skills), Keito (time tracking skill), Salesforce AI Research (Agentforce skills), SVD AI Lab (CAE simulation skills). The skill is not just documentation — it's a product distribution mechanism.

**5. Skill registries and package managers emerging**
`luna-prompts/skillnote` is a self-hosted skill registry. `netresearch/composer-agent-skill-plugin` installs skills as Composer packages. `vtex/skills` uses `gh skill install`. `nicepkg/vsync` syncs configs across tools. These point to a distribution infrastructure layer above individual repos.

**6. Security tooling specifically for ACIF content types**
`ryo-ebata/cc-audit` (Rust static scanner), `agent-sh/agnix` (LSP/linter), `pdugan20/claudelint` (npm linter), `inspicere/autoclaude` (transcript analyzer) all treat hooks/skills/MCP configs as auditable artifacts with specific security properties. This is a new tooling category not present in Round 1.

**7. Conference/blog companion repos**
`krzemienski/claude-code-discipline-hooks` is explicit companion to a "Hooks as a Control Plane" piece. `fnefh/vanilla-boris` implements Boris Cherny's documented workflow. `yegor256/prompt` is from a technical author. These repos exist because of written content, not because of GitHub discovery — they won't appear in star-sorted searches.

**8. Non-English developer communities**
Chinese (`shaozhengmao/claude-java-lint` for Alibaba guidelines), Japanese (`thkt/formatter`), Portuguese (`BrasilAPI`), Korean (`jumoooo/claude-windows-toast-hooks`), German (`netresearch/`, `wuemaikblume/dsgvo-skills`). Round 1's top repos were almost entirely English-language. The long tail is international.
