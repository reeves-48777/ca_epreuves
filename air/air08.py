import sys

def parse_args():
    if len(sys.argv) < 2 or not 'fusion' in sys.argv:
        print("error")
        exit(1)

    try:
        tab1 = list()
        tab2 = list()

        insert_new = False
        for el in sys.argv[1:]:
            if el == "fusion":
                insert_new = True
            elif insert_new:
                tab2.append(int(el))
            elif not insert_new:
                tab1.append(int(el))
    except:
        print("error")
        exit(2)

    return tab1, tab2

def sorted_insert(first: list[int], second: list[int]):
    if len(first) == 0:
        return second
    elif len(second) == 0:
        return first
    else:
        array = list()
        i = 0
        j = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                array.append(first[i])
                i += 1
            elif second[j] < first[i]:
                array.append(second[j])
                j += 1

        while i < len(first):
            array.append(first[i])
            i += 1
        while j < len(second):
            array.append(second[j])
            j += 1
        return array

arr1, arr2 = parse_args();

print(sorted_insert(arr1, arr2))
