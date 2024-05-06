# Installation

# Using pip

[pip] is a package manager for Python.
You can use it to install `pathurl` and try it out:

```console
$ pip install pathurl
```

# Using poetry

[poetry] is a tool for managing Python project dependencies, and is the recommended way
to add `pathurl` to your project's dependencies. If you want to do so, you can do it
with the following command:

```console
$ poetry add pathurl
```

Or you can add `pathurl` to your `pyproject.toml` file:

```toml
[tool.poetry.dependencies]
pathurl = "^0.7"
```

## Python Version Requirement

Please note that `pathurl` requires Python 3.8 or higher. Please ensure
that you have such a version installed in your system. If not,
consider using a tool like [pyenv] to create a shell with the required Python version.

[pip]: https://pip.pypa.io/en/stable/
[poetry]: https://python-poetry.org/
[pyenv]: https://github.com/pyenv/pyenv
