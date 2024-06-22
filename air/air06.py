import sys

def pass_sanitaire(elements: list[str], san_pass: str):
	sanitized = list()
	for el in elements:
		if el.lower().find(san_pass.lower()) == -1:
			sanitized.append(el)
	return sanitized


if len(sys.argv) < 2:
	print("error")
	exit(1)

elements = list()
for el in sys.argv[1:-1]:
	if el.isdigit():
		print("error")
		exit(2)
	elements.append(el)

san_pass = sys.argv[-1]

print(pass_sanitaire(elements, san_pass))