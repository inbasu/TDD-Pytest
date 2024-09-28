class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multipier: int) -> "Dollar":
        return Dollar(self.amount * multipier)

    def equals(self, dollar: "Dollar") -> bool:
        return self.amount == dollar.amount
