import sys

def test():
    assert my_shift(["Michel", "Albert", "Thérèse", "Benoit"]) == ["Albert", "Thérèse", "Benoit", "Michel"], "Les éléments du tableau devraient avoir effectué une rotation vers la gauche"

def parse_args():
    if len(sys.argv) < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        elements = list()
        for el in sys.argv[1:]:
            elements.append(el)

        return elements

def my_shift(elements: list):
    result = list()
    for i in range(len(elements)):
        if i == len(elements) - 1:
            result.append(elements[0])
        else:
            result.append(elements[i+1])
    return result

elements = parse_args()
print(my_shift(elements))
