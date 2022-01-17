import pytest

from pathurl.path import Path


@pytest.mark.parametrize(["string"], [[""], ["/"], ["/foo"], ["/foo/"], ["/foo/bar"]])
def test_str(string):
    path = Path(string)
    assert path.string == string


@pytest.mark.parametrize(["string"], [[""], ["/"], ["/foo"], ["/foo/"], ["/foo/bar"]])
def test_eq(string):
    path_1 = Path(string)
    path_2 = Path(string)
    assert path_1 == path_2


@pytest.mark.parametrize(
    ["string", "expected"],
    [
        ["", False],
        ["/", True],
        ["/foo", True],
        ["/foo/", True],
        ["/foo/bar", True],
    ]
)
def test_bool(string, expected):
    path = Path(string)
    assert bool(path) is expected


@pytest.mark.parametrize(
    ["string", "expected"],
    [
        ["", False],
        ["/", True],
        ["/foo", True],
        ["/foo/", True],
        ["/foo/bar", True],
        ["foo", False],
        ["foo/", False],
        ["foo/bar", False],
    ]
)
def test_is_absolute(string, expected):
    path = Path(string)
    assert path.is_absolute is expected


@pytest.mark.parametrize(
    ["string", "expected"],
    [
        ["", []],
        ["/", []],
        ["/foo", ["foo"]],
        ["/foo/", ["foo"]],
        ["/foo/bar", ["foo", "bar"]],
        ["foo", ["foo"]],
        ["foo/", ["foo"]],
        ["foo/bar", ["foo", "bar"]],
    ]
)
def test_segments(string, expected):
    path = Path(string)
    assert path.segments == expected
