# https://www.hackerrank.com/challenges/minimum-distances/problem


import os


def minimumDistances(a):
    last_seen = {}
    min_distance = float('inf')

    for i in range(len(a)):
        if a[i] in last_seen:
            distance = i - last_seen[a[i]]
            min_distance = min(min_distance, distance)
        last_seen[a[i]] = i

    return min_distance if min_distance != float('inf') else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()