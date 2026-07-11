# Category 1: Claude Skills API + skill-shaped repos — Raw Agent Output

> **Edit note (2026-05-12):** Vendor-specific plugin/marketplace distribution systems (`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, etc.) are out of scope for ACIF — it is provider-agnostic content interchange, not a distribution-system spec. Observations about those files have been stripped from this raw file; what remains is content-shape data (SKILL.md conventions, multi-file layout, frontmatter, discovery, versioning).

Surveyed **17 repos** (18 distinct entries; 3 are pattern-illustrative — simonw archive, two "awesome" lists, dotagents CLI).

## Table

| repo | stars | content_types | layout_pattern | skill_unit | multi_file_aux | versioning | discovery_pattern | frontmatter_fields | quirks |
|---|---|---|---|---|---|---|---|---|---|
| anthropics/skills | ~133k | skill | by-type (skills/) | dir-with-SKILL.md | scripts-dir + references/assets + per-item LICENSE.txt | repo-level | dir-convention | name, description, license | Per-skill `LICENSE.txt` shipped alongside `SKILL.md` |
| obra/superpowers | ~188k | skill, hook, agent, command (multi-platform) | hybrid (skills/ + parallel runtime dirs) | dir-with-SKILL.md | scripts-dir + sibling .md companions (e.g. `testing-anti-patterns.md`, `visual-companion.md`) | semver | dir-convention | name, description | Ships parallel runtime config dirs for several tools — one source of truth packaged N ways |
| simonw/claude-skills | 922 | skill (archival snapshots) | flat | zip archives + README links | none | none | filename-convention (zip name) | n/a | Repo is a *historical archive* of Anthropic's `/mnt/skills` snapshots; no live skill files |
| SawyerHood/dev-browser | 6081 | skill (+ daemon CLI) | by-type (skills/<name>) | dir-with-SKILL.md (single file in dir) | none (companion source is in /cli /daemon) | semver | dir-convention | name, description | The skill is a thin wrapper; the heavy lifting is a sibling npm CLI shipped via `package.json` |
| alirezarezvani/claude-skills | ~14.5k | skill, agent, command, mcp, hook, rule | hybrid by-topic (engineering/, marketing-skill/, finance/, …) and by-platform (multiple runtime dirs) | dir-with-SKILL.md inside `<topic>/<plugin>/skills/<skill>/` | scripts-dir + references-dir | repo-level + per-topic | mixed (dir convention) | name, description (and many doc-only fields) | Nested topic dirs — sub-tree pattern |
| travisvn/awesome-claude-skills | ~12.4k | n/a (curated README list) | flat | external links | none | none | README list | n/a | Pure README — no skills hosted; useful for discovery only |
| BehiSecc/awesome-claude-skills | ~9k | n/a (curated README list) | flat | external links | none | none | README list | n/a | Same pattern as travisvn (likely fork/clone of curated list) |
| ComposioHQ/awesome-claude-skills | ~59k | skill | flat (each top-dir is a skill) | dir-with-SKILL.md | scripts-dir + per-skill LICENSE.txt | none observed | dir-convention + README list | name, description, license | Despite the "awesome" name, this repo *hosts* skills at top level rather than being a list — flat layout |
| Jeffallan/claude-skills | ~9k | skill, command | by-type (skills/, commands/, specs/) | dir-with-SKILL.md | references/ subdir (multiple `.md`) | semver | dir-convention | name, description, license, metadata.{author,version,domain,triggers,role,scope,output-format,related-skills} | Rich custom metadata under `metadata:` sub-key — extends Anthropic frontmatter heavily |
| coleam00/second-brain-skills | 720 | skill | by-platform (.claude/skills/) | dir-with-SKILL.md | references-dir + scripts-dir + LICENSE.txt | none | dir-convention | name, description | Pure folder drop-in for the runtime `.claude/skills/` location |
| jezweb/claude-skills | 776 | skill | by-topic | dir-with-SKILL.md | scripts dir; assets in `.claude/skills/artifacts` | none observed | dir-convention | name, description | Splits "delivered" content from "live working skills" |
| iannuttall/dotagents | 683 | tool (CLI, not content) | n/a (TypeScript app) | n/a | none | npm semver | n/a | n/a | A tool that *manages* AGENT/CLAUDE/SKILL.md files via symlinks — meta-pattern |
| mhattingpete/claude-skills-marketplace | 571 | skill, agent, command | hybrid (top dirs each containing skills/, agents/, commands/) | dir-with-SKILL.md | none in sample | per-topic semver | dir-convention | name, description | Multi-section repo; each section self-contained |
| microsoft/skills | 2291 | skill, agent, command, mcp, hook | hybrid layout under `.github/plugins/<topic>/{skills,agents,commands}/` | dir-with-SKILL.md | per-topic scripts | per-topic semver | dir-convention | name, description | Unusual host dir (`.github/`); mixes skills+agents+commands+hooks per topic |
| blacktop/ipsw-skill | 53 | skill | flat-with-named-dir (`ipsw/`) | dir-with-SKILL.md | references-dir + per-skill LICENSE.txt | npm semver in package.json | mixed (package.json `pi.skills` array + dir convention) | name, description | "pi-package" keyword in package.json — an emerging language-native convention (`pi.skills: ["./ipsw"]`); also ships `gemini-extension.json` for Gemini CLI |
| geekjourneyx/md2wechat-skill | 2175 | skill (skill is wrapper over a Go CLI) | flat (skills/<name>) | dir-with-SKILL.md | sibling Go module is the actual impl | semver via VERSION file + package.json | dir-convention | name, description | The "skill" is a thin instructional wrapper around a Go binary; ships AGENTS.md + CLAUDE.md too |
| dgreenheck/webgpu-claude-skill | 895 | skill | flat (skills/<name>) | dir-with-SKILL.md | none in sample | semver | dir-convention | name, description | Also ships `.cursor/` parallel runtime dir — same skill, two tool conventions |
| FrancyJGLisboa/agent-skill-creator | 902 | skill (+ multi-platform exports) | hybrid (top-level SKILL.md + references/ + registry/ + exports/) | single SKILL.md at root | references-dir (lots of `.md` companions) + scripts-dir + registry/skills/ | per-skill `metadata.version` (`4.0.0`) | mixed (dir convention) | name, description, license, metadata.{author, version, ...} | Self-describes as "14+ tool" exporter — generates per-platform variants into `exports/` |
| SnailSploit/Claude-Red | 1251 | skill | by-topic (Skills/<topic>/<skill>/) | dir-with-SKILL.md | scripts + references | semver | dir-convention | name, description | Custom non-vendor categorized layout |

## Narrative

**Skill-unit shape is overwhelmingly consistent.** Across every content-bearing repo, a "skill" is a **directory whose entry point is `SKILL.md`** containing a thin YAML frontmatter with at minimum `name` + `description`. Anthropic's template (`name`, `description`, optional `license`) is treated as canonical and copied verbatim — even repos with elaborate ecosystems (Jeffallan, FrancyJGLisboa) put their custom keys under a `metadata:` sub-key rather than at the top, preserving the simple base shape.

**Multi-file structure is *implicit by directory*, not declared.** Across 14 content repos, **zero** declare auxiliary files in frontmatter. Auxiliary files live next to `SKILL.md` by convention: `scripts/` (10/14 repos), `references/` (8/14), `assets/` (3/14), `examples/` (2/14), or sibling `.md` companions (superpowers' `testing-anti-patterns.md`, `visual-companion.md`). Tools are expected to walk the directory. **This is a strong signal for ACIF OQ-8: skills want implicit-bundle semantics, not an explicit `supplementary_files` list.**

**Discovery is split half-and-half** between *explicit listing* (anthropics, mhattingpete, microsoft, SawyerHood, blacktop) and *directory convention* (superpowers, Jeffallan, coleam00, dgreenheck, ComposioHQ). Some hybrid patterns point at a directory rather than a list — an implicit fan-out.

**Versioning lives at the pack/repo level, not per-skill.** Almost no repo versions individual skills. Versions appear on `package.json` or on repo-level VERSION/git-tag mechanisms. Jeffallan is the only outlier with `metadata.version` per skill. **Decision-relevant: ACIF per-item version is rare in practice.**

**Cross-platform mirroring is emerging.** Superpowers, alirezarezvani, blacktop, geekjourneyx, and dgreenheck ship parallel platform-specific runtime config dirs (e.g. `.claude/`, `.codex/`, `.cursor/`, `.opencode/`, `gemini-extension.json`). FrancyJGLisboa explicitly *generates* per-platform exports. This is exactly the gap ACIF targets — these repos are hand-rolling carrier transforms.

**Surprises:**
1. simonw/claude-skills is just an archive of zips, no manifests at all — yet has ~922 stars. Shows raw filesystem snapshots remain a viable distribution unit.
2. ComposioHQ/awesome-claude-skills despite ~59k stars and the "awesome" name actually *hosts* skills at top level with no manifest — pure dir-convention.
3. Frontmatter custom fields are remarkably restrained — most repos resist adding keys; Jeffallan's `metadata.{author, version, domain, triggers, role, scope, output-format, related-skills}` is the most aggressive observed.

**Decision #19 (directory hashing) signal:** every content repo with a skill that has auxiliaries (scripts/references/assets/examples + sibling .md) treats the *directory* as the atomic unit. Hashing the skill dir is the right granularity — not just `SKILL.md`. Multiple repos commit per-skill `LICENSE.txt` files inside the dir, which would be missed by single-file hashing.

## ACIF implications

- **Carrier must accept "skill = directory with `SKILL.md` + implicit siblings"** as the dominant pattern (14/14 content repos). Don't force authors to enumerate supplementary files.
- **OQ-8 supplementary_files: lean implicit/glob.** No surveyed repo declares aux files explicitly. An ACIF requirement to enumerate would force a behavior change with zero upstream precedent. Consider: "all files in the skill directory are part of the skill unless gitignored."
- **Decision #19 hash should be over the skill directory tree** (sorted, content-only), since per-skill LICENSE, scripts, references, and companion `.md` files are universal and load-bearing.
- **Per-item versioning is not the norm — pack-level versioning is.** ACIF can keep per-item version optional.
- **Cross-platform mirror dirs are an authored-by-hand pain point** ACIF can solve. Five of fourteen content repos already maintain parallel trees — strong product demand signal.
- **Discovery should support both styles**: explicit lists *and* directory-fan-out. A pure-explicit ACIF would force migration; a pure-implicit one would lose patterns already in use.
