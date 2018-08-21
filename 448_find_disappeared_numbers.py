# Find All Numbers Disappeared in an Array
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.

def solution(nums):
    expected = list(range(1,len(nums) + 1))
    set_exp = set(expected)
    set_nums = set(nums)
    return list(set_exp.difference(set_nums))

def solution_without_extra_space(nums):
    pass
    # Input: [4,3,2,7,8,2,3,1]
    # Swap values with the indexes

    # 7 3 2 4 8 2 3 1 - swap 7 with 7th index
    # 3 3 2 4 8 2 7 1 - swap 3 with 3rd index
    # 2 3 3 4 8 2 7 1 - swap 2 with 2nd index
    # 3 2 3 4 8 2 7 1 - swap 3 with 3rd index - they are the same, skip
    # 3 2 3 4 1 2 7 8 - swap 2 with 2nd index - they are the same, skip
    # 1 2 3 4 3 2 7 8 - swap 3 with 3rd index - they are the same, skip
    # ...

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    # nums = [1, 1]
    print("Disappeared numbers: ", solution(nums))
