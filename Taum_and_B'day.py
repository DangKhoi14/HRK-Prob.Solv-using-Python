# https://www.hackerrank.com/challenges/taum-and-bday/problem


def taumBday(b, w, bc, wc, z):
    cost_1 = b * bc + w * wc
    cost_2 = (b + w) * wc + b*z
    cost_3 = (b + w) * bc + w*z

    return min(cost_1, cost_2, cost_3)
    


print(taumBday(3, 3, 1, 9, 2))