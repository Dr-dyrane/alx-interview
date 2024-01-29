# Making Change

## Author

- **Alexander Udeogaranya** - Software Engineer at ALX Software Engineering
  - GitHub: [Dr-dyrane](https://github.com/Dr-dyrane)

## Description

This project contains a Python implementation of a function called `makeChange`, which is designed to determine the fewest number of coins needed to meet a given amount total. The project is part of the ALX Software Engineering curriculum.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- PEP 8 style (version 1.7.x) should be followed
- All files must be executable

## Files

- `0-making_change.py`: Python script containing the implementation of the `makeChange` function
- `0-main.py`: Main file for testing the `makeChange` function

## Usage

To test the `makeChange` function, run the provided `0-main.py` script:

```bash
./0-main.py
```

## Function Prototype

```python
def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
```

## Examples

```python
# Example 1
print(makeChange([1, 2, 25], 37))  # Output: 7

# Example 2
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Evaluation

Your solution's runtime will be evaluated in this task. A checker will be released, and an auto-review will be launched at the deadline.

## Repository

GitHub repository: [alx-interview](https://github.com/Dr-dyrane/alx-interview)
