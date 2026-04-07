from __future__ import annotations

class Node:
    def __init__(self, data, parent: Node | None = None):
        self.data = data
        self.color = "red" #red
        self.parent: Node | None = parent
        self.l_child: Node | None = None
        self.r_child: Node | None = None