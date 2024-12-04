from typing import Any, Callable


def const(value: Any) -> Callable[..., Any]:
    """
    Returns a constant function that always returns the given value,
    regardless of any arguments passed to it.

    Args:
        value: The value that the constant function should always return.

    Returns:
        A function that takes any arguments and always returns the given value.
    """
    return lambda *args, **kwargs: value
