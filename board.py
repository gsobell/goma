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
        self.white = Stones(WHITE)
        self.black = Stones(BLACK)


class Stones:
    """All stones on the board."""
    def __init__(self, color):
        self.stones = ()
        self.groups = ()
        self.color = color

    def add_stone(self, row, col, board):
        """Adds stone to stones, and to new or existing group."""
        self.stones = (*self.stones, row, col)
        friends = self.adjacent_loc(row, col, board)


    def rm_stones(self, stone_list):
        """Is passed list of coordinates of group to be removed"""
        self.stones = (stone for stone in self.stones if stone not in stone_list)


    def adjacent_loc(self, row, col, board):
        """Returns location of adjacent stones"""
        return [(row+a[0],
                col+a[1]) for a in [(-1, 0), (1, 0), (0, -1), (0, 1)] if ((0 <= row+a[0] < board.size) and (0 <= col+a[1] < board.size))]

    def adjacent_val(self, row, col, board):
        """Returns values of adjacent stones"""
        location = [(row+a[0], col+a[1]) for a in [(-1, 0), (1, 0), (0, -1), (0, 1)] if ((0 <= row+a[0] < board.size) and (0 <= col+a[1] < board.size))]
        return [board.board[a[0]][a[1]] for a in location]




# class Groups(self):
#     def __init__(self):
#         self.stones = ()
#         self.liberties = ()
#
#     def join(self):
#         """Joins two groups when a stone connects them"""
#         pass
