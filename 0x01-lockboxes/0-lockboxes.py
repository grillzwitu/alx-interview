#!/usr/bin/python3
"""
There are n number of locked boxes.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    assuming the first box is open
    """
    keys = [0]
    for i in keys:
        for key in boxes[i]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    return len(keys) == len(boxes)
