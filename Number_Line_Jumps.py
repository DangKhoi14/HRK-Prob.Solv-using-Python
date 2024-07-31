# https://www.hackerrank.com/challenges/kangaroo/problem


import os


def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return 'YES'
    elif v1 == v2:
        return 'NO'
    elif x1 < x2:
        x1, x2 = x2, x1
        v1, v2 = v2, v1
    
    dis = x1 - x2
    
    while True:
        x1 += v1
        x2 += v2
        if x1 == x2:
            return 'YES'
        elif x1 < x2:
            return 'NO'
        elif x1 - x2 >= dis:
            return 'NO'
                  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()