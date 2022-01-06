=====
Usage
=====

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
