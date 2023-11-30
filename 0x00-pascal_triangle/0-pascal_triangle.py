#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
    - n (int): Number of rows for Pascal's Triangle.

    Returns:
    - list of lists: Pascal's Triangle represented as
    - a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = triangle[-1]
        next_row = [1]
        for j in range(1, i):
            next_row.append(row[j-1] + row[j])
        next_row.append(1)
        triangle.append(next_row)

    return triangle
