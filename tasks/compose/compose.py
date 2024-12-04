from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


def compose(f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:
    """
    Constructs a composition of two given functions.
    The resulting function applies g first, then f.

    Args:
        f: A function that takes an argument of type U and returns a value of type V.
        g: A function that takes an argument of type T and returns a value of type U.

    Returns:
        A new function that represents the composition of f and g.
    """
    return lambda x: f(g(x))
