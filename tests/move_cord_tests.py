size = 19


moves = [str(a) + str(b) for a in 'ABCDEFGHJKLMNOPQRST'[1:size] for b in range(size)]


def coord_to_move(row, col, size):
    col = 'ABCDEFGHJKLMNOPQRST'[col]
    row = int(row) + 1
    move = str(col) + str(row)
    return move

def move_to_coord(move, size): # ValueError: invalid literal for int() with base 10: '' <---fix me
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

for move in moves:
    # print(f'move: {move}')
    coord = move_to_coord(move, size)
    # print(f'coord: {coord}')
    nmove = coord_to_move(coord[0], coord[1], size)
    # print(f'ok: {nmove}')
    # print('move, coord, newmove')
    print(f"{move} = {nmove}, {coord}")
