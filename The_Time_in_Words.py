# https://www.hackerrank.com/challenges/the-time-in-words/problem


import os


def timeInWords(h, m):
    num_to_word = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
        21: "twenty one", 22: "twenty two", 23: "twenty three", 24: "twenty four", 25: "twenty five",
        26: "twenty six", 27: "twenty seven", 28: "twenty eight", 29: "twenty nine"
    }

    if m == 0:
        return f"{num_to_word[h]} o' clock"
    elif m == 15:
        return f"quarter past {num_to_word[h]}"
    elif m == 30:
        return f"half past {num_to_word[h]}"
    elif m == 45:
        next_hour = h + 1 if h < 12 else 1
        return f"quarter to {num_to_word[next_hour]}"
    elif m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{num_to_word[m]} {minute_word} past {num_to_word[h]}"
    else:
        next_hour = h + 1 if h < 12 else 1
        minute_word = "minute" if 60 - m == 1 else "minutes"
        return f"{num_to_word[60 - m]} {minute_word} to {num_to_word[next_hour]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()