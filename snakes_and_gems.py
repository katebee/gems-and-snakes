import random
import time

class SnakesAndGems(object):
    """docstring for SnakesAndGems"""
    def __init__(self):
        self.boxes = ['gems', 'snakes', 'snakes']
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
        print self.boxes
        self.wait_and_space(0.5)
        random.shuffle(self.boxes)

    def remove_a_box(self, player):
        player.box = self.boxes.pop(player.choice - 1)
        self.boxes.remove('snakes')
        print self.boxes # see all!

    def run_game(self, player):
        self.game_intro()
        player.choose_box('The boxes have been shuffled, which one will you pick? (1,2,3) >> ')
        self.remove_a_box(player)

class Player(object):
    """docstring for Player"""
    def __init__(self):
        self.box = None
        self.choice = None

    def choose_box(self, prompt):
        while True:
            try:
                player_input = int(raw_input(prompt))
                if 1 <= player_input <= len(game.boxes):
                    self.choice = player_input
                    return
                else:
                    self.choose_box(prompt)
            except ValueError:
                print "That is not a number!"

# ############ GAME START ############ #
if __name__ == '__main__':
    # create a new game

    game = SnakesAndGems()
    player = Player()
    game.run_game(player)
