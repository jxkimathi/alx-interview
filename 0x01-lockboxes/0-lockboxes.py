#!/usr/bin/python3
"""Module for the canUnlockAll method"""

def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    if not boxes:
        return False

    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a set to keep track of keys
    keys = set(boxes[0])

    # Loop until no new keys are found
    while keys:

        # Pop a key from the set
        key = keys.pop()

        # If the key opens a box that hasn't been opened yet
        if key < len(boxes) and key not in opened_boxes:

            # Add the box to the opened_boxes set
            opened_boxes.add(key)

            # Add the keys in the opened box to the keys set
            keys.update(boxes[key])

    # If all boxes have been opened, return True
    return len(opened_boxes) == len(boxes)
