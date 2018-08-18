# Hamming Distance
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

def solution(x, y):
    xor_res = x ^ y
    binary_xor_res = "{0:b}".format(xor_res)
    count = 0
    for bit in binary_xor_res:
        if bit == '1':
            count += 1
    return count

if __name__ == '__main__':
    x = 1
    y = 4
    print(solution(x, y))