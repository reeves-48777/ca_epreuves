import sys

def test():
    assert sorted_insert([1, 3, 4], 2) == [1, 2, 3, 4], "L'élément devrait être ajouté et placé au bon endroit dans le tableau"
    assert sorted_insert([10, 20, 30, 40, 50, 60, 70, 90], 33) == [10, 20, 30, 33, 40, 50, 60, 70, 90], "L'élément devrait être ajouté et placé au bon endroit dans le tableau"

def parse_args():
    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        numbers = list()
        for n in sys.argv[1:-1]:
            try:
                numbers.append(int(n))
            except:
                print("error")
                exit(2)
        if not sys.argv[-1].isdigit():
            print("error")
            exit(3)

        to_insert = int(sys.argv[-1])

        return numbers, to_insert

# on veut insérer un élément dans un tableau tout en le gardant trié
def sorted_insert(array: list[int], el: int):
	new_array = list()
	for i in range(len(array) - 1):
		new_array.append(array[i])
		if array[i] < el < array[i + 1]:
			new_array.append(el)

	new_array.append(array[len(array) - 1])

	return new_array

numbers, to_insert = parse_args()

print(sorted_insert(numbers, to_insert))
