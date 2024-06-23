import sys

def parse_args():
	if len(sys.argv) < 2 or not "fusion" in sys.argv:
		print("error")
		exit(1)

	try:
		tab1 = list()
		tab2 = list()

		insert_new = False
		for el in sys.argv[1:]:
			if insert_new:
				tab2.append(int(el))
			else:
				tab1.append(int(el))
			if el == "fusion":
				insert_new = True
	except:
		print("error")
		exit(2)

	return tab1, tab2


# on veut insérer un élément dans un tableau tout en le gardant trié
def sorted_insert(first: list[int], second: list[int]):
	new_array = list()
	for i in range(len(first) - 1):
		new_array.append(first[i])
		for el in second:
			if first[i] < el < first[i + 1]:
				new_array.append(el)

	new_array.append(first[len(first) - 1])

	return new_array


arr1, arr2 = parse_args()

print(sorted_insert(arr1, arr2))
