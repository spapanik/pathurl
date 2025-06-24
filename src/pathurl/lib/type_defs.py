from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from pathurl.path import Path
    from pathurl.query import Query


class URLParts(TypedDict, total=False):
    scheme: str
    username: str | None
    password: str | None
    hostname: str
    port: int | None
    path: "str | Path"
    query: "str | Query"
    fragment: str
