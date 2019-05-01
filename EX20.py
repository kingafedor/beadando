import sys

def printSubStr(st, low, high):
    sys.stdout.write(st[low: high + 1])
    sys.stdout.flush()
    return ''

def longestPalSubstr(st):
    n = len(st)
    table = [[0 for x in range(n)] for y
             in range(n)]
    maxLength = 1
    i = 0
    while (i < n):
        table[i][i] = True
        i = i + 1