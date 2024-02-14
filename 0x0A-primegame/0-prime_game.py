#!/usr/bin/python3
"""
Prime Game Module
-----------------
This module contains the implementation of the prime game.

The prime game involves selecting prime numbers from a set of consecutive
integers and eliminating them along with their multiples until
no prime numbers are left to choose from.

The player who cannot make a move loses the game.
"""


def generate_prime_numbers(n):
    """
    Generate prime numbers up to a given limit using the Sieve of Eratosthenes.

    Args:
        n (int): The upper boundary of the range.

    Returns:
        list: A list of prime numbers between 1 and n (inclusive).
    """
    prime_numbers = []
    sieve = [True] * (n + 1)  # Create a boolean list to mark primes

    # Mark multiples of primes as False
    for num in range(2, n + 1):
        if sieve[num]:
            prime_numbers.append(num)  # Add prime to the list
            for multiple in range(num, n + 1, num):
                sieve[multiple] = False

    return prime_numbers


def isWinner(x, nums):
    """
    Determines the winner of each round of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the upper limit
                             of range for each round.

    Returns:
        str or None: The name of the player who won the most rounds.
                     If the winner cannot be determined, returns None.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = 0
    ben_wins = 0

    for limit in range(x):
        prime_numbers = generate_prime_numbers(nums[limit])
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
