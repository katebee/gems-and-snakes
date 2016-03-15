
import unittest

from scrabble import Game

class TestGame(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()

    def test_letter_value(self):
        self.assertEqual(len(self.game.letter_values), 3)

    def test_word_score(self):
        self.assertEqual(self.game.word_score(''), 0)
        self.assertEqual(self.game.word_score('BEE'), 5)
        self.assertEqual(self.game.word_score('BED'), 6)

    def test_scrabble_bag(self):
        self.assertEqual(len(self.game.scrabble_bag), 18)


if __name__ == '__main__':
    unittest.main()
