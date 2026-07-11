# Round 2 — Reddit + HN Community Signals

## Methodology

Searched for community citations via:
- WebSearch queries targeting Reddit discussions across r/ClaudeAI, r/ClaudeCode, r/LocalLLaMA, r/AI_Agents, r/PromptEngineering
- Hacker News Algolia API (`hn.algolia.com/api/v1/search`) with queries: "claude code skills hooks", "cursor rules github", "MCP server config agent", "AGENTS.md subagents claude", "awesome claude code skills", "prompt library agents github", "claude code agents subagents orchestration"
- Fetched HN threads: item/43305919 (PostHog cursorrules, 193 pts / 93 comments), item/46693426, item/46422264, item/46990733
- WebSearch queries for specific repo names surfaced by searches to find Reddit citation context
- `gh repo view --json stargazerCount,description` to verify repos and get current star counts
- Cross-checked against all 109 existing repos.csv entries; excluded one duplicate (rohitg00/awesome-claude-code-toolkit was already in CSV)

**Note on Reddit access:** Direct Reddit fetches (www.reddit.com, old.reddit.com) were blocked. Community signal was inferred via Google/WebSearch surfacing reddit.com URLs with upvote context, HN Algolia API, and community blog sources citing Reddit discussion threads. Sources include claudefa.st, KDnuggets, AnalyticsVidhya, and practitioner blogs that aggregate Reddit findings.

---

## New repos found

### hesreallyhim/awesome-claude-code
- **URL:** https://github.com/hesreallyhim/awesome-claude-code
- **Stars:** 43,498
- **Source:** Consistently cited across r/ClaudeAI and r/ClaudeCode as "the canonical hand-curated list"; claudefa.st notes it as first recommendation for new Claude Code users; KDnuggets article on mastering Claude Code lists it; GitHub Discussions show active community with feature bounty ($100 prize) and makeover feedback threads. Multiple community sources describe it as "the unofficial community bible for Claude Code."
- **Content types:** skill, hook, command, agent, mcp_config (curated index — no content units itself)
- **Layout:** README list / curated directory, no content files — links out to other repos
- **Why cited:** Practitioners use it as the primary discovery/filter layer for the Claude Code ecosystem. Hand-curated with quality bar (broken tools get cut). Active GitHub Discussions community with 1,495+ issues.
- **Notable:** 43k stars; CC0-1.0 license. Acts as the authoritative ecosystem aggregator — comparable to sindresorhus/awesome for Claude Code.

---

### affaan-m/everything-claude-code
- **URL:** https://github.com/affaan-m/everything-claude-code
- **Stars:** 180,298
- **Source:** Listed in KDnuggets "10 GitHub Repositories to Master Claude Code"; surfaced in multiple WebSearch Reddit-adjacent community blogs. Built at Claude Code Hackathon (Cerebral Valley × Anthropic, Feb 2026); won Anthropic × Forum Ventures hackathon Sep 2025. Community description: "battle-tested across multiple production applications."
- **Content types:** skill, hook, command, agent, mcp_config, rule
- **Layout:** hybrid multi-dir — `.claude/agents/`, `.claude/skills/`, `.claude/commands/`, `.claude/hooks/`, MCP configs, rules all present
- **Why cited:** Most complete "batteries-included" harness. Ships 58 specialized subagents, 119 skills, 60 slash commands, 34 rules, 20+ hooks, 14 MCP configs, and AgentShield security scanner. Cited for cost management techniques and production-readiness.
- **Notable:** 180k stars. Covers every ACIF content type simultaneously. Hackathon origin gives it credibility signal.

---

