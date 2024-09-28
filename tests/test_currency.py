from currency import Money


def test_dollar_times() -> None:
    assert Money.dollar(5, "USD").times(2) == Money.dollar(10, "USD")
    assert Money.dollar(5, "USD").times(3) == Money.dollar(15, "USD")


def test_equality() -> None:
    assert Money.dollar(5, "CHF") == Money.dollar(5, "CHF")
    assert Money.frank(5, "CHF") == Money.frank(5, "CHF")
    assert Money.frank(5, "CHF") != Money.dollar(5, "USD")


def test_frank_times() -> None:
    assert Money.frank(5, "CHF").times(2) == Money.frank(10, "CHF")
    assert Money.frank(5, "CHF").times(3) == Money.frank(15, "CHF")


def test_currency() -> None:
    assert Money.frank(1, "CHF").get_currency() == "CHF"
    assert Money.dollar(1, "USD").get_currency() == "USD"
