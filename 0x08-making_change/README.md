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

A diagrammatic representation for both examples: `makeChange([1, 2, 25], 37)` and `makeChange([1256, 54, 48, 16, 102], 1453)`;

### Example 1: `makeChange([1, 2, 25], 37)`

#### Initial state:
- `coins`: [1, 2, 25]
- `total`: 37
- `sorted_coins`: [25, 2, 1]
- `coins_used`: 0

#### Loop 1 (coin = 25):
```
total >= coin (37 >= 25):
    coins_used += 1   # Update coins_used: 1
    total -= coin     # Update total: 12
```

#### Loop 2 (coin = 2):
```
total >= coin (12 >= 2):
    coins_used += 6   # Update coins_used: 7
    total -= coin*6   # Update total: 0
```

#### Result:
- The fewest number of coins needed to make change for 37 is 7.

### Example 2: `makeChange([1256, 54, 48, 16, 102], 1453)`

#### Initial state:
- `coins`: [1256, 54, 48, 16, 102]
- `total`: 1453
- `sorted_coins`: [1256, 102, 54, 48, 16]
- `coins_used`: 0

#### Loop 1 (coin = 1256):
```
total >= coin (1453 >= 1256):
    # Cannot use any 1256s as the total is smaller than the coin.
```

#### Loop 2 (coin = 102):
```
total >= coin (1453 >= 102):
    coins_used += 14  # Update coins_used: 14
    total -= coin*14  # Update total: 25
```

#### Loop 3 (coin = 54):
```
total >= coin (25 >= 54):
    # Cannot use any 54s as the total is smaller than the coin.
```

#### Loop 4 (coin = 48):
```
total >= coin (25 >= 48):
    # Cannot use any 48s as the total is smaller than the coin.
```

#### Loop 5 (coin = 16):
```
total >= coin (25 >= 16):
    coins_used += 1   # Update coins_used: 15
    total -= coin     # Update total: 9
```

#### Result:
- It's not possible to make change for 1453 with the given coins.

## Evaluation

Your solution's runtime will be evaluated in this task. A checker will be released, and an auto-review will be launched at the deadline.
O(n log n)

## Repository

GitHub repository: [alx-interview](https://github.com/Dr-dyrane/alx-interview)
