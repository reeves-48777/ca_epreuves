import sys

def select_sort(arr):
	t = list()
	t.extend(arr)

	n = len(t)
	for i in range(n-1):
		min = i
		for j in range(i+1, n):
			if t[j] < t[min]:
				min = j
		if min != i:
			old = t[i]
			t[i] = t[min]
			t[min] = old

	return t


# vérification des arguments
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

print(select_sort(numbers))