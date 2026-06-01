"""Mouse click position capture utility for Task Bar Hero setup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from pynput import keyboard, mouse


@dataclass(frozen=True)
class ClickPoint:
    x: int
    y: int
    button: str


class ClickRecorder:
    def __init__(self) -> None:
        self.points: List[ClickPoint] = []
        self._mouse_listener: mouse.Listener | None = None
        self._keyboard_listener: keyboard.Listener | None = None
        self._stopped = False

    def run(self) -> int:
        print("クリックした位置を記録します。")
        print("Task Bar Hero 上の位置をクリックしてください。")
        print("終了するには Esc キー、または Ctrl+C を押してください。")

        self._mouse_listener = mouse.Listener(on_click=self._on_click)
        self._keyboard_listener = keyboard.Listener(on_press=self._on_key_press)

        self._mouse_listener.start()
        self._keyboard_listener.start()

        self._keyboard_listener.join()
        self._mouse_listener.stop()
        self._mouse_listener.join()

        return len(self.points)

    def _on_click(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        if not pressed or self._stopped:
            return

        point = ClickPoint(x=x, y=y, button=str(button))
        self.points.append(point)
        print(f"[{len(self.points)}] x={point.x}, y={point.y}, button={point.button}")

    def _on_key_press(self, key: keyboard.Key | keyboard.KeyCode) -> bool | None:
        if key != keyboard.Key.esc:
            return None

        self._stopped = True
        print("記録を終了します。")
        return False


def run_click_probe() -> int:
    recorder = ClickRecorder()
    count = recorder.run()
    print(f"合計 {count} 件のクリックを記録しました。")
    return 0
