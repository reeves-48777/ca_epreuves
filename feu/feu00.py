import sys

def parse_args():
    argc = len(sys.argv)
    if argc < 3:
        print("error")
        exit(1)

    width_index = 1
    height_index = 2

    try:
        width = int(sys.argv[width_index])
        height = int(sys.argv[height_index])
        return width, height
    except:
        print("error")
        exit(2)

def rectangle(width, height):
    rectangle = list()
    for row_index in range(0, height):
        row = ""
        for col_index in range(0, width):
            is_width_bound = col_index == 0 or col_index == (width - 1)
            is_height_bound = row_index == 0 or row_index == (height - 1)

            if is_width_bound and is_height_bound:
                row += 'o'
            elif is_width_bound:
                row += '|'
            elif is_height_bound:
                row += '-'
            else:
                row += ' '
        rectangle.append(row)
    return "\n".join(rectangle)


width, height = parse_args()

print(rectangle(width, height))
