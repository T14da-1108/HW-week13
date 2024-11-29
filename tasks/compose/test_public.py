from .compose import compose


def test_compose_simple():
    f = compose(lambda x: x**2, lambda x: x + 1)
    assert f(42) == 1849


def test_compose_identity():
    def identity(x):
        return x

    f = compose(identity, lambda x: x + 1)
    assert f(10) == 11


def test_compose_multiple_layers():
    f = compose(lambda x: x * 3, lambda x: x + 2)
    g = compose(lambda x: x**2, f)
    assert g(1) == 81
    assert g(0) == 36
    assert g(-1) == 9


def test_compose_with_zero():
    f = compose(lambda x: 0, lambda x: x + 5)
    assert f(100) == 0
    assert f(-50) == 0
