# Prime Game

This is a Python program developed as part of the ALX curriculum, focusing on the implementation of a game involving prime numbers. The game simulates two players, Maria and Ben, taking turns selecting prime numbers from a set of consecutive integers and removing them along with their multiples from the set. The player who cannot make a move loses the game. The program determines the winner of multiple rounds of this game.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Introduction

Maria and Ben engage in a game where they select prime numbers from a set of consecutive integers and eliminate them along with their multiples. This program allows users to simulate this game for multiple rounds and determine the winner of each round based on a given set of integers.

## Installation

To run this program, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Dr-dyrane/alx-interview.git
    ```

2. Navigate to the directory:

    ```bash
    cd alx-interview/0x0A-primegame
    ```

3. Execute the program:

    ```bash
    ./main_0.py
    ```

## Usage

The program is designed to be run from the command line. You can specify the number of rounds and the set of integers for each round within the `main_0.py` file. Ensure that the `main_0.py` file has executable permissions.

## Functionality

The program provides a function `isWinner(x, nums)` to determine the winner of each round of the prime game. Here's how it works:

- **isWinner(x, nums)**: This function takes two arguments, `x` representing the number of rounds and `nums` representing an array of integers for each round.
  
  - It simulates the game for each round, determining the winner based on the rules mentioned earlier.
  - The function returns the name of the player who won the most rounds. If the winner cannot be determined, it returns `None`.
  - The function does not import any external packages and ensures optimal gameplay.
  
## Examples

Here's an example of how to use the program:

```python
from 0-prime_game import isWinner

# Example usage
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

This will output:

```
Winner: Ben
```

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, please open an issue or create a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Author

- **Alexander Udeogaranya**
  - GitHub: [Dr-dyrane](https://github.com/Dr-dyrane)
