# URL class

The `URL` class can be used to manipulate URLs.

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

# Use multiple segments in a join (1)
>>> url.join("12/", "34")
URL('https://example.com/questions/12/34')

# Replace parts of the URL
>>> url.replace(port=8000, fragment="last")
URL('https://example.com:8000/questions/#last')

```

1.  Multiple segments are joined according to [RFC-3986]

[RFC-3986]: https://datatracker.ietf.org/doc/html/rfc3986.html#section-5.4
