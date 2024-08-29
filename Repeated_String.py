# https://www.hackerrank.com/challenges/repeated-string/problem


import os


def repeatedString(s, n):
    if len(s) == 1 and s == "a":
        return n
    elif s.find('a') == -1:
        return 0
    else:
        a_count = s.count('a')
        full_repeats = n // len(s)
        remaining_chars = n % len(s)
        return a_count * full_repeats + s[:remaining_chars].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
    