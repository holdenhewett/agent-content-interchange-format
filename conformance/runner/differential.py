"""Differential mode — DESIGN.md §8 graduation evidence.

Generates randomized equivalence-preserving inputs (fresh bodies through
`ingest`, fresh URI strings through `normalize_uri`) and requires two
independent implementations to agree with each other. The pair is its own
oracle: every generated input lives in an equivalence class where the spec
pins a deterministic answer, so the harness never needs to know the answer
itself. This kills the lookup-table adapter class — you cannot pre-compute
answers to inputs that did not exist yesterday.

Trials are generated deterministically from --seed before any adapter is
spawned; the same seed and count reproduce the same run byte-for-byte
(modulo fixture paths).

Family discipline:
- required families (body, sidecar, envelope, pack_id) mirror request
  forms the core-scope static vectors already force both adapters to
  serve; an `unsupported` there breaks the run.
- the normalize_uri family is informative until both implementations
  claim registry scope: either side answering `unsupported` marks the
  trial uncomparable, never a disagreement.
"""

from __future__ import annotations

import argparse
import random
import shutil
from typing import Any

from . import RUNNER_PROTOCOL, RUNNER_VERSION
from .fixtures import EnvBlocked, FixtureContext, probe_environment
from .protocol import AdapterSession
from .report import write_report

ABSENT = "<absent>"

# TV-3's pinned inference namespace ([ACIF-PUBLISHER] §9.4).
PINNED_NAMESPACE = "93516344-00e5-419b-a230-6e8b1d02f87d"

KINDS = ["hook", "skill", "rule", "command", "agent", "mcp_config", "pack"]
FRONTMATTER_KINDS = ["skill", "rule", "command", "agent"]
FORBIDDEN_FIELDS = [
    "effective_version",
    "derived_version",
    "pack_inherited_version",
    "resolved_version",
]

REQUIRED_FAMILIES = {"body", "sidecar", "envelope", "pack_id"}
FAMILY_WEIGHTS = [
    ("body", 35),
    ("sidecar", 25),
    ("envelope", 20),
    ("pack_id", 10),
    ("normalize_uri", 10),
]

_WORDS = [
    "hash", "canonical", "sidecar", "registry", "publisher", "envelope",
    "conformance", "vector", "adapter", "fixture", "scope", "record",
    "café", "naïve", "Zürich", "日本語", "emoji ☕", "tab\tstop",
    "quote \"inner\"", "back\\slash", "trailing space ",
]

_FILE_NAMES = [
    "notes.md", "README.md", "docs/guide.md", "docs/deep/ref.md",
    "scripts/run.sh", "data/values.json", "sub/acif-sidecar.yaml",
    "LICENSE", "assets/café.txt",
]

_DISPLAY_NAMES = [
    "Demo Skill", "Review PR", "café ☕ tool", "quote\"back\\slash",
    "line\nbreak name", "tab\tname", "Ünïcodé Nàme", "日本語ツール",
    "  padded  ", "0", "a" * 80,
]

_SPDX_VALID = ["MIT", "Apache-2.0", "BSD-3-Clause", "ISC", "MPL-2.0"]
_SPDX_INVALID = ["MIT License", "Apache 2.0", "GPL v3", ""]

_SEMVER_VALID = ["1.2.3", "0.1.0", "10.20.30", "1.0.0-rc.1", "2.3.4-alpha.7", "1.2.3+build.5"]
_SEMVER_INVALID = ["1.0", "v1.0.0", "1.0.0.0", "01.2.3", "1.2", "1.2.3 "]

_KIND_INVALID = ["Skill", "SKILL", "skills", "plugin", "mcp", "Rule"]

