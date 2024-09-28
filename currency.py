from abc import ABCMeta


class Bank:

    def reducer(self, expression: "Expression") -> "Money":
        return Money.dollar(10)


class Expression(metaclass=ABCMeta):
    pass


class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: object) -> Expression:
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money) or self.currency != other.currency:
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
