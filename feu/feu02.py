import sys

def remove_carrets(lines):
    output = list()
    for row in lines:
        new_row = ""
        for car in row:
            if car != '\n':
                new_row += car
        output.append(new_row)
    return output

def parse_args():
    argc = len(sys.argv)

    if argc < 3:
        print("error")
        exit(1)

    board_index = 1
    find_index = 2

    if sys.argv[board_index].isdigit() or sys.argv[find_index].isdigit():
        print("error")
        exit(2)

    board = list()
    to_find = list()

    try:
        with open(sys.argv[board_index], "r") as f_board:
            board = remove_carrets(f_board.readlines())
            f_board.close()
        with open(sys.argv[find_index], "r") as f_find:
            to_find = remove_carrets(f_find.readlines())
            f_find.close()
    except FileNotFoundError:
        print("Les fichiers n'ont pas été trouvés")
        exit(3)
    return board, to_find

def check_equality(found, to_find):
    if len(found) != len(to_find) or len(found[0]) != len(to_find[0]):
        return False

    for row in range(len(found)):
        for col in range(len(found[0])):
            if found[row][col] != to_find[row][col]:
                if to_find[row][col] == ' ':
                    continue
                else:
                    return False
    return True


def find_within_board(board, to_find):
    board_w = len(board[0])
    board_h = len(board)

    to_find_w = len(to_find[0])
    to_find_h = len(to_find)

    position = (None, None)

    found = False
    for board_row in range(board_h):
        for board_col in range(board_w):
            # on vérifie qu'on ne dépasse pas les bordures
            if (board_row + (to_find_h - 1)) < board_h and (board_col + (to_find_w - 1)) < board_w:
                # on créé une liste temporaire qui va nous permettre de stocker les valeurs de l'itération courrante
                temp = list()

                # on va parcourir la partie interne (le to_find)
                for inner_row in range(to_find_h):
                    row = ""
                    for inner_col in range(to_find_w):
                        row += board[board_row + inner_row][board_col + inner_col]
                    temp.append(row)
                if check_equality(temp, to_find):
                    found = True
                    position = (board_row, board_col)
                    return position
    if not found:
        return None

def display_found(board, to_find, position):
    display = list()

    display_row = 0
    display_col = 0

    while display_row < len(board):
        display_col = 0
        row = list()
        while display_col < len(board[0]):
            row.append('-')
            display_col += 1
        display.append(row)
        display_row += 1

    for i in range(len(to_find)):
        for j in range(len(to_find[0])):
            display[position[0]+i][position[1]+j] = to_find[i][j]

    result = list()
    for line in display:
        result.append("".join(line))
    print("\n".join(result))


board, to_find = parse_args()

position = find_within_board(board, to_find)
if position:
    print("Trouvé")
    print(f"Coordonnées: {position}")
    display_found(board, to_find, position)
else:
    print("Introuvable")
