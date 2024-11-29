from .const import const


def test_const_simple():
    f = const(42)
    assert f() == 42
    assert f(1, 2, 3) == 42
    assert f(foo="bar") == 42


def test_const_with_none():
    f = const(None)
    assert f() is None
    assert f("test") is None


def test_const_with_complex_object():
    obj = {"key": "value"}
    f = const(obj)
    assert f() == obj
    assert f([]) == obj


def test_const_with_callable():
    def my_callable():
        return 99

    f = const(my_callable)
    assert f() is my_callable
    assert f()() == 99
