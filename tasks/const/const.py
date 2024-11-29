# 2. const
# Create a function that, given a value, returns a constant function.
# This returned function should always return the initial value,
# regardless of its arguments.

# >>> f = const(42)
# >>> f()
# 42
# >>> f(range(4), range(2), foo="bar")
# 42

from typing import Any, Callable


def const(value: Any) -> Callable[..., Any]:
    """
    Returns a constant function.
    """
