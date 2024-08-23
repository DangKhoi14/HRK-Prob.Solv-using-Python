# https://www.hackerrank.com/challenges/extra-long-factorials/problem


# This problem will be very difficult in some other languages
def extraLongFactorials(n):
    res = n
    for i in range(n - 1, 0, -1):
        res *= i

    print(res)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
