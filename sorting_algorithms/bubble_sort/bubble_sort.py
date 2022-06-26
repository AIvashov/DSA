from typing import List

from sorting_algorithms import copy_array, VALID_VALUES


def bubble_sort(array: List[VALID_VALUES]) -> List[VALID_VALUES]:
    """
    Bubble sort algorithm.
    Time complexity - O(n^2).
    Space complexity - O(1).
    :param array: Input array.
    :return: New sorted array.
    """
    output_array = copy_array(array)

    for bypass in range(1, len(output_array)):
        for i in range(0, len(output_array) - bypass):
            if output_array[i] > output_array[i+1]:
                output_array[i], output_array[i+1] = output_array[i+1], output_array[i]

    return output_array
