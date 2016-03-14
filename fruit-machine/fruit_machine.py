
import random

class Player(object):
    """Player has a fund of cash (integer) to play machines with"""
    def __init__(self, wallet_fund):
        self.wallet_fund = wallet_fund

    def gamble(self, machine):
        if (self.wallet_fund - machine.play_cost) > 0:
            self.wallet_fund -= machine.play_cost
            # TODO: run machine

class Machine(object):
    """Each machine has an initial bank and an cost (integer) for each turn"""
    def __init__(self, machine_bank, play_cost):
        self.machine_bank = machine_bank
        self.play_cost = play_cost

    def run(self):
        # TODO: use credit if possible, else use player cash and increment fund
        pass

    def roll_slots(self):
        """Display four 'slots' each with a randomly selected colour in each slot"""
        colours = ['black', 'white', 'green', 'yellow']
        return [random.choice(colours), random.choice(colours), random.choice(colours), random.choice(colours)]

    def unique_set_win(self, slots):
        """If each slot has a different colour then the machine should pay out half the current money in the machine"""
        if len(set(slots)) == len(slots):
            return True

    def adjacent_win(self, slots):
        """If two or more adjacent slots contain the same colour then the machine should pay out a prize of 5 times the cost of a single play"""
        for index in range(len(slots) - 1):
            if slots[index] == slots[index + 1]:
                return True

    def determine_prize(self, result):
        """Check all win conditions from major to minor wins and return prize amount"""
        if self.unique_set_win(result):
            prize = int(self.machine_bank / 2)
            self.machine_bank -= prize
            return prize
        elif self.adjacent_win(result):
            prize = self.play_cost * 5
            self.machine_bank -= prize
            return prize
        else:
            return 0

# ########### GAME START ########### #

if __name__ == '__main__':

    machine1 = Machine(2222, 50)
    machine2 = Machine(1111, 10)

    player = Player(100)

    result = machine1.roll_slots()
    print result
    print machine1.determine_prize(result)
