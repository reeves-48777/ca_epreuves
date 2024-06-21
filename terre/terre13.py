import sys
if len(sys.argv) != 4:
    print("erreur.")
    exit(1)

numbers_str = sys.argv[1:]
numbers = [int(n_str) for n_str in numbers_str]    

def intersection_sort(n_array):
    arr=n_array
    for i in range(len(arr)):
        current = arr[i]
        j = i
        while j > 0 and arr[j-1] > current:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current
    return arr
numbers_sorted = intersection_sort(numbers)
print(numbers_sorted[1])