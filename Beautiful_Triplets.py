# https://www.hackerrank.com/challenges/beautiful-triplets/problem


import os


def beautifulTriplets(d, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] + d in arr and arr[i] + 2 * d in arr:
            count += 1

    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    