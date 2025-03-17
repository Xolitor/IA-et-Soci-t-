import os
import time
from .board import Board
from .card import Card

class Game:
    """Manages the Three for Ten game flow."""
    
    def __init__(self, player1, player2, board_size):
        """
        Initialize a new game with the specified players.
        
        Args:
            player1: The first player.
            player2: The second player.
            board_size (int): The size of the game board.
        """
        self.board = Board(size=board_size)
        self.players = [player1, player2]
        self.current_player_idx = 0
        self.scores = {player1.id: 0, player2.id: 0}
        player1.initialize_cards(range(1, 9))
        player2.initialize_cards(range(1, 9))
    
    def play_turn(self):
        """
        Play a single turn of the game.
        
        Returns:
            bool: True if the game continues, False if it's over.
        """
        current_player = self.players[self.current_player_idx]
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_game_state()
        card, row, col = current_player.make_move(self.board)
        if self.board.place_card(row, col, card, current_player.id):
            points = self.board.check_combinations(current_player.id)
            self.scores[current_player.id] += points
            if points > 0:
                print(f"{current_player.id} scored {points} point(s)!")
                print("\nScoring combinations:")
                print(self.board.highlight_combinations())
                time.sleep(2)
            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
            return True
        else:
            print(f"Invalid move by {current_player.id}: {card} at ({row}, {col})")
            time.sleep(2)
            return True
    
    def is_game_over(self):
        """
        Check if the game is over.
        
        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.board.is_full()
    
    def declare_winner(self):
        """Announce the winner of the game."""
        winner = self.get_winner()
        print("\n" + "=" * 30)
        print("Game Over!")
        if winner:
            print(f"{winner.id} wins with {self.scores[winner.id]} points!")
        else:
            max_score = max(self.scores.values())
            tied_players = [player.id for player in self.players if self.scores[player.id] == max_score]
            print(f"It's a tie between {', '.join(tied_players)} with {max_score} points each!")
        print("Final scores:")
        for player in self.players:
            print(f"{player.id}: {self.scores[player.id]} points")
        print("=" * 30)
    
    def get_winner(self):
        """
        Determine the winner of the game.
        
        Returns:
            The player who won, or None if it's a tie.
        """
        max_score = max(self.scores.values())
        winners = [player for player in self.players if self.scores[player.id] == max_score]
        if len(winners) == 1:
            return winners[0]
        return None
    
    def print_game_state(self):
        """Print the current state of the game."""
        print("\n" + "=" * 30)
        print(f"Current player: {self.players[self.current_player_idx].id}")
        print(f"Scores: {self.scores}")
        print("Target sum: 10")
        print("\nBoard:")
        print(self.board)
        print("=" * 30 + "\n")
