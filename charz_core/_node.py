from __future__ import annotations

from itertools import count
from typing import Any, ClassVar

from typing_extensions import Self

from ._grouping import Group, group
from ._scene import Scene
from ._annotations import NodeID


class NodeMixinSorter(type):
    """Node metaclass for initializing `Node` subclass after other `mixin` classes"""

    def __new__(
        cls,
        name: str,
        bases: tuple[type, ...],
        attrs: dict[str, object],
    ) -> type:
        def sorter(base: type) -> bool:
            # Ensures `Node` will be last in MRO (except for `object`),
            # to help `__new__` chain for nodes (instances of `Node`/`Node` subclass)
            # work despite wrong order in subclass declaration
            return issubclass(base, Node)

        sorted_bases = tuple(sorted(bases, key=sorter))
        new_type = super().__new__(cls, name, sorted_bases, attrs)
        return new_type


@group(Group.NODE)
class Node(metaclass=NodeMixinSorter):
    _uid_counter: ClassVar[count[NodeID]] = count(0, 1)

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Self:
        # NOTE: Additional args and kwargs are ignored!
        instance = super().__new__(cls)
        instance.uid = next(Node._uid_counter)
        return instance

    uid: NodeID  # Is set in `Node.__new__`
    parent: Node | None = None

    def __init__(self, parent: Node | None = None) -> None:
        if parent is not None:
            self.parent = parent

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(#{self.uid})"

    def with_parent(self, parent: Node | None, /) -> Self:
        self.parent = parent
        return self

    def update(self) -> None:
        """Called each frame"""

    def queue_free(self) -> None:
        if self not in Scene.current._queued_nodes:
            Scene.current._queued_nodes.append(self)

    def _free(self) -> None: ...  # Overridden by using `@group`