### disler/claude-code-hooks-mastery
- **URL:** https://github.com/disler/claude-code-hooks-mastery
- **Stars:** 3,655
- **Source:** Listed in hesreallyhim/awesome-claude-code as "🔥 claude-code-hooks-mastery (2.1k ⭐)" — hooks mastery; listed on Cult of Claude community site; has associated YouTube video (youtube.com/watch?v=um1o-bnhoTA). Community blog yuv.ai covers it as "Deterministic AI Control & Agent Orchestration." HN submission surfaced via Algolia search with community interest.
- **Content types:** hook, command, agent
- **Layout:** `.claude/hooks/` with Python UV single-file scripts, `.claude/commands/`, `.claude/agents/`; settings.json included
- **Why cited:** The dedicated reference implementation for Claude Code hooks. Provides 13 lifecycle hooks covering PreToolUse (dangerous command blocking), PostToolUse (execution capture), Stop (TTS feedback), SubagentStart/Stop (orchestration). Cited specifically by practitioners learning hook patterns.
- **Notable:** Companion repo `disler/claude-code-hooks-multi-agent-observability` (1,410 stars) covers real-time monitoring. disler appears repeatedly in the Claude Code practitioner community.

---

### disler/claude-code-hooks-multi-agent-observability
- **URL:** https://github.com/disler/claude-code-hooks-multi-agent-observability
- **Stars:** 1,410
- **Source:** Surfaced alongside hooks-mastery in community searches; listed in awesome-claude-code ecosystem.
- **Content types:** hook
- **Layout:** hook scripts for agent event tracking, no skill/command units
- **Why cited:** Solves a real production pain point: observing what multiple concurrent Claude Code agents are doing. Hook-based event tracking with real-time monitoring.
- **Notable:** Companion to hooks-mastery; together they form a practitioner "hooks" reference pair.

---

### shanraisshan/claude-code-best-practice
- **URL:** https://github.com/shanraisshan/claude-code-best-practice
- **Stars:** 52,611
- **Source:** Listed in KDnuggets article; community blogs (sitepoint, analyticsvidhya) cite it; awesomeskills.dev has a dedicated entry. GitHub trending in March 2026. Community description across multiple sources: "from vibe coding to agentic engineering — practice makes Claude perfect." Multiple Reddit-adjacent community sources describe it as "recommended reading before installing anything."
- **Content types:** skill, hook, command, agent (patterns/examples, not a content library)
- **Layout:** CLAUDE.md + `.claude/hooks/` (cross-platform sound notifications) + `.claude/commands/` + `.claude/agents/`; reads as a playbook repo
- **Why cited:** Practitioners cite it for decision frameworks: when to use skill vs command vs agent; whether generalist vs role-specific subagents work better; how to measure skill usage with PreToolUse hooks. Described as the "how to think about Claude Code" counterpart to "how to use Claude Code" repos.
- **Notable:** 52k stars. Cross-platform hook notification system. Trigger field as "the model's activation condition, not a summary" is a widely cited insight.

---

### davepoon/buildwithclaude
- **URL:** https://github.com/davepoon/buildwithclaude
- **Stars:** 2,914
- **Source:** Surfaced in WebSearch results for "claude code subagents hooks commands github repository"; cited in community aggregator articles as "a single hub to find Claude Skills, Agents, Commands, Hooks, Plugins."
- **Content types:** skill, agent, command, hook, mcp_config (hub/index)
- **Layout:** Hub/directory — links to installable plugin marketplace entries, manual clone instructions; no inline content units
- **Why cited:** Practitioners use it as a one-stop discovery hub for installable content across Claude Code, Claude Desktop, Agent SDK, and OpenClaw.
- **Notable:** Explicitly supports installing agents, commands, and hooks simultaneously. Covers multi-platform (OpenClaw listed alongside Claude Code).

---

### VoltAgent/awesome-agent-skills
- **URL:** https://github.com/VoltAgent/awesome-agent-skills
- **Stars:** 21,405
- **Source:** Cited in AnalyticsVidhya "Top 5 GitHub Repositories to get Free Claude Code Skills" article which aggregates Reddit and community discussions; listed on hesreallyhim/awesome-claude-code. HN submission (item/46693426, 4 pts) references it as one of 60k+ GitHub skills sources. Community description: "1000+ agent skills from official dev teams and the community."
- **Content types:** skill (primary), agent
- **Layout:** Flat collection of SKILL.md dirs; multi-platform install via `npx` or plugin marketplace
- **Why cited:** Claims to include official skills from Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma. Quality-over-quantity framing (vs bulk-generated collections) is the community differentiator.
- **Notable:** 21k stars; works across Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, OpenCode, Windsurf, Antigravity.

---

