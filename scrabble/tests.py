
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
        rack = self.game.generate_rack()
        self.assertEqual(len(rack), 7)
        self.assertEqual(len(self.game.scrabble_bag), 91)


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()
        self.player = Player(['E', 'D', 'B'])

    def test_player_rack(self):
        self.assertEqual(self.player.rack, ['E', 'D', 'B'])

    def test_take_turn(self):
        self

    def test_update_score(self):
        self.assertEqual(self.player.update_score('BEE', 5), "'BEE' is worth 5 points!")
        self.assertEqual(self.player.score, 5)

    def test_validate_answer(self):
        self.assertEqual(self.player._validate_answer(self.player.rack, 'BED'), True)
        self.assertEqual(self.player._validate_answer(self.player.rack, 'BEE'), False)
        self.assertEqual(self.player._validate_answer(self.player.rack, 'DEED'), False)

    def test_validate_input(self):
        self.assertEqual(self.player._validate_input('TRUE'), True)
        self.assertEqual(self.player._validate_input('ABC123'), False)
        self.assertEqual(self.player._validate_input('F4L$E'), False)

if __name__ == '__main__':
    unittest.main()
