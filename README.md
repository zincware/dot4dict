[![Coverage Status](https://coveralls.io/repos/github/zincware/dot4dict/badge.svg?branch=main)](https://coveralls.io/github/zincware/dot4dict?branch=main)
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
