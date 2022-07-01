from typing import Optional, List

from utils import VALID_VALUES


def binary_search(sorted_array: List[VALID_VALUES], key: VALID_VALUES) -> Optional[int]:
    """
    Binary Search is a searching algorithm for finding an element's position in a sorted array.
    Time complexity - O(log n).
    Space complexity - O(1).
    :param sorted_array: Sorted input array.
    :param key: Searchable element.
    :return: Element index if it is in array otherwise None.
    """
    left_border = 0
    right_border = len(sorted_array) - 1
    while left_border <= right_border:
        middle = (left_border + right_border) // 2
        if sorted_array[middle] < key:
            left_border = middle + 1
        elif sorted_array[middle] > key:
            right_border = middle - 1
        else:
            return middle

    return

