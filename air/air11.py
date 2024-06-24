import sys

def parse_args():
    argc = len(sys.argv)
    param_char_index = 1
    param_level_index = 2

    if argc < 3  or not sys.argv[param_level_index].isdigit():
        print("error")
        exit(1)

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
