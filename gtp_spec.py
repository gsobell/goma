from engine import genmove, play

SIZE = 19
KOMI = 6.5
WHITE = 1
BLACK = -1
id_num = ' '

def output(id_num, msg = ''):
    print('=' + id_num + msg + '\n' )

def error(id_num, msg=''):
    print('? ' + msg + '\n' )

known_commands = {
'protocol_version': '2',
'name': 'goma',
'version': '0.0.1' ,
'known_command': True,
'list_commands': True,
'quit': True,
'boardsize': SIZE,
'clear_board': None,
'komi': KOMI ,
'play': None,
'genmove': None}

def recieve_input():
    user_in = input()
    commands =  user_in.split(' ')
    if commands[0].isnumeric():
        id_num = commands[0] + ' '
        command = commands[1]
    else:
        id_num = ' '
        command =  commands[0]
    if command == 'play':
        if ('W' or 'w') in commands:
            play(WHITE)
        elif ('B' or 'b') in command:
            play(BLACK)
        else:
            error(id_num, f"{commands} is not a valid move.")
        return
        pass
    elif command == 'genmove':
        if ('W' or 'w') in commands:
            genmove(WHITE)
        elif ('B' or 'b') in command:
            genmove(BLACK)
        else:
            genmove(BLACK)
            # error(id_num, f"{commands} is not a valid move.")
        return
    elif command == 'undo':
        output(id_num, 'Cannot undo.')
    elif command == 'clear_board':
        output(id_num)
    elif command == 'komi':
        global KOMI
        KOMI = float(commands[1])
        output(id_num)
        return
    elif command == 'boardsize':
        try:
            if int(commands[1]) > 19:
                raise ValueError
            if commands[1].isnumeric():
                    global SIZE
                    SIZE = int(commands[1])
                    output(id_num)
                    return
        except IndexError:
            output('Please include an interger argument')
        except ValueError:
            output('Unacceptable size')
        return
    elif command in known_commands:
        if command == 'quit':
            output(id_num)
            exit()
        elif command == 'known_command':
            result = True if user_in.split(' ')[1] in known_commands else False
            output(result)
        elif command == 'list_commands':
            print('=', id_num)
            for item in known_commands.keys():
                print(item, sep = "\n")
            print('\n')
        elif command == 'clear_board':
            # reset everything
            pass
        else:
            output(id_num, known_commands[command])
            return
    else:
        error(id_num, f'{user_in} is not a valid command')
        error(id_num, f"Type 'list_commands' for valid commands")
        # output(f"? unknown command")
    return
