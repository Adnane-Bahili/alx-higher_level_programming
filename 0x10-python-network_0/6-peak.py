#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """returns the peak"""
    if list_of_integers == []:
        return None

    list_size = len(list_of_integers)

    if list_size == 1:
        return list_of_integers[0]
    elif list_size == 2:
        return max(list_of_integers)

    med = int(list_size / 2)
    high = list_of_integers[med]

    if high > list_of_integers[med - 1] and high > list_of_integers[med + 1]:
        return high
    elif high < list_of_integers[med - 1]:
        return find_peak(list_of_integers[:med])
    else:
        return find_peak(list_of_integers[med + 1:])
