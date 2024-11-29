# 3. flip:
# Implement a function that takes a function `func` and returns a new function.
# This new function should apply `func`
# to its positional arguments in reverse order.
# Keyword arguments should be passed unchanged.

# >>> f = flip(map)
# >>> list(f(range(5), range(0, 10, 2), lambda x, y: x**y))
# [1, 2, 16, 216, 4096]
# >>> list(map(lambda x, y: x**y, range(0, 10, 2), range(5)))
# [1, 2, 16, 216, 4096]

from typing import Callable, Any


def flip(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Returns a new function with reversed positional arguments.
    """
