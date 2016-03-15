
class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.letter_values = {'E' : 1, 'D' : 2, 'B' : 3}

    def word_score(self, word):
        score = 0
        for letter in word:
            score += self.letter_values[letter]
        return score

# ########### GAME START ########### #

if __name__ == '__main__':

    print 'Running Scrabble'

    game = Game()
    print '\'BEE\' is worth %d points' % game.word_score('BEE')
    print '\'BED\' is worth %d points' % game.word_score('BED')
