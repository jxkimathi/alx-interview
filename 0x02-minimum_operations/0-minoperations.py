#!/usr/bin/python3
"""Minimum operations challenge"""


def minOperations(n):
    """Calculates the fewest number of operations needed"""
    copied_chars = 0 # Number of H
    pasted_chars = 1 # Number of hars
    counter = 0

    while pasted_chars < n:
        if copied_chars == 0: # If no chars are copied
            pasted_chars = copied_chars
            counter += 1

        if pasted_chars == 1: # If nothing has been pasted
            pasted_chars += copied_chars
            counter += 1
            continue

    remaining_chars = n - pasted_chars # Remainig chars to paste

    if remaining_chars < copied_chars:
        return 0

    if remaining_chars % pasted_chars != 0:
        pasted_chars += copied_chars
        counter += 1
    else:
        copied_chars = pasted_chars
        pasted_chars += copied_chars
        counter += 2

    if pasted_chars == n:
        return counter
    else:
        return 0
