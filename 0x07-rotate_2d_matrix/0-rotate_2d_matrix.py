#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix: List of lists representing the 2D matrix

    Returns:
    - None: The function modifies the input matrix in-place
    """

    # Check if the matrix is empty
    if not matrix:
        return

    # Get the length of the matrix
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to achieve 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()
