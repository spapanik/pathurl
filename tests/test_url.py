import pytest

from pathurl.url import URL


@pytest.mark.parametrize(
    ["string"],
    [
        [""],
        ["https://www.example.com/path?key=value#fragment"],
        ["https://www.example.com/path?key=value"],
        ["http://www.example.com"],
        ["https://www.example.com/"],
        ["http://www.example.com:8000/"],
        ["https://user:pass@www.example.com/"],
        ["http://user:pass@www.example.com:8000/"],
        ["//www.example.com/path?key=value"],
    ]
)
def test_str(string):
    url = URL(string)
    assert url.string == string


@pytest.mark.parametrize(
    ["string"],
    [
        [""],
        ["https://www.example.com/path?key=value#fragment"],
        ["https://www.example.com/path?key=value"],
        ["http://www.example.com"],
        ["https://www.example.com/"],
        ["http://www.example.com:8000/"],
        ["https://user:pass@www.example.com/"],
        ["http://user:pass@www.example.com:8000/"],
        ["//www.example.com/path?key=value"],
    ]
)
def test_eq(string):
    url_1 = URL(string)
    url_2 = URL(string)
    assert url_1 == url_2


@pytest.mark.parametrize(
    ["string", "expected"],
    [
        ["", False],
        ["https://www.example.com/path?key=value#fragment", True],
        ["https://www.example.com/path?key=value", True],
        ["http://www.example.com", True],
        ["https://www.example.com/", True],
        ["http://www.example.com:8000/", True],
        ["https://user:pass@www.example.com/", True],
        ["http://user:pass@www.example.com:8000/", True],
        ["//www.example.com/path?key=value", True],
    ]
)
def test_bool(string, expected):
    url = URL(string)
    assert bool(url) is expected
