# Dot4Dict

Access dictionary keys with a Dot:

```python
from dot4dict import dotdict

my_dict = dotdict({"foo": "bar"})
assert my_dict.foo == "bar"
assert my_dict["foo"] == "bar"
```

This works also recursively

```python
from dot4dict import dotdict

my_dict = dotdict({"a": {"b": {"c": "foo"}}})

assert my_dict.a.b.c == "foo"
```