from typing import List

from utils import VALID_VALUES


def quick_sort(array: List[VALID_VALUES]) -> None:
    """
    Quick(Tom Hoar) sort algorithm.
    Time complexity - O(n * log n).
    Worst time complexity - O(n^2)
    Space complexity - O(n).
    Stability - No.
    :param array: Input array.
    """
    left = []
    middle = []
    right = []
    if len(array) <= 1:
        return
    barrier = array[0]
    for x in array:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)

    quick_sort(left)
    quick_sort(right)

    k = 0
    for x in left + middle + right:
        array[k] = x
        k += 1
