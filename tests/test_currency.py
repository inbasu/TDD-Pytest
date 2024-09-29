from currency import Bank, Expression, Money, Pair, Sum


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
    reducer = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reducer


def test_reduce_sum() -> None:
    sum: Expression = Sum(Money.dollar(1), Money.dollar(1))
    bank = Bank()
    reducer = bank.reduce(sum, "USD")
    assert Money.dollar(2) == reducer


def test_reduce_money() -> None:
    bank = Bank()
    reduced = bank.reduce(Money.dollar(1), "USD")
    assert reduced == Money.dollar(1)


def test_add_rate_to_bank() -> None:
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    assert bank.rates.get(Pair("CHF", "USD")) == 2


def test_reduce_differnt_currency() -> None:
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    reduced = bank.reduce(Money.frank(2), "USD")
    print(reduced.amount)
    print(reduced.currency)
    assert reduced == Money.dollar(1)
