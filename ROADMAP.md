# ACIF Roadmap

This is a list of items the ACIF spec has explicitly deferred. No version assignments — items here are not committed to any future release and are not prioritized.

The purpose of this file is to make deferrals visible: when someone asks "why doesn't ACIF handle X?", the answer is either "it does" (see SHAPE.md) or "it's listed here, with the rationale."

---

## Deferred items

### Single-file aggregations

Multi-item content stored as one CSV, JSON array, or single README (e.g., `f/prompts.chat` is one CSV containing 162k stars worth of prompts; `PlexPt` is one JSON array; awesome-list READMEs are single files of curated entries).

**Why deferred:** These collections are popular content but not unitized. Treating them as ACIF items would require an "exploder" carrier that declares how to slice one file into N logical items (path/JMESPath/CSV column mapping). Authoring burden is real, and the demand signal from publishers is weak — most aggregations are curated by hand, not synced as ACIF content.

**What it would take to revisit:** A publisher with a high-traffic aggregation asks for ACIF support, or a registry needs to ingest one.

### i18n / locale variants

Some publishers ship the same skill in multiple languages (PEG ships `_meta.{en,de,zh,...}.json` in 14 locales; `f/prompts.chat` has 30+ `messages/*.json`; obra/superpowers has localized README variants).

**Why deferred:** ACIF currently has no `locale` discriminator. Adding one touches identity (does each locale variant get its own UUID? share one?), discovery (which locale does a consumer prefer?), and rendering (does the runtime know the user's locale?). All resolvable, none urgent.

**What it would take to revisit:** A publisher with serious i18n needs asks for ACIF support, or a registry wants to surface localized variants distinctly.

### Multi-size content variants

Some publishers ship `.md`, `.mini.md`, `.nano.md` for different context-window budgets (ciembor's pattern). Authors are manually solving for context economy.

**Why deferred:** Could be modeled as `variants: [{name, body_hash}]` on a single item, or as N separate items. Either way, it's a feature addition, not a correctness issue.

**What it would take to revisit:** Context-window pressure shows up as a publisher-driven concern (rather than a runtime concern that the runtime handles).

### AGENTS.md full bidirectional emit/render

Round 1 finding #2 + Round 2 finding #16: ACIF v0.1 treats AGENTS.md as an informative marker. A full bidirectional workflow — read AGENTS.md as carrier input, write AGENTS.md as a canonical output target — is more than v0.1 needs.

**Why deferred:** Marker recognition is small and uncontroversial. Bidirectional CI is a larger surface (what's the round-trip guarantee? does AGENTS.md content map cleanly to ACIF's content types?).

**What it would take to revisit:** AGENTS.md adoption keeps accelerating *and* practitioners ask for ACIF tools that round-trip cleanly.

### Memory as a content type

Some practitioners ship git-backed agent memory (e.g., `gastownhall/gastown` uses `.beads/beads.jsonl`). This is not a hook, skill, rule, command, agent, or mcp_config — it's a 7th category.

**Why deferred:** Memory-as-content is an emerging pattern with one or two visible publishers. ACIF v0.1 has six well-bounded content types; adding a seventh on weak signal would dilute the spec.

**What it would take to revisit:** Multiple independent publishers converge on a memory-as-content pattern with similar shape.

### Cross-pack versioned dependencies

A skill declaring "requires hook X v2.x" from a different pack. ACIF v0.1 has same-pack cross-references for activation (Decision #21) using item UUIDv4, but no version constraints in the reference.

**Why deferred:** Single-pack activation cross-references are sufficient for the patterns observed so far. Cross-pack dependencies are a larger design surface (version range syntax, conflict resolution, transitive dependency handling) and the demand signal is currently zero.

**What it would take to revisit:** A pack publisher asks for the ability to constrain a referenced item by version, or a registry needs to express compatibility.

### Code-as-content (Python modules, TypeScript scripts, etc.)

LangChain / CrewAI / AutoGen agents live in `.py` files imported by `__init__.py`. Genaiscript skills are TypeScript modules. Dify workflows are YAML DSL in databases.

**Why deferred:** These are not portable units in the ACIF sense — they're code that runs in a specific runtime. ACIF cannot ingest them without parsing language-specific ASTs, which is a different scope.

**What it would take to revisit:** Unlikely. ACIF's design boundary is content interchange, not code distribution.

### Curated-index aggregator READMEs

Awesome-lists (e.g., `punkpeye/awesome-mcp-servers`, `jim-schwoebel/awesome_ai_agents`) are single READMEs of curated links. They're content discovery surfaces, not content publishers.

**Why deferred:** Out of scope by design. These point *to* publishers; ACIF talks to publishers directly.

**What it would take to revisit:** Never — this is a permanent scope boundary, not a deferral.
