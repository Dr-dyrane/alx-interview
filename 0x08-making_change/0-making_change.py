#!/usr/bin/python3
"""
Module for makeChange function
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.

    Args:
    - coins (list): A list of positive integers representing
        the values of available coins.
    - total (int): The target amount for which change needs to be made.

    Returns:
    - int: The fewest number of coins needed to meet the given total.
           If the total is 0 or less, return 0.
           If the total cannot be met by any combination of coins, return -1.

    Notes:
    - You can assume you have an infinite number
        of each denomination of coin in the list.
    - This implementation uses dynamic programming to
        efficiently calculate the minimum number of coins.

    Example:
    >>> makeChange([1, 2, 25], 37)
    7

    >>> makeChange([1256, 54, 48, 16, 102], 1453)
    -1
    """

    if total <= 0:
            return 0

    # Dictionary to memoize results of subproblems
    memo = {}


    def min_coins_helper(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if amount in memo:
            return memo[amount]

        # Calculate the minimum number of coins needed for the current amount
        min_coins_needed = float('inf')
        for coin in coins:
            min_coins_needed = min(
                min_coins_needed, min_coins_helper(amount - coin) + 1)

        memo[amount] = min_coins_needed
        return min_coins_needed

    result = min_coins_helper(total)

    return result if result != float('inf') else -1

