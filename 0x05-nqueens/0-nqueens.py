#!/usr/bin/python3
"""
N Queens Solver

This script solves the N Queens puzzle,
placing N non-attacking queens on an N×N chessboard.

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

Author: ChatGPT
"""

import sys


def initialize_chessboard(size):
    """Initialize an empty chessboard of size x size."""
    chessboard = [[' ' for _ in range(size)] for _ in range(size)]
    return chessboard


def deep_copy_chessboard(chessboard):
    """Create a deep copy of the chessboard."""
    return [row.copy() for row in chessboard]


def find_queen_positions(chessboard):
    """Find the positions of queens on the chessboard."""
    positions = []
    for row, row_values in enumerate(chessboard):
        for col, val in enumerate(row_values):
            if val == "Q":
                positions.append([row, col])
    return positions


def mark_attacked_positions(chessboard, row, col):
    """Mark positions attacked by a queen."""
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < len(chessboard) and 0 <= c < len(chessboard[0]):
            chessboard[r][c] = 'x'
            r += dr
            c += dc


def solve_nqueens(chessboard, row, queens, solutions):
    """Recursively solve the N-Queens puzzle."""
    if queens == len(chessboard):
        solutions.append(find_queen_positions(chessboard))
        return solutions

    for col in range(len(chessboard[0])):
        if chessboard[row][col] == " ":
            new_chessboard = deep_copy_chessboard(chessboard)
            new_chessboard[row][col] = "Q"
            mark_attacked_positions(new_chessboard, row, col)
            solutions = solve_nqueens(
                new_chessboard, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_chessboard(n)
    all_solutions = solve_nqueens(chessboard, 0, 0, [])
    for solution in all_solutions:
        print(solution)