_URI_POOL = [
    "https://example.com/skills/demo",
    "HTTPS://Example.COM/Skills/Demo",
    "https://example.com:443/skills/demo",
    "https://example.com/a/../b/./c",
    "https://example.com/a%2Fb/c%20d",
    "https://example.com/skills/demo/",
    "https://example.com//double//slash",
    "https://example.com/skills/demo?tag=v1#frag",
    "https://user@example.com/skills/demo",
    "http://example.com/skills/demo",
    "file:///opt/skills/demo",
    "https://example.com/%C3%A9clair",
    "https://xn--caf-dma.example/menu",
]


def _rand_uuid4(rng: random.Random) -> str:
    hexd = "0123456789abcdef"
    s = "".join(rng.choice(hexd) for _ in range(32))
    return f"{s[0:8]}-{s[8:12]}-4{s[13:16]}-{rng.choice('89ab')}{s[17:20]}-{s[20:32]}"


def _bad_uuid(rng: random.Random) -> str:
    choice = rng.randrange(4)
    if choice == 0:
        return "not-a-uuid"
    if choice == 1:
        return _rand_uuid4(rng).replace("-", "", 1)
    if choice == 2:
        # version nibble 1, not 4
        u = _rand_uuid4(rng)
        return u[:14] + "1" + u[15:]
    return _rand_uuid4(rng)[:-1]


def _rand_text(rng: random.Random, max_lines: int = 5) -> str:
    lines = [" ".join(rng.sample(_WORDS, rng.randrange(1, 4))) for _ in range(rng.randrange(0, max_lines))]
    text = "\n".join(lines)
    if rng.random() < 0.8:
        text += "\n"
    return text


def _gen_body(rng: random.Random) -> dict[str, Any]:
    files: dict[str, str] = {}
    entry = "SKILL.md"
    if rng.random() < 0.3:
        files[entry] = "---\ndescription: " + rng.choice(_WORDS) + "\n---\n" + _rand_text(rng)
    else:
        files[entry] = _rand_text(rng)
    for name in rng.sample(_FILE_NAMES, rng.randrange(0, 5)):
        files[name] = _rand_text(rng)
    if rng.random() < 0.25:
        files["acif-sidecar.yaml"] = "kind: skill\nid: " + _rand_uuid4(rng) + "\n"
    return {
        "family": "body",
        "input": {"kind": "skill", "files": files, "entry_file": entry},
        "compare": ["body_hash", "classification"],
    }


def _gen_sidecar(rng: random.Random) -> dict[str, Any]:
    kind = rng.choice(FRONTMATTER_KINDS)
    section: dict[str, Any] = {
        "kind": kind,
        "id": _rand_uuid4(rng),
        "display_name": rng.choice(_DISPLAY_NAMES),
    }
    if rng.random() < 0.6:
        section["version"] = rng.choice(_SEMVER_VALID)
    if rng.random() < 0.4:
        section["description"] = " ".join(rng.sample(_WORDS, rng.randrange(1, 5)))
    if rng.random() < 0.3:
        section["license"] = {"spdx": rng.choice(_SPDX_VALID)}
    if rng.random() < 0.2:
        section["pack_id"] = _rand_uuid4(rng)
    items = list(section.items())
    rng.shuffle(items)
    return {
        "family": "sidecar",
        "input": {"kind": kind, "sidecar": dict(items)},
        "compare": ["metadata_hash", "canonical_bytes"],
    }


def _gen_envelope(rng: random.Random) -> dict[str, Any]:
    kind = rng.choice(FRONTMATTER_KINDS)
    record: dict[str, Any] = {
        "kind": kind,
        "id": _rand_uuid4(rng),
        "display_name": rng.choice(_DISPLAY_NAMES),
    }
    defect = rng.choice(["kind", "id", "version", "spdx", "forbidden"])
    if defect == "kind":
        record["kind"] = rng.choice(_KIND_INVALID)
    elif defect == "id":
        record["id"] = _bad_uuid(rng)
    elif defect == "version":
        record["version"] = rng.choice(_SEMVER_INVALID)
    elif defect == "spdx":
        record["license"] = {"spdx": rng.choice(_SPDX_INVALID)}
    else:
        record[rng.choice(FORBIDDEN_FIELDS)] = rng.choice(_SEMVER_VALID)
    # Mirrors the TV-11 binding: input.kind carries the record's kind
    # verbatim, even when the defect under test is the kind itself.
    return {
        "family": "envelope",
        "input": {"kind": record["kind"], "sidecar": record},
        "compare": ["conformant", "reason", "params.field"],
    }


