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

The `0-lockboxes.py` script is part of the Lockboxes project in the ALX interview preparation curriculum. It provides a magical function `canUnlockAll` that answers the question: Can all the boxes be opened? The boxes are like treasure chests, represented as a list of lists. Each box might have keys to other boxes, and a key with the same number as a box can open that box.

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

No need for complicated installations! Just ensure the script is in a folder with the right files and follows the requirements mentioned above.

## Usage

The main star of the show is the `canUnlockAll(boxes)` function. Provide it with a list of lists (`boxes`), and it will tell you if all the boxes can be opened (returns `True`) or not (returns `False`).

### Logic Explanation

- **📦 `is_empty_or_first` Function:**
  - Checks if the box is either empty or the first box.

- **🔓 `can_unlock_current_box` Function:**
  - Checks if the current box can be unlocked based on the rules defined in `is_empty_or_first`.

- **🔑 `unlock_boxes` Function:**
  - Unlocks other boxes based on the keys in the current box.

- **🌟 `canUnlockAll` Function:**
  - Iterates through each box and checks if it can be unlocked.
  - Uses the functions mentioned above for clear and modular logic.
  - Keeps track of opened boxes using a magical set.

### Visual Aids

Consider the following representation:

```
Boxes:        [ [1], [2], [3], [4], [] ]
Box Numbers:     0    1    2    3   4

Unlocked Boxes: []
```

- **🌈 Initial State:**
  - The first box (box 0) is already unlocked.

- **✨ Step 1:**
  - Box 0 is unlocked.
  - Keys in box 0: [1]
  - Box 1 is unlocked.

- **✨ Step 2:**
  - Keys in box 1: [2]
  - Box 2 is unlocked.

- **✨ Step 3:**
  - Keys in box 2: [3]
  - Box 3 is unlocked.

- **✨ Step 4:**
  - Keys in box 3: [4]
  - Box 4 is unlocked.

- **🌟 Result:**
  - All boxes are unlocked. The function returns `True`.

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



Certainly! Let's break down the explanation for the two example cases:

### Example 1:

```python
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True
```

#### Visual Representation:

```
Boxes:               [ [1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6] ]
Box Numbers:             0         1       2          3       4      5     6

Unlocked Boxes: []
```

#### Steps:

1. **🌈 Initial State:**
   - The first box (box 0) is already unlocked.

2. **✨ Step 1:**
   - Box 0 is unlocked.
   - Keys in box 0: [1, 4, 6]
   - Box 1 is unlocked.

3. **✨ Step 2:**
   - Keys in box 1: [2]
   - Box 2 is unlocked.

4. **✨ Step 3:**
   - Keys in box 2: [0, 4, 1]
   - Box 0 (already unlocked), Box 4, and Box 1 are unlocked.

5. **✨ Step 4:**
   - Keys in box 3: [5, 6, 2]
   - Box 5 and Box 6 are unlocked.

6. **✨ Step 5:**
   - Keys in box 4: [3]
   - Box 3 is unlocked.

7. **🌟 Result:**
   - All boxes are unlocked. The function returns `True`.

### Example 2:

```python
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

#### Visual Representation:

```
Boxes:               [ [1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6] ]
Box Numbers:             0      1       2       3    4    5        6

Unlocked Boxes: []
```

#### Steps:

1. **🌈 Initial State:**
   - The first box (box 0) is already unlocked.

2. **✨ Step 1:**
   - Box 0 is unlocked.
   - Keys in box 0: [1, 4]
   - Box 1 and Box 4 are unlocked.

3. **✨ Step 2:**
   - Keys in box 1: [2]
   - Box 2 is unlocked.

4. **✨ Step 3:**
   - Keys in box 2: [0, 4, 1]
   - Box 0 (already unlocked) and Box 1 (already unlocked) are unlocked.

5. **✨ Step 4:**
   - Keys in box 3: [3]
   - Box 3 is unlocked.

6. **🌟 Result:**
   - Not all boxes are unlocked. The function returns `False`.

In summary, the function checks if it's possible to unlock all boxes following the rules, and the output reflects whether all boxes can be opened (`True`) or not (`False`).

## Contributing

Contributions are like adding more magic to the spellbook! Feel free to submit issues or pull requests.

## License

This project is licensed under the 🧙‍♂️ [ALX License](LICENSE).

## Author

- [Alexander Udeogaranya](https://github.com/Dr-dyrane) - ALX
