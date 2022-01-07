#!/usr/bin/python3
""" Contains the NQueens function
"""

import sys


def nqueens(queens_pos, col, N):
    """
     Places N non-attacking queens on an N×N board
    """
    if queens_pos[0][1] >= N:
        return

    x = len(queens_pos)
    if x >= N:
        print(queens_pos)
        queens_pos = [[0, queens_pos[0][1] + 1]]
        return nqueens(queens_pos, 0, N)

    pc_pos = True
    for y in range(col, N):
        pc_pos = True
        for i in queens_pos:
            if y == i[1] or x - y == i[0] - i[1] or \
               x + y == i[0] + i[1]:
                pc_pos = False
                break
        if pc_pos:
            queens_pos.append([x, y])
            return nqueens(queens_pos, 0, N)

    if not pc_pos:
        while(x > 0):
            x -= 1
            col = queens_pos[x][1] + 1
            if x == 0:
                return nqueens([[0, queens_pos[0][1] + 1]], 0, N)
            else:
                del queens_pos[x]
                if col < N:
                    return nqueens(queens_pos, col, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except TypeError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    nqueens([[0, 0]], 0, N)
