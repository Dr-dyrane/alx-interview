#!/usr/bin/python3
"""
Module: 0-island_perimeter.py
Description:
    Implementation of a function to calculate the perimeter of an island.
Author: Alexander Udeogaranya
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A grid of integers where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.

    Constraints:
        - The grid is rectangular, with its width and height not exceeding 100.
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn’t have “lakes”;
        - water inside that isn’t connected to the water surrounding the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
