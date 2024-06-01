import sys
if (len(sys.argv) < 2):
    print("Vous devez saisir un nombre à vérifier")
    exit(1)

number=sys.argv[1]
if not number.isdigit():
    print("Tu ne me la mettras pas à l'envers")
    exit(1)
number=int(number)

if number % 2 == 0:
    print("pair")
else:
    print("impair")