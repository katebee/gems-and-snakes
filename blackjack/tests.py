
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

    def test_evaluate_card(self):
        self.assertEqual(self.player.evaluate_card('JC'), 10)
        self.assertEqual(self.player.evaluate_card('QH'), 10)
        self.assertEqual(self.player.evaluate_card('KS'), 10)
        self.assertEqual(self.player.evaluate_card('AD'), 11)

    def test_evaluate_hand(self):
        self.assertEqual(self.player.evaluate_hand(), 15)
        self.assertEqual(self.dealer.evaluate_hand(), 21)

    def test_check_blackjack(self):
        self.assertTrue(self.dealer.check_blackjack())
        self.assertFalse(self.player.check_blackjack())


class TestTakeTurn(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.deck = ['5S', '2D', '3C']
        self.player = Player('Player', ['7C', '8H'])
        self.dealer = Player('Dealer', ['KS', 'AD'])

    def test_take_turn(self):
        self.player.take_turn(self.deck, 17)
        self.dealer.take_turn(self.deck, 18)
        self.assertEqual(self.player.evaluate_hand(), 18)
        self.assertEqual(self.dealer.evaluate_hand(), 21)


if __name__ == '__main__':
    unittest.main()
