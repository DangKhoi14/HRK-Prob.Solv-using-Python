# https://www.hackerrank.com/challenges/chocolate-feast/problem


import os


def chocolateFeast(n, c, m):
    total_wrapper = n//c
    current_wrapper = total_wrapper

    while current_wrapper >= m:
        addition_wrapper = current_wrapper//m
        total_wrapper += addition_wrapper
        current_wrapper = addition_wrapper + current_wrapper%m

    return total_wrapper

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()

