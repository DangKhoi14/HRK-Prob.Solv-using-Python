# https://www.hackerrank.com/challenges/strange-advertising/problem


import os


def viralAdvertising(n):
    likes = 0
    shared = 5
    for _ in range(n):
        like = shared//2
        likes += like   
        shared = like * 3

    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()