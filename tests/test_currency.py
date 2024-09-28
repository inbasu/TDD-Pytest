from currency import Dollar


def test_times() -> None:
    assert Dollar(5).times(2) == Dollar(10)
    assert Dollar(5).times(3) == Dollar(15)


def test_equality() -> None:
    assert Dollar(5) == Dollar(5)
