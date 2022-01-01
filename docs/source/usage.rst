=====
Usage
=====

.. py:module:: pathurl.url

The ``url`` module contains only the ``URL`` class:

.. py:class:: URL

   A generic class representing a URL

   :param str name: The name of the variable
   :param bool allow_env: Whether the environment variable can be used to get the value
   :param Path base_dir: The base directory of the project
   :param Path filename: The config file's filename
   :param Iterable sections: The section that the value is defined in the config file
   :param type rtype: The type of the return value
   :param default: The default value to be returned
   :return: the value defined in one of the files or the default

    .. py:method:: __init__( \
            scheme: str = "", \
            username: str = None, \
            password: str = None, \
            hostname: str = None, \
            port: int = None, \
            path: str = "", \
            params: str = "", \
            query: str = "", \
            fragment: str = "", \
        )

        :param str scheme: The URL's scheme
        :param str username: The URL's username
        :param str password: The URL's password
        :param str hostname: The URL's hostname
        :param int port: The URL's port
        :param str path: The URL's path
        :param str params: The URL's params
        :param str query: The URL's query as a string
        :param str fragment: The URL's fragment

        Initialise the URL by its parts
