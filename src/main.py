from game.game import Game
from players.human_player import HumanPlayer
from players.ai_player import AIPlayer

def main():
    print("Welcome to the '3 for 10' game!")
    
    player1 = HumanPlayer("Player 1")
    player2 = AIPlayer("AI Player")
    
    game = Game()
    game.add_player(player1)
    game.add_player(player2)
    
    game.initialize_board()
    
    while not game.is_game_over():
        game.play_turn()
    
    game.declare_winner()

if __name__ == "__main__":
    main()