from __future__ import annotations

import pytest

from pathurl.path import Path


@pytest.mark.parametrize("string", ["", "/", "/foo", "/foo/", "/foo/bar"])
def test_str(string: str) -> None:
    path = Path(string)
    assert str(path) == string
    assert repr(path) == f"Path('{string}')"
    assert path.string == string


def test_hash() -> None:
    path = Path("path")
    same_path = Path("path")
    different_path = Path("another/path")
    assert hash(path) == hash(same_path)
    assert hash(path) != hash(different_path)


@pytest.mark.parametrize(
    ("is_absolute", "is_dir", "expected"),
    [
        (True, True, "/path/sub/"),
        (True, False, "/path/sub"),
        (False, True, "path/sub/"),
        (False, False, "path/sub"),
    ],
)
def test_path_from_segments(is_absolute: bool, is_dir: bool, expected: str) -> None:
    path = Path.from_segments("path", "sub", is_absolute=is_absolute, is_dir=is_dir)
    assert path.string == expected


@pytest.mark.parametrize("string", ["", "/", "/foo", "/foo/", "/foo/bar"])
def test_eq(string: str) -> None:
    path_1 = Path(string)
    path_2 = Path(string)
    assert path_1 == path_2


def test_eq_with_string() -> None:
    path = Path("/foo")
    assert path != "/foo"


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", False),
        ("/", True),
        ("/foo", True),
        ("/foo/", True),
        ("/foo/bar", True),
    ],
)
def test_bool(string: str, expected: bool) -> None:
    path = Path(string)
    assert bool(path) is expected


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", False),
        ("/", True),
        ("/foo", True),
        ("/foo/", True),
        ("/foo/bar", True),
        ("foo", False),
        ("foo/", False),
        ("foo/bar", False),
    ],
)
def test_is_absolute(string: str, expected: bool) -> None:
    path = Path(string)
    assert path.is_absolute is expected


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", []),
        ("/", []),
        ("/foo", ["foo"]),
        ("/foo/", ["foo"]),
        ("/foo/bar", ["foo", "bar"]),
        ("foo", ["foo"]),
        ("foo/", ["foo"]),
        ("foo/bar", ["foo", "bar"]),
    ],
)
def test_segments(string: str, expected: list[str]) -> None:
    path = Path(string)
    assert path.segments == expected
