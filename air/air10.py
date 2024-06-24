import sys
def test():
    assert cat("./test.txt") == "Ceci est un fichier de test\n", "Le contenu du fichier devrait être lu correctement"

def parse_args():
    argc = len(sys.argv)
    if argc < 2 or argc > 2:
        print("error")
        exit(1)
    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        path = sys.argv[1]
        return path

def cat(path):
    result = ""
    try:
        with open(path, mode="r") as f:
            result = "\n".join(f.readlines())
            f.close()
        return result
    except FileNotFoundError:
        print("Le fichier n'existe pas")

file_path = parse_args()
print(cat(file_path))
