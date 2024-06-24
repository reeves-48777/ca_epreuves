import sys

def test():
    assert(only_one("Hello milady,    bien ou quoi ??")) == "Helo milady, bien ou quoi ?", 'Impossible d\'avoir plusieurs caractères identiques qui se suivent'

def parse_args():
    argc = len(sys.argv)
    if argc < 2 or argc > 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        return sys.argv[1]

def only_one(string):
	result = ""
	for i in range(len(string)):
		if i == 0:
			result += string[i]
		else:
			if string[i] != string[i-1]:
				result += string[i]
	return result

string = parse_args()
print(only_one(string))
