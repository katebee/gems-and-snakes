import random
import time

class SnakesAndGems(object):
    """docstring for SnakesAndGems"""
    def __init__(self):
        self.boxes = ['gems', 'snakes', 'snakes']
        self.player = None
        self.player_choice = None
    # set up the game
    # get user input_check
    def wait_and_space(self, secs=1):
        print '...'
        time.sleep(secs)

    def game_intro(self):
        print 'Welcome to Gems and Snakes!'
        self.wait_and_space(0.5)
        print 'I have three boxes, one contains gems, the others are full of snakes:'
        print '|Snakes| |Snakes| |Gems|'
        self.wait_and_space(0.5)
        random.shuffle(self.boxes)
        print 'The boxes have been shuffled, which one will you pick? (1,2,3)'

    def run_game(self):
        self.game_intro()

class Player(object):
    """docstring for Player"""
    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg


# ############ GAME START ############ #
if __name__ == '__main__':
    # create a new game

    game = SnakesAndGems()
    game.run_game()
