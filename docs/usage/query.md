# Query class

The `query` part of a `URL` object can be manipulated with the `Query` class:

```python
>>> from pathurl import Query

# Create a query
>>> query = Query("x=1&x=2&y=2")

# Get the string
>>> query.string
'x=1&x=2&y=2'

# Get the data dictionary (1)
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
```

1.  Notice that `query.data` is always of type `dict[str, list[str] | None]`.

!!! warning "Blank values"

    Query strings are parsed using `parse_qs(string, keep_blank_values=True)`,
    therefore the query strings `x=1&y` and `x=1&y=` are equal, but different
    to `x=1`.
