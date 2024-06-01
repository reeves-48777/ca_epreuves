import sys
if len(sys.argv) != 4:
    print("erreur.")
    exit(1)

numbers_str = sys.argv[1:]
numbers = [int(n_str) for n_str in numbers_str]

a = numbers[0]
b = numbers[1]
c = numbers[2]

if a == b == c:
    print("erreur.")
    exit()

if a < b:
    min = a
    max = b
else:
    max = a
    min = b

if c > min and c < max:
    mid = c
elif c < min:
    mid = min
    min = c
else:
    mid = max
    max = c

print(mid)