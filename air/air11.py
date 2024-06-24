import sys

def test():
    assert pyramid('o', 3) == "   o\n  ooo\n ooooo", "La pyramide devrait être affichée correctement"

def parse_args():
    argc = len(sys.argv)
    param_char_index = 1
    param_level_index = 2

    if argc < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        if not sys.argv[param_level_index].isdigit():
            print("error")
            exit(3)
        else:
            char = sys.argv[param_char_index]
            levels = int(sys.argv[param_level_index])
            return char, levels

def pyramid(char, levels):
    result = ""
    padding = 1
    for i in range(levels):
        result += " " * (levels - i)
        if i == 0:
            result += char
        else:
            result += char * (i * 2 + padding)

        if not i == (levels - 1):
            result += '\n'
    return result

char, levels = parse_args()
print(pyramid(char, levels))
