#!/usr/bin/python3
"""
    Find a peak in a list of unsorted integers.

    Returns:
    - The peak element.
    """


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
    else:
        return None
