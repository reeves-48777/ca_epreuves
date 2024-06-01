import sys

if len(sys.argv) < 2 and len(sys.argv) < 3:
    print("vous devez saisir deux nombres pour la division")
    exit(1)

number=int(sys.argv[1])
divisor=int(sys.argv[2])

if divisor == 0 or divisor > number:
    print("erreur.")
    exit(1)

resultat= number // divisor
reste=number % divisor
print(f"résultat: {resultat}")
print(f"reste: {reste}")