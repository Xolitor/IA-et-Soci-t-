from players.player import Player

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self, board):
        while True:
            try:
                move = input(f"{self.name}, enter your move (card number, row, column): ")
                # Parse input - expecting format: "card_number row column"
                parts = move.split()
                if len(parts) != 3:
                    print("Invalid input format. Please enter card number, row, and column separated by spaces.")
                    continue
                    
                card_number = int(parts[0])
                row = int(parts[1])
                col = int(parts[2])
                
                # Validate the move
                if not (1 <= card_number <= 8):
                    print("Card number must be between 1 and 8.")
                    continue
                    
                if not board.is_valid_move(row, col):
                    print("Invalid position. Try again.")
                    continue
                    
                return card_number, row, col
                
            except ValueError:
                print("Invalid input. Please enter numeric values.")