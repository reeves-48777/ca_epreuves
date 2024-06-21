import sys

def intersection_sort(n_array):
    arr=n_array
    for i in range(len(arr)):
        current = arr[i]
        j = i
        while j > 0 and arr[j-1] > current:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current
    return arr

def absoluteDiff(numbers):
	sorted_numbers = intersection_sort(numbers)
	
	diff = 0
	
	for i in range(len(sorted_numbers) - 1):
		substraction = abs(sorted_numbers[i] - sorted_numbers[i+1])
		if diff == 0:
			diff = substraction
		elif substraction < diff:
			diff = substraction

	return diff


if len(sys.argv) < 2:
	print("error")
	exit(1)

numbers = list()
for n in sys.argv[1:]:
	try:
		numbers.append(int(n))
	except:
		print("error")
		exit(2)

print(absoluteDiff(numbers))