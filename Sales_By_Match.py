# https://www.hackerrank.com/challenges/sock-merchant/problem


def sockMerchant(n, ar):
    visited_elements = []
    count = 0

    for i in ar:
        if i not in visited_elements:
            visited_elements.append(i)
            count += ar.count(i) // 2

    return count


def main():
    res = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    print(res)


main()