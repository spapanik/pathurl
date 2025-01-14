from __future__ import annotations

import pytest

from pathurl.path import Path
from pathurl.query import Query
from pathurl.url import URL


@pytest.mark.parametrize(
    "string",
    [
        "",
        "https://www.example.com/path?key=value#fragment",
        "https://www.example.com/path?key=value",
        "http://www.example.com",
        "https://www.example.com/",
        "http://www.example.com:8000/",
        "https://user:pass@www.example.com/",
        "http://user:pass@www.example.com:8000/",
        "//www.example.com/path?key=value",
    ],
)
def test_str(string: str) -> None:
    url = URL(string)
    assert str(url) == string
    assert repr(url) == f"URL('{string}')"
    assert url.string == string


def test_hash() -> None:
    url = URL("https://example.com")
    same_url = URL("https://example.com")
    different_url = URL("https://www.example.com")
    assert hash(url) == hash(same_url)
    assert hash(url) != hash(different_url)


@pytest.mark.parametrize(
    ("username", "password", "port", "expected"),
    [
        (None, None, None, "https://www.example.com"),
        (None, None, 8000, "https://www.example.com:8000"),
        ("user", None, None, "https://user@www.example.com"),
        (None, "password", None, "https://:password@www.example.com"),
        ("username", "password", None, "https://username:password@www.example.com"),
    ],
)
def test_from_parts(
    username: str | None, password: str | None, port: int | None, expected: str
) -> None:
    url = URL.from_parts(
        scheme="https",
        username=username,
        password=password,
        hostname="www.example.com",
        port=port,
    )
    assert str(url) == expected


@pytest.mark.parametrize(
    "string",
    [
        "",
        "https://www.example.com/path?key=value#fragment",
        "https://www.example.com/path?key=value",
        "http://www.example.com",
        "https://www.example.com/",
        "http://www.example.com:8000/",
        "https://user:pass@www.example.com/",
        "http://user:pass@www.example.com:8000/",
        "//www.example.com/path?key=value",
    ],
)
def test_eq(string: str) -> None:
    url_1 = URL(string)
    url_2 = URL(string)
    assert url_1 == url_2


def test_eq_with_string() -> None:
    string = "https://www.example.com/"
    url = URL(string)
    assert url != string


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", False),
        ("https://www.example.com/path?key=value#fragment", True),
        ("https://www.example.com/path?key=value", True),
        ("http://www.example.com", True),
        ("https://www.example.com/", True),
        ("http://www.example.com:8000/", True),
        ("https://user:pass@www.example.com/", True),
        ("http://user:pass@www.example.com:8000/", True),
        ("//www.example.com/path?key=value", True),
    ],
)
def test_bool(string: str, expected: bool) -> None:
    url = URL(string)
    assert bool(url) is expected


def test_replace() -> None:
    url = URL("https://www.example.com/")
    expected = "https://www.example.com/?x=2#xyz"
    assert url.replace(query=Query("x=2"), fragment="xyz").string == expected


def test_join() -> None:
    url = URL("https://www.example.com/")
    paths = ("/path/", "subpath/", Path("third_level"))
    assert url.join(*paths).string == "https://www.example.com/path/subpath/third_level"


def test_parts() -> None:
    url = URL("http://user:pass@www.example.com:8000/path?key=value#fragment")
    assert url.netloc == "user:pass@www.example.com:8000"
    assert url.scheme == "http"
    assert url.username == "user"
    assert url.password == "pass"  # noqa: S105
    assert url.hostname == "www.example.com"
    assert url.port == 8000
    assert url.path == Path("/path")
    assert url.query == Query("key=value")
    assert url.fragment == "fragment"
