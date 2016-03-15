
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

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
