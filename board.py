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
        # groups = board.white if color == 1 else board.black
        if color == 1:
            groups = self.white
        else:
            groups = self.black
        a = (row + 1, col)
        b = (row - 1, col)
        c = (row, col + 1)
        d = (row, col - 1)
        adjacent = (a, b, c, d)
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
        for group in other:
            for stone in adjacent:
                if stone in group:
                    if self.liberty_check(group):
                        self.remove_group(group)

    def liberty_check(self, group):
        """True if exist liberty, else false"""
        for row, col in group: # check here
            adjacent = [(row + a[0], col + a[1]) for a in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        if ((0 <= row + a[0] < self.size) and (0 <= col + a[1] < self.size))]
            for k in adjacent:
                if adjacent in self.empty:
                    return True
        return False

    def remove_group(self, to_delete):  # needs unit tests
        # print("to_delete")
        # print(to_delete)
        for stone in to_delete:  # NOTE does not work as expected!!!
            self.empty.append(stone)
        for row, col in to_delete:
            self.board[row][col] = 0
        # groups = board.white if color == 1 else board.black
        if to_delete in self.white:
            self.white.remove(to_delete)
        elif to_delete in self.black:
            self.black.remove(to_delete)
        else:
            print('Removal failed')

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

    def asciiboard1(self):
        """"Prints board of 2D array self.board"""
        white = '●'
        black = '○'
        empty = '·'
        col_num0 = iter(range(self.size, 0, -1))
        col_num1 = iter(range(self.size, 0, -1))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))
        print('\n'.join(f"{next(col_num0):>2}" + ' ' + ' '.join(str(white if piece == 1 else black if piece == -1 else empty) for piece in row) + ' ' + f"{next(col_num1):<2}" for row in self.board))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))

    def asciiboard2(self):
        """"Prints board of self.white and self.white"""
        guideboard = [[(row, col) for col in range(self.size)] for row in range(self.size)]
        white = '●'
        black = '○'
        empty = '·'
        # error = 'x'

        col_num0 = iter(range(self.size, 0, -1))
        col_num1 = iter(range(self.size, 0, -1))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))
        print('\n'.join(f"{next(col_num0):>2}" + ' ' + ' '.join(str(white if any(piece in group for group in self.white) else black if any(piece in group for group in self.black) else empty) for piece in row) + ' ' + f"{next(col_num1):<2}" for row in guideboard))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))

