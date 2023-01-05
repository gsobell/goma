#!/usr/bin/env python3
from engine import game_round, Game

def goma():
    game = Game()
    while True:
        game_round(game)


if __name__ == "__main__":
    goma()
