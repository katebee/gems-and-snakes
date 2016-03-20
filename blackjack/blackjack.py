
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

    def evaluate_card(self, card):
        value = card[:-1]
        if value == 'J' or value == 'Q' or value == 'K':
            return 10
        elif value == 'A':
            return 11
        else:
            return int(value)

    def evaluate_hand(self, hand):
        hand_total = 0
        for card in hand:
            hand_total += self.evaluate_card(card)
        return hand_total

    def draw_a_card(self):
        if len(self.card_deck) > 0:
            card = self.card_deck.pop()
            return card


class Player(object):
    """docstring for Player"""
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def draw_a_card(self, card_deck):
        if len(card_deck) > 0:
            card = card_deck.pop()
            self.hand.append(card)
            return card

    def display_hand(self):
        return ' '.join(self.hand)


# ############ GAME START ############ #

if __name__ == '__main__':

    print 'Hello, Blackjack'

    game = Game()
    player = Player('Player', game.deal_hand())
    dealer = Player('Dealer', game.deal_hand())

    for _ in range(10):
        player.draw_a_card(game.card_deck)

    print player.display_hand()
