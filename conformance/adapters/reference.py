#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "reference"))

from acif_hash import canonical_text, jcs, sidecar_only_body_hash  # noqa: E402


class Unsupported(Exception):
    pass


class SpecError(Exception):
    def __init__(self, error: str):
        super().__init__(error)
        self.error = error


EVENT_MAP = {
    "PreToolUse": "before_tool_execute",
    "BeforeTool": "before_tool_execute",
    "tool.execute.before": "before_tool_execute",
}
CANONICAL_EVENTS = {"session_start", "before_tool_execute"}


def emit(obj: dict[str, Any]) -> None:
    print(json.dumps(obj, ensure_ascii=False, separators=(",", ":")), flush=True)


def main() -> int:
    for line in sys.stdin:
        try:
            request = json.loads(line)
            response = handle(request)
        except Unsupported:
            response = {"unsupported": True}
        except SpecError as exc:
            response = {"ok": False, "error": exc.error, "diagnostics": []}
        except Exception as exc:  # pragma: no cover - deliberately adapter-internal
            response = {"ok": False, "error": f"adapter: {exc}"}
        emit(response)
    return 0


def handle(request: dict[str, Any]) -> dict[str, Any]:
    if request.get("op") == "hello":
        return {
            "ok": True,
            "result": {
                "implementation": "acif-reference",
                "version": "0.1",
                "adapter_protocol": 1,
                "scopes": ["core", "hook"],
            },
        }
    if request.get("op") != "ingest":
        raise Unsupported()
    inp = request.get("input")
    if not isinstance(inp, dict) or inp.get("kind") != "hook":
        raise Unsupported()
    hook = _hook_source(inp)
    body_root = inp.get("body_root")
    if body_root is not None and not isinstance(body_root, str):
        raise Unsupported()
    canonical, referenced_files = canonical_hook(hook, body_root)
    return {
        "ok": True,
        "result": {
            "canonical": canonical,
            "body_hash": sidecar_only_body_hash(canonical, referenced_files),
        },
    }


def _hook_source(inp: dict[str, Any]) -> dict[str, Any]:
    if "sidecar" in inp and isinstance(inp["sidecar"], dict):
        return inp["sidecar"]
    provider = inp.get("provider_config")
    if isinstance(provider, dict) and isinstance(provider.get("content"), dict):
        return provider["content"]
    raise Unsupported()


def canonical_hook(hook: dict[str, Any], body_root: str | None) -> tuple[dict[str, Any], dict[str, bytes]]:
    event = hook.get("event")
    if event in EVENT_MAP:
        event = EVENT_MAP[event]
    elif event not in CANONICAL_EVENTS:
        raise SpecError("acif.hook.event_unrecognized")

    handlers = hook.get("handlers")
    if not isinstance(handlers, list) or not handlers:
        raise SpecError("acif.hook.handlers_missing")

    referenced_files: dict[str, bytes] = {}
    canonical_handlers = []
    for handler in handlers:
        if not isinstance(handler, dict):
            raise Unsupported()
        handler_type = handler.get("type", "command")
        if handler_type != "command":
            raise SpecError("acif.hook.handler_type_unrecognized")
        scripts = handler.get("scripts", [])
        if not isinstance(scripts, list):
            raise Unsupported()
        canonical_scripts = []
        for script in scripts:
            canonical_script = canonicalize_script(script, body_root, referenced_files)
            canonical_scripts.append(canonical_script)
        canonical_scripts.sort(key=jcs)
        canonical_handler: dict[str, Any] = {
            "type": "command",
            "scripts": canonical_scripts,
            "async": bool(handler.get("async", False)),
        }
        canonical_handlers.append(canonical_handler)

    block: dict[str, Any] = {
        "event": event,
        "handlers": canonical_handlers,
        "blocking": bool(hook.get("blocking", False)),
    }
    if "matcher" in hook:
        block["matcher"] = hook["matcher"]
    return block, referenced_files


def canonicalize_script(script: Any, body_root: str | None, referenced_files: dict[str, bytes]) -> dict[str, Any]:
    if not isinstance(script, dict):
        raise Unsupported()
    script_type = script.get("type")
    if script_type == "inline":
        content = script.get("content")
        if not isinstance(content, str):
            raise Unsupported()
        canonical: dict[str, Any] = {
            "type": "inline",
            "content": canonical_text(content.encode("utf-8")).decode("utf-8"),
        }
    elif script_type == "file":
        rel = script.get("path")
        if not isinstance(rel, str):
            raise Unsupported()
        _validate_relpath(rel)
        if body_root is None:
            raise Unsupported()
        path = Path(body_root).joinpath(*PurePosixPath(rel).parts)
        try:
            data = path.read_bytes()
        except OSError:
            raise SpecError("acif.hook.script_file_missing") from None
        referenced_files[rel] = data
        canonical = {"type": "file", "path": rel}
    else:
        raise Unsupported()

    if "os" in script:
        canonical["os"] = script["os"]
    return canonical


def _validate_relpath(rel: str) -> None:
    if "\\" in rel:
        raise SpecError("acif.hook.script_path_invalid")
    if rel.startswith("//") or rel.startswith("\\\\"):
        raise SpecError("acif.hook.script_path_invalid")
    if len(rel) >= 2 and rel[1] == ":" and rel[0].isalpha():
        raise SpecError("acif.hook.script_path_invalid")
    if any(part in {"", ".", ".."} for part in rel.split("/")):
        raise SpecError("acif.hook.script_path_invalid")
    p = PurePosixPath(rel)
    if p.is_absolute():
        raise SpecError("acif.hook.script_path_invalid")


if __name__ == "__main__":
    raise SystemExit(main())
