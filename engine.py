#!/usr/bin/env python3
from random import choice
from board import Board


class Game:
    def __init__(self, SIZE=19):  # default testing size = 3
        self.size = SIZE
        self.komi = 6.5
        self.white = 1
        self.black = -1
        self.id_ = ''
        self.board = Board(self.size)
        self.known_commands = ('protocol_version', 'name', 'version',
                               'known_command', 'list_commands',
                               'quit', 'boardsize', 'clear_board',
                               'komi', 'play', 'genmove')
        self.info = self.known_commands[0:5]
        self.admin = self.known_commands[5:9]
        self.gameplay = self.known_commands[9:]
        self.hist = []  # coords, not moves

    def output(self, msg=''):
        print('=' + self.id_ + msg + '\n')

    def error(self, msg=''):
        print('? ' + self.id_ + msg + '\n')


def receive_input(game):
    """Recieves user input and parses."""
    user_in = input().split(' ')
    # fix this with *args unpacking!!
    try:
        if user_in == ['']:
            raise ValueError
        if type(user_in[0]) == int:
            print('yes')
            print(user_in[0])
            game.id_, command, arg = user_in[0], user_in[1], user_in[2:]
        else:
            command, arg = user_in[0], user_in[1:]
    except IndexError:
        # Nothing to see here, just an explicitly silenced error.
        pass
    except ValueError:
        # user_in is null
        return 'no input', '', ''
    return user_in, command, arg


def info(game, user_in, command, arg):
    if command == 'name':
        game.output('goma')
    elif command == 'version':
        game.output('0.0.2')
    elif command == 'protocol_version':
        game.output('2')
    elif command == 'known_command':
        result = True if user_in.split(' ')[1] in game.known_commands else False
        game.output(result)
    elif command == 'list_commands':
        print('=')
        for item in game.known_commands:
            print(item, sep="\n")
        print('\n')


def gameplay(game, user_in, command, arg):
    if command == 'play':
        color, move = arg
        if move == 'pass':
            game.output()
            return
        if len(move) != (2 or 3):
            pass
        elif ('W' or 'w') in color:
            play(game.white, move, game)  # hacky move parseing
        elif ('B' or 'b') in color:
            play(game.black, move, game)
        return
    elif command == 'genmove':
        if ('W' or 'w') in user_in:
            genmove(game.white, game)
        elif ('B' or 'b') in user_in:
            genmove(game.black, game)
        return
    game.error(f"{command} is not a valid move.")


def admin(game, user_in, command, arg):
    if command == 'undo':
        game.output('Cannot undo.')
    if command == 'komi': # komi is broken
        if arg:
            game.komi = arg
            game.output()
            return
        game.error("No komi given")
    elif command == 'boardsize':
        try:
            if int(user_in[1]) > 19:
                raise ValueError
            if user_in[1].isnumeric():
                new_size = int(user_in[1])  # everything becomes arbitrary
                game.board.empty = [(row, col) for row in
                                    range(new_size) for col in range(new_size)]
                game.board.white = game.board.black = []
                game.size = new_size
                game.board.size = new_size
                game.output()
                return
        except IndexError:
            game.output('Please include an interger argument')
        except ValueError:
            game.output('Unacceptable size')
    elif command == 'clear_board':
        # everything becomes arbitrary
        game.board.empty = [(row, col) for row in range(game.size)
                            for col in range(game.size)]
        game.board.white = game.board.black = []
        game.output()
    elif command == 'quit':
            game.output()
            exit()


def game_round(game):
    user_in, command, arg = receive_input(game)
    if command in game.gameplay:
        gameplay(game, user_in, command, arg)
    elif command in game.info:
        info(game, user_in, command, arg)
    elif command in game.admin:
        admin(game, user_in, command, arg)
    else:
        game.error(f"{user_in} is not a valid command")
        game.error("Type 'list_commands' for valid commands")
    return


def genmove(color, game):
    if not game.board.empty:
        return game.output('PASS')
    row, col = choice(game.board.empty)
    # needs to check move is not self-atari, borrow snipet from dango
    game.board.empty.remove((row, col))
    game.hist.append((row, col))
    game.board.add_stone(row, col, color)
    return game.output(coord_to_move(row, col, game.size))


def play(color, move, game):
    row, col = move_to_coord(move, game.size)
    print(move)
    print((row, col))
    if (row, col) in game.board.empty:  # until capture implemented
        game.board.empty.remove((row, col))
    game.hist.append((row, col))
    game.board.add_stone(row, col, color)
    # work on capture here
    game.output()


def coord_to_move(row, col, size):
    col = 'ABCDEFGHJKLMNOPQRST'[col]
    row = int(row) + 1
    move = str(col) + str(row)
    return move


def move_to_coord(move, size):
    row = ''
    for k in move:
        if k.isupper():
            col = int('ABCDEFGHJKLMNOPQRST'.find(k))
        if k.islower():
            col = int('abcdefghjklmnopqrst'.find(k))
        elif k.isnumeric():
            row += k
    if row.isnumeric():
        row = int(row) - 1
    return row, col
