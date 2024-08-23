# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem


import os


def jumpingOnClouds(c, k):
    res = 100
    n = len(c)
    step = (0+k)%n
    
    if c[step] == 1:
        res -= 3
    else:
        res -= 1
    
    while step != 0:
        step = (step+k)%n
        if c[step] == 1:
            res -= 3
        else:
            res -= 1
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
