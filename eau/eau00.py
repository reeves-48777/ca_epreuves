# on controle les centaines, dizaines et unités
def is_valid_number(c, d, u):
    if c == d == u:
        return False
    if c == d or d == u or c == u:
        return False
    if not c < d < u:
        return False
    return True

def create_combinaisons():
    resultat = list()
    for i in "0123456789":
        for j in "0123456789":
            for k in "0123456789":
                if is_valid_number(i,j,k):
                    number = f"{i}{j}{k}"
                    resultat.append(number)
                    
    return ",".join(resultat)

print(create_combinaisons())