def _gen_pack_id(rng: random.Random) -> dict[str, Any]:
    org = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randrange(3, 10)))
    repo = "-".join(rng.sample(["agent", "skills", "tools", "pack", "acif", "demo"], rng.randrange(1, 3)))
    return {
        "family": "pack_id",
        "input": {
            "namespace": PINNED_NAMESPACE,
            "repository_url": f"https://github.com/{org}/{repo}",
            "display_name": rng.choice(_DISPLAY_NAMES),
        },
        "compare": ["inferred_pack_id"],
    }


def _gen_normalize_uri(rng: random.Random) -> dict[str, Any]:
    return {
        "family": "normalize_uri",
        "input": {"uri": rng.choice(_URI_POOL)},
        "compare": ["source_uri"],
    }


_GENERATORS = {
    "body": _gen_body,
    "sidecar": _gen_sidecar,
    "envelope": _gen_envelope,
    "pack_id": _gen_pack_id,
    "normalize_uri": _gen_normalize_uri,
}


def generate_trials(seed: int, count: int) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    families = [name for name, weight in FAMILY_WEIGHTS for _ in range(weight)]
    trials = []
    for index in range(count):
        family = rng.choice(families)
        trial = _GENERATORS[family](rng)
        trial["index"] = index
        trials.append(trial)
    return trials


def _build_request(trial: dict[str, Any], ctx: FixtureContext) -> dict[str, Any]:
    family = trial["family"]
    inp = trial["input"]
    if family == "body":
        root = ctx.materialize(inp["files"])
        return {
            "op": "ingest",
            "input": {"kind": inp["kind"], "body_root": root, "entry_file": inp["entry_file"]},
        }
    if family in {"sidecar", "envelope"}:
        return {"op": "ingest", "input": {"kind": inp["kind"], "sidecar": inp["sidecar"]}}
    if family == "pack_id":
        return {"op": "derive_pack_id", "input": dict(inp)}
    if family == "normalize_uri":
        return {"op": "normalize_uri", "input": {"uri": inp["uri"]}}
    raise ValueError(f"unknown trial family {family!r}")


def _lookup(result: dict[str, Any], path: str) -> Any:
    current: Any = result
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return ABSENT
    return current


def _observe(response: Any, fields: list[str]) -> dict[str, Any]:
    if response.kind == "harness-error":
        return {"class": "harness-error", "detail": response.harness_error}
    if response.kind == "unsupported":
        return {"class": "unsupported"}
    if response.kind == "spec-error":
        return {"class": "error", "error": response.error}
    observed = {f: _lookup(response.result or {}, f) for f in fields}
    return {"class": "ok", "fields": observed}


def _trial_status(a: dict[str, Any], b: dict[str, Any], family: str) -> str:
    if a["class"] == "harness-error" or b["class"] == "harness-error":
        return "harness-error"
    if a["class"] == "unsupported" or b["class"] == "unsupported":
        if family in REQUIRED_FAMILIES:
            return "disagree" if a["class"] != b["class"] else "unsupported"
        return "uncomparable"
    return "agree" if a == b else "disagree"


