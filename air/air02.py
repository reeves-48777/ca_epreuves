import sys

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

words = sys.argv[1:-1]
separator = sys.argv[-1]

print(concat(words, separator))