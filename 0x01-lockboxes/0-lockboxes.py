#!/usr/bin/python3
"""
create methods canUnlockAll:
    method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Check if it's possible to unlock all the boxes based on a set of keys.

    Parameters:
    - boxes (List[List[int]]): A list of lists.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """
    boxesKeys = []
    len_boxes = len(boxes)
    count = 0

    for key in boxes[0]:
        if key not in boxesKeys and 0 < key < len_boxes:
            boxesKeys.append(key)
            count += 1

    index = 0
    while index < len(boxesKeys):
        keys = boxesKeys[index]
        for key in boxes[keys]:
            if key not in boxesKeys and 0 < key < len_boxes:
                boxesKeys.append(key)
                count += 1
        index += 1

    return count == len_boxes - 1
