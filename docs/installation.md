# Installation

# Using uv

[uv] is an extremely fast Python package installer.
You can use it to install `pathurl` and try it out:

```console
$ uv pip install pathurl
```

# Using a PEP 621 compliant build backend

[PEP 621] is the standard way to store your dependencies in a `pyproject.toml` file.
You can add `pathurl` to your `pyproject.toml` file:

```toml
[project]
dependencies = [
    "pathurl~=0.7",
    ....
]
```

## Python Version Requirement

Please note that `pathurl` requires Python 3.10 or higher. If you're not using uv,
please ensure that you have such a version installed in your system.

[uv]: https://github.com/astral-sh/uv
[PEP 621]: https://peps.python.org/pep-0621/
