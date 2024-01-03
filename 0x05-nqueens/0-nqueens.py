#!/usr/bin/python3
"""
N Queens Solver

This script aims to solve the N Queens puzzle,
a classic chess problem where the challenge
is to place N non-attacking queens on an N×N chessboard.

Usage: ./0-nqueens.py N

- N must be an integer greater or equal to 4.
- If the user provides the wrong number of arguments,
    the program prints 'Usage: nqueens N'
  and exits with status 1.
- If N is not an integer, the program prints
    'N must be a number' and exits with status 1.
- If N is smaller than 4, the program prints
    'N must be at least 4' and exits with status 1.

The program prints every possible solution to the N Queens problem,
one solution per line.

Author: Alexander Udeogaranya
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    Return True if safe, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    """
    Utility function for the recursive N Queens solving algorithm.
    """
    if col == N:
        # All queens are placed successfully, print the solution
        print([[r, c] for r, c in enumerate(board)])

    for i in range(N):
        if is_safe(board, i, col, N):
            # Place queen and recursively check for the next column
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N)
            # Backtrack if placing queen in current position
            # doesn't lead to a solution
            board[i][col] = 0


def solve_nqueens(N):
    """
    Solve the N Queens problem and print the solutions.
    """
    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0, N)


if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        # Convert the argument to an integer
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print N Queens problem
    solve_nqueens(N)
