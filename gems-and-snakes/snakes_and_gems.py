import random
import time
import json
import sys


class SnakesAndGems(object):
    """docstring for SnakesAndGems"""
    def __init__(self):
        self.boxes = ['gems', 'snakes', 'snakes']
        self.player_choice = None

    def wait_and_space(self, secs=1):
        print '...'
        time.sleep(secs)

    def game_intro(self):
        print '\n~~~ GEMS AND SNAKES ~~~\n'
        print 'I have three boxes, one contains gems, the other two contain snakes:'
        print "\n\xF0\x9F\x90\x8D \xF0\x9F\x92\x8E \xF0\x9F\x90\x8D\n"
        random.shuffle(self.boxes)

    def remove_a_box(self, player):
        player.box = self.boxes.pop(player.choice - 1)
        self.boxes.remove('snakes')
        print 'I have removed one of the other boxes... it was full of snakes'
        # print self.boxes # see all!

    def offer_to_swap(self, player, prompt):
        if player.swap_or_not(prompt):
            player.box = self.boxes[0]
            print 'The boxes have been swapped!'
        else:
            print 'You will keep your first choice then!'

    def win_lose(self, player):
        if player.box == 'snakes':
            print 'Oh no! you open your box and find snakes! \xF0\x9F\x90\x8D \xF0\x9F\x90\x8D'
        else:
            print 'Hooray! You recieved a box of gems! \xF0\x9F\x92\x8E \xF0\x9F\x92\x8E'
            player.won = True

    def run_game(self, player):
        self.game_intro()
        player.choose_box('The boxes have been shuffled! Which one will you pick? (1,2,3) >> ')
        self.remove_a_box(player)
        self.wait_and_space(0.5)
        self.offer_to_swap(player, 'Would you like to swap you box with the remaining box? (y / N) >> ')
        self.wait_and_space(0.5)
        self.win_lose(player)
        self.update_stats(self.get_current_stats())
        self.print_stats(self.get_current_stats())

    def get_current_stats(self):
        """Imports game stats as a dictionary"""
        with open('stats.json', 'r+') as stats_file:
            stats = json.load(stats_file)
            return stats

    def update_stats(self, stats):
        with open('stats.json', 'r+') as stats_file:
            stats['play_count'] += 1
            if player.won:
                stats['won_count'] += 1
                if player.swap:
                    stats['swapped_and_won'] += 1
            else:
                if player.swap:
                    stats['swapped_and_lost'] += 1
            json.dump(stats, stats_file)

    def print_stats(self, stats):
        if len(sys.argv) > 1:
            total_losses = int(stats['play_count'] - stats['won_count'])
            stay_win_percentage = int(
                float(stats['won_count'] - stats['swapped_and_won']) / float(stats['play_count']) * 100)
            swap_win_percentage = int(
                float(stats['swapped_and_won']) / float(stats['play_count']) * 100)
            swap_percentage = int(float(stats['swapped_and_won'] + stats['swapped_and_lost']) / float(stats['play_count']) * 100)
            print
            print 'Total games: {0}  Wins: {1}  Losses: {2}'.format(
                stats['play_count'], stats['won_count'], total_losses)
            print 'People who swap win {0}% of the time'.format(swap_win_percentage)
            print 'People who stay win {0}% of the time'.format(stay_win_percentage)
            print '{0}% of people understand probability'.format(swap_percentage)


class Player(object):
    'docstring for Player'
    def __init__(self):
        self.box = None
        self.choice = None
        self.swap = False
        self.won = False

    def choose_box(self, prompt):
        while True:
            try:
                player_input = int(raw_input(prompt))
                if 1 <= player_input <= len(game.boxes):
                    self.choice = player_input
                    return
                else:
                    return self.choose_box(prompt)
            except ValueError:
                print 'That is not a number!'

    def swap_or_not(self, prompt):
        player_answer = raw_input(prompt).upper()
        if player_answer[:1] == 'Y':
            self.swap = True
            return True
        else:
            return False


# ############ GAME START ############ #

if __name__ == '__main__':

    game = SnakesAndGems()
    player = Player()
    game.run_game(player)
