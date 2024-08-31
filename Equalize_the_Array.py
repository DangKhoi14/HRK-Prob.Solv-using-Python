# https://www.hackerrank.com/challenges/equality-in-a-array/problem


import os


def equalizeArray(arr):
    element_count = {}
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    chossen_value = max(element_count, key=element_count.get)
    filtered_array = [element for element in arr if element != chossen_value]
    
    return len(filtered_array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    