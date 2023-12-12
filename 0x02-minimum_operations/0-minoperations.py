#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to reach n H characters
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters.

    Args:
        n (int): Target number of H characters.

    Returns:
        int: Minimum number of operations. If n is impossible to achieve,
        return 0.
    """
    # Base case: If the target is 0 or 1, no operations needed
    if n <= 1:
        return 0

    operations, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            operations += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return operations
