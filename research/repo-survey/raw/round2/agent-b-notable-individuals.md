# Round 2 — Notable Individuals

## Per-individual findings

---

### Matt Pocock (mattpocock)
- **Notable for:** TypeScript educator (Total TypeScript), prolific AI tooling writer at aihero.dev. One of the highest-profile TypeScript educators on the internet, with a newsletter and course audience in the tens of thousands. The skills repo is explicitly branded as "Skills for Real Engineers — not vibe coding," positioning it as a practitioner counterweight to bulk-generated repos.
- **Repos found:**
  - **mattpocock/skills** — 75,357 stars
    - Content types: skill, command (slash-style via SKILL.md triggers)
    - Layout: `skills/{bucket}/{skill-name}/SKILL.md` with sidecar `.md` reference files per skill; bucket dirs (`engineering/`, `productivity/`, `misc/`, `personal/`, `in-progress/`, `deprecated/`) enforce editorial policy via `CLAUDE.md` rules
    - Manifest: `.claude-plugin/plugin.json` only (no marketplace.json); plugin.json has `name` + `skills[]` path array, no version/author/description fields
    - Distinctive conventions:
      1. **Bucket governance:** `CLAUDE.md` at repo root specifies which buckets are published (`engineering/`, `productivity/`, `misc/`) vs private (`personal/`, `in-progress/`, `deprecated/`). Skills must appear in both `README.md` and `plugin.json` to count as published — explicit double-entry discipline.
      2. **Sidecar multi-file per skill:** Each skill dir can contain multiple `.md` files alongside `SKILL.md` (e.g., `deep-modules.md`, `mocking.md`, `tests.md`, `interface-design.md`). The SKILL.md body cross-links these with relative paths — treats the skill as a mini documentation site.
      3. **`disable-model-invocation: true` frontmatter flag:** The `zoom-out` skill uses this non-standard frontmatter key to signal the skill body should be injected verbatim without model reasoning.
      4. **Philosophy-first content:** Skill bodies include explicit "anti-patterns" sections and "why" before "how" — engineered for practitioners who will read the diff.
      5. **`write-a-skill` meta-skill:** Ships a skill for writing skills, encoding convention in executable form.
      6. Registered on **skills.sh** under badge `mattpocock/skills`.
- **Citations:** Referenced by multiple "best skills" roundups (firecrawl.dev, antigravity.codes). Simon Willison cited the skills ecosystem in Oct 2025 ("Claude Skills are awesome, maybe a bigger deal than MCP"). The newsletter-linked skills.sh badge in README indicates Pocock treats this as a first-class product alongside his TypeScript courses.

---

### Andrej Karpathy (karpathy) — via forrestchang
- **Notable for:** Karpathy coined "vibe coding" (early 2025), then in a Jan 26 2026 X post described three systematic failure modes of LLM coding agents after switching from 80% manual to 80% agent-driven coding. The post went viral and spawned a wave of CLAUDE.md templates.
- **Repos found:**
  - Karpathy has no ACIF-style content repos himself. His repos (nanoGPT, minGPT, llm.c, etc.) are ML implementation repos, not agent content.
  - **forrestchang/andrej-karpathy-skills** — 126,678 stars (as of survey)
    - Author: Forrest Chang (community author), created 2026-01-27, directly citing Karpathy's Jan 26 X post.
    - Content types: rule (CLAUDE.md), rule (CURSOR.md), skill
    - Layout: `CLAUDE.md` at repo root (drop-in copy pattern) + `.claude-plugin/{plugin.json, marketplace.json}` + `skills/karpathy-guidelines/` dir
    - Manifest: Full `plugin.json` with name/description/version/author/license/keywords + `marketplace.json`; also `.cursor/` parallel dir
    - Distinctive conventions:
      1. **Dual delivery:** Ships `CLAUDE.md` for direct drop-in AND a `skills/karpathy-guidelines/SKILL.md` for plugin installation — two modes from one content source.
      2. **`CURSOR.md` parallel:** Ships a separate CURSOR.md adapting the same principles for Cursor, showing explicit multi-tool awareness.
      3. **Four named principles as the content structure:** "Think Before Coding", "Simplicity First", "Surgical Changes", "Goal-Driven Execution" — declarative behavioral rules rather than procedural workflows.
      4. **i18n README:** `README.zh.md` alongside `README.md` — cross-audience positioning.
    - This is the 3rd most-starred repo in the entire survey (behind `f/prompts.chat` at 162k and `x1xhlol/system-prompts` at 137k), making it arguably the single most impactful content file in the agent-rules ecosystem.
  - **Orchestra-Research/AI-Research-SKILLs** — 8,285 stars — Karpathy's nanoGPT is directly referenced as a named skill (`nanogpt` in `01-model-architecture/nanogpt/`). Skill description explicitly reads: "Educational GPT implementation in ~300 lines... By Andrej Karpathy." This is Karpathy-as-reference rather than Karpathy-as-author; his code repos are the curriculum for the skill.
