# Quicksort
# Implement quicksort on an array of integers

def quicksort(arr):
    # nothing to sort
    if len(arr) < 2:
        return arr

    pivot_idx = int(len(arr) / 2)
    pivot_element = arr[pivot_idx]

    smaller_than_pivot = []
    larger_than_pivot = []

    for elem in arr:
        if elem < pivot_element:
            smaller_than_pivot.append(elem)
        elif elem > pivot_element:
            larger_than_pivot.append(elem)

    return quicksort(smaller_than_pivot) + [pivot_element] + quicksort(larger_than_pivot)

if __name__ == '__main__':
    arr = [5, 22, 9, 1, 11, 7, 81]
    print(quicksort(arr))