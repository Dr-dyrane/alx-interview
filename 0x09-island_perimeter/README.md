# Island Perimeter

## Introduction
This project implements a Python function to calculate the perimeter of an island represented by a grid of 1s and 0s. Each 1 represents land, and each 0 represents water. The function calculates the perimeter of the island based on the adjacency of land cells.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style compliance
- No external modules or libraries
- Documentation for all functions and modules

## Usage
To use the `island_perimeter` function, simply pass a grid as a list of lists of integers. The function will return the perimeter of the island.

Example usage:
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Function Description
### `island_perimeter(grid)`
Calculates the perimeter of the island described in the provided grid.

- **Parameters:**
  - `grid` (List[List[int]]): A grid of integers where 0 represents water and 1 represents land.

- **Returns:**
  - `int`: The perimeter of the island.

- **Constraints:**
  - The grid is rectangular, with its width and height not exceeding 100.
  - The grid is completely surrounded by water.
  - There is only one island (or nothing).
  - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## File Structure
```
0x09-island_perimeter/
│
├── 0-main.py
└── 0-island_perimeter.py
```

## Testing
To test the function, run the `0-main.py` script. Ensure that the output matches the expected result.

## Author
- **Alexander Udeogaranya**
  - GitHub: [Dr-dyrane](https://github.com/Dr-dyrane)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
