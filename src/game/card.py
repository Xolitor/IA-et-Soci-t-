class Card:
    def __init__(self, value):
        if value not in range(1, 9):
            raise ValueError("Card value must be between 1 and 8.")
        self.value = value

    def __repr__(self):
        return f"Card({self.value})"