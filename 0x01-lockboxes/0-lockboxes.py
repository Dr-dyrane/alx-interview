#!/usr/bin/python3
"""
Lockboxes Module

This module provides a method to determine if all the boxes can be opened.
Each box may contain keys to other boxes,
and a key with the same number as a box opens that box.

Author: Alexander Udeogaranya
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): Represents locked boxes and their keys.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """

    # Set to keep track of opened boxes
    opened_boxes = set()

    # Queue for BFS (Breadth-First Search)
    queue = [0]  # Start with the first box

    # BFS to explore and open boxes
    while queue:
        current_box = queue.pop(0)
        opened_boxes.add(current_box)

        # Add new keys to the queue (if any)
        queue.extend(
            key for key in boxes[current_box] if key not in opened_boxes)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)


if __name__ == "__main__":
    pass  # If this script is run directly, do nothing
