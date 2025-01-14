from __future__ import annotations

import pytest

from pathurl.query import Query


@pytest.mark.parametrize("string", ["", "x=1", "x=1&x=2", "x=1&x=2&y=2"])
def test_str(string: str) -> None:
    query = Query(string)
    assert str(query) == string
    assert repr(query) == f"Query('{string}')"
    assert query.string == string


def test_str_from_dict() -> None:
    query = Query.from_dict({"x": "1", "y": ["2", "3"]})
    assert query.string == "x=1&y=2&y=3"


def test_hash() -> None:
    query = Query("x=1")
    same_query = Query("x=1")
    different_query = Query("x=1&x=2")
    assert hash(query) == hash(same_query)
    assert hash(query) != hash(different_query)


@pytest.mark.parametrize("string", ["", "x=1", "x=1&x=2", "x=1&x=2&y=2"])
def test_eq(string: str) -> None:
    query_1 = Query(string)
    query_2 = Query(string)
    assert query_1 == query_2


def test_eq_with_string() -> None:
    query = Query("x=1")
    assert query != "x=1"


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", False),
        ("x=1", True),
        ("x=1&x=2", True),
        ("x=1&x=2&y=2", True),
    ],
)
def test_bool(string: str, expected: bool) -> None:
    query = Query(string)
    assert bool(query) is expected


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", {}),
        ("x=1", {"x": ["1"]}),
        ("x=1&x=2", {"x": ["1", "2"]}),
        ("x=1&x=2&y=2", {"x": ["1", "2"], "y": ["2"]}),
    ],
)
def test_data(string: str, expected: dict[str, list[str]]) -> None:
    query = Query(string)
    assert query.data == expected


@pytest.mark.parametrize(
    ("string", "key", "expected"),
    [
        ("", "x", None),
        (")=1", ")", ["1"]),
        ("x=1", "x", ["1"]),
        ("x=1&x=2", "x", ["1", "2"]),
        ("x=1&x=2", "y", None),
        ("x=1&x=2&y=2", "x", ["1", "2"]),
        ("x=1&x=2&y=2", "y", ["2"]),
    ],
)
def test_get(string: str, key: str, expected: list[str] | None) -> None:
    query = Query(string)
    assert query.get(key) == expected


@pytest.mark.parametrize(
    ("string", "kwargs", "expected"),
    [
        ("", {}, ""),
        ("", {"x": "1"}, "x=1"),
        ("", {"x": ["1", "2"]}, "x=1&x=2"),
        ("x=1", {}, "x=1"),
        ("x=1", {"x": "1"}, "x=1"),
        ("x=1", {"x": ["1", "2"]}, "x=1&x=2"),
        ("x=1&x=2", {}, "x=1&x=2"),
        ("x=1&x=2", {"x": "1"}, "x=1"),
        ("x=1&x=2", {"x": ["1", "2"]}, "x=1&x=2"),
        ("x=1&x=2&y=2", {}, "x=1&x=2&y=2"),
        ("x=1&x=2&y=2", {"x": "1"}, "x=1&y=2"),
    ],
)
def test_set(string: str, kwargs: dict[str, str], expected: str) -> None:
    query = Query(string)
    assert query.set(**kwargs).string == expected  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("string", "kwargs", "expected"),
    [
        ("", {}, ""),
        ("", {"x": "1"}, "x=1"),
        ("", {"x": ["1", "2"]}, "x=1&x=2"),
        ("x=1", {}, "x=1"),
        ("x=1", {"x": "1"}, "x=1&x=1"),
        ("x=1", {"y": ["1", "2"]}, "x=1&y=1&y=2"),
        ("x=1&x=2", {}, "x=1&x=2"),
    ],
)
def test_add(string: str, kwargs: dict[str, str], expected: str) -> None:
    query = Query(string)
    assert query.add(**kwargs).string == expected  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("string", "kwargs", "expected"),
    [
        ("", {}, ""),
        ("", {"x": ("1", "2")}, ""),
        ("x=1", {}, "x=1"),
        ("x=1", {"x": ("1", "2")}, "x=2"),
        ("x=1", {"x": ("2", "2")}, "x=1"),
        ("x=1&x=2", {}, "x=1&x=2"),
        ("x=1&x=2", {"x": ("1", "2")}, "x=2&x=2"),
        ("x=1&x=2", {"x": ("2", "2")}, "x=1&x=2"),
        ("x=1&x=2&y=2", {"x": ("2", "3")}, "x=1&x=3&y=2"),
        ("x=1&x=2&y=2", {"y": ("2", "3")}, "x=1&x=2&y=3"),
    ],
)
def test_replace(
    string: str, kwargs: dict[str, tuple[str, str]], expected: str
) -> None:
    query = Query(string)
    assert query.replace(**kwargs).string == expected  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("string", "key", "expected"),
    [
        (")=1", ")", ""),
        ("x=1", "x", ""),
        ("x=1&x=2", "x", ""),
        ("x=1&x=2&y=2", "x", "y=2"),
        ("x=1&x=2&y=2", "y", "x=1&x=2"),
    ],
)
def test_remove(string: str, key: str, expected: str) -> None:
    query = Query(string)
    assert query.remove(key).string == expected
