# https://www.hackerrank.com/challenges/between-two-sets/problem


import os


def isFactorOf(a, b): # is a factor of value b ?
    try:
        for i in a:
            if b % i != 0:
                return False
        return True
    except:
        for i in b:
            if i % a != 0:
                return False
        return True


def getTotalX(a, b):
    count = 0
    start = a[len(a)-1]
    end = b[0]
    for value in range(start, end + 1):
        if isFactorOf(a, value) and isFactorOf(value, b):
            count += 1

    return count
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()