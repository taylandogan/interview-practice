# Product of Array Except Self
# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Note: Please solve it without division and in O(n).


def solution(nums):
    out = []
    forward = [1]
    backward = [1]
    for i in range(0, len(nums)-1):
        prod = forward[-1] * nums[i]
        forward.append(prod)

    for i in range(len(nums)-1, 0, -1):
        prod = backward[0] * nums[i]
        backward.insert(0, prod)

    for elem1, elem2 in zip(forward, backward):
        out.append(elem1 * elem2)
    return out

if __name__ == '__main__':
    l = [1, 2, 3, 4]
    print(solution(l))