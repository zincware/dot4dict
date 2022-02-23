[![Coverage Status](https://coveralls.io/repos/github/zincware/dot4dict/badge.svg?branch=main)](https://coveralls.io/github/zincware/dot4dict?branch=main)
[![PyPI version](https://badge.fury.io/py/dot4dict.svg)](https://badge.fury.io/py/dot4dict)
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

Copyright
=========

This project is distributed under the [Apache license version 2.0](https://github.com/zincware/dot4dict/blob/main/LICENSE).