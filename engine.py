#!/usr/bin/env python3
from random import randint
from board import Board
from groups import Stones, Groups

class Game:
    def __init__(self):
        self.size = 19
        self.komi = 6.5
        self.white = 1
        self.black = -1
        self.id_ = ''
        self.stones = []
        self.known_commands = ('protocol_version', 'name', 'version',
                               'known_command', 'list_commands',
                               'quit', 'boardsize', 'clear_board',
                               'komi', 'play', 'genmove')

    def output(self, msg = ''):
        print('=' + self.id_ + msg + '\n' )

    def error(self, msg=''):
        print('? ' + self.id_ + msg + '\n' )


def receive_input(game):
    """Recieves user input and parses."""
    user_in =  input().split(' ')
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


def game_round(game):
    user_in, command, arg = receive_input(game)
    print(f"user_in is: {user_in}")
    print(f"command is: {command}")
    print(f"arg is: {arg}")
    if command == 'play':
        move = arg
        if arg[1] == 'pass':
            game.output()
            return
        elif ('W' or 'w') in user_in:
            play(move, game)
        elif ('B' or 'b') in command:
            play(move, game)
        game.output()
        return
    elif command == 'genmove':
        if ('W' or 'w') in user_in:
            genmove(game)
        elif ('B' or 'b') in user_in:
            genmove(game)
        else:
            game.error(f"{commands} is not a valid move.")
        return
    elif command == 'undo':
        game.output('Cannot undo.')
    elif command == 'clear_board':
        game.output()
    elif command == 'komi':
        if arg:
            game.komi = arg
        game.output()
        return
    elif command == 'boardsize':
        try:
            if int(user_in[1]) > 19:
                raise ValueError
            if user_in[1].isnumeric():
                    game.size = int(user_in[1])
                    game.output()
                    return
        except IndexError:
            game.output('Please include an interger argument')
        except ValueError:
            game.output('Unacceptable size')
        return
    elif command in game.known_commands:
        if command == 'quit':
            game.output()
            exit()
        elif command == 'known_command':
            result = True if user_in.split(' ')[1] in self.known_commands else False
            game.output(result)
        elif command == 'list_commands':
            print('=')
            for item in game.known_commands:
                print(item, sep = "\n")
            print('\n')
        elif command == 'clear_board':
            # reset everything
            pass
        elif command == 'name':
            game.output('goma')
            return
        elif command == 'version':
            game.output('0.0.1')
            return
        elif command == 'protocol_version':
            game.output('2')
            return
    else:
        game.error(f"{user_in} is not a valid command")
        game.error(f"Type 'list_commands' for valid commands")
        # game.output(f"? unknown command")
    return


def genmove(game):
    while True:
        row = randint(0, game.size - 1)
        col = randint(0, game.size - 1)
        if (row, col) not in game.stones:
            game.stones.append((row, col))
            break
    return game.output(coord_to_move(row, col, game.size))


def play(move, game):
    row, col = move_to_coord(move, game)
    game.stones.append(move)
    return


def coord_to_move(row, col, size):
    col = 'ABCDEFGHJKLMNOPQRST'[col]
    row =  int(row) + 1
    move = str(col) + str(row)
    return move

def move_to_coord(move, game): # ValueError: invalid literal for int() with base 10: '' <---fix me
    row = ''
    for k in move:
        if k.isupper():
            col = int('ABCDEFGHJKLMNOPQRST'.find(k))
        if k.islower():
            col = int('abcdefghjklmnopqrst'.find(k))
        elif k.isnumeric():
            row += k
    if row.isnumeric():
        row = game.size - int(row)
    return row, col
