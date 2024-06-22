import sys

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

if len(sys.argv) < 3 or sys.argv[1].isdigit() or sys.argv[2].isdigit():
	print("error")
	exit(1)

string = sys.argv[1]
separator = sys.argv[2]

for part in split(string, separator):
	print(part)
