from currency import Dollar


def test_times() -> None:
    dollar = Dollar(5)
    dollar.times(2)
    assert dollar.amount == 10
