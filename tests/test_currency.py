from currency import Bank, Expression, Money


def test_dollar_times() -> None:
    assert Money.dollar(5).times(2) == Money.dollar(10)
    assert Money.dollar(5).times(3) == Money.dollar(15)


def test_equality() -> None:
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.frank(3) != Money.frank(5)
    assert Money.frank(5) != Money.dollar(5)


def test_frank_times() -> None:
    assert Money.frank(5).times(2) == Money.frank(10)
    assert Money.frank(5).times(3) == Money.frank(15)


def test_currency() -> None:
    """Property was disabeled in python"""
    assert Money.frank(1).currency == "CHF"
    assert Money.dollar(1).currency == "USD"


def test_simple_add() -> None:
    sum: Expression = Money.dollar(5) + Money.dollar(5)
    bank = Bank()
    reducer = bank.reducer(sum)
    assert Money.dollar(10) == reducer
