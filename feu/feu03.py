import sys

def parse_sudoku(lines):
    sudoku = list()
    for line in lines:
        sudoku_line = list()
        for c in line:
            if c.isdigit():
                sudoku_line.append(int(c))
            elif c == '.':
                sudoku_line.append(0)
        sudoku.append(sudoku_line)
    return sudoku

def parse_args():
    argc = len(sys.argv)

    if argc < 2:
        print("error")
        exit(1)

    data = list()
    try:
        with open(sys.argv[1]) as sudoku_file:
            data = parse_sudoku(sudoku_file.readlines())
            sudoku_file.close()
    except FileNotFoundError:
        print("Le fichier n'a pas pu être trouvé")
        exit(2)

    return data

def find_empties(sudoku):
    positions = list()
    for row in range(len(sudoku)):
        for col in range(len(sudoku[0])):
            if sudoku[row][col] == 0:
                positions.append((row, col))
    return positions

def find_next_empty(sudoku):
    for row in range(len(sudoku)):
        for col in range(len(sudoku[0])):
            if sudoku[row][col] == 0:
                return (row, col)
    return (None, None)

def is_valid(sudoku, row, col, value):
    for i in range(9):
        if sudoku[row][i] == value or sudoku[i][col] == value:
            return False
    b_row = 3 * (row // 3)
    b_col = 3 * (col // 3)

    for i in range(3):
        for j in range(3):
            if sudoku[b_row + i][b_col + j] == value:
                return False
    return True

def solve_sudoku(sudoku):
    empty_positions = find_empties(sudoku)
    if len(empty_positions) == 0:
        return True

    (row, col) = find_next_empty(sudoku)
    for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if is_valid(sudoku, row, col, value):
            sudoku[row][col] = value

            if solve_sudoku(sudoku):
                return True
            # backtrack
            sudoku[row][col] = 0
    return False

sudoku = parse_args()

solve_sudoku(sudoku)
display = list()
for line in sudoku:
    new_line = ""
    for n in line:
        new_line += str(n)
    display.append(new_line)

print("\n".join(display))
