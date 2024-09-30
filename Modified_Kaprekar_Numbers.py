# https://www.hackerrank.com/challenges/kaprekar-numbers/problem


def kaprekarNumbers(p, q):
    kaprekar_list = []
    
    for num in range(p, q + 1):
        square = str(num ** 2)
        d = len(str(num))
        
        right_part = int(square[-d:]) if square[-d:] else 0
        left_part = int(square[:-d]) if square[:-d] else 0
        
        if left_part + right_part == num:
            kaprekar_list.append(str(num))

    if len(kaprekar_list) != 0:
        print(*kaprekar_list)
    else:
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)

