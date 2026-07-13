from __future__ import annotations

import hashlib
import importlib
from pathlib import Path
from typing import Callable

from ..report import VectorResult
from ..vectors import CatalogSet, Vector

Binding = Callable[[Vector, object, object], VectorResult]

_BINDINGS: dict[str, Binding] = {}
_LOADED = False


def binding(vector_id: str) -> Callable[[Binding], Binding]:
    def decorator(func: Binding) -> Binding:
        if vector_id in _BINDINGS:
            raise ValueError(f"duplicate binding for {vector_id}")
        _BINDINGS[vector_id] = func
        return func

    return decorator


def load_all() -> None:
    global _LOADED
    if _LOADED:
        return
    importlib.import_module(__name__ + ".hook")
    _LOADED = True


def get(vector_id: str) -> Binding | None:
    load_all()
    return _BINDINGS.get(vector_id)


def bound_ids() -> set[str]:
    load_all()
    return set(_BINDINGS)


def coverage_errors(catalogs: CatalogSet) -> list[str]:
    load_all()
    catalog_ids = set(catalogs.by_id)
    bound = set(_BINDINGS)
    allowed = set(UNBOUND)
    errors: list[str] = []
    for vid in sorted(catalog_ids - bound - allowed):
        errors.append(f"missing binding and not allowlisted: {vid}")
    for vid in sorted(bound & allowed):
        errors.append(f"bound id is still allowlisted: {vid}")
    for vid in sorted((bound | allowed) - catalog_ids):
        errors.append(f"binding registry mentions unknown vector id: {vid}")
    return errors


def binding_set_hash() -> str:
    root = Path(__file__).resolve().parent
    pieces: list[bytes] = []
    for path in sorted(root.glob("*.py")):
        if path.name == "__pycache__":
            continue
        pieces.append(path.name.encode("utf-8") + b"\0" + path.read_bytes())
    return hashlib.sha256(b"\n".join(pieces)).hexdigest()


