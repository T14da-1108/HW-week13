from typing import Callable, Any


def flip(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Returns a new function that applies `func` to its positional arguments
    in reverse order. Keyword arguments remain unchanged.

    Args:
        func: The function to flip the order of positional arguments for.

    Returns:
        A new function with reversed positional arguments.
    """

    def flipped(*args: Any, **kwargs: Any) -> Any:
        return func(*reversed(args), **kwargs)

    return flipped
