from players.player import Player
import random

class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self, board):
        
        valid_positions = []
        for row in range(len(board.grid)):
            for col in range(len(board.grid[row])):
                if board.is_valid_move(row, col):
                    valid_positions.append((row, col))
        
        if not valid_positions:
            return None
        
        
        row, col = random.choice(valid_positions)
        
        card_number = random.randint(1, 8)
        
        print(f"{self.name} plays card {card_number} at position ({row}, {col})")
        
        return card_number, row, col

    def get_valid_moves(self, board):
        return [card for card in self.hand if board.is_valid_move(card)]

    def evaluate_moves(self, valid_moves, board):
        return valid_moves[0]  