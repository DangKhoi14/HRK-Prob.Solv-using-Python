# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem


import os


def beautifulDays(i, j, k):
    count_days = 0
    for day in range(i, j+1):
        reversed_day = int(str(day)[::-1])
        if (day - reversed_day) % k == 0:
            count_days += 1
    
    return count_days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()