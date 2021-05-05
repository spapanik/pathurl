from pathurl.query import Query


def test_query_string():
    query_string = "x=1"
    query = Query(query_string)
    assert str(query) == query_string
