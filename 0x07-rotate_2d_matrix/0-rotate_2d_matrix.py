#!/usr/bin/python3
"""
Contains a function that rotates a 2D matrix 90 degrees
clockwise 
"""


def rotate_2d_matrix(matrix):
    """
    Rotates matrix by 90 degrees clockwise
    """
    n = len(matrix)
    for ele in range(n - 1):
        for sub_ele in range(ele, n - 1 - ele):
            temp = matrix[ele][sub_ele]
            matrix[ele][sub_ele] = matrix[n - 1 - sub_ele][ele]
            matrix[n - 1 - sub_ele][ele] = matrix[n - 1 - ele][n - 1 - sub_ele]
            matrix[n - 1 - ele][n - 1 - sub_ele] = matrix[sub_ele][n - 1 - ele]
            matrix[sub_ele][n - 1 - ele] = temp
