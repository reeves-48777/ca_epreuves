import sys
import random

def parse_args():
	argc = len(sys.argv)

	if argc < 2:
		print("error")
		exit(1)
	
	if sys.argv[1] == "--generate":
		print("Génération d'un plateau...")
		generate_board(9, 9, 2)
		exit(0)
	else:
		board = None
		path = sys.argv[1]
		try:

			with open(path, mode="r") as board_file:
				board_data = board_file.read()

				if not check_board(board_data):
					print("Le plateau n'est pas valide")
					exit(2)
				else:
					board = board_data
				board_file.close()

			return board
		except FileNotFoundError:
			print("Fichier non trouvé")
			exit(2)

def parse_chars(chars):
	try:
		n_lines = int(chars[0])
		empty = chars[1]
		obstacle = chars[2]
		filled = chars[3]
		return n_lines, empty, obstacle, filled
	except:
		print("Les caractères n'ont pas pu être récupérés correctement")
		exit(2)
	
def check_board(board: str):
	parts = board.split('\n')
	if len(parts) == 0:
		print("plateau vide")
		return False
	
	# la premiere ligne contient les caractères du plateau
	n_lines, empty, obstacle, filled = parse_chars(parts[0])

	if n_lines != len(parts[1:]):
		print("Le nombre de ligne ne correspond pas")
		print(parts[1:])
		print(n_lines, len(parts[1:]))
		return False

	sum = 0
	for row_index in range(1, len(parts)):
		for car in parts[row_index]:
			if car not in [empty, obstacle, filled]:
				print(f"{car} n'est pas présent dans la liste des caractères du plateau: {[empty, obstacle, filled]}")
				return False
		sum += len(parts[row_index])
	if sum % len(parts[1:]) != 0:
		print("Les lignes ne font pas toutes la même longueur")
		return False
	
	return True
		

def parse_board(board: str):
	rows = board.split('\n')
	valid_chars = rows[0]

	parsed = list()
	for row in rows[1:]:
		parsed.append(list(row))
	
	return valid_chars, parsed

def make_dp_table(board, empty, obstacle):
	dp_table = list()
	rows = board

	for row_index in range(1, len(rows)):
		new_row = list()
		for car in board[row_index]:
			if car == empty:
				new_row.append(1)
			elif car == obstacle:
				new_row.append(0)
		dp_table.append(new_row)

	return dp_table

def fill_dp_table(dp):
	for i in range(len(dp)):
		for j in range(len(dp[0])):
			if dp[i][j] == 1:
				# k = len(board) - 1 if i == 0 else i - 1
				# l = len(board[0]) - 1 if j == 0 else j - 1

				dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

def find_biggest(dp):
	coords = 0, 0
	max = 0
	
	for i in range(len(dp)):
		for j in range(len(dp[0])):
			if dp[i][j] > max:
				max = dp[i][j]
				coords = i, j
	return coords, max

def mark_biggest_in_board(board, coords, size, filled):
	x, y = coords
	for i in range(x - size + 1, x + 1):
		for j in range(y - size + 1, y + 1):
			board[i][j] = filled


def generate_board(x, y, density):
	generated_path = './feu/generated_board'

	with open(generated_path, mode="w") as generated:
		generated.write(f"{y}.xo\n")
		for i in range(y):
			for j in range(x):
				if random.randrange(y) * 2 < density:
					generated.write('x')
				else:
					generated.write('.')
			if i < y - 1:
				generated.write('\n')
		generated.close()

def solve(lines):
	valid_chars, board = parse_board(lines)
	_, empty, obstacle, filled = parse_chars(valid_chars)

	dp_table = make_dp_table(board, empty, obstacle)
	fill_dp_table(dp_table)
	coords, size = find_biggest(dp_table)
	mark_biggest_in_board(board, coords, size, filled)

	marked = list()
	for row in board:
		marked.append(''.join(row))
	return '\n'.join(marked)

board = parse_args()
solved = solve(board)
print(solved)