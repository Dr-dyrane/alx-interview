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

    # Initialize variables to keep track of operations and divisor
    operations, divisor = 0, 2

    # Loop until the divisor is less than or equal to n
    while divisor <= n:
        # Check if n is divisible by the current divisor
        if n % divisor == 0:
            # Total even-divisions by divisor equals total operations
            operations += divisor
            # Set n to the quotient to continue factoring
            n = n / divisor
            # Decrement the divisor to find remaining
            # smaller values that evenly-divide n
            divisor -= 1
        # Increment divisor to check the next potential factor
        divisor += 1

    # Return the minimum number of operations
    return operations
