import sys
import random
from collections import deque

def parse_args():
	argc = len(sys.argv)

	if argc < 2:
		print("error")
		exit(1)

	if sys.argv[1] == "--generate":
		generate_labyrinth(10, 10, "* o12")
		exit(0)
	else:
		path = sys.argv[1]
		
		labyrinth = None
		with open(path, "r") as labyrinth_data:
			data = labyrinth_data.read()
			if check_labyrinth(data):
				labyrinth = data
			else:
				print("error")
				exit(2)

			labyrinth_data.close()
		return labyrinth


def generate_labyrinth(height: int, width: int, chars: str):
	if height == 0 or width == 0:
		print("La hauteur ou la largeur ne peuvent pas être nulles")
		exit(1)
	if len(chars) < 5:
		print("Le jeu de caractère du labyrinthe n'est pas valide")
		exit(2)

	entry = random.randrange(width - 4) + 2
	entry2 = random.randrange(width - 4) + 2

	path = './feu/generated_labyrinth.txt'
	with open(path, mode="w") as generated:
		generated.write(f"{height}x{width}{"".join(chars)}\n")

		for y in range(height):
			for x in range(width):
				if y == 0 and x == entry:
					generated.write(chars[3])
				elif y == height - 1 and x == entry2:
					generated.write(chars[4])
				elif (1 <= y <= height - 2) and (1 <= x <= width - 2) and random.randrange(100) > 20:
					generated.write(chars[1])
				else:
					generated.write(chars[0])
			if y < height - 1:
				generated.write('\n')

	generated.close()

def check_labyrinth(data: str):
	lines = data.splitlines()
	height, width, chars = parse_informations(lines[0])
	labyrinth = lines[1:]

	if len(labyrinth) != height:
		return False
	
	for row in lines[1:]:
		if len(row) != width:
			return False
		
		for car in row:
			if car not in chars:
				return False

	return True

def parse_informations(infos:str):
	dim_parts = infos.split('x')
	if not dim_parts[0].isdigit():
		print("Error, invalid height")
		exit(4)
	height = int(dim_parts[0])
	
	width_part = dim_parts[1]
	i = 0
	width_str = ""
	while i < len(width_part):
		if width_part[i].isdigit():
			width_str += width_part[i]
		else:
			break
		i += 1

	if not width_str.isdigit():
		print("error, invalid width")
		exit(4)
	width = int(width_str)
	chars = parse_chars(width_part[i:])

	return height, width, chars

def parse_chars(chars):
	if len(chars) != 5:
		print("Le nombre de caractères ne correspond pas")
		exit(3)

	plain = chars[0]
	empty = chars[1]
	visited = chars[2]
	entry = chars[3]
	ex = chars[4]

	return [plain, empty, visited, entry, ex]


def parse_labyrinth(data: str):
	lines = data.splitlines()
	_, _, chars = parse_informations(lines[0])

	plain = chars[0]
	empty = chars[1]
	ent = chars[3]
	ex = chars[4]

	parsed = list()
	root = None
	target = None

	labyrinth = lines[1:]
	for y in range(len(labyrinth)):
		parsed_row = list()
		for x in range(len(labyrinth[y])):
			if labyrinth[y][x] == plain:
				parsed_row.append(0)
			elif labyrinth[y][x] == empty:
				parsed_row.append(1)
			elif labyrinth[y][x] == ent:
				root = (x,y)
				parsed_row.append(1)
			elif labyrinth[y][x] == ex:
				target = (x,y)
				parsed_row.append(1)

		parsed.append(parsed_row)

	if root is None or target is None:
		print("L'entrée et la sortie du labyrinthe n'ont pas été trouvées")
		exit(5)
	
	return parsed, root, target, chars

def get_neighbors(labyrinth, coord):
	x, y = coord

	height = len(labyrinth)
	width = len(labyrinth[1])

	neighbors = list()

	if x + 1 < width and labyrinth[y][x+1] == 1:
		neighbors.append((x + 1, y))
	if x - 1 >= 0 and labyrinth[y][x-1] == 1:
		neighbors.append((x-1, y))
	if y + 1 < height and labyrinth[y+1][x] == 1:
		neighbors.append((x, y+1))
	if y - 1 >= 0 and labyrinth[y-1][x] == 1:
		neighbors.append((x, y-1))

	return neighbors

def bfs(labyrinth, entry, ex):
	queue = deque()
	queue.append(entry)
	visited = set()
	visited.add(entry)
	parent = {entry: None}

	while queue:
		s = queue.popleft()
		# print(f"exploring: {s}")
		if s == ex:
			break
		
		for t in get_neighbors(labyrinth, s):
			if t not in visited:
				queue.append(t)
				visited.add(t)
				parent[t] = s

	if ex not in parent:
		return []
	
	path = list()
	step = ex
	while step is not None:
		path.append(step)
		step = parent[step]
	path.reverse()

	return path

def mark_path(labyrinth, steps, ent, ex):
	for step in steps:
		x,y = step
		if step != ent and step != ex:
			labyrinth[y][x] = 2
		elif step == ent:
			labyrinth[y][x] = 3
		else:
			labyrinth[y][x] = 4			

def display(labyrinth, chars):
	display = list()
	for row in labyrinth:
		d_row = ""
		for value in row:
			d_row += chars[value]
		display.append(d_row)
	return "\n".join(display)

	
data = parse_args()
labyrinth, ent, ex, chars = parse_labyrinth(data)

path = bfs(labyrinth, ent, ex)
if path:
	mark_path(labyrinth, path, ent, ex)
	print(display(labyrinth, chars))
	print(f"=> Sortie atteinte en {len(path)} coups !")
else:
	print("Aucun chemin vers la sortie n'a été trouvé...")
