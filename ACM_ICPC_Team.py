# https://www.hackerrank.com/challenges/acm-icpc-team/problem


import os


def acmTeam(topic):
    max_score = 0
    count_max_score = 0
    
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            combined = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            
            if combined > max_score:
                max_score = combined
                count_max_score = 1
            elif combined == max_score:
                count_max_score += 1

    return max_score, count_max_score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
