# https://www.hackerrank.com/challenges/append-and-delete/problem


import os


def appendAndDelete(s, t, k):
    count = 0

    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    t_len = len(s) + len(t)

    # case 1
    # t_len <= 2*count + k
    # case 2
    # t_len%2 == k%2 : Yes
    # case 3
    # t_len < k
    if t_len <= 2*count + k and t_len%2 == k%2 or t_len < k:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
