# Category 6: Broader Agentic + Prompt Collections — Raw Agent Output

> **Edit note (2026-05-12):** Vendor-specific plugin/marketplace distribution systems are out of scope for ACIF — it is provider-agnostic content interchange, not a distribution-system spec. This category is largely free of those systems; what's described here is language-native packaging (`pyproject.toml`, `package.json`), filename conventions, sidecar JSON catalogs (`_meta.json`), and single-file aggregations (CSV / JSON arrays / README-as-index).

Total: **16 repos**, combined ~1.06M stars.

## Table

| repo | stars | primary_content_types | layout_pattern | content_unit | manifest_style | pack_manifest_file | multi_file_aux | versioning | license_location | discovery_pattern | notable_quirks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| danielmiessler/Fabric | 41,663 | pattern | flat | dir-with-readme | none (convention) | none | relative-path-implicit (`system.md`, optional `user.md`) | git-tags | top-level-LICENSE | dir-convention (`data/patterns/<name>/system.md`) | 255 patterns, every dir MUST contain `system.md`; pure filename convention, no metadata anywhere |
| f/prompts.chat (awesome-chatgpt-prompts) | 162,102 | prompt | flat | csv-row + i18n-json | csv-index + sidecar-json | `.commandcode/prompts.csv` + `messages/*.json` | none | git-tags | top-level-LICENSE | csv-index | Hyper-famous "awesome" repo is literally one CSV (`act,prompt`) plus 30+ locale JSONs; the Next.js shell is the "platform" |
| 0xeb/TheBigPromptLibrary | 5,043 | prompt, system-prompt, custom-gpt | by-type then by-vendor | single-md | readme-as-index | per-dir `README.md` | none | none | top-level-LICENSE | readme-as-index | `SystemPrompts/<Vendor>/<dated-version>.md`; READMEs hand-curated TOCs; date-versioned filenames |
| linexjlin/GPTs | 31,979 | leaked-system-prompt | flat | single-md | none | none | none | none | none-observed | filename-convention | 600+ files named after GPT title (`AI Doctor.md`); body is heading + paragraph + fenced markdown block |
| jujumilk3/leaked-system-prompts | 14,566 | leaked-system-prompt | flat | single-md | none | none | none | per-item-version (in filename) | none-observed | filename-convention | Filename = `<vendor>-<model>_<YYYYMMDD>.md`; date-versioning baked into name |
| elder-plinius/CL4R1T4S | 26,069 | leaked-system-prompt | by-vendor | single-txt/md | none | none | none | per-item-version (in filename) | top-level-LICENSE | dir-convention + filename-convention | All-caps vendor dirs (`ANTHROPIC/`, `OPENAI/`); files are `.txt` raw dumps, dated suffix |
| crewAIInc/crewAI-examples | 5,942 | agent, crew, flow | by-type then by-topic | dir-with-readme | pyproject.toml + readme-as-index | per-example `pyproject.toml` | __init__.py-imports + `agents.py`/`tasks.py` | pyproject.toml | top-level-LICENSE | code-import (Python modules) | Each example is a tiny Python package; agent definitions live IN code, not config |
| microsoft/autogen | 57,964 | framework + agents (in code) | by-platform (python/dotnet) | single-py | pyproject.toml | per-package `pyproject.toml` | __init__.py-imports | pyproject.toml | top-level-LICENSE | code-import | Agents defined as Python classes; no separable "content" — everything is in the SDK |
| langchain-ai/langgraph | 31,858 | examples (notebooks), templates | by-topic | single-py or notebook | pyproject.toml + readme-as-index | per-lib `pyproject.toml` | __init__.py-imports | pyproject.toml | top-level-LICENSE | code-import + readme-as-index | Examples are `.ipynb` files; reusable agents live in separate `*-template` repos |
| langgenius/dify | 141,090 | workflow, agent, prompt-tool | by-type (in app) | yaml-spec (DSL) | mixed | none in repo (DSL files exported per workflow) | explicit-list-in-frontmatter (DSL refs nodes) | per-item-version | top-level-LICENSE | code-import (DB-backed) | Content is a YAML DSL but lives in user databases, not repo; repo is the *engine* |
| microsoft/promptflow | 11,122 | flow, prompty, eval | by-type (`standard`, `chat`, `evaluation`) | dir-with-yaml-spec | yaml-spec (`flow.dag.yaml`) + frontmatter-yaml (`.prompty`) | `flow.dag.yaml` per flow | explicit-list-in-frontmatter (DAG refs `.jinja2`/`.py`) | git-tags | top-level-LICENSE | dir-convention + filename-convention (`*.prompty`) | `.prompty` is a real spec: YAML frontmatter + chat-format body in one file. Closest analog to ACIF skill |
| dair-ai/Prompt-Engineering-Guide | 74,475 | guide, prompt-example | by-topic | single-mdx | sidecar-json (`_meta.json`) | `_meta.<locale>.json` per dir | none | git-tags | top-level-LICENSE | dir-convention + sidecar-index | Nextra docs site; `_meta.json` files define nav order in 14 locales |
| PlexPt/awesome-chatgpt-prompts-zh | 60,001 | prompt | flat | json-array-entry | sidecar-json | `prompts-zh.json` | none | none | top-level-LICENSE | readme-as-index | One big JSON array — `[{act, prompt}]` — that's it |
| n8n-io/n8n | 187,560 | workflow (in app) | by-package | other (workflow DSL, in DB) | package.json | per-package `package.json` | none in repo | package.json | top-level-LICENSE | code-import | Repo is the engine; "templates" in repo are HTML/handlebars, not workflows. Workflow templates ship via api.n8n.io |
| EmbraceAGI/awesome-chatgpt-zh | 11,534 | curated-link | flat | readme-as-index | readme-as-index | `README.md` only | none | none | top-level-LICENSE | readme-as-index | Pure "awesome list" — no content files, all entries are README bullets with URLs |
| promptslab/Awesome-Prompt-Engineering | 5,905 | curated-link, paper-ref | flat | readme-as-index | readme-as-index | `README.md` | none | none | top-level-LICENSE | readme-as-index | Classic awesome-list pattern; `_source` dir holds bib citations |

