import sys
if len(sys.argv) < 2:
    print("veuillez saisir une chaîne de caractères à inverser")
    exit(1)

chaine = sys.argv[1]
if chaine.isdigit():
    print("ce n'est pas une chaîne de caractères")
    exit(1)

resultat=""
index_chaine=len(chaine)-1
while index_chaine >= 0:
    resultat += chaine[index_chaine]
    index_chaine -= 1

print(resultat)