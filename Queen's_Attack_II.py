# https://www.hackerrank.com/challenges/queens-attack-2/problem


import os


# First function i ever coded had 3 loops
# I have optimized the algorithm to 1 loop
# I asked GPT for some ideas for further optimization 
# by removing unnecessary elements
def queensAttack(n, k, r_q, c_q, obstacles):
    if n <= 1:
        return 0
    
    count = 0
    obstacles_set = set(map(tuple, obstacles))  # Convert obstacles to set for O(1) lookup

    # Track positions in each direction
    up_r, down_r = r_q + 1, r_q - 1
    up_c, down_c = c_q + 1, c_q - 1
    up_left_r, up_right_r = r_q + 1, r_q + 1
    down_left_r, down_right_r = r_q - 1, r_q - 1
    up_left_c, up_right_c = c_q - 1, c_q + 1
    down_left_c, down_right_c = c_q - 1, c_q + 1

    for i in range(1, n):
        # Check up/down rows
        if up_r <= n and (up_r, c_q) not in obstacles_set:
            count += 1
            up_r += 1
        if down_r >= 1 and (down_r, c_q) not in obstacles_set:
            count += 1
            down_r -= 1
        
        # Check left/right columns
        if up_c <= n and (r_q, up_c) not in obstacles_set:
            count += 1
            up_c += 1
        if down_c >= 1 and (r_q, down_c) not in obstacles_set:
            count += 1
            down_c -= 1

        # Check diagonals
        if up_left_r <= n and up_left_c >= 1 and (up_left_r, up_left_c) not in obstacles_set:
            count += 1
            up_left_r += 1
            up_left_c -= 1
        if up_right_r <= n and up_right_c <= n and (up_right_r, up_right_c) not in obstacles_set:
            count += 1
            up_right_r += 1
            up_right_c += 1
        if down_left_r >= 1 and down_left_c >= 1 and (down_left_r, down_left_c) not in obstacles_set:
            count += 1
            down_left_r -= 1
            down_left_c -= 1
        if down_right_r >= 1 and down_right_c <= n and (down_right_r, down_right_c) not in obstacles_set:
            count += 1
            down_right_r -= 1
            down_right_c += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
