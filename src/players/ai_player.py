import random
from game.card import Card

class AIPlayer:
    """Represents an AI player in the Three for Ten game."""
    
    def __init__(self, name):
        """
        Initialize a new AI player.
        
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
        Determine AI player's move.
        
        Args:
            board: The game board.
            
        Returns:
            tuple: (card, row, col) representing the AI's move.
        """
        print(f"\n{self.id} is thinking...")
        
        # Get all empty positions on the board
        empty_positions = []
        for row in range(board.size):
            for col in range(board.size):
                if board.is_valid_move(row, col):
                    empty_positions.append((row, col))
        
        # Choose a random empty position
        row, col = random.choice(empty_positions)
        
        # Choose a random card value in the allowed range (1-8)
        value = random.choice(self.available_values)
        card = Card(value)
        
        # Simulate thinking
        import time
        time.sleep(1)
        
        print(f"{self.id} plays {card} at position ({row}, {col})")
        return card, row, col
    
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