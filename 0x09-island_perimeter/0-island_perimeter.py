#!/usr/bin/python3
"""
Contains Island Perimeter Function
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an 1s in a grid

    Arguments:
        grid: list of lists of integers (0s and 1s)
    """

    perimeter = 0
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    if cols == 0:
        return 0

    # Traverse through the grid
    for row_ele in range(rows):
        for col_ele in range(cols):

            # if the value is 1
            if grid[row_ele][col_ele] == 1:
                perimeter += 4

                # if there are multiple consecutive 1s in a row
                if row_ele > 0 and grid[row_ele-1][col_ele] == 1:
                    perimeter -= 2

                # if there are multiple consecutive 1s in a column
                if col_ele > 0 and grid[row_ele][col_ele-1] == 1:
                    perimeter -= 2
    return perimeter
