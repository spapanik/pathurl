import pytest

from pathurl.query import Query


@pytest.mark.parametrize("string", ["", "x=1", "x=1&x=2", "x=1&x=2&y=2"])
def test_str(string):
    query = Query(string)
    assert query.string == string


@pytest.mark.parametrize("string", ["", "x=1", "x=1&x=2", "x=1&x=2&y=2"])
def test_eq(string):
    query_1 = Query(string)
    query_2 = Query(string)
    assert query_1 == query_2


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", False),
        ("x=1", True),
        ("x=1&x=2", True),
        ("x=1&x=2&y=2", True),
    ],
)
def test_bool(string, expected):
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
def test_data(string, expected):
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
def test_get(string, key, expected):
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
def test_set(string, kwargs, expected):
    query = Query(string)
    assert query.set(**kwargs).string == expected


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
def test_replace(string, kwargs, expected):
    query = Query(string)
    assert query.replace(**kwargs).string == expected


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
def test_remove(string, key, expected):
    query = Query(string)
    assert query.remove(key).string == expected
