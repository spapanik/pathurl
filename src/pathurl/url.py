from __future__ import annotations

from typing import TypeVar, Union
from urllib.parse import urljoin, urlsplit, urlunsplit

from pathurl._constants import Port
from pathurl.path import Path
from pathurl.query import Query

_T = TypeVar("_T", bound=Union[int, str, None, Path, Query])


class URL:
    __slots__ = (
        "_fragment",
        "_hostname",
        "_netloc",
        "_password",
        "_path",
        "_port",
        "_query",
        "_scheme",
        "_string",
        "_username",
    )

    def __init__(self, string: str = "") -> None:
        parsed_url = urlsplit(string)
        self._string = string
        self._netloc = parsed_url.netloc
        self._scheme = parsed_url.scheme
        self._username = parsed_url.username
        self._hostname = parsed_url.hostname or ""
        self._password = parsed_url.password
        self._port = parsed_url.port or self._infer_port(self._scheme)
        self._path = Path(parsed_url.path)
        self._query = Query(parsed_url.query)
        self._fragment = parsed_url.fragment

    @classmethod
    def from_parts(
        cls,
        scheme: str,
        username: str | None = None,
        password: str | None = None,
        hostname: str = "",
        port: int | None = None,
        path: str | Path = "",
        query: str | Query = "",
        fragment: str = "",
    ) -> URL:
        netloc = cls._create_netloc(scheme, username, password, hostname, port)
        return cls(urlunsplit((scheme, netloc, str(path), str(query), fragment)))

    def __str__(self) -> str:
        return self._string

    def __hash__(self) -> int:
        return hash(self._string)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._string == other._string

    def __repr__(self) -> str:
        return f"URL('{self}')"

    def __bool__(self) -> bool:
        return bool(self._string)

    @property
    def string(self) -> str:
        return self._string

    @property
    def netloc(self) -> str:
        return self._netloc

    @property
    def scheme(self) -> str:
        return self._scheme

    @property
    def username(self) -> str | None:
        return self._username

    @property
    def hostname(self) -> str:
        return self._hostname

    @property
    def password(self) -> str | None:
        return self._password

    @property
    def port(self) -> int | None:
        return self._port

    @property
    def path(self) -> Path:
        return self._path

    @property
    def query(self) -> Query:
        return self._query

    @property
    def fragment(self) -> str:
        return self._fragment

    @staticmethod
    def _infer_port(scheme: str) -> int | None:
        try:
            port = Port[scheme]
        except KeyError:
            return None

        return port.value

    @classmethod
    def _create_netloc(
        cls,
        scheme: str,
        username: str | None,
        password: str | None,
        hostname: str,
        port: int | None,
    ) -> str:
        parts = []
        if username or password:
            if username:
                parts.append(username)
            if password:
                parts.append(f":{password}")
            parts.append("@")
        parts.append(hostname)
        if port and port != cls._infer_port(scheme):
            parts.append(f":{port}")
        return "".join(parts)

    def replace(self, **kwargs: _T) -> URL:
        scheme: str = kwargs.get("scheme", self.scheme)  # type: ignore[assignment]
        username: str | None = kwargs.get("username", self.username)  # type: ignore[assignment]
        password: str | None = kwargs.get("password", self.password)  # type: ignore[assignment]
        hostname: str = kwargs.get("hostname", self.hostname)  # type: ignore[assignment]
        port: int | None = kwargs.get("port", self.port)  # type: ignore[assignment]
        path: str | Path = kwargs.get("path", self.path)  # type: ignore[assignment]
        query: str | Query = kwargs.get("query", self.query)  # type: ignore[assignment]
        fragment: str = kwargs.get("fragment", self.fragment)  # type: ignore[assignment]
        return self.from_parts(
            scheme=scheme,
            username=username,
            password=password,
            hostname=hostname,
            port=port,
            path=path,
            query=query,
            fragment=fragment,
        )

    def join(self, *paths: str | Path) -> URL:
        result = str(self)
        for path in paths:
            result = urljoin(result, str(path))

        return self.__class__(result)
