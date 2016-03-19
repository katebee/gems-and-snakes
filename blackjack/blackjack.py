
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

# ############ GAME START ############ #

if __name__ == '__main__':

    print 'Hello, Blackjack'
