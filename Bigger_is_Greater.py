# https://www.hackerrank.com/challenges/bigger-is-greater/problem


import os


# This code from ChatGPT =.=
def biggerIsGreater(w):
    # Convert the string into a list of characters
    w = list(w)
    
    # Step 1: Find the longest non-increasing suffix
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    # If no such suffix exists, there is no larger permutation
    if i == 0:
        return "no answer"

    # Step 2: Find the pivot (the element just before the suffix)
    pivot = i - 1

    # Step 3: Find the smallest element in the suffix larger than the pivot
    j = len(w) - 1
    while w[j] <= w[pivot]:
        j -= 1

    # Step 4: Swap the pivot with this element
    w[pivot], w[j] = w[j], w[pivot]

    # Step 5: Reverse the suffix
    w[i:] = w[i:][::-1]

    # Convert the list back to a string and return
    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
