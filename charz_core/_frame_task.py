from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias, Callable

if TYPE_CHECKING:
    from ._scene import Scene

Priority: TypeAlias = int
FrameTask: TypeAlias = Callable[["Scene"], None]


class FrameTaskManager(dict[Priority, FrameTask]):
    def __setitem__(self, key: int, value: Callable[[Scene], None]) -> None:
        super().__setitem__(key, value)
        # a higher priority means the callable will be called earlier
        sorted_items = sorted(self.items(), reverse=True)
        self.clear()
        self.update(sorted_items)
