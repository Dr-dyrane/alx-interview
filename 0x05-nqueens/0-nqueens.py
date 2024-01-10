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

Author: Alexander Udeogaranya
"""

import sys


def init_board(n):
    """
    Initialize an `n`x`n` sized chessboard with 0's.
    """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]

    return (board)


def board_deepcopy(board):
    """
    Return a deepcopy of a chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))

    return (board)


def get_solution(board):
    """
    Return the list of lists representation of a solved chessboard.
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break

    return (solution)


def Markout(board, row, col):
    """
    Mark out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # Mark out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # Mark out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """
    Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.

    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))

        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            Markout(tmp_board, row, c)
            solutions = recursive_solve(
                tmp_board, row + 1, queens + 1, solutions
            )

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])

    for solution in solutions:
        print(solution)
