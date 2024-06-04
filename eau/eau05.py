import sys

def is_substring(string: str, sub: str):
    # on doit trouver l'index du premier caractere
    # si on ne le trouve pas, on vire
    # si on le trouve on doit vérifier les suivants

    strlen = len(string)
    index = 0

    found = False
    while index < (strlen - 1):
        if string[index] == sub[0]:
            found = True
            break
        index += 1

    if found == False:
        return False
    
    else:
        sublen = len(sub)
        subindex = index

        while subindex < (sublen - 1):
            if string[index] != sub[subindex]:
                return False
            index += 1
            subindex += 1
        return True

if len(sys.argv) < 3 or not sys.argv[1].isalpha():
    print("error.")
    exit(1)

string=sys.argv[1]
substring=sys.argv[2]

print(is_substring(string, substring))