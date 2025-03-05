import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.scored_combinations = set()
        
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

    def calculate_new_points(self, player_name):
        """Calculate new points earned by a player's most recent move."""
        points = 0
        new_combinations = set()
        
        # A optimiser 
        for row in range(self.size):
            for col in range(self.size):

                if self.grid[row][col] is None:
                    continue

                if col <= self.size - 3:
                    combination = ((row, col), (row, col+1), (row, col+2))
                    if self._is_valid_combination(combination) and self._sum_equals_ten(combination):
                        combo_key = tuple(sorted(combination))
                        if combo_key not in self.scored_combinations:
                            self.scored_combinations.add(combo_key)
                            new_combinations.add(combo_key)
                            points += 1

                if row <= self.size - 3:
                    combination = ((row, col), (row+1, col), (row+2, col))
                    if self._is_valid_combination(combination) and self._sum_equals_ten(combination):
                        combo_key = tuple(sorted(combination))
                        if combo_key not in self.scored_combinations:
                            self.scored_combinations.add(combo_key)
                            new_combinations.add(combo_key)
                            points += 1

                if row <= self.size - 3 and col <= self.size - 3:
                    combination = ((row, col), (row+1, col+1), (row+2, col+2))
                    if self._is_valid_combination(combination) and self._sum_equals_ten(combination):
                        combo_key = tuple(sorted(combination))
                        if combo_key not in self.scored_combinations:
                            self.scored_combinations.add(combo_key)
                            new_combinations.add(combo_key)
                            points += 1
                
                if row >= 2 and col <= self.size - 3:
                    combination = ((row, col), (row-1, col+1), (row-2, col+2))
                    if self._is_valid_combination(combination) and self._sum_equals_ten(combination):
                        combo_key = tuple(sorted(combination))
                        if combo_key not in self.scored_combinations:
                            self.scored_combinations.add(combo_key)
                            new_combinations.add(combo_key)
                            points += 1
        
        return points

    def _is_valid_combination(self, combination):
        """Check if all cells in the combination have cards."""
        return all(0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] is not None 
                for r, c in combination)

    def _sum_equals_ten(self, combination):
        """Check if the sum of cards in the combination equals 10."""
        return sum(self.grid[r][c] for r, c in combination) == 10
    
    # def calculate_score(self, player):
    #     """Calculate the score for a player based on the current board state."""
    #     score = 0
        
    #     # Check all possible 3-in-a-row combinations
    #     # Horizontal, vertical, and diagonal checks
    #     for row in range(self.size):
    #         for col in range(self.size):
    #             # Check horizontal
    #             if col <= self.size - 3:
    #                 combination = ((row, col), (row, col+1), (row, col+2))
    #                 score += self._check_combination(combination, player.name)
                
    #             # Check vertical
    #             if row <= self.size - 3:
    #                 combination = ((row, col), (row+1, col), (row+2, col))
    #                 score += self._check_combination(combination, player.name)
                
    #             # Check diagonal (down-right)
    #             if row <= self.size - 3 and col <= self.size - 3:
    #                 combination = ((row, col), (row+1, col+1), (row+2, col+2))
    #                 score += self._check_combination(combination, player.name)
                
    #             # Check diagonal (up-right)
    #             if row >= 2 and col <= self.size - 3:
    #                 combination = ((row, col), (row-1, col+1), (row-2, col+2))
    #                 score += self._check_combination(combination, player.name)
        
    #     return score

    def _check_combination(self, combination, player_name):
        """Check if a combination of three cells sums to 10 and hasn't been counted before."""
        # Convert combination to a hashable format that includes the direction
        sorted_combo = tuple(sorted(combination))
        
        # If this combination has already been counted, return 0
        if sorted_combo in self.scored_combinations:
            return 0
        
        # Check if all cells have cards
        if any(self.grid[row][col] is None for row, col in combination):
            return 0
        
        # Calculate sum of cards in the combination
        total = sum(self.grid[row][col] for row, col in combination)
        
        # If sum is 10, mark as scored and return 1 point
        if total == 10:
            self.scored_combinations.add(sorted_combo)
            return 1
        
        return 0

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
                    row_cells.append(f"{color}{cell:2}{Style.RESET_ALL}")
            
            row_str = f"{i:2}| " + " ".join(row_cells) + " |"
            result.append(row_str)
        
        # Add final horizontal separator
        result.append(separator)
        
        return "\n".join(result)

    def highlight_combinations(self):
        """Display the board with highlighted scoring combinations."""
        # Create a copy of the grid for highlighting
        highlighted_grid = [row[:] for row in self.grid]
        
        # Highlight all combinations that sum to 10
        for combo in self.scored_combinations:
            for row, col in combo:
                highlighted_grid[row][col] = f"*{self.grid[row][col]}*"
                
        # Return a string representation with highlights
        result = []
        
        # Add column headers (0, 1, 2, ...)
        header = "    " + " ".join(f"{i:2}" for i in range(self.size))
        result.append(header)
        
        # Add horizontal separator
        separator = "  +" + "-" * (3 * self.size + 1) + "+"
        result.append(separator)
        
        # Add rows with numbers and highlighted combinations
        for i, row in enumerate(highlighted_grid):
            row_cells = []
            for col, cell in enumerate(row):
                if highlighted_grid[i][col] is None:
                    row_cells.append("  ")
                elif isinstance(cell, str) and cell.startswith("*"):
                    # This is a highlighted cell
                    value = cell.strip("*")
                    player_name = self.ownership[i][col]
                    color = self.player_colors.get(player_name, self.default_color)
                    row_cells.append(f"{color}{Back.YELLOW}{value:2}{Style.RESET_ALL}")
                else:
                    player_name = self.ownership[i][col]
                    color = self.player_colors.get(player_name, self.default_color)
                    row_cells.append(f"{color}{cell:2}{Style.RESET_ALL}")
            
            row_str = f"{i:2}| " + " ".join(row_cells) + " |"
            result.append(row_str)
        
        # Add final horizontal separator
        result.append(separator)
        
        return "\n".join(result)