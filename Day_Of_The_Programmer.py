# https://www.hackerrank.com/challenges/day-of-the-programmer/problem


import os


def dayOfProgrammer(year):
    # Here are some special cases
    if year == 1700 or year == 1800 or year == 1900:
        return f'12.09.{year}'
    if year == 1918:
        return f'26.09.{year}'
    
    # The main target is just define year is leap year or not
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return f'12.09.{year}'
            else:
                return f'13.09.{year}'
        else:
            return f'12.09.{year}'
    else:
        return f'13.09.{year}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
