# 4. curry
# Write a function that takes a function `func` and
# returns a new function with some
# positional and keyword arguments fixed.
# These fixed arguments should be passed to
# `curry` alongside `func`.

# >>> def pow(x: int, p: int) -> int:
# ...     return x**p
# >>> ten_pow = curry(pow, 10)
# >>> ten_pow(3)
# 1000
# >>> square = curry(pow, p=2)
# >>> square(42)
# 1764

from typing import Callable, Any

def curry(
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any
) -> Callable[..., Any]:
    """
    Returns a new function with some arguments pre-applied.
    """
