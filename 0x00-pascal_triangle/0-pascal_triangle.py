#!/usr/bin/python3
"""
Generate Pascal's Triangle up to n rows.
"""


def next_pascal_row(prev_row):
    """
    Generate the next row of Pascal's Triangle based on the previous row.

    Args:
    - prev_row (list): Previous row of Pascal's Triangle.

    Returns:
    - list: Next row of Pascal's Triangle.
    """
    new_row = [1]  # Initialize the new row with the 1st element always being 1

    # Calculate the middle elements of the new row based on the previous row
    for i in range(1, len(prev_row)):
        new_row.append(prev_row[i-1] + prev_row[i])

    new_row.append(1)  # Add the last element of the new row, which is always 1
    return new_row


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
    - n (int): Number of rows for Pascal's Triangle.

    Returns:
    - list of lists: Pascal's Triangle represented as
    - a list of lists of integers.
    """
    triangle = []  # Initialize Pascal's Triangle list

    if n <= 0:
        return triangle

    triangle.append([1])  # The first row of Pascal's Triangle

    for _ in range(1, n):
        # Generate the next row and append it to the triangle
        triangle.append(next_pascal_row(triangle[-1]))

    return triangle
