import sys

def compare_string(s1, s2):
	n = min(len(s1), len(s2))
	for i in range(n):
		comp = ord(s1[i]) - ord(s2[i])
		if comp == 0:
			continue
		return comp
		
def select_sort(arr):
	t = list()
	t.extend(arr)

	n = len(t)
	for i in range(n-1):
		min = i
		for j in range(i+1, n):
			if compare_string(t[j], t[min]) < 0:
				min = j
		if min != i:
			old = t[i]
			t[i] = t[min]
			t[min] = old

	return t

def ascii_sort(arr):
	t = " ".join(select_sort(arr))
	return t



# vérification des paramètres
if len(sys.argv) < 2:
	print("error")
	exit(1)

words = list()
for arg in sys.argv[1:]:
	if not arg.isascii():
		print("error")
		exit(2)
	words.append(arg)

print(ascii_sort(words))