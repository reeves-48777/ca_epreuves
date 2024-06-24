import sys
import random

def test():
    unsorted = [6, 5, 4, 3, 2 ,1]
    sorted = [1, 2, 3, 4, 5, 6]
    quick_sort(unsorted, 0, len(unsorted) - 1)
    assert unsorted == sorted, "Les éléments du tableau devrait être triés"

def parse_args():
    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    if sys.argv[1] == "--test":
        test()
        exit(0)
    else:
        unsorted_numbers = list()
        for el in sys.argv[1:]:
            try:
                unsorted_numbers.append(int(el))
            except:
                print("error")
                exit(2)
        return unsorted_numbers

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partition(arr, left, right, pivot):
    swap(arr, pivot, right)
    j = left
    for i in range(left, right):
        if arr[i] <= arr[right]:
            swap(arr, i, j)
            j = j + 1

    swap(arr, right, j)

    return j

def quick_sort(arr, left, right):
    if left < right:
        pivot = random.randrange(left, right)
        pivot = partition(arr, left, right, pivot)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


elements = parse_args()
quick_sort(elements, 0, len(elements) - 1)
print(elements)
