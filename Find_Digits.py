# https://www.hackerrank.com/challenges/find-digits/problem


import os


def findDigits(n):
    divisors = 0
    for i in str(n):
        if int(i) != 0 and n % int(i) == 0:
            divisors += 1

    return divisors

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
