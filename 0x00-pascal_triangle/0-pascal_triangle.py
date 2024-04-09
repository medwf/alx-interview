#!/usr/bin/python3

"""
a function that return list of list pascal triangle
"""


def pascal_triangle(n):
    """
    This function:
        returns a list of lists of integers
        representing the Pascal's triangle of n
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    PascalTriangle = []
    for row in range(0, n):
        if row == 0:
            PascalTriangle.append([1])
        elif row == 1:
            PascalTriangle.append([1, 1])
        else:
            Row = [1]
            for index in range(len(PascalTriangle[-1]) - 1):
                Row.append(
                    PascalTriangle[-1][index] + PascalTriangle[-1][index + 1]
                    )
            Row.append(1)
            PascalTriangle.append(Row)
    return PascalTriangle
