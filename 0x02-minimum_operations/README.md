# ALX Interview Project: 0x02 - Minimum Operations 🚀

## Overview

Welcome to the exciting world of operations with the magical character 'H'! 🧙‍♂️ In this project, you'll be using Python to perform two enchanting operations: Copy All and Paste. Your mission is to find the minimum number of operations needed to create a magical sequence of 'H' characters.

## Project Details

### Project Structure

- **Repository Name:** alx-interview
- **Directory:** 0x02-minimum_operations
- **File:** 0-minoperations.py

### Project Author

- **Author:** Alexander Udeogaranya
- **Email:** Ogranya.alex@gmail.com
- **GitHub Username:** [Dr-dyrane](https://github.com/Dr-dyrane)

### Environment

- **Operating System:** Ubuntu 20.04 LTS
- **Python Version:** 3.4.3

### Code Style

Make your code sparkle! ✨ Follow the PEP 8 style guide (version 1.7.x) to keep things neat and organized.

## Task: Minimum Operations Spell ✨

In a magical text file, there's a single character 'H'. Your enchanted text editor can perform two magical operations: Copy All and Paste. Your task is to create a Python method that calculates the fewest number of operations needed to conjure exactly 'n' 'H' characters in the file.

### Function Prototype

```python
def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.
    
    Args:
        n (int): Target number of H characters.
        
    Returns:
        int: Minimum number of operations. If n is impossible to achieve, return 0.
    """
```

### Example Magic Spell

```python
n = 9

# Magic Sequence: H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```

## Implementation Explanation

### The Magical File: `0-minoperations.py`

```python
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
```

### Explanation in Simple Terms

1. **Base Case:** If you want 0 or 1 'H' characters, no magic operations are needed (return 0).

2. **Efficient Factorization Loop:** We use an efficient factorization loop that continuously divides the target number 'n' by its smallest divisors. For each divisor, we add it to the total operations needed and update 'n' accordingly. This process is repeated until 'n' is reduced to 1. This approach ensures the fewest number of operations.

3. **Return the Magic:** Finally, the number of operations needed to create 'n' 'H' characters is returned.

This optimized algorithm minimizes the number of operations required to reach the target 'n' characters by efficiently factoring the number.

### Testing Your Magic Powers 🧙‍♂️

Use the provided `0-main.py` file for testing your magical abilities:

```python
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

Simply run `./0-main.py` and see the magic unfold!

## Remember: Keep Your Spells Documented! 📜

Document your magical code using comments. This helps wizards (and interviewers) understand your spellcasting techniques.

## Copyright Notice

Copyright © 2023 ALX. All rights reserved. No unauthorized magic allowed! 🚫✨