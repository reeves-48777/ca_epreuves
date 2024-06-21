import sys



def capitalize(s: str):
	result = ""

	separators = ["\n", " ", "\t"]

	index = 0
	capitalizeNext = True
	while index < len(s):
		if capitalizeNext:
			result += s[index].upper()
			capitalizeNext = False
		else:
			result += s[index]

		if s[index] in separators:
			capitalizeNext = True

		index += 1
	return result

if len(sys.argv) < 2 or sys.argv[1].isdigit():
	print("error")
	exit(1)

string = sys.argv[1]

print(capitalize(string))