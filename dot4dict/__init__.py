from typing import Any, Iterable

__version__ = "0.1.1"


class dotdict(dict):
    """Simple dotdict implementation

    Allow access to dictionary keys via getitem and getattr

    Examples
    --------

    >>> my_dict = dotdict({"name": "John Doe"})
    >>> my_dict.name

    """

    __getattr__ = dict.get
    __delattr__ = dict.__delitem__

    def __init__(self, seq: dict = None):
        """Create a dotdict"""
        if seq is not None:
            for name, value in seq.items():
                self.__setattr__(name, value)

    def __setattr__(self, name: str, value: Any) -> None:
        """Convert dict to dotdict via dict.key"""
        if isinstance(value, dict):
            self[name] = dotdict(value)
        else:
            self[name] = value

    def __setitem__(self, key, value: Any) -> None:
        """Convert dict to dotdict via dict[key]"""
        if isinstance(value, dict):
            super().__setitem__(key, dotdict(value))
        else:
            super().__setitem__(key, value)

    def __dir__(self) -> Iterable[str]:
        """Only allow str values and ignore other dict keys"""
        return [x for x in self.keys() if isinstance(x, str)]
