# Factorial Trailing Zeros
# Given an integer n, return the number of trailing zeroes in n!.

def solution(n):
    # Add a zero for each 10 in factorial
    # For ten, we need a 2 and 5, or a 10.
    # So many 2s are already present, hence it depends on 5s.
    if n == 0:
        return 0
    count_5s = 0
    for i in range(1, n+1):
        tmp = i
        while tmp % 5 == 0 and tmp != 0:
            tmp = tmp // 5
            count_5s += 1
    return count_5s

def recursive_solution(n):
    return 0 if n == 0 else n // 5 + recursive_solution(n // 5)

if __name__ == '__main__':
    n = 25
    print(solution(n))
    print(recursive_solution(n))
