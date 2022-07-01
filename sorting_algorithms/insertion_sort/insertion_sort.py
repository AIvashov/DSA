from typing import List

from utils import VALID_VALUES


def insertion_sort(array: List[VALID_VALUES]) -> None:
    """
    Insertion sort algorithm.
    Time complexity - O(n^2).
    Space complexity - O(1).
    Stability - Yes.
    :param array: Input array.
    """
    for top in range(1, len(array)):
        k = top
        while k > 0 and array[k-1] > array[k]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1