- **Citations:** The Karpathy X post (Jan 26, 2026) is the most-cited origin story for CLAUDE.md behavioral rules. Multiple blog posts (miraflow.ai, antigravity.codes, alphasignalai.substack.com) trace the pattern back to it. Community gists extend it (e.g., `renezander030/karpathy-skills-claude-md-v2`).

---

### Simon Willison (simonw)
- **Notable for:** Creator of Datasette and the `llm` CLI. Prolific LLM commentator (simonwillison.net). Published Oct 2025 post "Claude Skills are awesome, maybe a bigger deal than MCP" — one of the early mainstream endorsements of the skill pattern. Has been shipping code almost entirely via coding agents since late 2025.
- **Repos found:**
  - **simonw/claude-skills** (922 stars) — already covered in Round 1 as archival snapshot of Anthropic's /mnt/skills.
  - **simonw/showboat** — 1,102 stars
    - Content types: tooling (Go CLI) — not ACIF content itself, but architecturally interesting: the `--help` text is the behavioral ruleset for agents using the tool. Issue #12 explicitly discusses how help text serves the same role as a CLAUDE.md for CLI-using agents.
    - Layout: own-repo Go CLI; no SKILL.md or CLAUDE.md in repo
    - Not a direct ACIF source, but Willison's pattern (agent-readable CLI help as skill equivalent) is a distinct alternative to file-based skills.
  - **simonw/research** — 641 stars
    - Has `CLAUDE.md` (contents: `@AGENTS.md` — single-line delegation to AGENTS.md) and `AGENTS.md` at root.
    - Layout: per-research-task dirs. Each dir is a mini project from a coding agent session.
    - Distinctive: uses the `@filename` CLAUDE.md delegation syntax; AGENTS.md drives agent behavior.
    - Not ACIF content per se, but shows Willison's preference for `AGENTS.md` over `CLAUDE.md`.
  - **simonw/llm** — 11,847 stars (CLI tool, not content)
- **Citations:** Oct 2025 blog post widely linked ("Claude Skills are awesome"). "2025: Year in LLMs" post (Dec 2025) influenced community framing of agents. Willison is a high-trust signal — when he endorses a pattern, it spreads fast.

---

### Hamel Husain (hamelsmu)
- **Notable for:** ML practitioner, course instructor ("AI Evals for Engineers & PMs"), independent consultant who has audited 50+ companies' AI products. Blog at hamel.dev. Daily driver: Amp + Cursor + Claude Code. Known for evals-focused AI engineering.
- **Repos found:**
  - **hamelsmu/evals-skills** — 1,266 stars
    - Content types: skill
    - Layout: `skills/{skill-name}/SKILL.md` flat single-level; `.claude-plugin/{plugin.json, marketplace.json}`
    - Manifest: `plugin.json` has rich author object (`{name, url}`), `homepage` (Maven course page), `repository`, `license`, `keywords` array — most complete plugin.json metadata seen in survey
    - Skills: `build-review-interface`, `error-analysis`, `eval-audit`, `evaluate-rag`, `generate-synthetic-data`, `validate-evaluator`, `write-judge-prompt` (7 skills, all evals-domain)
    - Distinctive conventions:
      1. **Domain specialization:** Entire repo is one domain (evals). Contrast with general-purpose skill collections. No catch-all utility skills.
      2. **Course tie-in:** `homepage` in plugin.json points to Maven course page — skill package as course supplement.
      3. **Rich plugin.json:** Only repo surveyed that uses `url` inside `author` object and `homepage` as a distinct field from `repository`.
  - **hamelsmu/claude-review-loop** — 658 stars
    - Content types: hook, command
    - Layout: `.claude-plugin/{plugin.json, marketplace.json}` + `plugins/review-loop/{CLAUDE.md, AGENTS.md, commands/, hooks/, scripts/}`
    - Notable: a **stop hook** (hooks/stop-hook.sh) that intercepts Claude's "I'm done" signal and injects a Codex code review before allowing completion. This is the ACIF `hook` type in practice — a PreTool/PostTool equivalent.
    - Distinctive: the most sophisticated hook pattern in the survey — two-phase review loop where a stop hook pauses Claude and delegates to Codex, then Claude resumes to address feedback. Hook body has error handling, state management via `.claude/review-loop.local.md`, review ID validation (`^[0-9]{8}-[0-9]{6}-[0-9a-f]{6}$`), and structured telemetry log.
