import sys

def only_one(string):
	result = ""
	for i in range(len(string)):
		if i == 0:
			result += string[i]
		else:
			if string[i] != string[i-1]:
				result += string[i]
	return result

if len(sys.argv) < 2 or len(sys.argv) > 2 or sys.argv[1].isdigit():
	print("error")
	exit(1)

string = sys.argv[1]
print(only_one(string))