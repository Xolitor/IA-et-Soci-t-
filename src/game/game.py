import os
import time
## carte compte pour les deux joueurs
## une carte peux compter 4 fois donc seulement compter la nouvelle fois qu'elle est joué
class Game:
    def __init__(self):
        self.players = []
        self.current_turn = 0
        self.board = None
        self.scores = {}

    def add_player(self, player):
        self.players.append(player)
        self.scores[player.name] = 0

    def start_game(self):
        self.initialize_board()
        while not self.is_game_over():
            self.play_turn()
        self.declare_winner()

    def initialize_board(self):
        from .board import Board
        self.board = Board()
        self.display_game_state()

    def play_turn(self):
        current_player = self.players[self.current_turn]
        
        print(f"\n{current_player.name}'s turn")
        
        card, row, col = current_player.make_move(self.board)
        
        self.board.place_card(row, col, card, current_player.name)
        previous_score = self.scores[current_player.name]
        self.update_score(current_player)
        points_earned = self.scores[current_player.name] - previous_score
        
        self.display_game_state()
        
        if points_earned > 0:
            print(f"{current_player.name} earned {points_earned} point(s)!")
            
        self.current_turn = (self.current_turn + 1) % len(self.players)
        time.sleep(1)  

    # def update_score(self, player):
    #     self.scores[player.name] = self.board.calculate_score(player)
        
    def update_score(self, player):
        new_points = self.board.calculate_new_points(player.name)
        self.scores[player.name] += new_points
        return new_points

    def is_game_over(self):
        return self.board.is_full() or any(score >= 10 for score in self.scores.values())

    def declare_winner(self):
        winner = max(self.scores, key=self.scores.get)
        score = self.scores[winner]
        print("\n" + "=" * 40)
        print(f"Game Over! The winner is {winner} with a score of {score}!")
        print("=" * 40)

    def display_game_state(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "=" * 40)
        print("3 FOR 10 GAME".center(40))
        print("=" * 40 + "\n")
        
        print("SCORES:")
        for player, score in self.scores.items():
            print(f"  {player}: {score}")
        print()

        print(self.board)
        print()