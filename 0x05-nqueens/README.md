# N Queens Solver

## Overview

This project aims to solve the N Queens puzzle, a classic chess problem where the challenge is to place N non-attacking queens on an N×N chessboard. The program takes an integer N as input and outputs all possible solutions to the problem.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Coding Style](#coding-style)
- [License](#license)
- [Author](#author)

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.4.3)
- All files end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A mandatory `README.md` file at the root of the project folder
- Code should follow PEP 8 style (version 1.7.*)
- All files must be executable

## Usage

The program is executed from the command line with the following syntax:

```bash
./0-nqueens.py N
```

- `N` must be an integer greater or equal to 4.
- If the user provides the wrong number of arguments, the program prints `Usage: nqueens N` and exits with status 1.
- If `N` is not an integer, the program prints `N must be a number` and exits with status 1.
- If `N` is smaller than 4, the program prints `N must be at least 4` and exits with status 1.
- The program prints every possible solution to the N Queens problem, one solution per line.

## Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Project Structure

```
alx-interview/
└── 0x05-nqueens/
    └── 0-nqueens.py
    └── README.md
```

## How It Works

The program uses a backtracking algorithm to explore and find all possible solutions to the N Queens puzzle. The chessboard is represented as an N×N grid, and the goal is to place queens in such a way that no two queens attack each other. The backtracking algorithm systematically explores possible placements, backtracking when a solution is not viable.

## Dependencies

The program is written in Python and only uses the `sys` module.

## Coding Style

The code follows the PEP 8 style guide (version 1.7.*).

## License

This project is licensed under the [MIT License](LICENSE).

## Author

- **Alexander Udeogaranya** - Software Engineer at ALX Software Engineering
  - GitHub: [Dr-dyrane](https://github.com/Dr-dyrane)