
import random


class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.letter_values = {'E': 1, 'D': 2, 'B': 3}
        self.letter_distribution = {'E': 12, 'D': 4, 'B': 2}
        self.scrabble_bag = self._generate_scrabble_bag()

    def run(self):
        player = Player(self._generate_rack())
        print player.rack

    def word_score(self, word):
        """Calculate the score for a word"""
        score = 0
        for letter in word:
            score += self.letter_values[letter]
        return score

    def _generate_scrabble_bag(self):
        """Returns a shuffled list of letters. Letter distribution is based on
        the English Scrabble distribution"""
        scrabble_bag = []
        for letter in self.letter_distribution:
            for _ in range(self.letter_distribution[letter]):
                scrabble_bag.append(letter)
        random.shuffle(scrabble_bag)
        return scrabble_bag

    def _generate_rack(self):
        """Assign seven tiles from a scrabble_bag"""
        rack = []
        for _ in range(7):
            rack.append(self.scrabble_bag.pop())
        rack.sort()
        return rack


class Player(object):
    """docstring for Player"""
    def __init__(self, rack):
        self.rack = rack


# ########### GAME START ########### #

if __name__ == '__main__':

    print 'Running Scrabble'

    game = Game()
    game.run()

    print '\'BEE\' is worth %d points' % game.word_score('BEE')
    print '\'BED\' is worth %d points' % game.word_score('BED')
