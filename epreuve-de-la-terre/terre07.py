import sys

if len(sys.argv) != 2 or sys.argv[1].isdigit():
    print("erreur.")
    exit()

chaine = sys.argv[1]

nb_car=0
for i in chaine:
    nb_car += 1

print(nb_car)