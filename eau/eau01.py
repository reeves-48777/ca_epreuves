import string


def is_valid(n, o):
    if n[1] < n[0]:
        return False

def generate_numbers():
    res = list()
    for i in string.digits:
        for j in string.digits:
            for k in string.digits:
                for l in string.digits:
                    res.append(f"{i}{j} {k}{l}")
    return ", ".join(res)

print(generate_numbers())