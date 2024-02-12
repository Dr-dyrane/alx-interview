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


def is_prime(num):
    """
    Checks if a number is prime.
    
    Parameters:
        num (int): The number to check.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner of each round of the prime game.
    
    Parameters:
        x (int): The number of rounds.
        nums (list): An array of integers representing the set of consecutive
                     integers for each round.
                     
    Returns:
        str or None: The name of the player who won the most rounds.
        If the winner
                     cannot be determined, returns None.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(is_prime(i) for i in range(1, n + 1))

        # If the count of primes is even, Ben wins, otherwise Maria wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

