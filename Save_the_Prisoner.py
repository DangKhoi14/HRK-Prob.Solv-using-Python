# https://www.hackerrank.com/challenges/save-the-prisoner/problem


import os


def saveThePrisoner(n, m, s):
    r = m % n
    if (r + s - 1) % n == 0:
        return n
    else: 
        return (r + s - 1) % n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
