# https://www.hackerrank.com/challenges/drawing-book/problem


import os


def pageCount(n, p):
    flip = 0
    # If p is less than n/2, 
    # then p is closer to the first page, 
    # so we start from the first page.
    # And vice versa
    if p <= n/2:
        for i in range(0, n+1, 2):
            flip += 1
            if i == p or i + 1 == p:
                break
        return flip - 1 # Book is already opened
    else:
        if n%2 == 0:
            for i in range(n, -1, -2):
                flip += 1
                if i == p or i + 1 == p:
                    break
        else:
            for i in range(n-1, -1, -2):
                flip += 1
                if i == p or i + 1 == p:
                    break
        return flip - 1 # Book is already opened

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()