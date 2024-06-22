import sys

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
		
if len(sys.argv) < 2:
	print("error")
	exit(1)

elements = sys.argv[1:]
print(intruder(elements))