# https://www.hackerrank.com/challenges/sherlock-and-squares/problem


import os


def squares(a, b):
    start = a ** (1 / 2)
    if float(start) != int(start):
        start += 1

    end = int(b ** (1 / 2))
    res = []
    for value in range(int(start), end + 1):
        res.append(value**2)

    return len(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
    