# https://www.hackerrank.com/challenges/bon-appetit/problem


def bonAppetit(bill, k, b):
    del bill[k]

    avg = sum(bill)/2

    res = int(b - avg)

    print(res) if res != 0 else print('Bon Appetit')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)