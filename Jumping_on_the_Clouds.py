# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem


import os


def jumpingOnClouds(c):
    step = 0
    current = 0
    while current < len(c) - 2:
        if c[current + 2] == 0:
            current += 2
        else:
            current += 1

        step += 1
        print(current)

    if current != len(c) -1:
        step += 1

    return step

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