### sickn33/antigravity-awesome-skills
- **URL:** https://github.com/sickn33/antigravity-awesome-skills
- **Stars:** 37,290
- **Source:** Cited in AnalyticsVidhya as "the biggest repository on the list — 1,200+ skills, covers almost every use case." Surfaced in community aggregator articles. agentskills.so has per-skill entries linking back to this repo.
- **Content types:** skill (primary)
- **Layout:** Large flat collection with installer CLI (`npx antigravity-awesome-skills`), Starter Packs (`bundles.md`), plugin distribution described in `plugins.md`
- **Why cited:** Largest skill library by count. MIT-licensed original code + CC BY 4.0 docs. Installer supports `--cursor`, `--claude`, `--gemini`, `--codex`, `--kiro` flags for platform-specific installs. Starter Packs by role (Web Wizard, Hacker Pack) reduce "skill hunting" friction.
- **Notable:** 37k stars. Google Antigravity IDE focus gives it a distinct user base from Claude-first repos. `last30days` skill (research Reddit+X+Web for any topic) is frequently cited.

---

### garrytan/gstack
- **URL:** https://github.com/garrytan/gstack
- **Stars:** 94,483
- **Source:** Pulumi blog post explicitly frames it alongside GSD and Superpowers as "three major community frameworks" discussed across Claude Code practitioner forums. Product Hunt listing with community comments. SitePoint tutorial. DEV Community post titled "How to Combine Superpowers, gstack, and GSD Without the Chaos." Community figure: Garry Tan (YC CEO) — gives it practitioner credibility independent of stars.
- **Content types:** skill, command, agent
- **Layout:** `.claude/skills/gstack/` role-based directories, each with SKILL.md; setup script at repo root; slash commands for role invocation
- **Why cited:** Role-based orchestration (CEO, Eng Manager, Designer, QA Lead, Security Officer, Release Engineer). Cited for "structured roles not a single do-everything agent" pattern. Productivity claims (600k+ LOC in 60 days, part-time) fuel community discussion. Compatible with Claude Code, Codex, OpenCode, Cursor, Factory Droid, Slate, Kiro.
- **Notable:** 94k stars. YC founder provenance drives significant organic citation. Discussed alongside Superpowers and GSD as forming a skills-stack trio.

---

### gsd-build/get-shit-done
- **URL:** https://github.com/gsd-build/get-shit-done
- **Stars:** 61,732
- **Source:** Pulumi blog explicitly compares GSD vs GSTACK vs Superpowers as the three dominant community frameworks (2025-2026). DEV Community post "How to Combine Superpowers, gstack, and GSD." Cited on r/ClaudeAI via community blogs for solving "context rot." claudepluginhub.com has dedicated entry. 59,600+ stars by May 2026 per community sources.
- **Content types:** skill, command, rule (meta-prompting / spec-driven system)
- **Layout:** Markdown prompts in `~/.claude/commands/` (v1); v2 is a TypeScript application that controls agent sessions directly — generates per-task manifests, manages git branches, detects stuck loops
- **Why cited:** Solves context rot — quality degradation as context window fills during long sessions. The `--minimal` flag (94% system prompt reduction: 12,000 → 700 tokens) is cited for local LLM and metered API use. Widest agent support: 14 platforms including Claude Code, Cursor, Windsurf, Codex, Copilot, Gemini CLI, Cline, Augment.
- **Notable:** 61k stars; 138 contributors, 2,100+ commits, 57 releases in ~4 months since Dec 2025 launch. v2 bridges skills/prompts and full agent orchestration.

---

### ykdojo/claude-code-tips
- **URL:** https://github.com/ykdojo/claude-code-tips
- **Stars:** 8,218
- **Source:** Surfaced in WebSearch for "reddit ClaudeCode subagents hooks commands github"; listed in jqueryscript/awesome-claude-code. Community description: "45 tips for getting the most out of Claude Code, from basics to advanced." Includes `dx` plugin. Cited for custom status line script, cutting system prompt in half, Gemini CLI as Claude Code minion, Claude Code running itself in a container.
- **Content types:** skill (dx plugin), hook, command (tips/patterns)
- **Layout:** Tips documentation + dx plugin as installable Claude Code plugin; status line script
- **Why cited:** Practitioners cite it for the status line customization, the "Claude Code runs itself in a container" pattern, and the Gemini CLI delegation technique. 45-tip practical format is more actionable than theoretical guides.
- **Notable:** 8k stars. `dx` plugin ships alongside tips — unusual combination of docs + shipped content unit.

