from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, to: str) -> "Money":
        pass


class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: object) -> Expression:
        if not isinstance(other, Money):
            return NotImplemented
        return Sum(self, other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money) or self.currency != other.currency:
            return NotImplemented
        return self.amount == other.amount

    def reduce(self, to: str) -> "Money":
        return self

    def times(self, multipier: int) -> "Money":
        return Money(self.amount * multipier, self.currency)

    @classmethod
    def dollar(cls, amount: int) -> "Money":
        return Money(amount, "USD")

    @classmethod
    def frank(cls, amount: int) -> "Money":
        return Money(amount, "CHF")


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Money:
        amount: int = self.augend.amount + self.addend.amount
        return Money(amount, to)


class Bank:
    def reduce(self, expression: Expression, to: str) -> Money:
        if isinstance(expression, Money):
            return expression
        return expression.reduce(to)
