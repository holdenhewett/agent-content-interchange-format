from __future__ import annotations

import json
import re
import subprocess
import sys
from typing import Any

HEX_RE = re.compile(r"^[0-9a-f]{64}$")


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "--":
        argv = argv[1:]
    if not argv:
        print("mutating_adapter requires a child command", file=sys.stderr)
        return 2
    child = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None, text=True, encoding="utf-8")
    assert child.stdin is not None and child.stdout is not None
    for line in sys.stdin:
        request = json.loads(line)
        child.stdin.write(line)
        child.stdin.flush()
        response_line = child.stdout.readline()
        if not response_line:
            print(json.dumps({"ok": False, "error": "adapter: child exited"}), flush=True)
            continue
        if request.get("op") == "hello":
            print(response_line.rstrip("\n"), flush=True)
            continue
        try:
            response = json.loads(response_line)
        except json.JSONDecodeError:
            print(response_line.rstrip("\n"), flush=True)
            continue
        print(json.dumps(mutate_response(response), ensure_ascii=False, separators=(",", ":")), flush=True)
    child.terminate()
    return 0


def mutate_response(response: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(response))
    if out.get("ok") is True and isinstance(out.get("result"), dict):
        out["result"] = mutate_value(out["result"])
    if out.get("ok") is False and isinstance(out.get("error"), str) and out["error"].startswith("acif."):
        out["error"] = out["error"] + ".mutated"
    if isinstance(out.get("diagnostics"), list):
        out["diagnostics"] = mutate_value(out["diagnostics"])
    return out


def mutate_value(value: Any, key: str | None = None) -> Any:
    if isinstance(value, dict):
        return {k: mutate_value(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [mutate_value(v, key) for v in value]
    if isinstance(value, bool):
        return not value
    if isinstance(value, str):
        if key and "hash" in key and HEX_RE.match(value):
            return flip_hex(value)
        if key in {"id", "error"} and value.startswith("acif."):
            return value + ".mutated"
    return value


def flip_hex(value: str) -> str:
    first = "1" if value[0] != "1" else "0"
    return first + value[1:]


if __name__ == "__main__":
    raise SystemExit(main())
