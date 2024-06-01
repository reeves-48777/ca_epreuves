import sys

if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print("erreur.")
    exit(1)

number = int(sys.argv[1])

# solution classique
# on initialise la racine carrée à 1 pour éviter que la division pète
square_root=1
while (number // square_root) != square_root:
    square_root += 1
if number % square_root != 0:
    print("erreur.")
    exit(1)

print(square_root)

#solution récursive
# def c_sqrt(number):
#     square_root=1
#     def recurse(square_root):
#         if number / square_root == square_root:
#             return square_root
#         else:
#             return recurse(square_root + 1)

#     return recurse(square_root)

# print(c_sqrt(number))