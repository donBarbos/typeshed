from typing import Any

from .node import Node

def prepare(obj: Node, topnode: bool = ...) -> list[dict[str, Any]]: ...
def dumpJSON(obj: Node) -> str: ...
def dumpAST(obj: Node, ind: int = ..., topnode: bool = ...) -> None: ...
