# https://www.hackerrank.com/challenges/the-birthday-bar/problem


import os


def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()