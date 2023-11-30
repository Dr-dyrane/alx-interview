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

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)

    return triangle
