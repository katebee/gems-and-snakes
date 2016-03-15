
import unittest

from scrabble import Game, Player


class TestGame(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()

    def test_letter_value(self):
        self.assertEqual(len(self.game.letter_values), 26)

    def test_word_score(self):
        self.assertEqual(self.game.word_score(''), 0)
        self.assertEqual(self.game.word_score('BEE'), 5)
        self.assertEqual(self.game.word_score('BED'), 6)

    def test_scrabble_bag(self):
        self.assertEqual(len(self.game.scrabble_bag), 98)

    def test_generate_rack(self):
        rack = self.game._generate_rack()
        self.assertEqual(len(rack), 7)
        self.assertEqual(len(self.game.scrabble_bag), 91)


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()
        self.player = Player(['E', 'D', 'B'])

    def test_player_rack(self):
        self.assertEqual(self.player.rack, ['E', 'D', 'B'])


if __name__ == '__main__':
    unittest.main()
