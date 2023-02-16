#!/usr/bin/env python3
# import numpy
from random import choice


def genmove_logic(color, game):
    """Main flow controller for logic"""
    row, col = None, None
    choices = game.board.empty[:]
    while self_atari(row, col, color, game):
        if row is not None:
            choices.remove((row, col))
        if not choices:
            return None, None
        row, col = choice(choices)
    return row, col


def self_atari(row, col, color, game):
    """Checks stone placement doesn't kill group"""
    if row is None:
        return True
    adjacent = adjacent_cells(row, col)
    friend = game.board.white if color == 1 else game.board.black
    enemy = game.board.white if color == -1 else game.board.black
    for stone in adjacent:
        if stone in game.board.empty:
            return False
    for stone in adjacent:
        if any(stone in group for group in enemy):
            continue
        else:
            break
        return True
    for stone in adjacent:
        for group in friend:
            if stone not in group:
                continue
            if liberties(group, game) > 1:
                return False
    return True


def liberties(group, game):
    """Returns number of liberties"""
    liberties = []
    for stone in group:
        for cell in adjacent_cells(stone[0], stone[1]):
            if cell in game.board.empty:
                liberties.append(cell)
    return len(set(liberties))


def adjacent_cells(row, col):
    a = (row + 1, col)
    b = (row - 1, col)
    c = (row, col + 1)
    d = (row, col - 1)
    return a, b, c, d
