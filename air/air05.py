import sys

def apply_on_all(elements, operation):
	result = list()
	
	substract = False

	if operation[0] not in ["+", "-"]:
		print("error")
		exit(2)
	else:
		if operation[0] == "-":
			substract = True

	number = int(operation[1:])

	for el in elements:
		if substract:
			result.append(str(el - number))
		else:
			result.append(str(el + number))

	return " ".join(result)

if len(sys.argv) < 2:
	print("error")
	exit(1)

elements = list()
for el in sys.argv[1:-1]:
	try:
		elements.append(int(el))
	except:
		print("error")
		exit(1)

operation = sys.argv[-1]

print(apply_on_all(elements, operation))
