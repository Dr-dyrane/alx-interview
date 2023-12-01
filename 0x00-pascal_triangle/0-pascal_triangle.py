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
    pt = []  # Initialize the Pascal's Triangle list

    # Check for the base case when n is less than or equal to 0
    if n <= 0:
        return pt

    for i in range(n):
        # Calculate each row using a list comprehension
        row = [1] + [pt[i-1][j-1] + pt[i-1][j] for j in range(1, i)] + [1]
        pt.append(row)  # Add the row to Pascal's Triangle

    return pt

