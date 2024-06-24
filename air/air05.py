import sys

def test():
    assert apply_on_all([1, 2, 3, 4, 5], "+2") == [3, 4, 5, 6, 7], "L'opération devrait être appliquée à tous les nombres du tableau"
    assert apply_on_all([10, 11, 12, 20], "-5") == [5, 6, 7, 15], "L'opération devrait être appliquée à tous les nombres du tableau"

def parse_args():
    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        elements = list()
        for el in sys.argv[1:-1]:
            try:
                elements.append(int(el))
            except:
                print("error")
                exit(2)
        operation = sys.argv[-1]

        return elements, operation

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
			result.append(el - number)
		else:
			result.append(el + number)

	return result

elements, operation = parse_args()

print(apply_on_all(elements, operation))