def run_differential(
    *,
    adapter_a: str,
    adapter_b: str,
    seed: int,
    count: int,
    keep_fixtures: bool = False,
) -> dict[str, Any]:
    trials = generate_trials(seed, count)
    env = probe_environment()
    ctx = FixtureContext(env, keep_fixtures=keep_fixtures)

    rows: list[dict[str, Any]] = []
    counts = {"agree": 0, "disagree": 0, "uncomparable": 0, "unsupported": 0, "harness-error": 0, "env-skipped": 0}
    family_counts: dict[str, dict[str, int]] = {}

    with AdapterSession(adapter_a) as session_a, AdapterSession(adapter_b) as session_b:
        for trial in trials:
            row: dict[str, Any] = {
                "index": trial["index"],
                "family": trial["family"],
                "input": trial["input"],
            }
            try:
                request = _build_request(trial, ctx)
            except EnvBlocked as exc:
                row["status"] = "env-skipped"
                row["detail"] = str(exc)
            else:
                row["request_op"] = request["op"]
                response_a = session_a.request(request)
                response_b = session_b.request(request)
                a = _observe(response_a, trial["compare"])
                b = _observe(response_b, trial["compare"])
                row["a"] = a
                row["b"] = b
                row["status"] = _trial_status(a, b, trial["family"])
            counts[row["status"]] += 1
            fam = family_counts.setdefault(trial["family"], {})
            fam[row["status"]] = fam.get(row["status"], 0) + 1
            rows.append(row)

        hello_a = dict(session_a.hello or {})
        hello_b = dict(session_b.hello or {})

    kept = []
    if keep_fixtures:
        kept = [str(root) for root in ctx.roots]
    else:
        for root in ctx.roots:
            shutil.rmtree(root, ignore_errors=True)

    clean = (
        counts["disagree"] == 0
        and counts["harness-error"] == 0
        and counts["unsupported"] == 0
    )
    return {
        "differential": {
            "design": "DESIGN.md §8 differential pass (graduation evidence)",
            "seed": seed,
            "count": count,
            "clean": clean,
            "summary": counts,
            "families": family_counts,
        },
        "runner": {"version": RUNNER_VERSION, "runner_protocol": RUNNER_PROTOCOL},
        "adapters": {
            "a": {"invocation": adapter_a, "hello": hello_a},
            "b": {"invocation": adapter_b, "hello": hello_b},
        },
        "env_probes": env,
        "fixture_paths": kept,
        "trials": rows,
    }


def human_summary(report: dict[str, Any]) -> str:
    diff = report["differential"]
    a = report["adapters"]["a"]["hello"]
    b = report["adapters"]["b"]["hello"]
    lines = [
        f"Differential pass — seed {diff['seed']}, {diff['count']} trials",
        f"  A: {a.get('implementation')} {a.get('version')} (protocol {a.get('adapter_protocol')})",
        f"  B: {b.get('implementation')} {b.get('version')} (protocol {b.get('adapter_protocol')})",
        "  " + ", ".join(f"{k}={v}" for k, v in diff["summary"].items() if v),
        f"  clean: {diff['clean']}",
    ]
    for family, statuses in sorted(diff["families"].items()):
        detail = ", ".join(f"{k}={v}" for k, v in sorted(statuses.items()))
        lines.append(f"    {family}: {detail}")
    problems = [row for row in report["trials"] if row["status"] in {"disagree", "harness-error", "unsupported"}]
    if problems:
        lines.append("  Problem trials:")
        for row in problems:
            lines.append(f"    #{row['index']} [{row['family']}] {row['status']}: a={row.get('a')} b={row.get('b')}")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="python -m runner differential")
    parser.add_argument("--adapter-a", required=True, help="first adapter command")
    parser.add_argument("--adapter-b", required=True, help="second adapter command")
    parser.add_argument("--seed", type=int, default=0, help="deterministic generator seed")
    parser.add_argument("--count", type=int, default=200, help="number of generated trials")
    parser.add_argument("--report", help="write machine-readable report JSON")
    parser.add_argument("--keep-fixtures", action="store_true", help="keep materialized fixtures")
    args = parser.parse_args(argv)

    report = run_differential(
        adapter_a=args.adapter_a,
        adapter_b=args.adapter_b,
        seed=args.seed,
        count=args.count,
        keep_fixtures=args.keep_fixtures,
    )
    if args.report:
        write_report(args.report, report)
    print(human_summary(report))
    return 0 if report["differential"]["clean"] else 1
