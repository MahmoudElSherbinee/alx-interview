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
    open_boxes = [0]
    for box_indx, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in open_boxes and key != box_indx:
                open_boxes.append(key)
    if len(open_boxes) == len(boxes):
        return True
    return False
