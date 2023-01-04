#!/usr/bin/env python3

class Board:
    def __init__(self, SIZE):
        """Using the '1-1 Style'. the 'A1' style.
        Note that 'i' is ommited to avoid confusion with 'j'."""
        self.board = [[EMPTY for col in range(SIZE)] for row in range(SIZE)]
        self.size = SIZE
        self.row_alpha = 'ABCDEFGHJKLMNOPQRST'
