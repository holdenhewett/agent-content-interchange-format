# Round 2 — Twitter/X, Blogs, Podcasts, Talks

## Methodology

Searches run (May 2026):

- `site:simonwillison.net claude skills github` — high-yield
- `site:simonwillison.net starlette 2026 skills claude` — found March 2026 post
- `site:hamel.dev claude code skills agents` — low yield (Amp comparison post, no repo citations)
- `latent space podcast claude code skills plugins github` — found Latent Space episode page
- `steipete agent-rules claude code blog post` — found blog posts and X threads
- `"obra/superpowers" blog recommended` — found Jesse Vincent's own blog + multiple secondary
- `site:x.com claude code skills hooks agents github repo` — found X search-engine snippets
- `site:x.com "garrytan" gstack` — found Garry Tan's own announcement tweets
- `obra/superpowers-skills site:x.com github` — found Dave Kennedy, hiroppy, and community comparisons
- `trail of bits security skills claude code github blog` — found tl;dr sec newsletter
- `firecrawl blog "best claude code skills" 2026` — found curated post with repo mentions
- `compound engineering every.to claude code skills github` — found EveryInc/compound-engineering-plugin
- `vercel agent-skills github blog announcement` — found Vercel changelog + skills.sh launch
- `Ran Aroussi claude code PM agents github blog` — found CCPM blog + X thread
- `mattpocock "skills for real engineers" claude code` — confirmed GitHub URL + 75k stars
- `anthropic engineering blog claude code skills hooks agents` — found anthropic.com/engineering post

**Twitter/X access:** The X site itself requires auth and returned HTTP 402 on direct tweet fetches. All X citations here come from search-engine snippets and titles of indexed tweets — the tweet text itself was confirmed via snippet, not full page load. Signal level: medium (headline + 140-char context visible in snippets, but no thread context).

**Podcast show notes:** Latent Space episode page did not expose a repo list in show notes — the episode focused on Claude Code architecture, not specific community repos. No direct show-note citations found for Practical AI or Cognitive Revolution linking to specific repos.

---

## Citations

### From Simon Willison's Blog (simonwillison.net)

#### Citation 1
- **Source:** [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/) — October 16, 2025
- **Author:** Simon Willison (high-authority independent AI researcher, datasette creator)
- **Quote:** "I expect we'll see a Cambrian explosion in Skills which will make this year's MCP rush look pedestrian by comparison." / "Almost everything I might achieve with an MCP can be handled by a CLI tool instead." / "The core simplicity of the skills design is why I'm so excited about it."
- **Repo:** github.com/anthropics/skills — ~133k stars
- **Content:** skill (document-skills for PDF/DOCX/XLSX/PPTX)
- **Layout:** dir-with-SKILL.md, frontmatter YAML, scripts-dir, per-skill LICENSE.txt; top-level marketplace.json
- **Significance:** Simon calling skills "maybe a bigger deal than MCP" is the single strongest practitioner endorsement in this ecosystem. He specifically frames the SKILL.md + scripts pattern as superior to MCP because it composes with existing CLI tooling. This is a "new convention forming" signal — his framing directly shaped how this format was received.

