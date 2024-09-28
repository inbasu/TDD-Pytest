from abc import ABC


class Money(ABC):
    amount: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.amount == other.amount


class Dollar(Money):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multipier: int) -> "Dollar":
        return Dollar(self.amount * multipier)


class Frank(Money):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multipier: int) -> "Frank":
        return Frank(self.amount * multipier)
