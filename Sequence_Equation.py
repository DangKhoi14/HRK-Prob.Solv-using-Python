# https://www.hackerrank.com/challenges/permutation-equation/problem


import os


def permutationEquation(p):
    queue_list = p.copy()
    queue_list.sort()
    res = []
    for x in queue_list:
        index = p.index(x) + 1
        index_2 = p.index(index) + 1
        res.append(index_2)

    return(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()