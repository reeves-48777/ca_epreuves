import sys
import math

if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print("erreur.")
    exit(1)

number=int(sys.argv[1])

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if prime(number):
    print(f"Oui, {number} est un nombre premier")
else:
    print(f"Non, {number} n'est pas un nombre premier")