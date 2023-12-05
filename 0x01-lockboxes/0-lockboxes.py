#!/usr/bin/python3
"""
Lockboxes Module

This module provides a method to determine if all the boxes can be opened.
Each box may contain keys to other boxes,
and a key with the same number as a box opens that box.

Author: Alexander Udeogaranya
"""


def is_empty_or_first(box_id, box):
    """Check if the box is empty or the first box."""
    return not box or box_id == 0


def can_unlock_current_box(unlocked, box_id, boxes):
    """Check if the current box can be unlocked."""
    return is_empty_or_first(box_id, boxes[box_id]) and box_id not in unlocked


def unlock_boxes(unlocked, box_id, box, boxes):
    """Unlock boxes based on the keys in the current box."""
    for key in box:
        if 0 <= key < len(boxes) and key != box_id:
            unlocked.add(key)


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): Represents locked boxes and their keys.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """

    # Set to keep track of opened boxes
    unlocked = set()

    # Iterate through each box
    for box_id, box in enumerate(boxes):
        # Check if the current box can be unlocked
        if can_unlock_current_box(unlocked, box_id, boxes):
            unlocked.add(box_id)

        # Unlock boxes based on the keys in the current box
        unlock_boxes(unlocked, box_id, box, boxes)

        # Check if all boxes are unlocked
        if len(unlocked) == len(boxes):
            return True

    # If not all boxes can be unlocked
    return False


if __name__ == "__main__":
    pass  # If this script is run directly, do nothing
