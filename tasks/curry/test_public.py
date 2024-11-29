from .curry import curry


def test_curry_with_positional_args():
    def add(x, y):
        return x + y

    add_to_ten = curry(add, 10)
    assert add_to_ten(5) == 15
    assert add_to_ten(-10) == 0


def test_curry_with_keyword_args():
    def multiply(x, y=1):
        return x * y

    triple = curry(multiply, y=3)
    assert triple(5) == 15
    assert triple(0) == 0


def test_curry_with_mixed_args():
    def calculate(a, b, c=1):
        return (a + b) * c

    curried = curry(calculate, 2, c=4)
    assert curried(3) == 20
    assert curried(-2) == 0


def test_curry_with_higher_order_function():
    def outer(func, value):
        return func(value)

    def inner(x):
        return x**2

    curried = curry(outer, inner)
    assert curried(4) == 16
    assert curried(0) == 0


def test_curry_with_partial_application():
    def concat(a, b, c):
        return f"{a}-{b}-{c}"

    curried = curry(concat, "hello", c="world")
    assert curried("middle") == "hello-middle-world"
