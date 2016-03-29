
import random


class Player(object):
    """Player has a fund of cash (integer) to play machines with"""
    def __init__(self, wallet_fund):
        self.wallet_fund = wallet_fund

    def gamble(self, machine):
        if (self.wallet_fund - machine.play_cost) > 0:
            self.wallet_fund -= machine.play_cost
            machine.run()


class Machine(object):
    """Each machine has an initial bank and an cost (integer) for each turn"""
    def __init__(self, machine_bank, play_cost):
        self.machine_bank = machine_bank
        self.play_cost = play_cost
        self.play_credit = 0

    def run(self):
        self.credit_or_cash()
        result = self.roll_slots()
        print result
        prize = self.determine_prize(result)
        print 'WINNINGS: %i' % prize

    def credit_or_cash(self):
        if self.play_credit > 0:
            self.play_credit -= 1
        else:
            self.machine_bank += self.play_cost

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
            if self.machine_bank < self.play_cost * 5:
                self._provide_play_credit(self.play_cost * 5)
                prize = self.machine_bank
                self.machine_bank = 0
                return prize
            else:
                return self.play_cost * 5
        else:
            return 0

    def _provide_play_credit(self, target_payout):
        """House always wins: rounds down owed cash for machine credit"""
        credit = (target_payout - self.machine_bank) / self.play_cost
        self.play_credit += credit

# ########### GAME START ########### #

if __name__ == '__main__':

    machine1 = Machine(2222, 50)
    machine2 = Machine(1111, 10)

    player = Player(100)

    player.gamble(machine1)
