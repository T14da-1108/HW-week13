from .flip import flip


def test_flip_simple():
    f = flip(lambda x, y: x - y)
    assert f(10, 5) == -5
    assert f(5, 10) == 5


def test_flip_with_map():
    f = flip(map)
    result = list(f(range(5), range(0, 10, 2), lambda x, y: x**y))
    expected = [1, 2, 16, 216, 4096]
    assert result == expected


def test_flip_with_kwargs():
    def combine(x, y, sep=","):
        return f"{x}{sep}{y}"

    flipped = flip(combine)
    assert flipped("b", "a", sep="-") == "a-b"
    assert flipped("two", "one", sep=" ") == "one two"


def test_flip_with_multiple_args():
    f = flip(lambda *args: args)
    result = f(1, 2, 3, 4)
    expected = (4, 3, 2, 1)
    assert result == expected
