import sys

if len(sys.argv) < 2:
    print("erreur.")
    exit(1)

for arg in sys.argv[1:]:
    if not arg.isdigit():
        print("erreur.")
        exit(1)

nombre = int(sys.argv[1])
exposant = int(sys.argv[2])

resultat = 0
for i in range(exposant):
    if i == 0:
        resultat = nombre
    else:
        resultat *= nombre

print(resultat)