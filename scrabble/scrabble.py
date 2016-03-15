
import random


class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.letter_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4,
                              'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
                              'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
                              'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
                              'Y': 4, 'Z': 10}

        self.letter_distro = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2,
                              'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4,
                              'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
                              'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1,
                              'Y': 2, 'Z': 1}

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
        for letter in self.letter_distro:
            for _ in range(self.letter_distro[letter]):
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

    def check_word_score(self):
        """Find out the word score for any word"""
        player_input = raw_input('Enter a word >> ').upper()
        word_score(player_input)


# ########### GAME START ########### #

if __name__ == '__main__':

    print 'Running Scrabble'

    game = Game()
    game.run()

    print '\'BEE\' is worth %d points' % game.word_score('BEE')
    print '\'BED\' is worth %d points' % game.word_score('BED')
