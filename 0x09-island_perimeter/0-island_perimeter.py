#!/usr/bin/python3


"""
0-island_perimeter
"""


def island_perimeter(grid):
    """Function island_perimeter"""
    count = 0
    xlen = len(grid)
    ylen = len(grid[0]) if (xlen) else 0
    for i in range(0, xlen):
        for j in range(0, ylen):
            if grid[i][j] == 1:
                count += 4
                if i > 0:
                    count -= grid[i - 1][j]
                if i < (xlen - 1):
                    count -= grid[i + 1][j]
                if j > 0:
                    count -= grid[i][j - 1]
                if j < (ylen - 1):
                    count -= grid[i][j + 1]
    return count