---

### FlorianBruniaux/claude-code-ultimate-guide
- **URL:** https://github.com/FlorianBruniaux/claude-code-ultimate-guide
- **Stars:** 4,306
- **Source:** Surfaced in HN search results for "claude code hooks skills agents github"; referenced in GitHub Trending Weekly 2026-04-29 and 2026-04-22 posts (shareuhack.com). Community description: "a tremendous feat of documentation — covers Claude Code from beginner to power user."
- **Content types:** rule (templates for CLAUDE.md), command, agent, hook (templates and patterns)
- **Layout:** Documentation + production-ready templates; quizzes and cheatsheet; no standalone content unit directories
- **Why cited:** Comprehensive learning resource. Notable for flagging 28 CVEs in the Claude Code ecosystem and 655 malicious skills in the supply chain — security angle is unique. Production-ready templates cited by practitioners.
- **Notable:** 4k stars. Security-first framing is a community differentiator.

---

### VILA-Lab/Dive-into-Claude-Code
- **URL:** https://github.com/VILA-Lab/Dive-into-Claude-Code
- **Stars:** 1,122
- **Source:** Surfaced in HN Algolia search for "claude code hooks skills agents github." Community description: "systematic analysis of Claude Code for designing today's and future AI agent systems."
- **Content types:** rule (analysis / reference patterns)
- **Layout:** Analysis/reference repo — not a content library; documents 27 hook events across 5 categories with 4 execution types; plugin manifest spec covering 10 component types
- **Why cited:** Academic/technical analysis framing makes it a reference for understanding the agent system model rather than grabbing content. Documents the four-mechanism hierarchy: Hooks (zero cost) → Skills (low) → Plugins (medium) → MCP (high). Cited by practitioners designing their own harnesses.
- **Notable:** 1.1k stars. "Systematic analysis" framing is distinct from all other repos in this survey.

---

### Piebald-AI/claude-code-system-prompts
- **URL:** https://github.com/Piebald-AI/claude-code-system-prompts
- **Stars:** 10,148
- **Source:** Listed in KDnuggets "10 GitHub Repositories to Master Claude Code." Community description: "all parts of Claude Code's system prompt, 24 builtin tool descriptions, sub agent prompts, utility prompts." Updated per Claude Code version.
- **Content types:** rule (system prompt reference)
- **Layout:** Versioned markdown files — no SKILL.md or content units; pure reference artifacts
- **Why cited:** Only repo tracking Claude Code system prompts and builtin tool descriptions across versions. Practitioners use it to understand what Claude Code "knows" by default and where custom rules/skills have leverage. Covers Plan/Explore/Task sub-agent prompts, CLAUDE.md format, compact prompt, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation.
- **Notable:** 10k stars. Updated with each Claude Code release — functions as a changelog for the invisible system prompt layer.

---

### shareAI-lab/learn-claude-code
- **URL:** https://github.com/shareAI-lab/learn-claude-code
- **Stars:** 60,017
- **Source:** Listed in KDnuggets "10 GitHub Repositories to Master Claude Code." Community description: "Bash is all you need — a nano claude code-like agent harness, built from 0 to 1."
- **Content types:** agent (harness/framework)
- **Layout:** Bash implementation of a Claude Code-like agent harness — educational reference implementation; not a content library
- **Why cited:** Practitioners cite it for understanding how agentic coding systems work mechanically. "Built from 0 to 1" framing targets developers who want to understand the internals before relying on the real Claude Code. Chinese-language community origin (shareAI-lab).
- **Notable:** 60k stars. Unusual: a reference reimplementation rather than a configuration or content repo. High stars likely reflect Chinese AI community adoption.

---

