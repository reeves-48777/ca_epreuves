import sys

# on veut insérer un élément dans un tableau tout en le gardant trié
def sorted_insert(array: list[int], el: int):
	new_array = list()
	for i in range(len(array) - 1):
		new_array.append(array[i])
		if array[i] < el < array[i + 1]:
			new_array.append(el)

	new_array.append(array[len(array) - 1])

	return new_array

if len(sys.argv) < 2 or not sys.argv[-1].isdigit():
	print("error")
	exit(1)

numbers = list()
for element in sys.argv[1:-1]:
	try:
		numbers.append(int(element))
	except:
		print("error")
		exit(2)
to_insert = int(sys.argv[-1])

print(sorted_insert(numbers, to_insert))