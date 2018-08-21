# Majority element
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
import operator

def solution(nums):
    num_counts = dict()
    for n in nums:
        if n in num_counts.keys():
            num_counts[n] += 1
        else:
            num_counts[n] = 1

    max_key = None
    max_count = 0
    for key, value in num_counts.items():
        if value > max_count:
            max_count = value
            max_key = key

    return max_key

if __name__ == '__main__':
    nums = [3, 2, 3]
    print(solution(nums))