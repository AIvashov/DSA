from typing import List, Any, Union


VALID_VALUES = Union[int, float, str]


def copy_array(array: List[Any]) -> List[Any]:
    """
    Implementation of array copying in Python for this project.
    list.copy() - built-in method for copying lists in Python.
    list[:] - built-in method for copying lists by slicing in Python.
    :param array: Input array.
    :return: A new array that is a copy of the input array.
    """
    new_array = []
    for v in array:
        new_array.append(v)
    return new_array


def check_sorted(array: List[VALID_VALUES], ascending: bool = True) -> bool:
    """
    Check sorted array.
    :param array: Input array.
    :param ascending:
    :return: Sorted or no sorted.
    """
    sign = 2 * int(ascending) - 1
    for i in range(len(array) - 2):
        if sign * array[i] > sign * array[i+1]:
            return False
    return True
