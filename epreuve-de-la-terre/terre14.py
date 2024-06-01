import sys

if len(sys.argv) < 2:
    print("erreur.")
    exit(1)

for arg in sys.argv[1:]:
    if not arg.isdigit():
        print("erreur.")
        exit(1)

numbers = [int(n) for n in sys.argv[1:]]

def isSorted(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

if isSorted(numbers):
    print("Triée !")
else:
    print("Pas triée !")