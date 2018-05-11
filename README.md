# assert_types: the python decorator you never knew you needed
`Python decorator to assert types hints for python functions

Add this as a decorator in front of any python function and it will add assertions to the type hints

## Install

`pip install assert_types`

## Use it

```
from assert_types import assert_types

@assert_types
def some_function(a: int, b, c: float, d: str) -> float:
    return float(a)
```

It will add an assertion for each input that is specified, skip over non-specified inputs (e.g. b above) and check the output type if provided.

## Todo

Nested types (e.g. List[str])
Unions (e.g. Union[str, float])

any other issues, please put them in the issues and I'll fix them as soon as possible.  Or better yet, make a PR!

