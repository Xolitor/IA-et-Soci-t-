import random
import time
import copy
from game.card import Card
from game.board import CombinationType

class SmartAIPlayer:
    """
    A smart AI player that uses heuristics to make better decisions.
    Uses plateau analysis and strategic card placement to maximize points.
    """
    
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
    
    def has_cards(self):
        """
        With unlimited cards, this method always returns True.
        
        Returns:
            bool: Always True since players have unlimited cards.
        """
        return True
    
    def remove_card(self, card):
        """
        With unlimited cards, this method doesn't need to do anything.
        """
        pass
    
    def make_move(self, board):
        """
        Determine AI player's move using heuristic analysis.
        
        Args:
            board: The game board.
            
        Returns:
            tuple: (card, row, col) representing the AI's move.
        """
        print(f"\n{self.id} is thinking strategically...")
        
        empty_positions = []
        for row in range(board.size):
            for col in range(board.size):
                if board.is_valid_move(row, col):
                    empty_positions.append((row, col))
        
        if not empty_positions:
            raise ValueError("No valid moves available!")
        
        time.sleep(1.5)
        
        best_move = self._find_best_move(board, empty_positions)
        card, row, col = best_move
        
        if not board.is_valid_move(row, col):
            print(f"AI attempted invalid move, choosing a random move instead")
            row, col = random.choice(empty_positions)
            value = random.choice(self.available_values)
            card = Card(value)
        
        print(f"{self.id} plays {card} at position ({row}, {col})")
        return card, row, col
    
    def _find_best_move(self, board, empty_positions):
        """
        Find the best move based on heuristic analysis.
        
        Args:
            board: The current game board
            empty_positions: List of available positions
            
        Returns:
            tuple: (card, row, col) representing the best move
        """
        best_score = float('-inf')
        best_move = None
        
        for row, col in empty_positions:
            for value in self.available_values:
                card = Card(value)
                score = self._evaluate_move(board, card, row, col)
                if score > best_score:
                    best_score = score
                    best_move = (card, row, col)
        
        if best_move is None:
            row, col = random.choice(empty_positions)
            value = random.choice(self.available_values)
            best_move = (Card(value), row, col)
            
        return best_move
    
    def _copy_board(self, board):
        """Create a deep copy of the board for move simulation."""
        board_copy = copy.deepcopy(board)
        return board_copy
    
    def _evaluate_move(self, board, card, row, col):
        """
        Evaluate a potential move and assign it a score.
        
        Args:
            board: The game board
            card: The card to place
            row: Row position
            col: Column position
            
        Returns:
            float: Score for this move
        """
        if not board.is_valid_move(row, col):
            return float('-inf')
        
        try:
            board_copy = self._copy_board(board)
            
            if not board_copy.place_card(row, col, card, self.id):
                return float('-inf')
            
            score = 0.0
            
            points = self._count_potential_points(board_copy, row, col)
            score += points * 100
            
            future_points = self._analyze_future_potential(board_copy, row, col)
            score += future_points * 50
            
            blocking_value = self._evaluate_blocking(board_copy, row, col)
            score += blocking_value * 75
            
            positional_value = self._evaluate_position(board, row, col)
            score += positional_value * 20
            
            score += random.uniform(0, 10)
            
            return score
            
        except Exception as e:
            print(f"Error evaluating move ({row}, {col}): {e}")
            return float('-inf')
    
    def _count_potential_points(self, board, row, col):
        """
        Count how many points would be scored by placing a card at the given position.
        
        Args:
            board: The game board
            row: Row position
            col: Column position
            
        Returns:
            int: Number of potential points
        """
        potential_points = 0
        
        for start_col in range(max(0, col - 2), min(col + 1, board.size - 2)):
            if self._can_form_sum_of_10(board, row, start_col, "horizontal"):
                potential_points += 1
        
        for start_row in range(max(0, row - 2), min(row + 1, board.size - 2)):
            if self._can_form_sum_of_10(board, start_row, col, "vertical"):
                potential_points += 1
        
        for offset in range(-2, 1):
            start_row = row + offset
            start_col = col + offset
            if (0 <= start_row < board.size - 2 and 
                0 <= start_col < board.size - 2):
                if self._can_form_sum_of_10(board, start_row, start_col, "diagonal_down"):
                    potential_points += 1
        
        for offset in range(-2, 1):
            start_row = row - offset
            start_col = col + offset
            if (2 <= start_row < board.size and 
                0 <= start_col < board.size - 2):
                if self._can_form_sum_of_10(board, start_row, start_col, "diagonal_up"):
                    potential_points += 1
        
        return potential_points
    
    def _can_form_sum_of_10(self, board, start_row, start_col, direction):
        """
        Check if a window starting at (start_row, start_col) can form a sum of 10.
        
        Args:
            board: The game board
            start_row: Starting row
            start_col: Starting column
            direction: Direction to check ("horizontal", "vertical", "diagonal_down", "diagonal_up")
            
        Returns:
            bool: True if the window can form a sum of 10
        """
        cells = []
        
        if direction == "horizontal":
            positions = [(start_row, start_col + i) for i in range(3)]
        elif direction == "vertical":
            positions = [(start_row + i, start_col) for i in range(3)]
        elif direction == "diagonal_down":
            positions = [(start_row + i, start_col + i) for i in range(3)]
        elif direction == "diagonal_up":
            positions = [(start_row - i, start_col + i) for i in range(3)]
        else:
            return False
        
        if not all(0 <= r < board.size and 0 <= c < board.size for r, c in positions):
            return False
        
        if not all(board.grid[r][c] is not None for r, c in positions):
            return False
        
        if direction == "horizontal":
            combo_type = CombinationType.HORIZONTAL
        elif direction == "vertical":
            combo_type = CombinationType.VERTICAL
        elif direction == "diagonal_down":
            combo_type = CombinationType.DIAGONAL_DOWN
        else:
            combo_type = CombinationType.DIAGONAL_UP
            
        if any(combo_type in board.card_used_in_combination[r][c] for r, c in positions):
            return False
        
        window_sum = sum(int(board.grid[r][c]) for r, c in positions)
        return window_sum == 10
    
    def _analyze_future_potential(self, board, row, col):
        """
        Analyze the future scoring potential created by this move.
        
        Args:
            board: The game board
            row: Row position
            col: Column position
            
        Returns:
            float: Score for future potential
        """
        score = 0.0
        
        for start_col in range(max(0, col - 2), min(col + 1, board.size - 2)):
            score += self._check_near_complete(board, row, start_col, "horizontal")
        
        for start_row in range(max(0, row - 2), min(row + 1, board.size - 2)):
            score += self._check_near_complete(board, start_row, col, "vertical")
        
        for offset in range(-2, 1):
            start_row = row + offset
            start_col = col + offset
            if (0 <= start_row < board.size - 2 and 
                0 <= start_col < board.size - 2):
                score += self._check_near_complete(board, start_row, start_col, "diagonal_down")
        
        for offset in range(-2, 1):
            start_row = row - offset
            start_col = col + offset
            if (2 <= start_row < board.size and 
                0 <= start_col < board.size - 2):
                score += self._check_near_complete(board, start_row, start_col, "diagonal_up")
        
        return score
    
    def _check_near_complete(self, board, start_row, start_col, direction):
        """
        Check if a window is near-complete (only 1 card missing) and could form a sum of 10.
        
        Args:
            board: The game board
            start_row: Starting row
            start_col: Starting column
            direction: Direction to check
        Returns:
            float: Score based on near-completeness
        """
        if direction == "horizontal":
            positions = [(start_row, start_col + i) for i in range(3)]
        elif direction == "vertical":
            positions = [(start_row + i, start_col) for i in range(3)]
        elif direction == "diagonal_down":
            positions = [(start_row + i, start_col + i) for i in range(3)]
        elif direction == "diagonal_up":
            positions = [(start_row - i, start_col + i) for i in range(3)]
        else:
            return 0.0
        
        if not all(0 <= r < board.size and 0 <= c < board.size for r, c in positions):
            return 0.0
        
        empty_cells = []
        filled_sum = 0
        
        for r, c in positions:
            if board.grid[r][c] is None:
                empty_cells.append((r, c))
            else:
                filled_sum += int(board.grid[r][c])
        
        if len(empty_cells) == 1:
            target_value = 10 - filled_sum
            if 1 <= target_value <= 8:
                return 1.0
        
        return 0.0
    
    def _evaluate_blocking(self, board, row, col):
        """
        Evaluate how effectively this move blocks opponent scoring opportunities.
        
        Args:
            board: The game board
            row: Row position
            col: Column position
            
        Returns:
            float: Blocking score
        """
        blocking_score = 0.0
        
        for direction in ["horizontal", "vertical", "diagonal_down", "diagonal_up"]:
            if self._blocks_opponent(board, row, col, direction):
                blocking_score += 1.0
        
        return blocking_score
    
    def _blocks_opponent(self, board, row, col, direction):
        """
        Check if placing a card at (row, col) blocks an opponent's potential scoring.
        
        Args:
            board: The game board
            row: Row position
            col: Column position
            direction: Direction to check
            
        Returns:
            bool: True if this move blocks opponent scoring
        """
        windows = []
        
        if direction == "horizontal":
            for start_col in range(max(0, col - 2), min(col + 1, board.size - 2)):
                windows.append([(row, start_col + i) for i in range(3)])
        elif direction == "vertical":
            for start_row in range(max(0, row - 2), min(row + 1, board.size - 2)):
                windows.append([(start_row + i, col) for i in range(3)])
        elif direction == "diagonal_down":
            for offset in range(-2, 1):
                if 0 <= row + offset < board.size - 2 and 0 <= col + offset < board.size - 2:
                    windows.append([(row + offset + i, col + offset + i) for i in range(3)])
        elif direction == "diagonal_up":
            for offset in range(-2, 1):
                if 2 <= row - offset < board.size and 0 <= col + offset < board.size - 2:
                    windows.append([(row - offset - i, col + offset + i) for i in range(3)])
        
        for window in windows:
            opponent_count = 0
            opponent_sum = 0
            empty_count = 0
            
            for r, c in window:
                if board.grid[r][c] is None:
                    empty_count += 1
                elif board.ownership[r][c] != self.id:
                    opponent_count += 1
                    opponent_sum += int(board.grid[r][c])
            
            if opponent_count == 2 and empty_count == 1:
                needed_value = 10 - opponent_sum
                if 1 <= needed_value <= 8:
                    return True
        
        return False
    
    def _evaluate_position(self, board, row, col):
        """
        Evaluate the strategic value of a board position.
        
        Args:
            board: The game board
            row: Row position
            col: Column position
            
        Returns:
            float: Position score (higher is better)
        """
        center = board.size // 2
        row_distance = abs(row - center)
        col_distance = abs(col - center)
        
        distance = (row_distance + col_distance) / (2 * center)
        
        return 1.0 - distance
