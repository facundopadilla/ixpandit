from typing import Any, List, Optional


class SearchListInMemory:
    _elements = []

    def __init__(self, max_size: Optional[int] = None):
        self.max_size = max_size

    def put(self, element: Any) -> None:
        self._elements.insert(0, element)
        if self.max_size:
            self._elements = self._elements[: self.max_size]

    def elements(self) -> List[Any]:
        return self._elements if not self.max_size else self._elements[: self.max_size]
