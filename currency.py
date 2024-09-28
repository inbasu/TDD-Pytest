class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multipier: int) -> None:
        self.amount *= multipier