- **Citations:** hamel.dev blog post "Evals Skills for Coding Agents" (Mar 2026) directly announces `evals-skills` repo. Listed in multiple skills roundups.

---

### Steve Yegge (steveyegge / gastownhall)
- **Notable for:** Ex-Googler, ex-Amazon, prolific essayist. Published "Welcome to Gas Town" (Jan 2026), "The Future of Coding Agents", and follow-up posts. Created Gas Town orchestration system and Beads issue tracker — both now under `gastownhall` org. His writing shapes how practitioners think about multi-agent orchestration.
- **Repos found:**
  - **gastownhall/gastown** — 15,118 stars
    - Content types: skill, command, hook (via `.beads/` + `plugins/` dirs), agent (implicit via Mayor/Witness/Deacon roles)
    - Layout: `.claude/skills/{skill-name}/SKILL.md` + `.claude/commands/{name}.md` + `plugins/{plugin-name}/{plugin.md, run.sh}` + `.beads/` dir for Beads state
    - Skills in `.claude/skills/`: `crew-commit`, `ghi-list`, `pr-list`, `pr-sheriff` (4 skills, all git/PR workflow automation)
    - Commands in `.claude/commands/`: `backup.md`, `patrol.md`, `reaper.md` (lifecycle management)
    - Plugins in `plugins/`: `compactor-dog`, `dolt-archive`, `dolt-backup`, `dolt-log-rotate`, `dolt-snapshots`, `git-hygiene`, `github-sheriff`, `gitignore-reconcile`, `quality-review`, `rebuild-gt`, `stuck-agent-dog`, `submodule-commit`, `tool-updater` (13 plugins, each a `{plugin.md, run.sh}` pair — agent-callable shell scripts with markdown description)
    - Distinctive conventions:
      1. **Beads in `.beads/`:** Uses git-backed JSONL issue tracking as agent memory — `.beads/beads.jsonl` is stored in the repo, giving agents durable state across sessions. This is a distinct alternative to skills/hooks for agent workflow management.
      2. **Plugin architecture (`plugins/`):** Each plugin is `{plugin.md, run.sh}` — markdown description + executable script. Not SKILL.md format. No YAML frontmatter. The AGENTS.md/CLAUDE.md files in `.claude/` inject context about how to use these.
      3. **Role-based agent personas:** Commands encode agent roles (Mayor, Witness/Deacon patrol, Refinery) with `allowed-tools` fields scoping exactly which `gt *` CLI commands each role can call.
      4. **`allowed-tools` with CLI prefixes:** Commands use `Bash(gt patrol:*)`, `Bash(gt hook:*)` etc. — scoped allow-lists for custom CLIs.
      5. **AGENTS.md + CLAUDE.md dual approach:** Uses both `AGENTS.md` (content) with `CLAUDE.md` (delegating to AGENTS.md via `@AGENTS.md` shorthand).
- **Citations:** "Welcome to Gas Town" (Jan 2026, steve-yegge.medium.com) widely circulated. DoltHub blog "A Day in Gas Town" (Jan 2026). Software Engineering Daily podcast (Feb 2026). The `gastownhall/beads` repo (Beads standalone issue tracker) reportedly crossed 20k stars ~5 months post-launch.

---