### nblintao/awesome-claude-code-postleak-insights
- **URL:** https://github.com/nblintao/awesome-claude-code-postleak-insights
- **Stars:** 70
- **Source:** Surfaced in community blog articles discussing the Claude Code npm sourcemap leak (March 31, 2026). Listed in community aggregator articles as the collection of high-signal analyses from the leak.
- **Content types:** rule (analysis of leaked system prompts and patterns)
- **Layout:** Curated links / markdown analysis — no content units
- **Why cited:** The March 2026 Claude Code npm sourcemap leak (security researcher Chaofan Shou, exposing ~1,900 files, 512K+ lines of TypeScript) generated significant community analysis. This repo collects the highest-signal insights. Low stars but high topicality — security-conscious practitioners cite it.
- **Notable:** 70 stars. Historically significant: captures post-leak community analysis of Claude Code internals. Relevant to ACIF because leaked prompts reveal how Anthropic structures content units internally.

---

### patoles/agent-flow
- **URL:** https://github.com/patoles/agent-flow
- **Stars:** 908
- **Source:** HN submission (Show HN: Agent Flow: Visualize Claude Code actions, 5 pts / 3 comments). Listed in jqueryscript/awesome-claude-code as "agent-flow (538 ⭐) — Real-time visualization of Claude Code agent orchestration."
- **Content types:** hook (event stream consumer for visualization)
- **Layout:** Visualization tool consuming Claude Code hook events; not a content library
- **Why cited:** Solves observability for multi-agent orchestration. Practitioners building complex hook pipelines cite it for debugging agent coordination. HN community found the real-time branch visualization genuinely useful.
- **Notable:** 908 stars. Companion tool to hook-heavy workflows; referenced alongside disler's observability repo as a visualization alternative.

---

### quemsah/awesome-claude-plugins
- **URL:** https://github.com/quemsah/awesome-claude-plugins
- **Stars:** 685
- **Source:** Surfaced in WebSearch for community plugin adoption data; cited in community articles as having indexed 16,467 total repositories and tracking Claude Code plugin adoption metrics via n8n workflows.
- **Content types:** mcp_config, skill, agent, hook, command (adoption tracking index)
- **Layout:** Automated metrics collection via n8n; not a content library — tracks adoption stats across the ecosystem
- **Why cited:** Meta-level signal: practitioners use it to understand ecosystem adoption patterns. "16,467 repositories indexed" is cited by community researchers. Automated via n8n workflows — distinct methodology.
- **Notable:** 685 stars. Unique automated-collection methodology vs manual curation. Useful for ACIF survey meta-analysis.

---

### alvinunreal/awesome-claude
- **URL:** https://github.com/alvinunreal/awesome-claude (also webfuse-com/awesome-claude)
- **Stars:** 1,445
- **Source:** Surfaced in WebSearch community results. Community description: "a curated list of awesome things related to Anthropic Claude" — broader scope than Claude Code specifically.
- **Content types:** mcp_config, skill, agent (curated index)
- **Layout:** README curated list — broader than Claude Code, covers Claude API, Claude Desktop, Claude.ai
- **Why cited:** Covers the broader Claude ecosystem (not just Claude Code), including desktop MCP configs and API integrations. Alternative entry point for practitioners coming from Claude Desktop rather than Claude Code.
- **Notable:** 1.4k stars. Broader scope is its differentiator vs Claude Code-specific lists.

---

### jqueryscript/awesome-claude-code
- **URL:** https://github.com/jqueryscript/awesome-claude-code
- **Stars:** 357
- **Source:** Surfaced in WebSearch community results; cited in practitioner blog articles alongside hesreallyhim as a secondary curated list.
- **Content types:** skill, hook, command, agent, mcp_config (curated index)
- **Layout:** README curated list with category breakdowns and star counts noted inline
- **Why cited:** Secondary curated list that explicitly notes star counts per entry, making it useful for quantitative comparison. Includes entries like agent-flow, translate-book, claude_code_agent_farm, claudecode.nvim.
- **Notable:** 357 stars. Notable for including claudecode.nvim (1.7k stars) — Neovim IDE extension — which other lists miss.

---

