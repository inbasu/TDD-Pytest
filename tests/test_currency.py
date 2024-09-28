from currency import Dollar


def test_times() -> None:
    dollar = Dollar(5)
    product = dollar.times(2)
    assert product.amount == 10
    product = dollar.times(3)
    assert product.amount == 15
