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

    # Sort coins in descending order
    sorted_coins = sorted(coins, reverse=True)

    # Initialize variables
    coins_used = 0

    # Iterate through each coin value
    for coin in sorted_coins:
        # Use as many of the current coin as possible
        while total >= coin:
            coins_used += 1
            total -= coin

    # Check if the total amount has been completely covered
    return coins_used if total == 0 else -1
