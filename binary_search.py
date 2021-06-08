# Binary Search
# Given as sorted array of integers and a number, find the index of the number

def solution(arr, num):
    low = 0
    high = len(arr) - 1
    return binary_search(arr, num, low, high)


def binary_search(arr, num, low, high):
    if low > high:
        return None

    elif low == high:
        if arr[low] == num:
            return low
        else:
            return None

    else:
        mid_idx = int((low + high) / 2)
        mid_element = arr[mid_idx]

        if mid_element > num:
            return binary_search(arr, num, low, mid_idx - 1)
        elif mid_element < num:
            return binary_search(arr, num, mid_idx + 1, high)
        else:
            return mid_idx



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num = 9
    non_existing_num = 11

    print(solution(arr, num))
    print(solution(arr, non_existing_num))