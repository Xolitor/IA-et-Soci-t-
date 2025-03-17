from game.game import Game
from players.human_player import HumanPlayer
from players.ai_player import AIPlayer

def main():
    board_size = 5  # Change this to your desired board size
    
    print("Welcome to the '3 for 10' game!")
    print(f"With a {board_size}x{board_size} board, the target sum is 10!")
    print("Try to make combinations of cards that sum to 10!")
    print("You can make combinations in rows, columns, or diagonals.")
    print("The player with the most points at the end wins.")
    print("\nPress Enter to start...")
    input()
    
    player1 = HumanPlayer("Player 1")
    player2 = AIPlayer("AI Player")
    
    # Create the game instance with the players passed to the constructor
    game = Game(player1, player2, board_size=board_size)
    
    # Main game loop
    while not game.is_game_over():
        game.play_turn()
    
    # Game is over, declare the winner
    game.declare_winner()

if __name__ == "__main__":
    main()