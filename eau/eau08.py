import sys

def isdigit(s: str):
	nums = "0123456789"

	for c in s:
		if c not in nums:
			return False
	return True


if len(sys.argv) < 2:
	print("error")
	exit(1)

s = sys.argv[1]

print(isdigit(s))