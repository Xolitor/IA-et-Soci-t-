from src.game.game import Game
from src.players.human_player import HumanPlayer
from src.players.ai_player import AIPlayer
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.human_player = HumanPlayer("Alice")
        self.ai_player = AIPlayer("Bot")

    def test_initial_score(self):
        self.assertEqual(self.game.get_score(self.human_player), 0)
        self.assertEqual(self.game.get_score(self.ai_player), 0)

    def test_turn_management(self):
        self.game.add_player(self.human_player)
        self.game.add_player(self.ai_player)
        self.game.start_game()
        self.assertEqual(self.game.current_turn, self.human_player)

        self.game.next_turn()
        self.assertEqual(self.game.current_turn, self.ai_player)

    def test_score_calculation(self):
        self.game.add_player(self.human_player)
        self.game.add_player(self.ai_player)
        self.game.start_game()

        # Simulate some moves
        self.human_player.play_card(1)
        self.ai_player.play_card(2)

        self.assertGreater(self.game.get_score(self.human_player), 0)
        self.assertGreater(self.game.get_score(self.ai_player), 0)

    def test_winner_determination(self):
        self.game.add_player(self.human_player)
        self.game.add_player(self.ai_player)
        self.game.start_game()

        # Simulate moves to determine a winner
        for _ in range(5):
            self.human_player.play_card(1)
            self.ai_player.play_card(2)

        winner = self.game.determine_winner()
        self.assertIn(winner, [self.human_player, self.ai_player])

if __name__ == '__main__':
    unittest.main()