### Phil Schmid (philschmid)
- **Notable for:** Head of Developer Relations at Hugging Face. Prolific ML practitioner blog (philschmid.de). Writes about fine-tuning, deployment, and agent tooling. Large Twitter/X following in ML community.
- **Repos found:**
  - **philschmid/gemini-cli-extension** — 148 stars
    - Content types: command (Gemini CLI toml-format commands)
    - Layout: `.gemini/commands/plan/{impl.toml, new.toml}` — Gemini CLI's `~/.gemini/commands/*.toml` convention
    - Distinctive: Uses TOML format (Gemini CLI's native command format) rather than SKILL.md/markdown. Commands have `description` + `prompt` fields with template vars (`{{args}}`). Shows the Gemini CLI command pattern as an alternative to ACIF skill format.
    - Not SKILL.md; different wire format entirely.
  - **philschmid/self-learning-skill** — 63 stars
    - Content types: skill
    - Layout: `skills/self-learning/SKILL.md` + `skills/self-learning/references/`
    - Distinctive: The skill is meta — it teaches the agent to autonomously research and generate new skills using web search. Invoked via `/learn <topic>`. Produces new SKILL.md files. "Self-replicating skill" pattern.
- **Citations:** philschmid is a top-5 HuggingFace account by follower count. His content reaches ML practitioners directly. The `self-learning-skill` pattern (agent that creates skills from web research) is novel and likely to be copied.

---

### Vercel Labs (vercel-labs)
- **Notable for:** Vercel (Guillermo Rauch's company) launched the open `skills` ecosystem, including `skills.sh` as a directory/leaderboard and `npx skills` as the canonical install CLI. Vercel is the company most responsible for formalizing the skills distribution ecosystem beyond GitHub manual installs.
- **Repos found:**
  - **vercel-labs/agent-skills** — 26,457 stars
    - Content types: skill
    - Layout: `skills/{skill-name}/SKILL.md` + `skills/{skill-name}/scripts/*.sh` + `skills/{skill-name}.zip` (pre-packaged zip alongside dir)
    - Skills: `deploy-to-vercel`, `vercel-cli-with-tokens`, `react-best-practices`, `react-view-transitions`, `react-native-skills`, `web-design-guidelines`, `composition-patterns` (7 skills)
    - Manifest: top-level `packages/` dir (separate build tooling); no `.claude-plugin/` observed — distribution via `npx skills add` CLI rather than Claude plugin marketplace
    - Distinctive conventions:
      1. **Zip co-location:** Each skill dir has a corresponding `.zip` file at the same level (`deploy-to-vercel.zip` alongside `deploy-to-vercel/`). Pre-packaged for direct download without CLI.
      2. **CLAUDE.md = AGENTS.md alias pattern:** The repo's `CLAUDE.md` is actually titled `# AGENTS.md` internally — Vercel standardizes on AGENTS.md content in CLAUDE.md filename for cross-tool compatibility.
      3. **`metadata:` block in frontmatter:** `SKILL.md` frontmatter uses `metadata: {author: vercel, version: "3.0.0"}` nested structure — different from flat `author:` top-level used by most repos.
      4. **Action-verb first skill descriptions:** Every skill description starts with a verb: "Deploy applications..." "Apply React best practices..." Consistent imperative style.
      5. **Resources subdir (not references):** Uses `skills/deploy-to-vercel/resources/` (not `references/`) for supplementary files — minor naming variant.
  - **vercel-labs/skills** — 18,167 stars (CLI tool, not content)
    - The `npx skills add owner/repo` CLI for installing skills. Has `skills/find-skills/SKILL.md` — a skill for finding and discovering other skills via skills.sh.
- **Citations:** Vercel changelog "Introducing skills, the open agent skills ecosystem." VoltAgent/awesome-agent-skills credits Vercel skills in its official section listing. The skills.sh leaderboard runs on Vercel infrastructure. Vercel's scale (millions of developer accounts) makes this a high-influence entry point.

---

### Hamel Husain's design-research Skill (hamelsmu/design-research)
- **Notable for:** A separate single-skill repo from Hamel focused on design research via browser automation agents.
- **Repo:** hamelsmu/design-research — 64 stars
  - Not investigated in detail; lower priority given evals-skills already covers his contribution.

---

### HashiCorp (hashicorp)
- **Notable for:** Enterprise infrastructure company (Terraform, Vault, Packer). Their `agent-skills` repo is the clearest example of a domain-expert company publishing practitioner-quality skills tied to specific products. "Reflects years of infrastructure best practices."
- **Repos found:**
  - **hashicorp/agent-skills** — 613 stars
    - Content types: skill, agent (via per-plugin `agents/openai.yaml` sidecars)
    - Layout: `{product}/{pack}/skills/{skill-name}/SKILL.md` — deeply nested by product-then-pack-then-skill; `.claude-plugin/marketplace.json` at root
    - Products covered: `terraform/` (3 packs: `code-generation`, `module-generation`, `provider-development`), `packer/` (1 pack: `builders`)
    - Manifest: `marketplace.json` only at root (no per-skill plugin.json); marketplace has `owner.name`, `metadata.description`, `metadata.version`, `plugins[]` array with per-plugin `name/source/description/version/author/keywords/category/license/strict`
    - Distinctive conventions:
      1. **`strict: false` in marketplace:** Explicit opt-out of strict mode — signals soft advisory rather than enforcement.
      2. **`agents/openai.yaml` sidecars:** Some skills have an `agents/` subdir with per-agent YAML files (e.g., `openai.yaml`) — extending skills with per-agent wiring configs. This is an unreported pattern.
      3. **MPL-2.0 license:** Product-specific licensing (not MIT), per plugin, declared in marketplace.json `license` field.
      4. **Nested packs-under-products:** Deepest nesting observed: `terraform/provider-development/skills/new-terraform-provider/SKILL.md` — 5 levels deep.
      5. **AGENTS.md + CHANGELOG.md + CODEOWNERS:** Treats this as a product repo, not a personal repo — full open-source project hygiene (code owners, changelog, contributing).
- **Citations:** Listed in VoltAgent/awesome-agent-skills under "HashiCorp team" section. Install command featured in multiple "best skills" articles. 303 install-via-CLI references in community roundups.

---

### Orchestra Research (Orchestra-Research)
- **Notable for:** ML research org (no public members listed) publishing a comprehensive AI-research skills library spanning the full research lifecycle. The `nanogpt` skill explicitly credits Karpathy. Notable for being the most complete domain-specific skill collection in the survey.
- **Repos found:**
  - **Orchestra-Research/AI-Research-SKILLs** — 8,285 stars
    - Content types: skill (98+ skills across 23 categories)
    - Layout: `{NN}-{category}/{framework-name}/SKILL.md` + `references/` dir — numeric-prefix category dirs with framework-named skill dirs inside
    - Categories include: model-architecture, tokenization, fine-tuning, mechanistic-interpretability, data-processing, post-training (RLHF/DPO/GRPO), safety-alignment, distributed-training, infrastructure, optimization, evaluation, inference-serving, mlops, agents, rag, prompt-engineering, observability, multimodal, emerging-techniques, ml-paper-writing, research-ideation, agent-native-research-artifact
    - Manifest: `.claude-plugin/marketplace.json` at root; also `package.json` for npm distribution (`npx @orchestra-research/ai-research-skills`)
    - Distinctive conventions:
      1. **Numeric category prefixes:** `01-model-architecture/`, `02-tokenization/`, etc. — encodes intended curriculum order.
      2. **`version:` + `tags:` + `dependencies:` in SKILL.md frontmatter:** Extended frontmatter beyond `name/description` — adds version, author, license, tags (array), dependencies (array). Most metadata-rich frontmatter in the survey.
      3. **GitHub Actions → npm auto-publish:** `publish-npm.yml` auto-publishes to npm with `--provenance` (Sigstore signing) on version bump. Supply-chain security for skills.
      4. **`CITATION.cff`:** Treats this as a citable research artifact (Common Citation Format) — unique in the survey.
      5. **`0-autoresearch-skill` dir:** A meta-skill for autonomous research orchestration using two-loop architecture. Skill zero in a curriculum.
      6. **Multiple agent support dirs:** `.claude/`, plus packaging for Cursor, Codex, Gemini CLI, Qwen Code, OpenCode.
- **Citations:** Listed in VoltAgent/awesome-agent-skills. The Karpathy/nanoGPT connection via named skill attracts ML community traffic.

---

## Cross-cutting observations

**1. The notable-individual signal is star velocity, not total count.**
`forrestchang/andrej-karpathy-skills` reached 126k stars in ~3.5 months (created Jan 27, 2026). That's faster growth than any framework repo in Round 1. One practitioner endorsement from Karpathy's X post produced the most-starred "rules" artifact in the ecosystem.

**2. Plugin.json richness correlates with practitioner credibility.**
Hamel Husain's `evals-skills` has the most complete `plugin.json` (author URL, homepage, repository, keywords, license). Vercel uses `metadata:` nesting. HashiCorp uses per-plugin `strict: false`. Practitioners from engineering cultures add metadata; community mass-gen repos leave it minimal.

**3. Hooks are under-represented in the public ecosystem but sophisticated when present.**
`hamelsmu/claude-review-loop` is the only repo in the entire survey with a production-quality stop hook. The hook enforces a two-model review pattern (Claude implements, Codex reviews). This pattern is not represented in any "awesome" list — it's a practitioner-only contribution.

**4. Skill-as-meta (write-a-skill, self-learning-skill) is a practitioner signature.**
Both Pocock (`write-a-skill`) and Schmid (`self-learning-skill`) ship meta-skills that generate or discover more skills. These are absent from bulk-generated repos and signal considered design rather than content farming.

**5. Multi-tool co-residence is the emerging norm among notable practitioners.**
gastownhall/gastown ships `.claude/`, `.cursor/`, `.opencode/` together. vercel-labs/agent-skills ships CLAUDE.md = AGENTS.md content. forrestchang/andrej-karpathy-skills ships CLAUDE.md, CURSOR.md, and `.cursor/` dir. The implicit standard: "one source, many targets."

**6. Beads/Gas Town introduces a new content type: git-backed agent memory.**
Yegge's `.beads/beads.jsonl` is not covered by any existing ACIF content type. It's closer to an agent state store than a skill/hook/rule/command. Worth tracking as a potential new category.

**7. Vercel is de facto infrastructure owner of the skills ecosystem.**
skills.sh + `npx skills` CLI + vercel-labs/agent-skills = Vercel controls the canonical install path. This gives Vercel/Guillermo Rauch a similar position to npm in the skills ecosystem.

---

## Unresolved

- **Hrishi Olickel:** No GitHub repos found matching ACIF content types. GitHub user `hrishioa` has repos (lumentis, mandark, wishful-search) but none are skill/rule/agent content. He may have content under a different handle or only private repos.
- **swyx (Shawn Wang / sw-yx):** GitHub user `swyx` has only `swyx.github.io` (0 stars). smol-ai org repos (`smol-ai/developer` at 12k stars) are framework code, not ACIF content. No skills/rules/commands published under his handle.
- **Simon Willison:** Has notable blog influence but no ACIF content repos beyond the already-covered archival `simonw/claude-skills`. His `showboat` and `research` repos use AGENTS.md/CLAUDE.md but are tooling/research repos, not publishable content packs.
- **Andrej Karpathy (directly):** No ACIF content. His contribution to the ecosystem is as a cited authority (vibe coding, the Jan 2026 X post), not a direct publisher.
- **Eugene Yan (eugeneyan):** No ACIF content repos found. His repos (applied-ml, open-llms) are curated reading lists. Not active in the skill/rule publishing space.
- **Nathan Lambert (natolambert):** Has `colloquium` (189 stars, Python CLI for academic slides — has CLAUDE.md and AGENTS.md), but it's a tool repo, not a content pack. No skills/rules published.
- **Geoffrey Litt (geoffreylitt):** No ACIF content repos. His work (Wildcard browser extension, malleable software research) is in a different space. Not active in the skill/rule publishing space.
- **Jeremy Howard / fastai:** No ACIF content repos found under `jph00` or the fastai org.
- **Patrick Collison:** No GitHub repos of any kind beyond organizational accounts.
- **Phil Schmid / Gemini CLI:** The gemini-cli-extension uses TOML command format, not SKILL.md — a different wire format not currently in ACIF scope. Worth noting as a parallel standard.
