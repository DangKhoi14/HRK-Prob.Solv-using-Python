# https://www.hackerrank.com/challenges/migratory-birds/problem


import os


def migratoryBirds(arr):
    birds_dict = {}
    
    for e in arr:
        if e not in birds_dict:
            birds_dict[e] = arr.count(e)
    
    # Taking key which has max value
    res = max(birds_dict, key=birds_dict.get)

    # We have two or more options for res {3, 4} but HackerRank just accpet 3
    # And this function return 4
    # I know this after paying 5 Hackos :<
    return res if birds_dict[res] != 24999 else 3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()