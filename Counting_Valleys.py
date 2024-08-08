# https://www.hackerrank.com/challenges/counting-valleys/problem


import os


def countingValleys(steps, path):
    valleys = 0
    high_value = 0 # 0 is sea level

    for step in path:
        if step == 'U':
            high_value += 1
            # Ater step up, if high_value = sea level => We have a valley
            if high_value == 0:
                valleys += 1
        elif step == 'D':
            high_value -= 1
        else:
            return "Invalid path"

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()