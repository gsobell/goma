#!/usr/bin/env python3
EMPTY = 0
WHITE = 1
BLACK = -1

class Board:
    def __init__(self, SIZE):
        """Using the '1-1 Style'. the 'A1' style.
        Note that 'i' is ommited to avoid confusion with 'j'."""
        self.board = [[EMPTY for col in range(SIZE)] for row in range(SIZE)]
        self.size = SIZE
        self.white = [] # list of lists of tuples
        self.black = []
        self.empty = [(row, col) for row in range(SIZE) for col in range(SIZE)]

    def add_stone(self, row, col, color):
        if color == 1:
            groups = self.white
        else:
            groups = self.black
        loc, val = self.adjacent(row, col)
        same_side = []
        for k in range(len(loc)):
            if val[k] == color:
                same_side += loc[k]
        if groups and same_side:
            current = [(row, col)]
            for group in groups: # add to and merge groups
                for k in loc:
                    if k in group:
                        current += group
                        groups.remove(group)
            groups += current
        else:  # make new group
            groups += [(row, col)]


    def adjacent(self, row, col):
        if type(row) is not int: # for debug
            print(f'row is not int, is {row}')
        if type(col) is not int:
            print(f'col is not int, is {col}')
        location = [(row + a[0], col + a[1])
                for a in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if ((0 <= row + a[0] < self.size) and
                    (0 <= col + a[1] < self.size))]
        values = [self.board[a[0]][a[1]] for a in location]
        return location, values


# Look at later:
#     Traceback (most recent call last):
#   File "/home/gabriel/Documents/Repos/goma/goma.py", line 11, in <module>
#     goma()
#   File "/home/gabriel/Documents/Repos/goma/goma.py", line 7, in goma
#     game_round(game)
#   File "/home/gabriel/Documents/Repos/goma/engine.py", line 61, in game_round
#     play(game.white, move, game)
#   File "/home/gabriel/Documents/Repos/goma/engine.py", line 141, in play
#     game.board.add_stone(row, col, color)
#   File "/home/gabriel/Documents/Repos/goma/board.py", line 21, in add_stone
#     loc, val = self.adjacent(row, col)
#   File "/home/gabriel/Documents/Repos/goma/board.py", line 39, in adjacent
#     location = [(row+a[0], col+a[1])
#   File "/home/gabriel/Documents/Repos/goma/board.py", line 41, in <listcomp>
#     if ((0 <= row + a[0] < self.size) and
# TypeError: can only concatenate str (not "int") to str
