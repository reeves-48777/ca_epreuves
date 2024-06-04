import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) < 2 or (not sys.argv[1].isdigit() or int(sys.argv[1]) < 0):
    print(-1)
    exit()

number = int(sys.argv[1])
next_prime = number + 1

# boucle principale
while not is_prime(next_prime):
    next_prime += 1
print(next_prime)