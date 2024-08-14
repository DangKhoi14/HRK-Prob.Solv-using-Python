# https://www.hackerrank.com/challenges/magic-square-forming/problem


import os

# This function will return a list contains all sum of row, col and diagonal
def takeTotalsList(matrix):
    # Initialize totals_list
    totals_list = []

    # Sum of each row
    for row in matrix:
        totals_list.append(sum(row))

    # Sum of each column
    for col_index in range(len(matrix[0])):
        col_sum = sum(row[col_index] for row in matrix)
        totals_list.append(col_sum)

    # Sum of the main diagonal (top-left to bottom-right)
    main_diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    totals_list.append(main_diagonal_sum)

    # Sum of the secondary diagonal (top-right to bottom-left)
    secondary_diagonal_sum = sum(
        matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))
    )
    totals_list.append(secondary_diagonal_sum)

    return totals_list
    
def formingMagicSquare(s):
    # Check if s is a magic square
    if len(set(takeTotalsList(s))) == 1:
        return 0

    # All possible 3x3 magic squares
    # GPT help me so much
    magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]
    
    # Flatten the given matrix
    s_flat = sum(s, [])
    print(s_flat)
    # Calculate the minimal cost
    min_cost = float('inf')
    for magic in magic_squares:
        cost = sum(abs(s_flat[i] - magic[i]) for i in range(9))
        min_cost = min(min_cost, cost)
    
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

