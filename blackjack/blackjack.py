
import random


class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.card_deck = self.generate_deck()

    def generate_deck(self):
        card_deck = []
        houses = ('C', 'H', 'S', 'D')
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        for value in values:
            for house in houses:
                card_deck.append(value+house)
        random.shuffle(card_deck)
        return card_deck

    def deal_hand(self):
        hand = []
        hand.append(self.card_deck.pop())
        hand.append(self.card_deck.pop())
        return hand

    def draw_a_card(self):
        if len(self.card_deck) > 0:
            card = self.card_deck.pop()
            return card


class Player(object):
    """docstring for Player"""
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.bust = False

    def display_hand(self):
        return ' '.join(self.hand)

    def draw_a_card(self, card_deck):
        if len(card_deck) > 0:
            card = card_deck.pop()
            self.hand.append(card)
            return card

    def evaluate_card(self, card):
        value = card[:-1]
        if value == 'J' or value == 'Q' or value == 'K':
            return 10
        elif value == 'A':
            return 11
        else:
            return int(value)

    def evaluate_hand(self):
        hand_total = 0
        for card in self.hand:
            hand_total += self.evaluate_card(card)
        return hand_total

    def check_blackjack(self):
        if self.evaluate_hand() == 21 and len(self.hand) == 2:
            return True

    def take_turn(self, deck, min_goal):
        hand_total = 0
        while hand_total < min_goal:
            hand_total = self.evaluate_hand()
            if hand_total > 21:
                self.bust = True
            elif hand_total < min_goal:
                self.draw_a_card(deck)


# ############ GAME START ############ #

if __name__ == '__main__':

    print '\n--- BLACKJACK ---\n'

    game = Game()
    player = Player('Player', game.deal_hand())
    dealer = Player('Dealer', game.deal_hand())

    # If the player has Blackjack they win unless the dealer also has Blackjack
    player.check_blackjack()
    player.take_turn(game.card_deck, 17)

    dealer.check_blackjack()
    dealer.take_turn(game.card_deck, player.evaluate_hand())

    print "PLAYER hand: {0}\nPLAYER score: {1}".format(player.display_hand(), player.evaluate_hand())
    print "DEALER hand: {0}\nDEALER score: {1}".format(dealer.display_hand(), dealer.evaluate_hand())
