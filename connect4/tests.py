
import unittest

from connect4 import Game, Player


class TestGame(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()

    def test_game_init(self):
        self.assertEqual(self.player_1.name, 'Player 1')
        self.assertEqual(self.player_2.name, 'Player 2')


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()
        self.player = Player('Player 1', 'X')

    def test_player_init(self):
        self.assertEqual(self.player.name, 'Player 1')

if __name__ == '__main__':

    unittest.main()
