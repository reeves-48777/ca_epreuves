import sys

def parse_args():
    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    arg = sys.argv[1]
    if arg == "--test":
        test()
        exit(0)
    elif not arg.isascii():
        print("error")
        exit(2)

    return arg

def test():
    assert split("Bonjour les gars") == ["Bonjour", "les", "gars"], 'La phrase devrait être splittée correctement'

def split(tocut, separator = " "):
	parts = list()
	start = 0
	end = 0
	while end < len(tocut):
		if tocut[end] == separator:
			parts.append(tocut[start:end])
			start = end + 1
		end += 1
	parts.append(tocut[start:])
	return parts

string = parse_args()

for word in split(string):
	print(word)
