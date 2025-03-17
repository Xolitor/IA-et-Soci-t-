from game.game import Game
from players.human_player import HumanPlayer
from players.smart_ai_player import SmartAIPlayer

def main():
    board_size = 5  
    
    print("Welcome to the '3 for 10' game!")
    print(f"With a {board_size}x{board_size} board, the target sum is 10!")
    print("Try to make combinations of cards that sum to 10!")
    print("You can make combinations in rows, columns, or diagonals.")
    print("The player with the most points at the end wins.")
    
    
    print("\nPress Enter to start...")
    input()
    
    player1 = HumanPlayer("Player 1")
    player2 = SmartAIPlayer("Smart AI")
    
    game = Game(player1, player2, board_size=board_size)
    
    while not game.is_game_over():
        game.play_turn()
        
    game.declare_winner()

if __name__ == "__main__":
    main()