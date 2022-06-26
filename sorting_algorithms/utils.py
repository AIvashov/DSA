from typing import List, Any


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
