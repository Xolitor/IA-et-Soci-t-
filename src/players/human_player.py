from game.card import Card

class HumanPlayer:
    """Represents a human player in the Three for Ten game."""
    
    def __init__(self, name):
        """
        Initialize a new human player.
        
        Args:
            name (str): The name of the player.
        """
        self.id = name
        self.available_values = []
    
    def initialize_cards(self, card_values):
        """
        Set up the available card values for the player.
        
        Args:
            card_values: Range or list of available values.
        """
        self.available_values = list(card_values)
    
    def make_move(self, board):
        """
        Ask the human player for their move.
        
        Args:
            board: The game board.
            
        Returns:
            tuple: (card, row, col) representing the player's move.
        """
        print(f"\n{self.id}, it's your turn!")
        
        while True:
            try:
                print(f"Available card values: {', '.join(str(v) for v in self.available_values)}")
                
                value = int(input(f"Enter card value ({min(self.available_values)}-{max(self.available_values)}): "))
                if value not in self.available_values:
                    print(f"Invalid value! Please choose one of: {self.available_values}")
                    continue
                
                card = Card(value)
                
                row = int(input(f"Enter row (0-{board.size-1}): "))
                col = int(input(f"Enter column (0-{board.size-1}): "))
                
                if not (0 <= row < board.size and 0 <= col < board.size):
                    print(f"Position ({row}, {col}) is outside the board! Try again.")
                    continue
                
                if not board.is_valid_move(row, col):
                    print(f"Position ({row}, {col}) is already occupied! Try again.")
                    continue
                
                return card, row, col
                
            except ValueError as e:
                if "Card value must be" in str(e):
                    print(e)
                else:
                    print("Invalid input! Please enter a number.")
    
    def remove_card(self, card):
        """
        With unlimited cards, this method doesn't need to do anything.
        """
        pass
    
    def has_cards(self):
        """
        With unlimited cards, this method always returns True.
        
        Returns:
            bool: Always True since players have unlimited cards.
        """
        return True