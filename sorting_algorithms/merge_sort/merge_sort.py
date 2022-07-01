from typing import List

from utils import VALID_VALUES


def merge_sort(array: List[VALID_VALUES]) -> None:
    """
    Merge sort algorithm.
    Time complexity - O(n * log n).
    Space complexity - O(n).
    Stability - Yes. BUT look down.
    :param array: Input array.
    """
    if len(array) > 1:

        middle = len(array) // 2

        array_left = array[:middle]
        array_right = array[middle:]

        merge_sort(array_left)
        merge_sort(array_right)

        i = j = k = 0

        while i < len(array_left) and j < len(array_right):
            """
            Sorting is called stable if it does not change the order of equal elements
            
            <= it is set for the stability of the sorting algorithm, otherwise the algorithm will be unstable.
            """
            if array_left[i] <= array_right[j]:
                array[k] = array_left[i]
                i += 1
            else:
                array[k] = array_right[j]
                j += 1
            k += 1

        while i < len(array_left):
            array[k] = array_left[i]
            i += 1
            k += 1

        while j < len(array_right):
            array[k] = array_right[j]
            j += 1
            k += 1
