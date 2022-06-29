from typing import List

from sorting_algorithms import VALID_VALUES


def bubble_sort(array: List[VALID_VALUES]) -> None:
    """
    Bubble sort algorithm.
    Time complexity - O(n^2).
    Space complexity - O(1).
    Stability - Yes.
    :param array: Input array.
    """

    for bypass in range(1, len(array)):
        for i in range(0, len(array) - bypass):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
