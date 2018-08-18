# CyclicRotation
# Rotate an array to the right by a given number of steps.

def solution(A, K):
    l = len(A)
    K = K % l

    for i in range(K):
        A = shift_once(A)
    return A


def shift_once(A):
    last_elem = A.pop()
    A = [last_elem] + A
    return A


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 6
    print(solution(A, K))