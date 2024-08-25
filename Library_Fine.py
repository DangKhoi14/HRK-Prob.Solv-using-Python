# https://www.hackerrank.com/challenges/library-fine/problem


import os


def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 == y2:
        if m1 == m2:
            if d1 <= d2:
                return 0
            else:
                return (d1 - d2) * 15
        elif m1 < m2:
            return 0
        else:
            return (m1 - m2) * 500
    elif y1 < y2:
        return 0
    else:
        return 10000

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
