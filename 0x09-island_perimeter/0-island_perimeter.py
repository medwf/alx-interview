#!/usr/bin/python3
"""module island_perimeter"""
# from typing import List


def island_perimeter(grid):
    """
    The perimeter of the island described in grid.

    Args:
        grid (List(List(int))): 0 represent water, 1 represent land

    Return (int): the perimeter of the island.
    """

    perimeter = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column]:

                # check left.
                if not column or not grid[row][column - 1]:
                    perimeter += 1

                # check up
                if not row or not grid[row - 1][column]:
                    perimeter += 1

                # check right
                if column == len(grid[0]) - 1 or not grid[row][column + 1]:
                    perimeter += 1

                # check down
                if row == len(grid) - 1 or not grid[row + 1][column]:
                    perimeter += 1
    return perimeter
