class Card:
    """Represents a card with a numeric value."""
    
    def __init__(self, value):
        """
        Initialize a new card with the specified value.
        
        Args:
            value (int): The numeric value of the card.
        """
        
        if not (1 <= value <= 8):
            raise ValueError("Card value must be between 1 and 8")
        
        self.value = value
    
    def __eq__(self, other):
        """Compare two cards for equality based on their value."""
        if isinstance(other, Card):
            return self.value == other.value
        return False
    
    def __str__(self):
        """Return a string representation of the card."""
        return str(self.value)
    
    def __repr__(self):
        """Return a formal string representation of the card."""
        return f"Card({self.value})"
    
    def __format__(self, format_spec):
        """Format the card for display."""
        return format(self.value, format_spec)
    
    def __int__(self):
        """Convert the card to an integer."""
        return self.value
    
    def __add__(self, other):
        """Add the card's value to another value."""
        if isinstance(other, Card):
            return self.value + other.value
        return self.value + other
    
    def __radd__(self, other):
        """Support adding a card to another value."""
        return self.__add__(other)