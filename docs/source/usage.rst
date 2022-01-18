=====
Usage
=====

.. py:module:: pathurl.query

The ``query`` module contains only the ``Query`` class:

.. py:class:: Query

    A class representing a query string

    .. py:method:: __init__(_string: str)

        Initialise the URL from a string.

    .. py:property:: string
        :type: str

        Get the query string

    .. py:property:: data
        :type: Dict[str, List[str]]

        Get the query as a dictionary

    .. py:method:: get(key: str) -> List[str]

        Get the value of a single key from the query string. Return None if the key isn't present.

    .. py:method:: add(**kwargs: qs_value) -> Query

        Append to the values of each keyword argument the new value.

        If the new value is a list, it extends the old list.

    .. py:method:: set(**kwargs: qs_value) -> Query

        Set the values of each keyword argument

    .. py:method:: replace(**kwargs: Tuple[str, str]) -> Query

        For every keyword argument, replace the first value with the second

    .. py:method:: remove(key: str) -> Query

        Drop the key from the query string. Raise a KeyError if missing.

Worked example:

.. code-block:: python

    >>> from pathurl import Query
    # Create a query
    >>> query = Query("x=1&x=2&y=2")
    # Get the string
    >>> query.string
    'x=1&x=2&y=2'
    # Get the data dictionary
    >>> query.data
    {'x': ['1', '2'], 'y': ['2']}
    # Get the value of "x"
    >>> query.get("x")
    ['1', '2']
    # Get the value of "z" (it's None)
    >>> query.get("z")
    # Append to "x"
    >>> query.add(x="1")
    Query('x=1&x=2&x=1&y=2')
    # Append to "z"
    >>> query.add(z="1")
    Query('x=1&x=2&y=2&z=1')
    # Set "x" to be equal to ["s"]
    >>> query.set(x="s")
    Query('x=s&y=2')
    # Set "z" to be equal to ["s"]
    >>> query.set(z="s")
    Query('x=1&x=2&y=2&z=s')
    # Replace the value of "z" when it's "1" with "2"
    >>> query.replace(z=("1", "2"))
    Query('x=1&x=2&y=2')
    # Replace the value of "x" when it's "1"
    >>> query.replace(x=("1", "s"))
    Query('x=s&x=2&y=2')
    >>> query.remove("x")
    Query('y=2')
    >>> query.remove("z")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/stephanos/programming/personal/libs/pathurl/src/pathurl/query.py", line 81, in remove
        del data[key]
    KeyError: 'z'

    'z'

.. py:module:: pathurl.url

The ``url`` module contains only the ``URL`` class:

.. py:class:: URL

    A generic class representing a URL

    After it's initialised, it will try to guess the port, and create two objects: ``path`` and ``query``.

    .. py:method:: __init__( \
            *, \
            scheme: str = "", \
            username: str = None, \
            password: str = None, \
            hostname: str = None, \
            port: int = None, \
            path: str = "", \
            query: str = "", \
            fragment: str = "", \
        )

        Initialise the URL by its parts.

    .. py:method:: from_string(url: str) -> URL

        Initialise the URL as a string. It accepts strings that have no scheme, but they start with ``//``.
