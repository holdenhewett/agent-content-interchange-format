from __future__ import annotations

import argparse
import sys

from .report import human_report, write_report
from .run import RunOptions, run_conformance
from .scopes import SCOPE_ORDER


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "selftest":
        from .selftest import main as selftest_main

        return selftest_main(argv[1:])

    parser = argparse.ArgumentParser(prog="python -m runner")
    parser.add_argument("--adapter", required=True, help="adapter command to spawn")
    parser.add_argument("--scope", action="append", default=[], help="scope to run; may be repeated")
    parser.add_argument("--only", action="append", default=[], help="vector id to run; may be repeated")
    parser.add_argument("--report", help="write machine-readable report JSON")
    parser.add_argument("--keep-fixtures", action="store_true", help="keep materialized fixtures")
    args = parser.parse_args(argv)

    unknown_scopes = sorted(set(args.scope) - set(SCOPE_ORDER))
    if unknown_scopes:
        parser.error("unknown scope(s): " + ", ".join(unknown_scopes))

    try:
        report = run_conformance(
            RunOptions(
                adapter=args.adapter,
                scopes=args.scope,
                only=args.only,
                keep_fixtures=args.keep_fixtures,
            )
        )
    except ValueError as exc:
        parser.error(str(exc))
    if args.report:
        write_report(args.report, report)
    print(human_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
