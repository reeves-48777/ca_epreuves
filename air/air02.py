import sys

def test():
    assert concat(["je", "teste", "des", "trucs"], " ") == "je teste des trucs", 'Les éléments du tableau devraient avoir fusionné'

def parse_args():
    words = None
    sep = None

    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        words = sys.argv[1:-1]
        sep = sys.argv[-1]

    return words, sep

def concat(words, separator):
	result = ""
	for i in range(len(words)):
		result += words[i]
		if i != len(words) - 1:
			result += separator
	return result


if len(sys.argv) < 2:
	print("error")
	exit(1)

words, separator = parse_args()

print(concat(words, separator))
