"""CLI entrypoint for the Task Bar Hero debug right-click loop."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _bootstrap_import_path() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Right-click the normal and boss chest positions on a loop."
    )
    parser.add_argument(
        "--interval-seconds",
        type=float,
        default=10.0,
        help="Seconds to wait between right-click cycles. Default: 10",
    )
    parser.add_argument(
        "--startup-delay-seconds",
        type=float,
        default=3.0,
        help="Seconds to wait before the first click cycle. Default: 3",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    _bootstrap_import_path()

    from task_bar_hero.debug_click_loop import run_debug_right_click_loop

    return run_debug_right_click_loop(
        interval_seconds=args.interval_seconds,
        startup_delay_seconds=args.startup_delay_seconds,
    )


if __name__ == "__main__":
    raise SystemExit(main())
