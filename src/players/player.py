class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def make_move(self, board):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def update_score(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}"