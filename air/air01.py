import sys

def test():
    assert split("Crevette magique dans la mer des étoiles", "la") == ["Crevette magique dans ", " mer des étoiles"], 'Le split devrait être correct'

def parse_args():
    argc = len(sys.argv)

    if argc < 2:
        print("error")
        exit(1)

    first_arg = sys.argv[1]
    second_arg = None

    if first_arg == "--test":
        test()
        exit(0)
    else:
        if argc < 3:
            print("error")
            exit(2)
        else:
            second_arg = sys.argv[2]
            if not first_arg.isdigit() or not second_arg.isdigit():
                print("error")
                exit(3)
    return first_arg, second_arg

def split(tocut, separator):
	parts=list()

	start=0
	end=0

	while end < len(tocut):
		if tocut[end] == separator[0]:
			separate = True
			for j in range(1, len(separator)):
				if tocut[end + j] != separator[j]:
					separate = False
			if separate:
				parts.append(tocut[start:end])
				end += len(separator)
				start = end
		end += 1
	parts.append(tocut[start:end])
	return parts


string, separator = parse_args()

for part in split(string, separator):
	print(part)
