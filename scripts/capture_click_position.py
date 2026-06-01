"""CLI entrypoint for capturing click positions on Windows."""

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
        description="Capture mouse click coordinates for Task Bar Hero targets."
    )
    return parser.parse_args()


def main() -> int:
    parse_args()
    _bootstrap_import_path()

    from task_bar_hero.click_probe import run_click_probe

    return run_click_probe()


if __name__ == "__main__":
    raise SystemExit(main())
