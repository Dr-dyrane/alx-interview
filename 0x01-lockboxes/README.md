# Lockboxes

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Description

The `0-lockboxes.py` script is part of the Lockboxes project in the ALX interview preparation curriculum. It provides a method `canUnlockAll` that determines if all the boxes can be opened. The boxes are represented as a list of lists, where each box may contain keys to other boxes, and a key with the same number as a box opens that box.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should be documented
- Code should follow the PEP 8 style (version 1.7.x)
- All files must be executable

## Installation

No specific installation is required for this script. Simply ensure the script is in a directory with the necessary files and follows the specified requirements.

## Usage

The main function in this script is `canUnlockAll(boxes)`, where `boxes` is a list of lists representing the locked boxes and their keys. The function returns `True` if all boxes can be opened, otherwise, it returns `False`.

## Examples

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the [ALX License](LICENSE).

## Author

- [Alexander Udeogaranya](https://github.com/Dr-dyrane) - ALX