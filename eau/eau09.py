import sys

def between(min, max):
	result = list()
	for i in range(min, max):
		result.append(str(i))

	return " ".join(result)


if len(sys.argv) < 3 or not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
	print("error")
	exit(1)

min = int(sys.argv[1])
max = int(sys.argv[2])

print(between(min, max))