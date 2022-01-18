from typing import List


class Path:
    __slots__ = ["_string"]

    def __init__(self, string: str = ""):
        self._string = string

    def __str__(self):
        return self._string

    def __hash__(self) -> int:
        return hash(self._string)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._string == other._string

    def __repr__(self):
        return f"Path('{self}')"

    def __bool__(self) -> bool:
        return bool(self._string)

    @property
    def string(self) -> str:
        return self._string

    @property
    def is_absolute(self) -> bool:
        return self._string.startswith("/")

    @property
    def segments(self) -> List[str]:
        split = self._string.rstrip("/").split("/")
        if self.is_absolute or not self:
            return split[1:]
        return split
