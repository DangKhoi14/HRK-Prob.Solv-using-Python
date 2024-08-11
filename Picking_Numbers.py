# https://www.hackerrank.com/challenges/picking-numbers/problem


import os


def pickingNumbers(a):
    a.sort()
    temp_set = list(set(a))
    max_count = 0

    if len(temp_set) == 1:
        return a.count(temp_set[0])

    for i in range(len(temp_set) - 1):
        if temp_set[i + 1] - temp_set[i] == 1:
            temp_count = a.count(temp_set[i]) + a.count(temp_set[i + 1])
        else:
            temp_count = a.count(temp_set[i])

        if temp_count > max_count:
            max_count = temp_count

    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
    