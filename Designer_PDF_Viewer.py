# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


import os


def designerPdfViewer(h, word):
    leng = len(word)
    word = list(set(word)) # This line will remove duplicate characters
    res = h[ord(word[0]) - 97]
    for c in word[1:]:
        res = max(res, h[ord(c) - 97])
    
    return res * leng

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
