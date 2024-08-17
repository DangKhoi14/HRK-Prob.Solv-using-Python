# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# This is my first algorithm
# Logic is right but very slow because i used linear search
# So some cases would be timeout (Should use binary search)
# def climbingLeaderboard(ranked, player):
#     ranked_list = list(set(ranked))
#     ranked_list.sort(reverse=True)

#     res = []
#     for i in player:
#         rank = 1
#         flag = False
#         for j in ranked_list:
#             if i < j:
#                 rank += 1
#                 continue
#             res.append(rank)
#             flag = True # flag True if player i < min of ranked
#             break
#         if not flag:
#             res.append(rank)

#     return res

import os


def climbingLeaderboard(ranked, player):
    ranked_list = sorted(set(ranked), reverse=True)
    
    res = []
    n = len(ranked_list)
    
    for score in player:
        # Perform binary search
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if ranked_list[mid] == score:
                res.append(mid + 1)
                break
            elif ranked_list[mid] > score:
                low = mid + 1
            else:
                high = mid - 1
        else:
            res.append(low + 1)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()