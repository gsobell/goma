#!/usr/bin/env python3

import random
from board import *

def coord_to_move(row, col, board):
    col = ('ABCDEFGHJKLMNOPQRST'[col]
    row = board.size + int(row)
    return str(row) + str(col)

def move_to_coord(move, board):
    row = ''
    for k in move.current:
        if k.isupper():
            col = int('ABCDEFGHJKLMNOPQRST'.find(k))
        if k.islower():
            col = int('abcdefghjklmnopqrst'.find(k))
        elif k.isnumeric():
            row += k
        else:
            print('Not a valid move')
            return
    row = board.size - int(row)
    return row, col
