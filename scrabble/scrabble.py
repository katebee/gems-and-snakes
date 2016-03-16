
import random


def main():
    print 'Running Scrabble'
    game = Game()
    player = Player(game.generate_rack())
    print player.rack
    player.take_turn(game)

    # print '\'BEE\' is worth %d points' % game.word_score('BEE')
    # print '\'BED\' is worth %d points' % game.word_score('BED')


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

    def generate_rack(self):
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
        self.score = 0

    def take_turn(self, game):
        word = self.get_player_input()
        if word:
            score = game.word_score(word)
            print self.update_score(word, score)

    def get_player_input(self):
        """Find out the word score for any word"""
        player_input = raw_input('Enter a word >> ').upper()
        # TODO: input validation
        if self._validate_answer(self.rack, player_input):
            return player_input

    def update_score(self, word, score):
        self.score += score
        return "'{0}' is worth {1} points!".format(word, score)

    def _validate_input(self, input):
        # hello regex my old friend
        pass

    def _validate_answer(self, rack, word):
        """Ensure the player has the correct tiles to create the word"""
        word_to_check = word
        rack_to_check = rack
        try:
            for letter in word:
                index_to_pop = rack_to_check.index(letter)
                rack_to_check.pop(index_to_pop)
            return True
        except Exception as e:
            return False


# ########### GAME START ########### #

if __name__ == '__main__':

    main()
