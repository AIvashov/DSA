from typing import List

from sorting_algorithms import copy_array, VALID_VALUES


def insertion_sort(array: List[VALID_VALUES]) -> List[VALID_VALUES]:
    """
    Insertion sort algorithm.
    Time complexity - O(n^2).
    Space complexity - O(1).
    :param array: Input array.
    :return: New sorted array.
    """

    output_array = copy_array(array)

    for top in range(1, len(output_array)):
        k = top
        while k > 0 and output_array[k-1] > output_array[k]:
            output_array[k], output_array[k-1] = output_array[k-1], output_array[k]
            k -= 1

    return output_array
