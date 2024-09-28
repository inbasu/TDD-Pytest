from abc import ABC


class Money(ABC):

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money) or self.currency != other.get_currency():
            return NotImplemented
        return self.amount == other.amount

    def times(self, multipier: int) -> "Money":
        return Money(self.amount * multipier, self.currency)

    @classmethod
    def dollar(cls, amount: int) -> "Money":
        return Money(amount, "USD")

    @classmethod
    def frank(cls, amount: int) -> "Money":
        return Money(amount, "CHF")

    def get_currency(self) -> str:
        return self.currency
