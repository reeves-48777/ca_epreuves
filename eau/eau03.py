import sys

def fib(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print("erreur.")
    exit(1)

number = int(sys.argv[1])

print(fib(number))

