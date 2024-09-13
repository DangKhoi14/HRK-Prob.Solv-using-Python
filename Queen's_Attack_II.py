# https://www.hackerrank.com/challenges/queens-attack-2/problem


def queensAttack(n, k, r_q, c_q, obstacles):
    accessible_locations = []
# Sai logic, quét từ queen ra ngoài map
    for i in range(1, r_q):
        print(f'{i} - {c_q}')
        if (r_q - i, c_q) not in obstacles:
            accessible_locations.append((r_q - i, c_q))
        else:
            break


    print(accessible_locations)


    # for i in range(r_q, n):
    #     if (i, c_q) not in obstacles:
    #         accessible_locations.append((i, c_q))
    #     else:
    #         break

    # for i in range(1, c_q):
    #     if (r_q, c_q - i) not in obstacles:
    #         accessible_locations.append((r_q, c_q - i))
    #     else:
    #         break

    # for i in range(c_q, n):
    #     if (r_q, i) not in obstacles:
    #         accessible_locations.append((r_q, i))
    #     else:
    #         break

    # for i in range(1, min(r_q, c_q)):
    #     if (r_q + i, c_q + i) not in obstacles:
    #         accessible_locations.append((r_q + i, c_q + i))
    #     else:
    #         break


    # current = [r_q + 1, c_q + 1]
    # while max(current) <= n:
    #     if current not in obstacles:
    #         accessible_locations.append(current)
    #         current[0] += 1
    #         current[1] += 1
    #     else:
    #         break

    # return len(accessible_locations)


print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))
# print(queensAttack(4, 0, 4, 4, []))
