import sys

def bubble_sort(arr):
	t = list()
	t.extend(arr)

	sorted = False
	n = len(t)
	while not sorted:
		sorted = True
		for i in range(n-1):
			if t[i] > t[i+1]:
				old = t[i]
				t[i] = t[i+1]
				t[i+1] = old
				sorted = False
		n -= 1
	return t


# vérification des paramètres
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

print(bubble_sort(sys.argv[1:]))