UNBOUND = {
    "TV-AGENT-a",  # stage-2
    "TV-AGENT-b",  # stage-2
    "TV-AGENT-c",  # stage-2
    "TV-AGENT-d",  # stage-2
    "TV-AGENT-e",  # stage-2
    "TV-AGENT-f",  # stage-2
    "TV-AGENT-g",  # stage-2
    "TV-AGENT-h",  # stage-2
    "TV-AGENT-i",  # stage-2
    "TV-AGENT-j",  # stage-2
    "TV-AGENT-k",  # stage-2
    "TV-COMMAND-a",  # stage-2
    "TV-COMMAND-b",  # stage-2
    "TV-COMMAND-c",  # stage-2
    "TV-COMMAND-d",  # stage-2
    "TV-COMMAND-e",  # stage-2
    "TV-COMMAND-f",  # stage-2
    "TV-COMMAND-g",  # stage-2
    "TV-COMMAND-h",  # stage-2
    "TV-COMMAND-i",  # stage-2
    "TV-COMMAND-j",  # stage-2
    "TV-COMMAND-k",  # stage-2
    "TV-COMMAND-l",  # stage-2
    "TV-COMMAND-m",  # stage-2
    "TV-1",  # stage-2
    "TV-2",  # stage-2
    "TV-3",  # stage-2
    "TV-4",  # stage-2
    "TV-5",  # stage-2
    "TV-6",  # stage-2
    "TV-7",  # stage-2
    "TV-8",  # stage-2
    "TV-9",  # stage-2
    "TV-10",  # stage-2
    "TV-11",  # stage-2
    "TV-12",  # stage-2
    "TV-13",  # stage-2
    "TV-L2-a",  # stage-2
    "TV-L2-b",  # stage-2
    "TV-L2-c",  # stage-2
    "TV-L2-d",  # stage-2
    "TV-L2-e",  # stage-2
    "TV-L2-f",  # stage-2
    "TV-L3-a",  # stage-2
    "TV-L3-b",  # stage-2
    "TV-L3-c",  # stage-2
    "TV-L3-d",  # stage-2
    "TV-FRESH-a",  # stage-2
    "TV-FRESH-b",  # stage-2
    "TV-FRESH-c",  # stage-2
    "TV-FRESH-d",  # stage-2
    "TV-FRESH-e",  # stage-2
    "TV-FRESH-f",  # stage-2
    "TV-FRESH-g",  # stage-2
    "TV-FRESH-h",  # stage-2
    "TV-FRESH-i",  # stage-2
    "TV-FRESH-j",  # stage-2
    "TV-FRESH-k",  # stage-2
    "TV-MCP-a",  # stage-2
    "TV-MCP-b",  # stage-2
    "TV-MCP-c",  # stage-2
    "TV-MCP-d",  # stage-2
    "TV-MCP-e",  # stage-2
    "TV-MCP-f",  # stage-2
    "TV-MCP-g",  # stage-2
    "TV-MCP-h",  # stage-2
    "TV-MCP-i",  # stage-2
    "TV-MCP-j",  # stage-2
    "TV-MCP-k",  # stage-2
    "TV-MCP-k2",  # stage-2
    "TV-MCP-l",  # stage-2
    "TV-MCP-m",  # stage-2
    "TV-PLATFORM-a",  # stage-2
    "TV-PLATFORM-b",  # stage-2
    "TV-PLATFORM-c",  # stage-2
    "TV-PLATFORM-d",  # stage-2
    "TV-PLATFORM-e",  # stage-2
    "TV-PLATFORM-f",  # stage-2
    "TV-PLATFORM-g",  # stage-2
    "TV-PLATFORM-g2",  # stage-2
    "TV-PLATFORM-h",  # stage-2
    "TV-PLATFORM-i",  # stage-2
    "TV-PLATFORM-j",  # stage-2
    "TV-PLATFORM-k",  # stage-2
    "TV-PLATFORM-l",  # stage-2
    "TV-PLATFORM-m",  # stage-2
    "TV-PLATFORM-n",  # stage-2
    "TV-PLATFORM-o",  # stage-2
    "TV-PLATFORM-p",  # stage-2
    "TV-PLATFORM-q",  # stage-2
    "TV-PLATFORM-q2",  # stage-2
    "TV-PLATFORM-r",  # stage-2
    "TV-PLATFORM-s",  # stage-2
    "TV-PLATFORM-t",  # stage-2
    "TV-RENDER-a",  # stage-2
    "TV-RENDER-b",  # stage-2
    "TV-RENDER-c",  # stage-2
    "TV-RENDER-d",  # stage-2
    "TV-RULE-a",  # stage-2
    "TV-RULE-b",  # stage-2
    "TV-RULE-c",  # stage-2
    "TV-RULE-d",  # stage-2
    "TV-RULE-e",  # stage-2
    "TV-RULE-f",  # stage-2
    "TV-RULE-g",  # stage-2
    "TV-RULE-h",  # stage-2
    "TV-RULE-i",  # stage-2
    "TV-RULE-j",  # stage-2
    "TV-RULE-k",  # stage-2
    "TV-RULE-l",  # stage-2
    "TV-RULE-m",  # stage-2
    "TV-SKILL-a",  # stage-2
    "TV-SKILL-b",  # stage-2
    "TV-SKILL-c",  # stage-2
    "TV-SKILL-d",  # stage-2
    "TV-SKILL-e",  # stage-2
    "TV-SKILL-f",  # stage-2
    "TV-SKILL-g",  # stage-2
    "TV-SKILL-h",  # stage-2
    "TV-SKILL-i",  # stage-2
    "TV-SKILL-j",  # stage-2
    "TV-SKILL-k",  # stage-2
    "TV-SKILL-l",  # stage-2
    "TV-SKILL-m",  # stage-2
    "TV-SKILL-n",  # stage-2
    "TV-URI-a",  # stage-2
    "TV-URI-b",  # stage-2
    "TV-URI-c",  # stage-2
    "TV-URI-d",  # stage-2
    "TV-URI-e",  # stage-2
    "TV-URI-f",  # stage-2
    "TV-URI-g",  # stage-2
    "TV-URI-h",  # stage-2
    "TV-URI-i",  # stage-2
    "TV-URI-j",  # stage-2
    "TV-URI-k",  # stage-2
    "TV-URI-l",  # stage-2
    "TV-URI-l2",  # stage-2
    "TV-URI-m",  # stage-2
    "TV-URI-n",  # stage-2
    "TV-URI-o",  # stage-2
    "TV-URI-o2",  # stage-2
    "TV-URI-p",  # stage-2
    "TV-URI-q",  # stage-2
    "TV-URI-r",  # stage-2
    "TV-URI-s",  # stage-2
    "TV-URI-t",  # stage-2
    "TV-URI-u",  # stage-2
    "TV-URI-v",  # stage-2
}
