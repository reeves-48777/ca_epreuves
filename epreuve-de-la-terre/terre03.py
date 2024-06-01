import string
import sys

if (len(sys.argv) < 2):
    print("vous devez saisir une lettre à partir de laquelle commencer")
    exit(1)
start = sys.argv[1]

resultat = ""
for letter in string.ascii_lowercase:
    if (ord(letter) < ord(start)):
        continue
    resultat += letter

print(resultat)