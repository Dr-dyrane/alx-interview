#!/usr/bin/python3
"""
Module for makeChange function
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """

    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each amount
    # Initialize the list with float('inf') for each amount from 0 to total
    min_coins = [float('inf')] * (total + 1)

    # The minimum number of coins needed to make change for 0 is 0
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each amount
        for amount in range(coin, total + 1):
            min_coins[amount] = min(
                min_coins[amount], min_coins[amount - coin] + 1)

    # If the minimum number of coins for the total is still float('inf'),
    # it means it's not possible
    return min_coins[total] if min_coins[total] != float('inf') else -1
