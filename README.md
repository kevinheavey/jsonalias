# jsontype

A microlibrary that defines a `Json` type alias for Python.

## This README is longer than the library

Seriously, this is all the code:

```python
from typing import Dict, List, Union

Json = Union[Dict[str, "Json"], List["Json"], str, int, float, bool, None]
```

If we only supported Python >= 3.10, it would fit on one line:

```python
Json = dict[str, 'Json'] | list['Json'] | str | int | float | bool | None
```

## Then why make a library out of it?

I want to use this type alias in multiple projects and it's
just about long enough to be annoying.

This alias should probably get added to the Python `typing` module.
If it does and I haven't put a big notice on this README,
please open a PR.

## Example

```python
from jsontype import Json

d: Json = {"foo": ["bar", {"x": "y"}]}
```

## It's not working please help???

Make sure you're using mypy >= 0.981 and running with the
`--enable-recursive-aliases` flag.

## Special Thanks

GitHub user wbolster for [this comment](https://github.com/python/typing/issues/182#issuecomment-1259412066)
notifying us that mypy could now do JSON.
