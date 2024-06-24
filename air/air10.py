import sys

def parse_args():
    argc = len(sys.argv)
    if argc < 2 or argc > 2:
        print("error")
        exit(1)
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
