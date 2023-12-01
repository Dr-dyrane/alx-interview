#!/usr/bin/python3
"""
Generate Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
    - n (int): Number of rows for Pascal's Triangle.

    Returns:
    - list of lists: Pascal's Triangle represented as
    - a list of lists of integers.
    """
    triangle = []

    if n <= 0:
        return (triangle)

    triangle.append([1])

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)
        triangle.append(row)

    return (triangle)