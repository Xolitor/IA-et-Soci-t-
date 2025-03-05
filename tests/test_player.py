from src.players.player import Player
from src.players.human_player import HumanPlayer
from src.players.ai_player import AIPlayer

def test_human_player_initialization():
    player = HumanPlayer("Alice")
    assert player.name == "Alice"
    assert isinstance(player, Player)

def test_ai_player_initialization():
    player = AIPlayer("Bot")
    assert player.name == "Bot"
    assert isinstance(player, Player)

def test_human_player_make_move():
    player = HumanPlayer("Alice")
    move = player.make_move()  # Assuming this method prompts for input
    assert move is not None  # Replace with actual validation based on game rules

def test_ai_player_make_move():
    player = AIPlayer("Bot")
    move = player.make_move()  # Assuming this method calculates a move
    assert move is not None  # Replace with actual validation based on game rules

def test_player_score():
    player = HumanPlayer("Alice")
    player.score = 10
    assert player.score == 10

    ai_player = AIPlayer("Bot")
    ai_player.score = 15
    assert ai_player.score == 15