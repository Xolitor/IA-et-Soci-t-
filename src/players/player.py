from abc import ABC, abstractmethod

class Player(ABC):
    """Abstract base class for players in the Three for Ten game."""
    
    def __init__(self, player_id):
        """
        Initialize a new player.
        
        Args:
            player_id: A unique identifier for the player.
        """
        self.id = player_id
        self.cards = []
    
    @abstractmethod
    def make_move(self, board):
        """
        Decide on a move to make.
        
        Args:
            board: The current game board.
            
        Returns:
            tuple: (card, row, col) representing the card to play and where to place it.
        """
        pass
    
    def remove_card(self, card):
        """
        Remove a card from the player's hand.
        
        Args:
            card: The card to remove.
        """
        self.cards.remove(card)
    
    def has_cards(self):
        """
        Check if the player has any cards left.
        
        Returns:
            bool: True if the player has cards, False otherwise.
        """
        return len(self.cards) > 0