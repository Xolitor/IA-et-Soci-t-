import colorama
from colorama import Fore, Back, Style
from enum import Enum, auto

colorama.init(autoreset=True)

class CombinationType(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()
    DIAGONAL_UP = auto()
    DIAGONAL_DOWN = auto()

class Board:
    """Represents the game board for the Three for Ten game."""
    
    def __init__(self, size=5):
        """
        Initialize a new game board.
        
        Args:
            size (int): The size of the board (default 5x5).
        """
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        # Keep track of which combinations have already been scored
        self.scored_combinations = {
            CombinationType.HORIZONTAL: set(),
            CombinationType.VERTICAL: set(),
            CombinationType.DIAGONAL_UP: set(),
            CombinationType.DIAGONAL_DOWN: set()
        }
        
        # Track which cards have been used in combinations by direction
        # This is a 2D grid where each cell contains a set of CombinationType values
        self.card_used_in_combination = [[set() for _ in range(size)] for _ in range(size)]
        
        # Set fixed target sum to 10 for all board sizes
        self.target_sum = 10
        
        self.ownership = [[None for _ in range(size)] for _ in range(size)]
        self.player_colors = {
            "Player 1": Fore.BLUE,
            "AI Player": Fore.RED
        }
        self.default_color = Fore.WHITE

    def place_card(self, row, col, card, player_name):
        """Place a card on the board at the specified position."""
        if self.is_valid_move(row, col):
            self.grid[row][col] = card
            self.ownership[row][col] = player_name
            return True
        return False

    def is_valid_move(self, row, col):
        """Check if a move is valid (within bounds and cell is empty)."""
        return (0 <= row < self.size and 
                0 <= col < self.size and 
                self.grid[row][col] is None)

    def is_full(self):
        """Check if the board is completely filled."""
        return all(cell is not None for row in self.grid for cell in row)

    def check_combinations(self, player_id):
        """
        Check for scoring combinations for the given player.
        
        Args:
            player_id: The ID of the player to check for.
            
        Returns:
            int: The number of new points scored.
        """
        points = 0
        
        # Check horizontal combinations (sliding window of 3)
        for row in range(self.size):
            for start_col in range(self.size - 2):
                if self._check_horizontal_window(row, start_col):
                    points += 1
        
        # Check vertical combinations (sliding window of 3)
        for col in range(self.size):
            for start_row in range(self.size - 2):
                if self._check_vertical_window(start_row, col):
                    points += 1
        
        # Check diagonal down combinations (sliding window of 3)
        for start_row in range(self.size - 2):
            for start_col in range(self.size - 2):
                if self._check_diagonal_down_window(start_row, start_col):
                    points += 1
        
        # Check diagonal up combinations (sliding window of 3)
        for start_row in range(2, self.size):
            for start_col in range(self.size - 2):
                if self._check_diagonal_up_window(start_row, start_col):
                    points += 1
        
        return points

    def _check_horizontal_window(self, row, start_col):
        """Check if a horizontal window of 3 cards forms a scoring combination."""
        # Check if all 3 positions in the window have cards
        if all(self.grid[row][start_col + i] is not None for i in range(3)):
            # Generate a unique key for this combination
            combo_key = (row, start_col)
            if combo_key in self.scored_combinations[CombinationType.HORIZONTAL]:
                return False
            
            # Check if any card in the window has already been used in a horizontal combination
            if any(CombinationType.HORIZONTAL in self.card_used_in_combination[row][start_col + i] for i in range(3)):
                return False
            
            # Calculate sum of cards in the window
            window_values = [int(self.grid[row][start_col + i]) for i in range(3)]
            window_sum = sum(window_values)
            
            if window_sum == 10:  # Fixed target sum of 10
                # Mark this combination as scored
                self.scored_combinations[CombinationType.HORIZONTAL].add(combo_key)
                
                # Mark each card in the window as used in a horizontal combination
                for i in range(3):
                    self.card_used_in_combination[row][start_col + i].add(CombinationType.HORIZONTAL)
                
                return True
        return False

    def _check_vertical_window(self, start_row, col):
        """Check if a vertical window of 3 cards forms a scoring combination."""
        # Check if all 3 positions in the window have cards
        if all(self.grid[start_row + i][col] is not None for i in range(3)):
            # Generate a unique key for this combination
            combo_key = (start_row, col)
            if combo_key in self.scored_combinations[CombinationType.VERTICAL]:
                return False
            
            # Check if any card in the window has already been used in a vertical combination
            if any(CombinationType.VERTICAL in self.card_used_in_combination[start_row + i][col] for i in range(3)):
                return False
            
            # Calculate sum of cards in the window
            window_values = [int(self.grid[start_row + i][col]) for i in range(3)]
            window_sum = sum(window_values)
            
            if window_sum == 10:  # Fixed target sum of 10
                # Mark this combination as scored
                self.scored_combinations[CombinationType.VERTICAL].add(combo_key)
                
                # Mark each card in the window as used in a vertical combination
                for i in range(3):
                    self.card_used_in_combination[start_row + i][col].add(CombinationType.VERTICAL)
                
                return True
        return False

    def _check_diagonal_down_window(self, start_row, start_col):
        """Check if a diagonal down window of 3 cards forms a scoring combination."""
        # Check if all 3 positions in the window have cards
        if all(self.grid[start_row + i][start_col + i] is not None for i in range(3)):
            # Generate a unique key for this combination
            combo_key = (start_row, start_col)
            if combo_key in self.scored_combinations[CombinationType.DIAGONAL_DOWN]:
                return False
            
            # Check if any card in the window has already been used in a diagonal down combination
            if any(CombinationType.DIAGONAL_DOWN in self.card_used_in_combination[start_row + i][start_col + i] for i in range(3)):
                return False
            
            # Calculate sum of cards in the window
            window_values = [int(self.grid[start_row + i][start_col + i]) for i in range(3)]
            window_sum = sum(window_values)
            
            if window_sum == 10:  # Fixed target sum of 10
                # Mark this combination as scored
                self.scored_combinations[CombinationType.DIAGONAL_DOWN].add(combo_key)
                
                # Mark each card in the window as used in a diagonal down combination
                for i in range(3):
                    self.card_used_in_combination[start_row + i][start_col + i].add(CombinationType.DIAGONAL_DOWN)
                
                return True
        return False

    def _check_diagonal_up_window(self, start_row, start_col):
        """Check if a diagonal up window of 3 cards forms a scoring combination."""
        # Check if all 3 positions in the window have cards
        if all(self.grid[start_row - i][start_col + i] is not None for i in range(3)):
            # Generate a unique key for this combination
            combo_key = (start_row, start_col)
            if combo_key in self.scored_combinations[CombinationType.DIAGONAL_UP]:
                return False
            
            # Check if any card in the window has already been used in a diagonal up combination
            if any(CombinationType.DIAGONAL_UP in self.card_used_in_combination[start_row - i][start_col + i] for i in range(3)):
                return False
            
            # Calculate sum of cards in the window
            window_values = [int(self.grid[start_row - i][start_col + i]) for i in range(3)]
            window_sum = sum(window_values)
            
            if window_sum == 10:  # Fixed target sum of 10
                # Mark this combination as scored
                self.scored_combinations[CombinationType.DIAGONAL_UP].add(combo_key)
                
                # Mark each card in the window as used in a diagonal up combination
                for i in range(3):
                    self.card_used_in_combination[start_row - i][start_col + i].add(CombinationType.DIAGONAL_UP)
                
                return True
        return False

    def __str__(self):
        """Create an enhanced visual representation of the board."""
        result = []
        
        # Add column headers (0, 1, 2, ...)
        header = "    " + " ".join(f"{i:2}" for i in range(self.size))
        result.append(header)
        
        # Add horizontal separator
        separator = "  +" + "-" * (3 * self.size + 1) + "+"
        result.append(separator)
        
        # Add rows with numbers and colored cards based on player ownership
        for i, row in enumerate(self.grid):
            row_cells = []
            for col, cell in enumerate(row):
                if cell is None:
                    row_cells.append("  ")
                else:
                    player_name = self.ownership[i][col]
                    color = self.player_colors.get(player_name, self.default_color)
                    
                    # Add symbols to indicate which combinations the card has been used in
                    card_str = str(cell)
                    used_in = self.card_used_in_combination[i][col]
                    
                    # You can use special characters or formatting to indicate scored directions
                    # Here we'll add a background color
                    if used_in:
                        row_cells.append(f"{color}{Back.YELLOW}{card_str:2}{Style.RESET_ALL}")
                    else:
                        row_cells.append(f"{color}{card_str:2}{Style.RESET_ALL}")
            
            row_str = f"{i:2}| " + " ".join(row_cells) + " |"
            result.append(row_str)
        
        # Add final horizontal separator
        result.append(separator)
        
        return "\n".join(result)
    
    def highlight_combinations(self):
        """Display the board with highlighted scoring combinations."""
        # Create a copy of the grid for highlighting
        highlighted_grid = [row[:] for row in self.grid]
        
        # Build a helper grid to show which combinations each cell is part of
        combination_grid = [[[] for _ in range(self.size)] for _ in range(self.size)]
        
        # Add horizontal combinations
        for row in range(self.size):
            for start_col in range(self.size - 2):
                combo_key = (row, start_col)
                if combo_key in self.scored_combinations[CombinationType.HORIZONTAL]:
                    for i in range(3):
                        combination_grid[row][start_col + i].append(CombinationType.HORIZONTAL)
        
        # Add vertical combinations
        for col in range(self.size):
            for start_row in range(self.size - 2):
                combo_key = (start_row, col)
                if combo_key in self.scored_combinations[CombinationType.VERTICAL]:
                    for i in range(3):
                        combination_grid[start_row + i][col].append(CombinationType.VERTICAL)
        
        # Add diagonal down combinations
        for start_row in range(self.size - 2):
            for start_col in range(self.size - 2):
                combo_key = (start_row, start_col)
                if combo_key in self.scored_combinations[CombinationType.DIAGONAL_DOWN]:
                    for i in range(3):
                        combination_grid[start_row + i][start_col + i].append(CombinationType.DIAGONAL_DOWN)
        
        # Add diagonal up combinations
        for start_row in range(2, self.size):
            for start_col in range(self.size - 2):
                combo_key = (start_row, start_col)
                if combo_key in self.scored_combinations[CombinationType.DIAGONAL_UP]:
                    for i in range(3):
                        combination_grid[start_row - i][start_col + i].append(CombinationType.DIAGONAL_UP)
        
        # Return a string representation with highlights
        result = []
        
        # Add column headers (0, 1, 2, ...)
        header = "    " + " ".join(f"{i:2}" for i in range(self.size))
        result.append(header)
        
        # Add horizontal separator
        separator = "  +" + "-" * (3 * self.size + 1) + "+"
        result.append(separator)
        
        # Add rows with numbers and highlighted combinations
        for i, row in enumerate(self.grid):
            row_cells = []
            for col, cell in enumerate(row):
                if cell is None:
                    row_cells.append("  ")
                elif combination_grid[i][col]:
                    # This card is part of at least one combination
                    player_name = self.ownership[i][col]
                    color = self.player_colors.get(player_name, self.default_color)
                    row_cells.append(f"{color}{Back.YELLOW}{cell:2}{Style.RESET_ALL}")
                else:
                    # Regular card display
                    player_name = self.ownership[i][col]
                    color = self.player_colors.get(player_name, self.default_color)
                    row_cells.append(f"{color}{cell:2}{Style.RESET_ALL}")
            
            row_str = f"{i:2}| " + " ".join(row_cells) + " |"
            result.append(row_str)
        
        # Add final horizontal separator
        result.append(separator)
        
        # Add legend
        result.append("\nLegend:")
        result.append(f"{Back.YELLOW} # {Style.RESET_ALL}: Part of a scoring combination")
        
        return "\n".join(result)