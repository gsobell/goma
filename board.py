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

    def add_stone(self, row, col, color):
        self.board[row][col] = color
        if color == 1:
            groups = self.white
        else:
            groups = self.black
        a = (row + 1, col)
        b = (row - 1, col)
        c = (row, col + 1)
        d = (row, col - 1)
        new = []
        for group in groups:
            if a in group:
                groups = [g for g in groups if g != group]
                new.extend(group)
                break
        for group in groups:
            if b in group:
                groups = [g for g in groups if g != group]
                new.extend(group)
                break
        for group in groups:
            if c in group:
                groups = [g for g in groups if g != group]
                new.extend(group)
                break
        for group in groups:
            if d in group:
                groups = [g for g in groups if g != group]
                new.extend(group)
                break
        new.append((row, col))
        if color == 1:
            self.white = groups + [new]
        else:
            self.black = groups + [new]

    def group_adjacent(self, group, same) -> bool:
        for k in same:
            if k in group:
                return True
        return False

    def adjacent(self, row, col):
        if type(row) is not int:  # for debug
            print(f'row is not int, is {row}')
        if type(col) is not int:
            print(f'col is not int, is {col}')
        location = [(row + a[0], col + a[1]) for a in
                    [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    if ((0 <= row + a[0] < self.size)
                        and (0 <= col + a[1] < self.size))]
        values = [self.board[a[0]][a[1]] for a in location]
        return location, values