## Narrative

When publishers have **no standard to follow**, they fall into a small number of repeating shapes — and the dominant pattern is **convention over manifest**.

**The four shapes that emerged:**

1. **Filename-convention flat collections** (Fabric, linexjlin/GPTs, jujumilk3, CL4R1T4S). One directory, one file per item, identity encoded in the filename. Zero metadata. Fabric mandates that every pattern dir contain `system.md` — that's the entire schema. linexjlin gets 600+ "custom GPTs" with just `<Title>.md`. CL4R1T4S and jujumilk3 jam version+date into the filename itself (`anthropic-claude-opus-4.5_20251124.md`) because there's no frontmatter slot for it.

2. **Single-file aggregations** (f/prompts.chat CSV; PlexPt JSON; awesome-lists). The most famous prompt repo on GitHub (162k stars) is *literally one CSV*. PlexPt is *literally one JSON array*. Awesome-lists are *literally one README*. These repos prove that for vast swaths of the ecosystem, "content" is just rows in a table.

3. **Dir-as-package with code manifests** (crewAI-examples, langgraph, autogen, promptflow, dify, n8n). When the content needs to *execute*, publishers reach for the language's native manifest — `pyproject.toml`, `package.json`. Agents are Python classes, not config. Discovery is `import`, not file-walking.

4. **Real specs, narrowly adopted** (Microsoft Prompty `.prompty`, Dify DSL, promptflow `flow.dag.yaml`). Only when a vendor builds an *engine* does a real declarative spec appear — and even then, the spec is single-tool, not portable.

**Signal for ACIF's Decision #18 (registry-inferred packs):** Almost none of these repos has a plugin.json or pack manifest. The "pack" is implicit — it's either the entire repo (`f/prompts.chat`), a top-level subdirectory (`data/patterns/` in Fabric), or a Python package boundary. A registry that infers packs from directory structure will absorb 80%+ of this content unchanged. Demanding an explicit `acif-pack.yaml` would force every one of these publishers to add a file they never wanted; the carrier model's universal sidecar + opt-in frontmatter (Decision #15) is exactly right because it lets the *registry* add metadata without touching the publisher's repo.

The biggest gap: **versioning**. Most of these repos have *no* per-item version. Fabric and Dify pin via git tags on the whole repo. CL4R1T4S/jujumilk3 stuff version into filenames. ACIF will need a "version is git-commit if absent" fallback.

## ACIF implications

- **README-as-index is the modal pack manifest.** Decision #18's registry-inferred pack model must handle "no manifest exists" as the *normal* case, not the exception. Demanding any new file would exclude the top-100 prompt repos.
- **Filename IS the metadata** for huge swathes of content (Fabric's `system.md` convention, jujumilk3's date-stamped names). ACIF carriers need to allow `id` and `version` to be *derived* from filename when no frontmatter/sidecar is present.
- **Single-file aggregations are real content.** `f/prompts.chat` (1 CSV, 162k stars) and PlexPt (1 JSON, 60k stars) mean ACIF needs an "exploder" pattern: a single carrier file declaring "this CSV/JSON contains N items, here's how to slice them." Otherwise these collections require human re-authoring.
- **Code-as-content is unavoidable.** crewAI/langgraph/autogen agents live in `.py` files imported by `__init__.py`. ACIF can't ingest these as portable content units — but it should at minimum recognize a `pyproject.toml`-bounded directory as a *pack* and treat the Python module as an opaque payload.
- **Per-item versioning is rare; default to git-commit + path hash.** Only Microsoft `.prompty` and Dify DSL carry explicit per-item versions. Everyone else relies on repo-level git tags. ACIF's `version` field must accept "inherit from registry" as a first-class value.
- **i18n is a sleeper requirement.** PEG has `_meta.{en,de,zh,...}.json`; `f/prompts.chat` has 30+ `messages/*.json` locale files. ACIF should not force a single canonical text body — `body` may need to be locale-keyed or the carrier needs a `locale` discriminator so multiple carriers can describe the same logical item in different languages.
- **License is almost always top-level only.** Per-item license metadata is essentially nonexistent. ACIF's `license` field at the item level should default to "inherit from pack/repo LICENSE file" rather than requiring per-item declaration.
- **The `.prompty` format is the closest existing analog** — YAML frontmatter + chat-format body in a single file. Worth a deliberate compatibility study; if ACIF skill carriers can losslessly round-trip a `.prompty`, ingestion of all Microsoft promptflow/Azure AI content comes for free.
