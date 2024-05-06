# Path class

The `path` part of a `URL` object can be manipulated with the `Path` class:

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
