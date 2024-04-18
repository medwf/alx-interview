#!/usr/bin/python3
"""
create methods canUnlockAll:
    method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    This function determines if all the boxes can be opened.

    Args:
      boxes: A list of lists, where each inner list represents the keys
        a box can open.

    Returns:
      True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to track visited boxes (opened boxes).
    visited = set()

    # Function to explore keys and mark visited boxes.
    def explore(box_num):
        if box_num in visited:
            return
        visited.add(box_num)

        for key in boxes[box_num]:
            explore(key)

    # Start exploring from the first box (box 0).
    explore(0)

    # Return True if all boxes have been visited (opened), False otherwise.
    return len(visited) == len(boxes)
