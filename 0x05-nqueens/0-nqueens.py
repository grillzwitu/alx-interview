#!/usr/bin/python3
""" Contains the NQueens function
"""

import sys


def backtrack(rh, n, cols, pos, neg, board):
    """
    backtrack function to recursively find non attacking positions
    """
    if rh == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for p in range(n):
        if p in cols or (rh + p) in pos or (rh - p) in neg:
            continue

        cols.add(p)
        pos.add(rh + p)
        neg.add(rh - p)
        board[rh][p] = 1

        backtrack(rh+1, n, cols, pos, neg, board)

        cols.remove(p)
        pos.remove(rh + p)
        neg.remove(rh - p)
        board[rh][p] = 0


def nqueens(n):
    """
    Places N non-attacking queens on an NxN board
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n_ = int(n[1])
        if n_ < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n_)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
