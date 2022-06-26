from typing import List

from sorting_algorithms import copy_array, VALID_VALUES


def selection_sort(array: List[VALID_VALUES]) -> List[VALID_VALUES]:
    """
    Selection sort algorithm.
    Time complexity - O(n^2).
    Space complexity - O(1).
    :param array: Input array.
    :return: New sorted array.
    """

    output_array = copy_array(array)

    for pos in range(0, len(output_array) - 1):
        for k in range(pos+1, len(output_array)):
            if output_array[k] < output_array[pos]:
                output_array[k], output_array[pos] = output_array[pos], output_array[k]

    return output_array
