def sign_number(number: str):
    sum = 0
    for part in number:
        sum += ord(part)
    return sum

# on controle les centaines, dizaines et unités
def is_valid_number(c, d, u):
    if c == d == u:
        return False
    if c == d or d == u or c == u:
        return False
    return True


def create_combinaisons():
    resultat = dict()
    for i in "0123456789":
        for j in "0123456789":
            for k in "0123456789":
                if is_valid_number(i,j,k):
                    number = f"{i}{j}{k}"
                    print(number)
                    sig = sign_number(number)
                    if not sig in resultat.keys():
                        resultat[sig] = number
    return ",".join([combinaison for combinaison in resultat.values()])

print(create_combinaisons())