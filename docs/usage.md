# Usage

The `query` module contains only the `Query` class:

```python
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
```

The `path` module contains only the `Path` class:

```python
>>> from pathurl import Path
# Create a path
>>> path = Path("/questions/1234")
# Create a path string
>>> path.string
'/questions/1234'
# Check if it is an absolute path
>>> path.is_absolute
True
# Get the path segments
>>> path.segments
['questions', '1234']
```

The `url` module contains only the `URL` class:

```python
>>> from pathurl import URL
# Create a URL
>>> url = URL("https://example.com/questions/")
# Get the string
>>> url.string
'https://example.com/questions/'
# Get the port
>>> url.port
443
# Join with a relative path
>>> url.join("1234")
URL('https://example.com/questions/1234')
# Replace parts of the URL
>>> url.replace(port=8000, fragment="last")
URL('https://example.com:8000/questions/#last')
```
