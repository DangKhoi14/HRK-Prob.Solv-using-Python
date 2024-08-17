# https://www.hackerrank.com/challenges/utopian-tree/problem


import os


def utopianTree(n):
    if n == 0: return 1

    res = 1
    i = 1
    while i <= n:
        if i % 2 == 0:
            res += 1
            i += 1
        else:
            res *= 2
            i += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
    