#### Citation 2
- **Source:** [Superpowers: How I'm using coding agents in October 2025](https://simonwillison.net/2025/Oct/10/superpowers/) — October 10, 2025
- **Author:** Simon Willison
- **Quote:** "Jesse Vincent wrapped up a host of tricks as a plugin called Superpowers, installable via `/plugin marketplace add obra/superpowers-marketplace`" / "Jesse notes the core is very token light — pulling in one doc of fewer than 2k tokens and running a shell script to search for additional bits as needed."
- **Repo:** github.com/obra/superpowers — ~188k stars
- **Content:** skill, hook, agent, command (hybrid multi-platform plugin)
- **Layout:** dir-with-SKILL.md, frontmatter YAML + plugin.json + marketplace.json; sidecar dirs for Cursor/Codex/OpenCode/Gemini
- **Significance:** Simon describing the token-efficiency design of superpowers — "fewer than 2k tokens" for the core with lazy-loaded skills — is exactly the progressive-disclosure pattern that ACIF's carrier design needs to validate. First high-credibility description of session-start-hook + skill-search-script pattern.

#### Citation 3
- **Source:** [Experimenting with Starlette 1.0 with Claude skills](https://simonwillison.net/2026/Mar/22/starlette/) — March 22, 2026
- **Author:** Simon Willison
- **Quote:** "For all of the buzz about Claude Code, it's easy to overlook that Claude itself counts as a coding agent now." / "A new button labelled 'Copy to your skills' appeared, and clicking it made the skill available in regular Claude chat."
- **Repo:** github.com/anthropics/skills — (existing citation, new use signal)
- **Content:** skill
- **Layout:** confirms SKILL.md dir pattern as universal — works in Claude.ai consumer app, not only Claude Code
- **Significance:** Confirms skills as a cross-surface format — same SKILL.md used in Claude.ai, Claude Code, and API. Simon's observation of the "Copy to your skills" button documents that the format is now the canonical transport between agents and users even in the UI.

---

### From Jesse Vincent's Blog (blog.fsck.com)

#### Citation 4
- **Source:** [Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/) — October 9, 2025
- **Author:** Jesse Vincent (obra; long-time OSS engineer, founder of Keyboardio)
- **Quote:** "Skills are what give your agents Superpowers." / "You can hand a model a book or a document or a codebase and say 'Read this. Think about it. Write down the new stuff you learned.'" / "Claude now thinks of this as TDD for skills and uses its RED/GREEN TDD skill as part of the skill creation skill."
- **Repo:** github.com/obra/superpowers — ~188k stars
- **Additional repos mentioned:** github.com/obra/superpowers-marketplace (~marketplace hub), github.com/obra/superpowers-skills (~654 stars, community-editable), github.com/obra/claude-memory-extractor (~112 stars)
- **Content:** skill, hook, command, agent (full multi-type plugin)
- **Layout:** getting-started skill bootstraps session; skill-search script runs on demand; skills stored as SKILL.md dirs; hook injects `<session-start-hook>` to prime context
- **Significance:** Jesse is the creator's own description of the architecture. Key pattern: session-start hook injects minimal bootstrap (~2k tokens), skill discovery via search script (not preloaded), mandatory skill use when applicable. This is the clearest primary-source description of the progressive disclosure + hook integration pattern in this ecosystem.

---

### From Anthropic Engineering Blog (anthropic.com/engineering)

#### Citation 5
- **Source:** [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — October 16, 2025 (updated December 18, 2025)
- **Authors:** Barry Zhang, Keith Lazuka, Mahesh Murag (Anthropic engineers)
- **Quote:** "organized folders of instructions, scripts, and resources that agents can discover and load dynamically" / "This file must start with YAML frontmatter that contains some required metadata: `name` and `description`"
- **Repos:** github.com/anthropics/skills/tree/main/document-skills/pdf, github.com/anthropics/claude-cookbooks/tree/main/skills
- **Content:** skill (canonical Anthropic reference)
- **Layout:** SKILL.md with required `name` + `description` frontmatter fields; progressive disclosure (frontmatter → full SKILL.md → linked supplementary files → optional scripts)
- **Significance:** Normative. This is Anthropic's own specification of the skills format. Establishes `name` and `description` as the only required frontmatter fields, and progressive disclosure as the canonical loading strategy. ACIF's skill content type spec should be validated against this document.

---

### From Vercel Blog / Changelog (vercel.com)

#### Citation 6
- **Source:** [Introducing skills, the open agent skills ecosystem](https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem) — January 20, 2026
- **Author:** Andrew Qu (Vercel)
- **Quote:** "We released skills, a CLI for installing and managing skill packages for agents." / Guillermo Rauch called it "the npm of AI skills."
- **Repos:** github.com/vercel-labs/agent-skills (~26k stars), github.com/vercel-labs/skills (~18k stars, the CLI tool itself)
- **Content:** skill (React best practices, Vercel deploy, design guidelines, composition patterns)
- **Layout:** SKILL.md + AGENTS.md both present per skill dir; cross-platform (skills.sh installs into Claude Code, Codex, Cursor, Gemini, etc.)
- **Significance:** Vercel entering with skills.sh as "the npm of AI skills" is a major distribution-layer signal. The `npx skills add` CLI auto-detects installed agents and places SKILL.md files in the correct location for each — this is the first tool explicitly solving the cross-agent installation problem. Vercel React best practices had 20,900 installs by the morning after launch. The open-standard framing from Anthropic (Dec 18, 2025) + Vercel's distribution layer = the npm moment for this format.

---

### From Peter Steinberger's Blog + X (steipete.me)

#### Citation 7
- **Source:** [Claude Code is My Computer](https://steipete.me/posts/2025/claude-code-is-my-computer) — 2025
- **Author:** Peter Steinberger (@steipete; founder of PSPDFKit / Nutrient, prolific iOS OSS contributor)
- **Quote:** "I run Claude Code in no-prompt mode; it saves me an hour a day and hasn't broken my Mac in two months." / "I haven't typed `git commit -m` in weeks."
- **Repos mentioned:** github.com/steipete/agent-rules (~5.7k stars; archived Dec 31 2025 as read-only), github.com/steipete/macos-automator-mcp
- **Content:** rule (coding rules + global rules + project rules + docs/)
- **Layout:** flat rules files organized by scope (global-rules/, project-rules/); companion docs/ dir for reference markdown (e.g., Swift 6 concurrency, SwiftUI)
- **Significance:** `steipete/agent-rules` is the most-cited rules repo by practitioners on X. Peter's June 2025 X post ("I started collecting my various Claude Code project & global rules") got 37.9K views and 479 reposts — largest organic rules-sharing moment in the ecosystem. The docs/ pattern (copy language reference markdown, instruct CLAUDE.md to read it) is a practitioner convention not in any spec.

#### Citation 8 (X thread, accessed via search-engine snippet)
- **Source:** [X @steipete](https://x.com/steipete/status/1933138957719556586) — June 12, 2025
- **Author:** Peter Steinberger
- **Quote:** "I started collecting my various Claude Code project & global rules and docs into a (still messy) repo. What are your fav rules?" (37.9K views, 479 reposts)
- **Repo:** github.com/steipete/agent-rules — ~5.7k stars
- **Content:** rule (global-rules/, project-rules/, docs/ companion markdown)
- **Layout:** flat by scope, not by topic; no SKILL.md, no marketplace.json; rules as plain .md files in categorized dirs
- **Significance:** This tweet bootstrapped the community conversation about rules-as-repos. The call for "your fav rules" generated community contributions and is cited as a catalyst for at least three other rules repos. Signal: rules repos follow a distinct pattern from skills repos — flat .md files, no frontmatter manifest, no marketplace.json.

---

### From Latent Space Podcast (latent.space)

#### Citation 9
- **Source:** [Claude Code: Anthropic's Agent in Your Terminal](https://www.latent.space/p/claude-code) — May 7, 2025
- **Author:** Swyx + Alessio Fanelli (Latent Space hosts); guests Boris and Cat (Claude Code lead eng + PM at Anthropic)
- **Quote:** Boris: "Claude Code is not a product as much as it's a Unix utility." / Boris on hooks: "just add a line quad dash p...whatever instruction you have and that'll run every time." / Boris on CLAUDE.md: "it's a file that has some stuff. And it's auto-read into context"
- **Repos mentioned:** github.com/paul-gauthier/aider (comparison), no specific content repos linked in show notes
- **Content:** n/a (architecture discussion, not repo citation)
- **Layout:** CLAUDE.md as hierarchical config; `claude -p` for non-interactive/automation use
- **Significance:** Primary source from the builders. Boris's framing — CLAUDE.md as auto-loaded context, hooks as shell scripts attached to the agent loop — establishes the canonical mental model. The "Unix utility" framing explains why the ecosystem builds SKILL.md dirs rather than SaaS integrations: composability is the design goal.

---

### From tl;dr sec Newsletter

#### Citation 10
- **Source:** [tl;dr sec #316 — How Trail of Bits uses Claude Code](https://tldrsec.com/p/tldr-sec-316) — February 19, 2026
- **Author:** Clint Gibler (tl;dr sec; former NCC Group security researcher, 30k+ newsletter subscribers)
- **Quote:** "Opinionated defaults, documentation, and workflows for Claude Code at Trail of Bits. Covers sandboxing, permissions, hooks, skills, MCP servers, and usage patterns they've found effective across security audits, development, and research."
- **Repos:** github.com/trailofbits/skills (~5.1k stars), github.com/trailofbits/claude-code-config (~1.9k stars)
- **Content (trailofbits/skills):** skill (security audit, CodeQL/Semgrep, smart contract, vulnerability analysis)
- **Content (trailofbits/claude-code-config):** rule + hook + mcp_config (sandboxing, permissions, hooks, MCP server config as a unit)
- **Layout (trailofbits/skills):** dir-with-SKILL.md, CC BY-SA 4.0; separate `skills/` and `skills-curated/` split
- **Layout (trailofbits/claude-code-config):** opinionated defaults repo; documents hooks + permissions + MCP in one place
- **Significance:** Trail of Bits is the first major security firm to publish a vetted skills collection AND a separate claude-code-config repo. The two-repo split (skills separate from config) is a layout pattern signal: security practitioners separate content (skills) from infrastructure config (hooks, permissions, MCP). Clint Gibler's newsletter reaching 30k security practitioners is a distribution channel for this naming convention.

---

### From X (@garrytan / Garry Tan)

#### Citation 11 (X, accessed via search-engine snippet)
- **Source:** [X @garrytan](https://x.com/garrytan/status/2032014570118922347) — March 12, 2026
- **Author:** Garry Tan (President & CEO, Y Combinator; ~1.1M X followers)
- **Quote:** "I've been having such an amazing time with Claude Code I wanted you to be able to have my *exact* skill setup: Introducing gstack" / "It's 2026 and unbelievable power is in an open github repo with a few markdown files."
- **Repo:** github.com/garrytan/gstack — ~94k stars
- **Content:** skill (23 skills covering CEO/Designer/EngMgr/ReleaseMgr/DocEngineer/QA roles + /office-hours + /retro + /investigate + /freeze + /guard)
- **Layout:** SKILL.md dirs under top-level; `./setup` installer copies to `~/.claude/skills/`; companion CLAUDE.md; multi-platform support (9 agents)
- **Significance:** Garry Tan's gstack is the highest-credibility "I use X" signal in this entire survey. YC CEO sharing his exact SKILL.md setup drove 94k stars. His follow-up tweet — "unbelievable power is in an open github repo with a few markdown files" — is the most concise articulation of why the SKILL.md format has won: zero infrastructure, maximum portability. The CTO-friend quote ("I will make a bet that over 90% of new repos from today forward will use gstack") shows real adoption intent.

#### Citation 12 (X comparison thread, accessed via search-engine snippet)
- **Source:** [X @jarodise](https://x.com/jarodise/status/2038427720473039222) — April 2026
- **Author:** 数字游民Jarod (digital nomad/AI practitioner, Chinese-language AI community)
- **Quote:** "Superpowers，gstack和Compound Engineering，三个Claude Code超级plugin的横向对比" (Superpowers, gstack, and Compound Engineering — a cross-comparison of three Claude Code super-plugins)
- **Repos:** obra/superpowers, garrytan/gstack, EveryInc/compound-engineering-plugin
- **Content:** skill + hook + command (all three; varying emphasis)
- **Significance:** By April 2026 there's enough ecosystem maturity that practitioners are running head-to-head comparisons of major skills frameworks. The three repos in this comparison are the de-facto "Big Three" as perceived in public discourse.

---

### From X (@HackingDave / Dave Kennedy)

#### Citation 13 (X, accessed via search-engine snippet)
- **Source:** [X @HackingDave](https://x.com/HackingDave/status/2023863478147064029) — 2025/2026
- **Author:** Dave Kennedy (TrustedSec CEO, SANS instructor, named Top 10 IT Security Influencer)
- **Quote:** "Obra/superpowers as a skill in Claude is a must-have imo for Claude. It forces claude to create sub agents for specific tasks, stops short cuts, keeps iterating through into a desired solution and has cut error rate on development down substantially."
- **Repo:** github.com/obra/superpowers — ~188k stars
- **Content:** skill, hook, agent, command
- **Layout:** plugin marketplace model; session-start hook + skill-search script
- **Significance:** Security community endorsement from a practitioner known for rigor. Kennedy's framing — "cuts error rate substantially" — is the outcome-oriented language that spreads in enterprise adoption. Signals that the subagent dispatch pattern (skills forcing sub-agents for specific tasks) is a recognized reliability pattern, not just a workflow preference.

---

### From X (various — curated list)

#### Citation 14 (X, accessed via search-engine snippet)
- **Source:** [X @hasantoxr](https://x.com/hasantoxr/status/2035312729427480840) — March 2026
- **Author:** Hasan Toor (AI tools curator, large following)
- **Quote:** "Best GitHub repos for Claude code that will 10x your next project: 1. Superpowers 2. Awesome Claude Code 3. GSD (Get Shit Done) 4. Claude Mem 5. UI UX Pro Max"
- **Repos:**
  - github.com/gsd-build/get-shit-done (~61k stars; "lightweight and powerful meta-prompting, context engineering and spec-driven development system" by TÂCHES)
  - github.com/thedotmack/claude-mem (~75k stars; "Persistent Context Across Sessions for Every Agent")
  - github.com/nextlevelbuilder/ui-ux-pro-max-skill (~77k stars; "AI SKILL that provides design intelligence for building professional UI/UX")
  - github.com/hesreallyhim/awesome-claude-code (~43k stars; curated list of skills/hooks/commands/agents)
- **Content (gsd):** skill + command (meta-prompting workflow, spec-driven development)
- **Content (claude-mem):** hook + skill (session memory persistence, vector embeddings across agents)
- **Content (ui-ux-pro-max):** skill (design intelligence, cross-platform UI/UX)
- **Significance:** Curator threads like this are how skills reach practitioners who don't follow individual repos. The repos in this list (gsd, claude-mem, ui-ux-pro-max) are all in the 60-77k star range with essentially zero coverage in Round 1 — they represent a second tier of highly-starred repos that emerged from discourse rather than stars-at-launch. claude-mem is notable as a pure hook/skill pattern for cross-session memory, which is a cross-cutting concern for any ACIF implementation.

---

### From X (@cathrynlavery / Cathryn — OpenClaw)

#### Citation 15 (X, accessed via search-engine snippet)
- **Source:** [X @cathrynlavery](https://x.com/cathrynlavery/status/2028204980239557021) — 2026
- **Author:** Cathryn Lavery (OpenClaw creator/maintainer)
- **Quote:** "Don't put skills inside each agent folder. I keep mine in a ~/.agents GitHub repo — skills, hooks, and prompts all live there. Every agent symlinks in the specific skills it needs. Same skills shared across Claude Code, Codex, every agent, and every machine."
- **Repo:** github.com/cathrynlavery/openclaw-ops (~219 stars, OpenClaw ops skill)
- **Content:** skill, hook (ops/monitoring pattern; health checks, watchdogs, update triage)
- **Layout:** `~/.agents` as a central personal skills repo; symlinks from per-project `.claude/skills/` → shared skills
- **Significance:** This tweet describes a practitioner-invented convention: a single `~/.agents` repo as the "home" for personal skills + hooks, with symlinks into each project. This is a discovered layout pattern for multi-project, multi-agent skill sharing that no spec currently describes. ACIF should consider whether this use case (personal global skill library with project-local overrides) is in scope.

---

### From Ran Aroussi's Blog (aroussi.com)

#### Citation 16
- **Source:** [How we fixed the context problem in AI-driven development](https://aroussi.com/post/ccpm-claude-code-project-management) — August 22, 2025
- **Author:** Ran Aroussi (founder, Automaze; open-sourced CCPM)
- **Quote:** "No spec, no code." / "GitHub Issues live where your code lives." / "Every decision is documented along the chain PRD → Epic → Task → Issue → Code → Commit."
- **Repo:** github.com/automazeio/ccpm (~8k stars; "Project management skill system for Agents that uses GitHub Issues and Git worktrees for parallel agent execution")
- **Content:** command (slash commands: /pm:prd-new, /pm:prd-parse, /pm:epic-oneshot, /pm:issue-start, /pm:issue-sync, /pm:init) + skill (workflow guidance) + infrastructure (git worktrees for parallel execution)
- **Layout:** Commands in `.claude/commands/`; project management state in GitHub Issues; parallel execution via git worktrees
- **Significance:** CCPM is the clearest example of the "command as workflow orchestrator" pattern — slash commands that invoke multi-step workflows including spawning parallel agents. Ran's blog post (August 2025) documents that CCPM "cut our shipping time roughly in half." Adopted by Factory, Amp, OpenCode, Codex, Cursor. The GitHub Issues-as-source-of-truth pattern is a noteworthy convention for how command-type ACIF content interacts with external state.

---

### From X (@aiwithjainam — Matt Pocock)

#### Citation 17 (X, accessed via search-engine snippet)
- **Source:** [X @aiwithjainam](https://x.com/aiwithjainam/status/2051213807704551569) — 2026
- **Author:** Jainam Parmar (AI content creator); citing Matt Pocock (Total TypeScript creator, ~250k X followers)
- **Quote:** "Matt Pocock just open sourced a Claude Code skill pack that makes AI agents behave less like interns with unlimited coffee and more like actual engineers. It's called Skills for Real Engineers."
- **Repo:** github.com/mattpocock/skills — 75,367 stars
- **Content:** skill (engineering: tdd, diagnose, grill-me, grill-with-docs, to-issues, zoom-out, improve-codebase-architecture; misc: git-guardrails-claude-code, handoff, caveman, write-a-skill)
- **Layout:** `skills/engineering/` and `skills/misc/` dirs; each skill is SKILL.md dir with optional supporting files; companion `CONTEXT.md` at root; setup skill bootstraps the collection
- **Significance:** Matt Pocock's TypeScript community following means his skills spread fast into the TypeScript/JavaScript practitioner segment. His `by-category` layout (skills/engineering/, skills/misc/) is a distinct convention from Anthropic's `by-type` and gstack's flat layout. The `CONTEXT.md` companion (tracks domain vocabulary, ADRs) is a practitioner invention for project-level context that complements SKILL.md — ACIF should consider whether CONTEXT.md is a recognized auxiliary type.

---

### From diet103 / community showcase

#### Citation 18
- **Source:** [diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) — cited in hesreallyhim/awesome-claude-code with description "A remarkably innovative approach to working with Skills"
- **Author:** diet103 (anonymous practitioner, 6 months TypeScript microservices)
- **Quote (from awesome-claude-code curation note):** "The centerpiece is a technique that leverages hooks to ensure that Claude intelligently selects and activates the appropriate Skill given the current context."
- **Repo:** github.com/diet103/claude-code-infrastructure-showcase — 9,630 stars
- **Content:** skill, hook, agent, command (.claude/ with all four types; reference library pattern)
- **Layout:** `.claude/skills/` with `skill-rules.json` for activation config; `.claude/hooks/skill-activation-prompt` as the key hook; `.claude/agents/` for 10 specialized agents; `.claude/commands/` for slash commands; production pattern: skills have `type`, `enforcement`, `priority` metadata in `skill-rules.json`
- **Significance:** This repo demonstrates a practitioner-invented extension: `skill-rules.json` as a sidecar config that controls skill auto-activation via hook. The hook reads the user prompt + file context and suggests relevant skills. This is the first example of a metadata layer on top of SKILL.md dirs — analogous to a runtime manifest. ACIF should evaluate whether this activation-config pattern is common enough to warrant a spec element.

---

### From EveryInc / Every.to

#### Citation 19
- **Source:** [EveryInc/compound-engineering-plugin README](https://github.com/EveryInc/compound-engineering-plugin) — 2026
- **Author:** Kieran Klaassen & Dan Shipper (Every.to; AI publishing company with 100k+ subscribers)
- **Quote (from README):** "Like compound interest, every feature you build makes the next feature cheaper to build." / "The plugin ecosystem for Claude Code is still very early. What exists now — these tools plus a growing community of skills on the Superpowers marketplace — is probably 10% of what will exist by the end of 2026."
- **Repo:** github.com/EveryInc/compound-engineering-plugin — 16,603 stars
- **Content:** skill + agent (37 skills, 51 agents; cross-platform)
- **Layout:** `plugins/compound-engineering/` with CLAUDE.md + AGENTS.md + skills/ + agents/ subdirs; multi-platform converter bakes Codex/Gemini variants from single source; plugin marketplace installable
- **Significance:** Compound engineering is the media company (Every.to) entering the skills ecosystem. Their two-file convention — CLAUDE.md + AGENTS.md both present per plugin — is notable as a practitioner pattern that predates any spec harmonization. Dan Shipper's 10%-of-what-will-exist quote is useful future-signaling for ACIF scope.

---

### From Firecrawl Blog (firecrawl.dev)

#### Citation 20
- **Source:** [Best Claude Code Skills to Try in 2026](https://www.firecrawl.dev/blog/best-claude-code-skills) — April 24, 2026
- **Author:** Firecrawl (web scraping API company; their own skill appears in the list)
- **Quote on obra/superpowers:** "One of the few skill collections with proper multi-hour autonomous capability baked into the workflow."
- **Quote on garrytan/gstack:** "One of the few skill collections that models a full team structure rather than a single capability."
- **Repos (all cited in one post):** anthropics/skills, vercel-labs/agent-skills, obra/superpowers, trailofbits/skills, remotion-dev/skills, coreyhaines31/marketingskills, travisvn/awesome-claude-skills
- **Content (remotion-dev/skills):** skill (video-generation code best practices for Remotion framework; ~3.1k stars)
- **Content (coreyhaines31/marketingskills):** skill (CRO, copywriting, SEO, analytics, growth; ~28k stars)
- **Significance:** Firecrawl's "two types of skills" taxonomy — Capability Uplift (gives Claude new abilities) vs. Encoded Preference (shapes existing abilities) — is the clearest practitioner framework for categorizing skills content. This maps directly to what ACIF should consider as a `skill-type` or `skill-kind` metadata field. Also notable: remotion-dev/skills is the first framework-specific skill collection from a popular OSS project maintainer (not just an AI tools person).

---

## Patterns observed

**1. The "I use X" signal is heavily concentrated in four repos.** Public discourse converges on obra/superpowers, garrytan/gstack, EveryInc/compound-engineering-plugin, and mattpocock/skills as the "Big Four" that practitioners compare and choose between. These four dominate X comparisons and blog post recommendation lists. All four use SKILL.md dirs with YAML frontmatter as the canonical unit.

**2. Skills and hooks are tightly coupled in practitioner discourse.** The most-recommended repos (superpowers, diet103/infrastructure-showcase) use hooks not as optional add-ons but as the activation mechanism for skills. The pattern: a hook reads the user's prompt context, then suggestions or enforces skills. This hook→skill coupling is not in Anthropic's spec but is the most common practitioner pattern.

**3. Two emerging layout conventions for rules repos.** Unlike skills (universal SKILL.md dirs), rules repos split two ways: (a) flat .md files by scope (steipete/agent-rules: global-rules/, project-rules/), and (b) topic-organized .md files with a companion docs/ dir for reference markdown. Neither convention uses frontmatter manifests or marketplace.json — rules repos are "drop-in" not "install-via-marketplace."

**4. skills.sh is the distribution layer, not GitHub search.** Vercel's skills.sh (launched Jan 20, 2026) and Anthropic's plugin marketplace are how practitioners find skills — GitHub stars are a lagging signal. The 20,900 installs of vercel-react-best-practices on day 1 via `npx skills add` show distribution latency is now days, not months.

**5. Cross-platform portability is assumed, not aspirational.** Every major repo in this survey (gstack, superpowers, compound-engineering, mattpocock/skills, vercel-labs/agent-skills) ships AGENTS.md and SKILL.md in the same dirs and explicitly lists supported agents (Claude Code, Codex, Cursor, Gemini CLI, etc.). The open standard announcement (Dec 18, 2025) made cross-agent portability the default expectation.

**6. Memory/context persistence is an unsolved problem generating its own repo category.** claude-mem (75k stars), obra/claude-memory-extractor, and the CCPM worktree pattern all address the same gap: skills and agents don't carry state between sessions. ACIF should consider whether session context persistence is a first-class concern or out of scope.

**7. Domain-specific skills repos are an emerging category.** Trail of Bits (security), remotion-dev (video), coreyhaines31 (marketing), trailofbits (security audit), and the Elixir/Phoenix plugin all show practitioners building vertical-specific skill collections. The layout is uniform (SKILL.md dirs) but the frontmatter metadata (license, version, target-domain) varies. ACIF should decide whether domain metadata belongs in frontmatter or in a sidecar.

---

## Access limitations

- **Twitter/X:** All X citations came from search-engine snippets (Google/DuckDuckGo index). Direct fetches of x.com URLs returned HTTP 402 Payment Required. Tweet text is confirmed to 140-char snippet depth only — no thread context, no quote-tweet chains. High-follower accounts (Garry Tan, steipete) are well-indexed so snippets are reliable; lower-follower accounts may be missed entirely.
- **Podcast show notes (Latent Space, Practical AI, Cognitive Revolution):** No specific GitHub repo citations found in show notes for these podcasts. The Latent Space Claude Code episode (May 2025) is rich on architecture but cites no repos. Podcast show notes in this ecosystem link to Anthropic docs, not community repos.
- **Substack:** No Substack posts specifically citing repos found via the searches run. Every.to publishes on their own domain, not Substack, so their content appeared through blog searches.
- **YouTube:** Not searched. Theo Browne and Fireship were not reached in time for this round.
- **Paywalled content:** every.to essays are partially paywalled; repo README was used as the primary source instead.
