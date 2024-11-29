# 1. compose:
# Write a function that constructs a composition of two given functions.

# >>> f = compose(lambda x: x ** 2, lambda x: x + 1)
# >>> f(42)
# 1849

from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


def compose(f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:
    """
    Constructs a composition of two given functions.
    """
