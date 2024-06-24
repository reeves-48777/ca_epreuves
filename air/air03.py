import sys

def test():
    assert intruder([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5, "L'intrus devrait être trouvé"
    assert intruder(["bonjour", "monsieur", "bonjour"]) == "monsieur", "L'intrus devrait être trouvé"

def parse_args():
    elements = None

    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        elements = sys.argv[1:]
    return elements

def intruder(l):
	result = dict()

	for el in l:
		if el in result.keys():
			result[el] += 1
		else:
			result[el] = 1

	keys = list(result.keys())
	prev = None
	for i in range(len(keys)):
		if i == 0:
			prev = result[keys[i]]
		else:
			if result[keys[i]] != prev:
				return keys[i]

elements = parse_args()

print(intruder(elements))
