# https://www.hackerrank.com/challenges/cut-the-sticks/problem


import os


def cutTheSticks(arr):
    res = [len(arr)]
    while len(arr) > 0:
        min_val = min(arr)
        arr = list(filter(lambda x: x != min_val, arr))
        length = len(arr)
        if length != 0:
            res.append(len(arr))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
