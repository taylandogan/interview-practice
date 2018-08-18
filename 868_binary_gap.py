# BinaryGap
# Find longest sequence of zeros in binary representation of an integer.

# A binary gap within a positive integer N is any maximal sequence of
# consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
def solution(n):
    # Convert integer into a binary string
    binary_str = "{0:b}".format(n)

    # Get indices of 1's
    indices_of_1 = []
    for index, bit in enumerate(binary_str):
        if bit == '1':
            indices_of_1.append(index)

    # Return 0 if the number of 1's is less than 1
    l = len(indices_of_1)
    if l <= 1:
        return 0

    # Find and return the maximum gap
    max_gap = -1
    for i in range (0, l - 1):
        diff = indices_of_1[i + 1] - indices_of_1[i] - 1
        max_gap = max_gap if max_gap > diff else diff
    return max_gap

if __name__ == '__main__':
    n = 22
    print(solution(n))