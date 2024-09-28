from abc import ABC


class Money(ABC):

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.amount == other.amount

    @classmethod
    def dollar(cls, amount: int, currency: str) -> "Dollar":
        return Dollar(amount, currency)

    @classmethod
    def frank(cls, amount: int, currency: str) -> "Frank":
        return Frank(amount, currency)

    def get_currency(self) -> str:
        return self.currency


class Dollar(Money):

    def times(self, multipier: int) -> Money:
        return Dollar(self.amount * multipier, self.currency)


class Frank(Money):

    def times(self, multipier: int) -> Money:
        return Frank(self.amount * multipier, self.currency)
