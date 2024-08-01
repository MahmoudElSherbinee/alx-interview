#!/usr/bin/python3
"""
This module contains the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists of int):
            Each box is a list containing keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    open_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key not in open_boxes:
            open_boxes.add(key)
            keys.update(boxes[key])

    return len(open_boxes) == len(boxes)
