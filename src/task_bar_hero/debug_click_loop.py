"""Debug left-click burst loop for Task Bar Hero chest buttons."""

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
    ClickTarget(name="normal_chest_double", x=812, y=942),
    ClickTarget(name="boss_chest_double", x=781, y=944),
    ClickTarget(name="single_chest", x=777, y=943),
)


class DebugRightClickLoop:
    def __init__(
        self,
        interval_seconds: float = 10.0,
        startup_delay_seconds: float = 3.0,
        click_delay_seconds: float = 0.5,
        clicks_per_target: int = 5,
    ) -> None:
        self.interval_seconds = interval_seconds
        self.startup_delay_seconds = startup_delay_seconds
        self.click_delay_seconds = click_delay_seconds
        self.clicks_per_target = clicks_per_target
        self.controller = mouse.Controller()

    def run(self) -> int:
        print("デバッグ左クリック連打ループを開始します。")
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
                    self._click_target_burst(target)

                print(
                    f"次の実行まで {self.interval_seconds:.1f} 秒待機します。"
                    " 停止は Ctrl+C です。"
                )
                time.sleep(self.interval_seconds)
        except KeyboardInterrupt:
            print("Ctrl+C を受け取ったため、左クリック連打ループを終了します。")
            return 0

    def _click_target_burst(self, target: ClickTarget) -> None:
        for click_index in range(1, self.clicks_per_target + 1):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(
                f"[{timestamp}] target={target.name} x={target.x} y={target.y}"
                f" action=left_click click_index={click_index}/{self.clicks_per_target}"
            )
            self.controller.position = (target.x, target.y)
            self.controller.click(mouse.Button.left, 1)
            if click_index < self.clicks_per_target:
                time.sleep(self.click_delay_seconds)


def run_debug_right_click_loop(
    interval_seconds: float = 10.0,
    startup_delay_seconds: float = 3.0,
    click_delay_seconds: float = 0.5,
    clicks_per_target: int = 5,
) -> int:
    loop = DebugRightClickLoop(
        interval_seconds=interval_seconds,
        startup_delay_seconds=startup_delay_seconds,
        click_delay_seconds=click_delay_seconds,
        clicks_per_target=clicks_per_target,
    )
    return loop.run()
