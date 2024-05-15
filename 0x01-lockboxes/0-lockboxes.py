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
    n = len(boxes)

    # The first box boxes[0] is unlocked
    keys = [0]

    for index, box in enumerate(boxes):
        # if keys does not have key should not be Open.
        if index not in keys:
            continue
        for key in box:
            if key not in keys and 0 < key < n:
                keys.append(key)
    return len(keys) == n
