import pytest

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
    assert url.string == string


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
