from typing import List

from sorting_algorithms import VALID_VALUES


def selection_sort(array: List[VALID_VALUES]) -> None:
    """
    Selection sort algorithm.
    Time complexity - O(n^2).
    Space complexity - O(1).
    Stability - Yes.
    :param array: Input array.
    :return: New sorted array.
    """
    for pos in range(0, len(array) - 1):
        for k in range(pos+1, len(array)):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]
