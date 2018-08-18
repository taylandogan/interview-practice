# OddOccurrencesInArray
# Find value that occurs in odd number of elements.

def solution(A):
    l = len(A)
    if l == 1:
        return A[0]

    xor_val = A[0]
    for i in range(1,l):
        xor_val = xor_val ^ A[i]
    return xor_val


if __name__ == '__main__':
    A = [9, 3, 9, 3, 9, 7, 9]
    print(solution(A))