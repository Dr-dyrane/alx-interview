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

    # Iterate through each box
    for box_id, box in enumerate(boxes):
        # Check if the box is empty or the first box (already unlocked)
        if len(box) == 0 or box_id == 0:
            opened_boxes.add(box_id)

        # Iterate through keys in the current box
        for key in box:
            # Check if the key can unlock a valid box
            if 0 <= key < len(boxes) and key != box_id:
                opened_boxes.add(key)

        # Check if all boxes are unlocked
        if len(opened_boxes) == len(boxes):
            return True

    # If not all boxes can be unlocked
    return False
