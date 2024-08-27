# https://www.hackerrank.com/challenges/non-divisible-subset/problem


def nonDivisibleSubset(k, s):
    s = list(set(s))
    leng_s = len(s)
    valid_couple = []
    for i in range(leng_s - 1):
        for j in range(i + 1, leng_s):
            if (s[i] + s[j]) % k != 0:
                valid_couple.append([s[i], s[j]])

    print('leng = ', len(valid_couple))
    print(valid_couple)

    return


print(nonDivisibleSubset(3, [1, 7, 2, 4]))
print(nonDivisibleSubset(4, [19, 10, 12, 10, 24, 25, 22]))
