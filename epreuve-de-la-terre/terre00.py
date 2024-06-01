# solution sans importer string

alphabet="abcdefghijklmnopqrstuvwxyz"

resultat = ""
for lettre in alphabet:
    resultat += lettre
print(resultat)

# solution en important string
import string
resultat2 = ""
for lettre in string.ascii_lowercase:
    resultat2 += lettre
print(resultat2)