### glebis/claude-skills
- **URL:** https://github.com/glebis/claude-skills
- **Stars:** 180
- **Source:** Surfaced in WebSearch community results for claude code skills recommendations. Listed on awesomeskills.dev.
- **Content types:** skill
- **Layout:** SKILL.md per skill with standard frontmatter; installable via `npx skills add glebis/claude-skills`; marketplace plugin install (`claude plugin install tdd@glebis-skills`)
- **Why cited:** Cited for TDD skill specifically (`tdd@glebis-skills`). Small collection with installable marketplace plugin distribution — cleaner install story than many repos. Russian-language author.
- **Notable:** 180 stars. Small but installable via multiple paths (npx, plugin marketplace). TDD skill is the primary community draw.

---

### blencorp/claude-code-kit
- **URL:** https://github.com/blencorp/claude-code-kit
- **Stars:** 89
- **Source:** HN submission (Show HN: Claude Code Kit: Reliable Coding Using Claude Skills, Hooks and Command, 1 pt / 1 comment). Listed as HN submission surfaced via Algolia search.
- **Content types:** skill, hook, command (framework-specific kits)
- **Layout:** CLI-based install (`npx` or clone); framework-specific kits (e.g., Tailwind CSS) with per-framework SKILL.md; auto-activation on framework detection
- **Why cited:** "Install complete Claude Code infrastructure in 30 seconds with automatic framework detection and skill auto-activation" is the community pitch. Framework-specific kits (Tailwind, etc.) are distinct from general-purpose skill libraries.
- **Notable:** 89 stars. HN Show HN submission with low engagement but distinctive framework-detection approach.

---

### PostHog/posthog (.cursorrules)
- **URL:** https://github.com/PostHog/posthog (specifically the `.cursorrules` file)
- **Stars:** 34,439
- **Source:** Hacker News — "Posthog/.cursorrules" story, **193 points / 93 comments** (item id 43305919). Highest-engagement HN thread found in this survey for a rules/prompts artifact. Discussion mixed skepticism ("bleakly funny that we must use elaborate instructions") with pragmatic adoption ("YOLO mode," memorable phrases to verify context persistence).
- **Content types:** rule (Cursor rules / `.cursorrules`)
- **Layout:** Single `.cursorrules` dotfile at repo root — not a standalone content repo; the cursorrules file is embedded in PostHog's production codebase
- **Why cited:** The HN thread became a practitioner discussion about cursorrules effectiveness generally. PostHog's rules are cited as a real-world production example (analytics platform, significant engineering team) vs hobby rules. The 193-pt / 93-comment engagement is the highest community-strength signal found in this survey for a rules artifact.
- **Notable:** 34k stars (PostHog is a real product, not an AI tooling repo). Cited not as a template library but as evidence that real teams invest in structured AI coding rules. High-signal HN artifact.

---

### browser-use/browser-use
- **URL:** https://github.com/browser-use/browser-use
- **Stars:** 93,574
- **Source:** HN — "Launch HN: Browser Use (YC W25) – open-source web agents" — **259 points / 100 comments** (surfaced via HN Algolia search). Firecrawl blog on browser agents (2026) cites it as the primary open-source browser agent framework. Reddit-adjacent community: r/LocalLLaMA users cite it for local LLM browser automation.
- **Content types:** agent (browser automation agent framework)
- **Layout:** Python package — not a skills/rules content repo; ships agent definitions for browser interaction tasks
- **Why cited:** Primary community reference for browser-use agent pattern. MCP-compatible; practitioners wire it into Claude Code via MCP config for browser automation skills. 259 HN points is the highest community-strength signal found in this survey for an agent framework.
- **Notable:** 93k stars. YC W25 pedigree. Not a typical ACIF content repo but widely cited as the browser-agent primitive that MCP configs wrap.

---

### jim-schwoebel/awesome_ai_agents
- **URL:** https://github.com/jim-schwoebel/awesome_ai_agents
- **Stars:** 1,744
- **Source:** Surfaced in WebSearch results for r/AI_Agents and r/LocalLLaMA community discussions about agent frameworks. Listed as "1,500+ resources and tools related to AI agents" — one of the most referenced pre-skills-era agent resource lists.
- **Content types:** agent (curated index — pre-SKILL.md era)
- **Layout:** README list — no content units; links to external frameworks and tools
- **Why cited:** Pre-skills-era (pre-Oct 2025) community reference that bridges the gap between LangChain/AutoGen-style agent frameworks and the newer skills ecosystem. Practitioners coming from older agent frameworks use it as a crosswalk.
- **Notable:** 1.7k stars. Predates the skills standard; useful as historical context for the agent-definition category.

