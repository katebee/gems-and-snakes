
import unittest

from blackjack import Game, Player


class TestGame(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = Game()

    def test_generate_deck(self):
        self.assertEqual(len(self.game.card_deck), 52)

    def test_deal_hand(self):
        hand = self.game.deal_hand()
        self.assertEqual(len(hand), 2)
        self.assertEqual(len(self.game.card_deck), 50)

    def test_evaluate_card(self):
        self.assertEqual(self.game.evaluate_card('JC'), 10)
        self.assertEqual(self.game.evaluate_card('QH'), 10)
        self.assertEqual(self.game.evaluate_card('KS'), 10)
        self.assertEqual(self.game.evaluate_card('AD'), 11)

    def test_evaluate_hand(self):
        self.assertEqual(self.game.evaluate_hand(['KS', 'AD']), 21)
        self.assertEqual(self.game.evaluate_hand(['7C', '8H']), 15)
        self.assertEqual(self.game.evaluate_hand(['4S', '10C']), 14)
        self.assertEqual(self.game.evaluate_hand(['QH', '10D']), 20)


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.player = Player('Player', ['7C', '8H'])
        self.dealer = Player('Dealer', ['KS', 'AD'])

    def test_display_hand(self):
        self.assertEqual(self.player.display_hand(), '7C 8H')
        self.assertEqual(self.dealer.display_hand(), 'KS AD')

    def test_draw_a_card(self):
        deck = ['5S', '2D', '3C']
        self.assertEqual(self.player.draw_a_card(deck), '3C')
        self.assertEqual(len(self.dealer.hand), 2)
        self.assertEqual(len(self.player.hand), 3)
        self.assertEqual(len(deck), 2)


if __name__ == '__main__':
    unittest.main()
