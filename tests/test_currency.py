from currency import Dollar, Frank


def test_dollar_times() -> None:
    assert Dollar(5).times(2) == Dollar(10)
    assert Dollar(5).times(3) == Dollar(15)


def test_dollar_equality() -> None:
    assert Dollar(5) == Dollar(5)


def test_frank_times() -> None:
    assert Frank(5).times(2) == Frank(10)
    assert Frank(5).times(3) == Frank(15)


def test_frank_equality() -> None:
    assert Frank(5) == Frank(5)
