import sys

def research(words, search):
	index = -1
	for i in range(len(words)):
		if words[i] == search:
			index = i
			break

	return index

if len(sys.argv) < 3:
	print("error")
	exit(1)

words = sys.argv[1:-1]
search = sys.argv[-1]

print(research(words, search))