---

## Community sentiment patterns

1. **Three-framework consensus**: The Claude Code community has converged on Superpowers (already in CSV), GSD, and gstack as the dominant skills-stacks. Practitioners actively discuss combining all three. This trinity framing appears in Pulumi blog, DEV Community, claudefa.st — suggests these three have escaped the "individual discovery" phase and become community vocabulary.

2. **Observability gap**: Multiple HN submissions and Reddit-adjacent discussions identify observability of multi-agent systems as the primary unsolved problem. disler's two repos and patoles/agent-flow exist specifically to address this. Community phrases: "you can't observe what 20 agents are doing," "key learning was how much difference background hooks made."

3. **Context rot as named problem**: GSD's rise is largely attributed to naming and solving "context rot" — quality degradation as context fills. The term has spread widely in community discussion (Pulumi blog, DEV Community, GitHub issue threads). This suggests token-management is a first-class community concern, not just a performance optimization.

4. **Security anxiety spike (March 2026)**: The Claude Code npm sourcemap leak (March 31, 2026) and supply-chain compromise reports (655 malicious skills flagged in FlorianBruniaux's guide) generated measurable community anxiety about skills security. nblintao/awesome-claude-code-postleak-insights and FlorianBruniaux/claude-code-ultimate-guide both explicitly address this. Practitioners in HN discussions raised "lethal trifecta" (private data + untrusted content + external comms) as a real concern.

5. **Platform fragmentation fatigue**: Multiple repos (davepoon/buildwithclaude, gsd-build/get-shit-done, sickn33/antigravity-awesome-skills) advertise "works across 8/14/16 platforms" as a primary feature. Community HN thread "I got tired of syncing Claude/Gemini/AGENTS.md and .cursorrules" (2 pts / 11 comments) surfaced as direct evidence of cross-platform friction.

6. **Star inflation concern**: quemsah/awesome-claude-plugins indexes 16,467 repositories — the community is aware that bulk-generated skill repos inflate ecosystem counts. hesreallyhim's explicit quality curation (broken tools get cut) is repeatedly cited as why it's trusted over larger aggregators.

7. **Real-world `.cursorrules` as practitioner evidence**: The PostHog HN thread (193 pts) had the highest engagement of any rules-specific discussion found. The community uses real production `.cursorrules` files (PostHog, not toy examples) as evidence that structured AI coding instructions have genuine value — meta-discussion about the format itself, not just another rules collection.

---

## Threads worth noting

- **PostHog/.cursorrules** (HN item/43305919, 193 pts / 93 comments): Highest-engagement rules discussion found. Community argued about whether detailed cursorrules "actually work" or just reflect developer frustration. High signal for the rule content type — practitioners are actively experimenting and debating.

- **Launch HN: Browser Use (YC W25)** (259 pts / 100 comments): Highest overall HN engagement found. Signals that browser agent tooling is a primary community concern — MCP configs wrapping browser-use are a natural content type for ACIF.

- **Show HN: 20+ Claude Code agents coordinating on real work** (mutable-state-inc/lean-collab, 53 pts / 39 comments): Substantive debate about single-agent vs multi-agent approaches. Commenter: "Even Anthropic research consistently demonstrates they use one agent and just tune the harness around it." Counter: "multi-agent becomes necessary when context required exceeds what one agent can hold." High-signal design debate.

- **GSD vs GSTACK vs Superpowers** (Pulumi blog, DEV Community): Not a single thread but a cross-platform community conversation that has crystallized into the "three frameworks" framing. Multiple independent sources use this exact framing — strong signal that these three are the practitioner reference set for 2026.

- **Agnix – lint your AI agent configs** (HN item/46983879): Low points but high technical specificity. "Agent Skills spec requires kebab-case names, but Claude Code doesn't validate it — silently ignores the skill." Documents real format-compliance pain points. Useful for ACIF spec validation requirements.
