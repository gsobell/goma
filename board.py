#!/usr/bin/env python3
EMPTY = 0
WHITE = 1
BLACK = -1


class Board:
    def __init__(self, SIZE):
        """Using the 'A1' style.
        Note that 'i' is ommited to avoid confusion with 'j'."""
        self.board = [[EMPTY for col in range(SIZE)] for row in range(SIZE)]
        self.size = SIZE
        self.white = []  # list of lists of tuples
        self.black = []
        self.empty = [(row, col) for row in range(SIZE) for col in range(SIZE)]

    def add_stone(self, row, col, color: int):
        self.board[row][col] = color
        if (row, col) in self.empty:  # should not be needed
            self.empty.remove((row, col))
        groups = self.white if color == 1 else self.black
        adjacent = self.adjacent(row, col)
        new = []
        for k in adjacent:
            for group in groups:
                if k in group:
                    groups = [g for g in groups if g != group]
                    new.extend(group)
                    break
        new.append((row, col))
        if color == 1:
            self.white = groups + [new]
            other = self.black
        else:
            self.black = groups + [new]
            other = self.white
        for stone in adjacent:
            for group in other:
                if stone in group:
                    if self.no_liberties(group):
                        self.remove_group(group)

    def adjacent(self, row, col):
        a = (row + 1, col)
        b = (row - 1, col)
        c = (row, col + 1)
        d = (row, col - 1)
        return a, b, c, d

    def no_liberties(self, group) -> bool:
        """returns True if exist liberty"""
        to_check = []
        for stone in group:
            row, col = stone
            to_check.extend(self.adjacent(row, col))
        for k in to_check:
            if k in self.empty:
                return False
        return True

    def remove_group(self, to_delete):
        print('delete initiated')
        for stone in to_delete:
            self.empty.append(stone)
        for row, col in to_delete:
            self.board[row][col] = EMPTY
        if to_delete in self.white:
            self.white.remove(to_delete)
        elif to_delete in self.black:
            self.black.remove(to_delete)

    # for debugging, will be added as optional flag in future
    def asciiboard(self):
        """"Prints board of self.white and self.white"""
        # NOTE  A1 format is flipped top bottom
        guideboard = [[(row, col) for col in range(self.size)]
                      for row in range(self.size)]
        white = '●'
        black = '○'
        empty = '·'
        # error = 'x'
        col_num0 = iter(range(1, self.size + 1, 1))
        col_num1 = iter(range(1, self.size + 1, 1))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))
        print('\n'.join(f"{next(col_num0):>2}" + ' ' + ' '.join(str(white if any(piece in group for group in self.white) else black if any(piece in group for group in self.black) else empty) for piece in row) + ' ' + f"{next(col_num1):<2}" for row in guideboard))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))

    def asciiboard1(self):
        """"Prints board of 2D array self.board"""
        # NOTE  A1 format is flipped top bottom
        white = '●'
        black = '○'
        empty = '·'
        col_num0 = iter(range(1, self.size + 1, 1))
        col_num1 = iter(range(1, self.size + 1, 1))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))
        print('\n'.join(f"{next(col_num0):>2}" + ' ' + ' '.join(str(white if piece == 1 else black if piece == -1 else empty) for piece in row) + ' ' + f"{next(col_num1):<2}" for row in self.board))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))
