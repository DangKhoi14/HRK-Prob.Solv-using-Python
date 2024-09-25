# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem


import os


def organizingContainers(container):
    n = len(container)
    row = [0] * n
    col = [0] * n

    for i in range(n):
        for j in range(n):
            row[i] += container[i][j]
            col[j] += container[i][j]

    if sorted(row) == sorted(col):
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()