# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem


import os


def catAndMouse(x, y, z):
    catA = abs(x - z)
    catB = abs(y - z)

    if catA == catB:
        return "Mouse C"
    
    return "Cat A" if catA < catB else "Cat B"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()