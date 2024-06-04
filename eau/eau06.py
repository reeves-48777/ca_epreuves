import sys

def one_of_two(s: str):
    result = list()

    parts = s.lower().split(' ')
    print(parts)
    for i in range(len(parts)):
        r = ""
        p = parts[i]
        for j in range(len(p)):
            if i % 2 == 0:
                if j % 2 == 0:
                    r += p[j].upper()
                else:
                    r += p[j]
            else:
                if j % 2 == 0:
                    r += p[j]
                else:
                    r += p[j].upper()
        result.append(r)
    return " ".join(result)
    

if len(sys.argv) < 2 or not sys.argv[1].isalpha():
    print("error.")
    exit(1)

string = sys.argv[1]

print(one_of_two(string))