SIZE = 19
KOMI =6.5

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
    user_in = input("command: ")
    for command in user_in.split(' '):
        if command == 'play':
            pass
        if command == 'genmove':
            pass
        if command == 'undo':
            print('Cannot undo.')
        if command in known_commands:
            if command == 'quit':
                print('Goodbye')
                exit()
            elif command == 'known_command':
                result = True if user_in.split(' ')[1] in known_commands else False
                print(result)
            elif command == 'list_commands':
                print(list(known_commands.keys()))
            elif command == 'clear_board':
                # reset everything
                pass
            else:
                print(known_commands[command])
                return known_commands[command]
        else:
            print(f'{user_in} is not a valid command')
            print(f"Type 'list_commands' for valid commands")
    return
