"""Debug right-click loop for Task Bar Hero chest buttons."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import time

from pynput import mouse


@dataclass(frozen=True)
class ClickTarget:
    name: str
    x: int
    y: int


DEFAULT_TARGETS = (
    ClickTarget(name="normal_chest", x=812, y=942),
    ClickTarget(name="boss_chest", x=781, y=944),
)


class DebugRightClickLoop:
    def __init__(
        self,
        interval_seconds: float = 10.0,
        startup_delay_seconds: float = 3.0,
    ) -> None:
        self.interval_seconds = interval_seconds
        self.startup_delay_seconds = startup_delay_seconds
        self.controller = mouse.Controller()

    def run(self) -> int:
        print("デバッグ右クリックループを開始します。")
        print(
            f"開始まで {self.startup_delay_seconds:.1f} 秒待機します。"
            " Task Bar Hero の画面に戻ってください。"
        )
        time.sleep(self.startup_delay_seconds)

        cycle_count = 0
        try:
            while True:
                cycle_count += 1
                print(f"--- cycle {cycle_count} ---")
                for target in DEFAULT_TARGETS:
                    self._right_click_target(target)

                print(
                    f"次の実行まで {self.interval_seconds:.1f} 秒待機します。"
                    " 停止は Ctrl+C です。"
                )
                time.sleep(self.interval_seconds)
        except KeyboardInterrupt:
            print("Ctrl+C を受け取ったため、右クリックループを終了します。")
            return 0

    def _right_click_target(self, target: ClickTarget) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"[{timestamp}] target={target.name} x={target.x} y={target.y}"
            " action=right_click"
        )
        self.controller.position = (target.x, target.y)
        self.controller.click(mouse.Button.right, 1)


def run_debug_right_click_loop(
    interval_seconds: float = 10.0,
    startup_delay_seconds: float = 3.0,
) -> int:
    loop = DebugRightClickLoop(
        interval_seconds=interval_seconds,
        startup_delay_seconds=startup_delay_seconds,
    )
    return loop.run()
