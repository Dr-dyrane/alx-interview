#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to reach n H characters
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.
    
    Args:
        n (int): Target number of H characters.
        
    Returns:
        int: Minimum number of operations. If n is impossible to achieve, return 0.
    """
    # Base case: If the target is 0 or 1, no operations needed
    if n <= 1:
        return 0

    # Initialize an array to store minimum operations for each number up to n
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 H requires 0 operations

    # Dynamic programming to fill the dp array
    for i in range(1, n + 1):
        for j in range(2 * i, n + 1, i):
            dp[j] = min(dp[j], dp[i] + j // i)

    return dp[n]
