
class Game(object):
    """docstring for Game"""
    def __init__(self, height=6, width=7):
        self.grid = self.generate_empty_grid(height, width)
        self.player_1 = Player('Player 1', 'X')
        self.player_2 = Player('Player 2', 'O')

    def generate_empty_grid(self, height, width):
        """Create game grid and add column and row numbers"""
        grid = [[" "]]
        for col in range(1, width + 1):
            grid[0].append(str(col))
        for row in range(1, height + 1):
            grid.append(["."] * width)
            grid[row].insert(0, str(row))
        return grid


class Player(object):
    """docstring for Player"""
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

# ########### GAME START ########### #

if __name__ == '__main__':

    game = Game(6, 7)
