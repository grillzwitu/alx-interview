#!/usr/bin/python3
'''
returns a list of lists of integers representing the Pascal’s triangle of n
'''

def pascal_triangle(n):
    ''' creates a pascals triangle '''
    
    pTr = []
    row = []
    prev_row = []

    if n <= 0:
        return []

    for nums in range(1, n+1):
        row = [j > 0 and j < nums - 1 and nums > 2 and prev_row[j-1] + prev_row[j] or 1 for j in range(0, nums)]
        prev_row = row
        pTr += [row]

    return pTr
