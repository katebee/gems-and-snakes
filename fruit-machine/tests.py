import unittest

from fruit_machine import Machine


class TestRollSLots(unittest.TestCase):

    def test_machine_slots(self):
        machine = Machine(2222, 50)
        self.assertEqual(len(machine.roll_slots()), 4)


class TestJackpot(unittest.TestCase):

    def setUp(self):
        self.result = ['black', 'white', 'green', 'yellow']

    def test_matching_set(self):
        machine = Machine(2222, 50)
        self.assertTrue(machine.unique_set_win(self.result))

    def test_jackpot_when_bank_even(self):
        machine = Machine(2222, 50)
        self.assertTrue(machine.unique_set_win(self.result))
        self.assertEqual(1111, machine.determine_prize(self.result))

    def test_jackpot_when_bank_odd(self):
        machine = Machine(1111, 50)
        self.assertTrue(machine.unique_set_win(self.result))
        self.assertEqual(555, machine.determine_prize(self.result))

    def test_low_machine_bank(self):
        machine = Machine(110, 50)
        self.assertTrue(machine.unique_set_win(self.result))
        self.assertFalse(machine.adjacent_win(self.result))
        self.assertEqual(55, machine.determine_prize(self.result))


class TestAdjacent(unittest.TestCase):

    def setUp(self):
        self.result = ['black', 'white', 'green', 'green']

    def test_adjacent_win(self):
        machine = Machine(2222, 50)
        self.assertTrue(machine.adjacent_win(self.result))

    def test_low_machine_bank(self):
        machine = Machine(110, 50)
        self.assertTrue(machine.adjacent_win(self.result))
        self.assertFalse(machine.unique_set_win(self.result))
        self.assertEqual(110, machine.determine_prize(self.result))
        self.assertEqual(machine.play_credit, 2)
        self.assertEqual(machine.machine_bank, 0)


class TestNoWin(unittest.TestCase):

    def test_no_win(self):
        machine = Machine(2222, 50)
        result = ['black', 'green', 'black', 'green']
        self.assertFalse(machine.unique_set_win(result))
        self.assertFalse(machine.adjacent_win(result))
        self.assertEqual(machine.determine_prize(result), 0)
        self.assertEqual(2222, machine.machine_bank)

if __name__ == '__main__':
    unittest.main()
