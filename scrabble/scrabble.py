
class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.letter_values = {'E': 1, 'D': 2, 'B': 3}
        self.letter_distribution = {'E': 12, 'D': 4, 'B': 2}
        self.scrabble_bag = self.generate_scrabble_bag()

    def word_score(self, word):
        """Calculate the score for a word"""
        score = 0
        for letter in word:
            score += self.letter_values[letter]
        return score

    def generate_scrabble_bag(self):
        """Letter distribution is based on the English Scrabble distribution"""
        scrabble_bag = []
        for letter in self.letter_distribution:
            for _ in range(self.letter_distribution[letter]):
                scrabble_bag.append(letter)
        return scrabble_bag

    def random_tile(self):
        """Assign seven tiles chosen randomly from the alphabet"""
        pass


# ########### GAME START ########### #

if __name__ == '__main__':

    print 'Running Scrabble'

    game = Game()

    print '\'BEE\' is worth %d points' % game.word_score('BEE')
    print '\'BED\' is worth %d points' % game.word_score('BED')
