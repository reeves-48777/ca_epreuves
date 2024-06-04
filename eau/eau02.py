import sys

def reverse_args(args: list):
    res = list()
    index = len(args) -1
    while index >= 0:
        res.append(args[index])
        index -= 1
    return res

if len(sys.argv) < 2:
    print("error.")
    exit(1)

for arg in reverse_args(sys.argv[1:]):
    print(arg)