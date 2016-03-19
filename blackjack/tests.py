
import unittest

from blackjack import Game


class TestGame(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()

    def test_generate_deck(self):
        self.assertEqual(len(self.game.card_deck), 52)

if __name__ == '__main__':
    unittest.main()
