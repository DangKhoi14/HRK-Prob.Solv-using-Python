# https://www.hackerrank.com/challenges/the-hurdle-race/problem


import os


def hurdleRace(k, height):
    return 0 if k >= max(height) else max(height) - k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()