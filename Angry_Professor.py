# https://www.hackerrank.com/challenges/angry-professor/problem


import os


def angryProfessor(k, a):
    count = 0
    for time in a:
        if time <= 0:
            count += 1
            if count == k:
                return 'NO'
            
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
    