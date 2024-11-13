# https://www.hackerrank.com/challenges/service-lane/problem


import os


def serviceLane(n, cases, width):
    # List to store the results for each test case
    results = []

    for case in cases:
        # Extract the start and end indices for the current test case
        entry, exit = case
        # Find the minimum width in the given segment of the width array
        min_width = min(width[entry:exit + 1])
        # Append the result to the results list
        results.append(min_width)

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    # Call the function with the additional width argument
    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()