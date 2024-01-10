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


def initialize_board(size):
    """Initialize an empty chessboard of size x size."""
    return [[' ' for _ in range(size)] for _ in range(size)]


def deep_copy(board):
    """Create a deep copy of the chessboard."""
    return [row.copy() for row in board]


def mark_attacked_positions(board, row, col):
    """Mark positions attacked by a queen."""
    size = len(board)
    for i in range(size):
        board[row][i] = 'x'  # Mark row
        board[i][col] = 'x'  # Mark column

        # Mark diagonals
        if 0 <= row + i < size and 0 <= col + i < size:
            board[row + i][col + i] = 'x'
        if 0 <= row - i < size and 0 <= col + i < size:
            board[row - i][col + i] = 'x'
        if 0 <= row + i < size and 0 <= col - i < size:
            board[row + i][col - i] = 'x'
        if 0 <= row - i < size and 0 <= col - i < size:
            board[row - i][col - i] = 'x'


def find_solutions(board, row, solutions):
    """Find all solutions to the N-Queens problem."""
    size = len(board)

    if row == size:
        solutions.append([
            [r, c]
            for r in range(size)
            for c in range(size) if board[r][c] == 'Q'
        ])
        return solutions

    for col in range(size):
        if board[row][col] == ' ':
            new_board = deep_copy(board)
            new_board[row][col] = 'Q'
            mark_attacked_positions(new_board, row, col)
            solutions = find_solutions(new_board, row + 1, solutions)

    return solutions


def print_solutions(solutions):
    """Print the solutions."""
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(n)
    all_solutions = find_solutions(chessboard, 0, [])
    print_solutions(all_solutions)
