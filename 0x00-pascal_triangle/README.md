# 0x00 Pascal's Triangle

This directory contains the solution for the Pascal's Triangle coding challenge. The challenge focuses on generating Pascal's Triangle up to a specified number of rows.

## Table of Contents

1. [Project Details](#project-details)
2. [Files](#files)
3. [Challenges and Solution](#challenges-and-solution)
4. [Usage](#usage)
5. [Illustration](#illustration)

## Project Details

- **Short Specializations**: Algorithm
- **Language**: Python
- **Author**: Alexa Orrico, Software Engineer at Holberton School
- **Project Weight**: 1

## Files

- `0-pascal_triangle.py`: Python script containing the solution for Pascal's Triangle.
- `0-main.py`: Example script demonstrating the usage of the solution.

## Challenges and Solution

The challenge required the generation of Pascal's Triangle up to a specified number of rows. The initial implementation used a straightforward iterative approach with nested loops. During the development process, considerations were made for edge cases, and comments were added for clarity. The code was then refined to improve readability and adhere to best practices, such as avoiding unnecessary list comprehensions.

## Usage

To generate Pascal's Triangle and see the result, run the provided example script:

```bash
./0-main.py
```

This will output the Pascal's Triangle for a specified number of rows.

## Illustration

Here's a visual representation of Pascal's Triangle generation using emojis:

```plaintext
🔍 Start
    |
    v
📦 Initialize triangle
    |
    v
🔄 For each row i in range(n):
    |
    v
📦 Initialize row with 1️⃣
    |
    v
🔄 For each middle element j in row:
    |
    v
📦 Calculate middle elements based on previous row
    |
    v
📦 Append elements to row
    |
    v
📦 Add last element (always 1️⃣) to row
    |
    v
📦 Append row to Pascal's Triangle
    |
    v
🔍 End
```

Feel free to explore and modify the solution script (`0-pascal_triangle.py`) for your use or as a reference for similar challenges.