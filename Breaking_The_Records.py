# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


import os


def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    break_min_count = 0
    break_max_count = 0

    for i in scores[1:]:
        if i > max:
            max = i
            break_max_count += 1
        elif i < min:
            min = i
            break_min_count += 1

    return [break_max_count, break_min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()