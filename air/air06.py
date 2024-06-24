import sys

def test():
    assert pass_sanitaire(["Michel", "Albert", "Thérèse", "Benoit"], "t") == ["Michel"], "On ne devrait pas avoir les éléments qui ont un T"
    assert pass_sanitaire(["Michel", "Albert", "Thérèse", "Benoit"], "a") == ["Michel", "Thérèse", "Benoit"], "On ne devrait pas avoir les éléments qui ont un A"

def parse_args():
    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        elements = list()
        for el in sys.argv[1:-1]:
            if el.isdigit():
                print("error")
                exit(2)
            elements.append(el)

        san_pass = sys.argv[-1]

        return elements, san_pass

def pass_sanitaire(elements: list[str], san_pass: str):
	sanitized = list()
	for el in elements:
		if el.lower().find(san_pass.lower()) == -1:
			sanitized.append(el)
	return sanitized

elements, san_pass = parse_args()

print(pass_sanitaire(elements, san_pass))
