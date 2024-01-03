# UTF-8 Validation

## Overview

This project aims to implement a method that determines if a given data set represents a valid UTF-8 encoding. The solution will be provided in the Python file `0-validate_utf8.py`.

## Table of Contents

1. [Description](#description)
2. [Tasks](#tasks)
3. [Usage](#usage)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Example](#example)
7. [Contributing](#contributing)
8. [License](#license)

## Description <a name="description"></a>

A character in UTF-8 can be 1 to 4 bytes long, and the data set can contain multiple characters. The provided solution will handle a list of integers, each representing 1 byte of data. The goal is to return `True` if the data is a valid UTF-8 encoding and `False` otherwise.

## Tasks <a name="tasks"></a>

- [x] Implement `validUTF8` method
- [x] Ensure PEP 8 style compliance
- [x] Create a README.md file
- [x] Document and comment code
- [x] Make all files executable

## Usage <a name="usage"></a>

To use the `validUTF8` method, import it from `0-validate_utf8.py` and pass a list of integers as the data set. The method will return `True` if the data is a valid UTF-8 encoding, and `False` otherwise.

## Requirements <a name="requirements"></a>

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow PEP 8 style (version 1.7.x)
- All files must be executable

## Installation <a name="installation"></a>

No special installation steps are required. Ensure the specified Python version and editors are available.

## Example <a name="example"></a>

```python
from o_validate_utf8 import validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Contributing <a name="contributing"></a>

Contributions are welcome! Feel free to submit issues or pull requests.

## License <a name="license"></a>

Copyright © 2024 ALX, All rights reserved.
