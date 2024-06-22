import sys

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

if len(sys.argv) < 2 or not sys.argv[1].isascii():
	print("error")
	exit(1)

string = sys.argv[1]

for word in split(string):
	print(word)