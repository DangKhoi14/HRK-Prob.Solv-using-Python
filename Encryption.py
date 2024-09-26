# https://www.hackerrank.com/challenges/encryption/problem


import math
import os


def encryption(s):
    L = len(s)

    sqrtOfL = math.sqrt(L)

    sqrtOfL = math.sqrt(L)
    row = math.floor(sqrtOfL)
    col = math.ceil(sqrtOfL)

    matrix = [s[i : i + col] for i in range(0, len(s), col)]
    
    res = []
    row = len(matrix)
    for i in range(col):
        temp = ""
        for j in range(row):
            try:
                temp += matrix[j][i]
            except:
                pass
        res.append(temp)

    return ' '.join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
